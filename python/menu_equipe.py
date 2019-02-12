template = Import('template.py')
bdd = Import('../data/bdd.py')
conf = Import('../data/config.py')
cookies = Import('../python/cookies.py')
chemin = conf.chemin()

def index():
    if "nom" in COOKIE :
        result = template.entete(chemin,'CB - Mon Equipe')
        result += template.main_header(chemin)
        result += template.sidebar(7, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


def liste_coeq_card():
    idEquipe = str(COOKIE["idEquipe"].value)
    idMembre = str(COOKIE["idMembre"].value)
    dico_membres = bdd.get_coequipiers(idEquipe,idMembre)
    lmc= '''<div class="card">
                <div class="card-header">
                    <div class="card-title">Liste de mes coéquipiers</div>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label for="exampleFormControlSelect2">Id membre - Nom - Prenom</label>
                        <select multiple class="form-control" id="exampleFormControlSelect2">
                            '''+afficher_coeq(dico_membres)+'''
                        </select>
                    </div>
                    <div class="form-group">
                        <label for="comment">Informations complémentaires</label>
                         <select multiple class="form-control" name="S1">
                            <option id="compl_idMembre"></option>
                            <option id="compl_nom"></option>
                            <option id="compl_prenom"></option>
                            <option id="compl_login"></option>
                            <option id="compl_equipe"></option>
                            <option id="compl_admin"></option>
                         </select>
                    </div>
                </div>
            </div>'''
    return lmc

def afficher_coeq(dico={}):
    html_code=""
    for id in dico:
        membrei = "membre"+str(id)
        html_code+="<option id="+membrei+">"+str(id)+" - "+dico[id]["nom"]+" - "+dico[id]["prenom"]+"</option>"
    return html_code


def footer():
    f1=''
    idEquipe = str(COOKIE["idEquipe"].value)
    dico_membre = bdd.get_coequipiers(idEquipe)
    for id in dico_membre:
        membrei = "membre"+str(id)
        f1+='''
            <script>
            document.getElementById("'''+membrei+'''").onclick = function() {myFunction'''+membrei+'''()};
            function myFunction'''+membrei+'''() {
                document.getElementById("compl_idMembre").innerHTML = "Identifiant du membre : '''+str(id)+'''";
                document.getElementById("compl_nom").innerHTML = "Nom : '''+dico_membre[id]["nom"]+'''";
                document.getElementById("compl_prenom").innerHTML = "Prénom : '''+dico_membre[id]["prenom"]+'''";
                document.getElementById("compl_login").innerHTML = "Email : '''+dico_membre[id]["login"]+'''";
                document.getElementById("compl_equipe").innerHTML = "Identifiant de l'équipe : '''+dico_membre[id]["idEquipe"]+'''";
                document.getElementById("compl_admin").innerHTML = "Admin : NON";
                }
            </script>
        '''
    return f1

def main_panel():
    vmain_panel='''<div class="main-panel">
                        <div class="content">
                            <div class="container-fluid">
                                <h4 class="page-title">Mon Equipe</h4>
                                <div class="row">
                                    <div class="col-md-6">'''
    vmain_panel+=liste_coeq_card()
    vmain_panel+='</div> <div class="col-md-6">'
    vmain_panel+='</div></div></div>'
    vmain_panel+=footer()
    vmain_panel+='</div></div>'
    return vmain_panel
