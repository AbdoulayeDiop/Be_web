template = Import('template.py')
bdd = Import('../data/bdd.py')
conf = Import('../data/config.py')
cookies = Import('../python/cookies.py')
chemin = conf.chemin()
import random as rd



def index():
    if "nom" in COOKIE and int(COOKIE["admin"].value)==1:
        result = template.entete(chemin,'CB - Ajouter Membre/Equipe')
        result += template.main_header(chemin)
        result += template.sidebar(5, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')

def ajouter_membre_card():
    idMembre = str(int(bdd.get_idMax()[0]) + 1)
    amc='''  <div class="card">
            <div class="card-header">
                <div class="card-title">Ajouter un membre</div>
            </div>
            <div class="card-body">
                 <form method="post" action="'''+chemin+'''/python/ajouter_equipe.py/ajouter_membre">
                    <div class="form-group">
                        <input type="nom" class="form-control" name="nom" placeholder="Nom">
                    </div>
                    <div class="form-group">
                        <input type="prenom" class="form-control" name="prenom" placeholder="Prénom">
                    </div>
                    <div class="form-group">
                        <input type="email" class="form-control" name="login" placeholder="Email">
                    </div>
                    <div class="form-group">
                        <input type="idEquipe" class="form-control" name="idEquipe" placeholder="Identifiant de l'équipe">
                    </div>
                    <div class="form-group">
                        <label class="control-label">
                            Le mot de passe provisoire de ce nouveau membre sera :
                        </label> 
                        <!----> <p class="form-control-static text-danger"> pwd : '''+save_mdp()+'''</p> <!---->  
                    </div>
                    <div class="form-group">
                        <label class="control-label">
                            L'identifiant de ce nouveau membre sera :
                        </label> <!----> <p class="form-control-static text-primary"> idMembre : '''+idMembre+'''</p> <!---->  
                    </div>
                    <div class="card-action">
                        <button class="btn btn-success">Ajouter membre</button>
                    </div>
                </form>
            </div>
        </div>'''
    return amc

def save_mdp():
    mdp_provisoire = str(rd.randint(1000, 999999))
    cookies.set_cookie("mdp_provisoire",mdp_provisoire )
    return mdp_provisoire

def ajouter_membre(nom='',prenom='',login='',idEquipe=''):
    idMembre = int(bdd.get_idMax()[0]) + 1
    if (nom,prenom,login,idEquipe)!=('','','',''):
        bdd.ajouter_membre_bdd(idMembre,nom,prenom,login,str(COOKIE["mdp_provisoire"].value),idEquipe)
    raise HTTP_REDIRECTION(chemin + '/python/ajouter_equipe.py')


def liste_membre_card(dico_membres):
    lmc= '''<div class="card">
                <div class="card-header">
                    <div class="card-title">Liste des membres</div>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label for="exampleFormControlSelect2">Id membre - Nom - Prenom</label>
                        <select multiple class="form-control" id="exampleFormControlSelect2">
                            '''+afficher_membres(dico_membres)+'''
                        </select>
                    </div>
                    <form id="info_compl" action="'''+chemin+'''/python/ajouter_equipe.py/supprimer_membre" method="POST">
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
                        <input type="hidden" name="btn_idMembre" id="btn_idMembre" />
                        <div class="card-action">
                            <button class="btn btn-danger">Supprimer ce membre</button>
                        </div>
                    </form>    
                </div>
            </div>'''
    return lmc

def afficher_membres(dico={}):
    html_code=""
    for id in dico:
        membrei = "membre"+str(id)
        html_code+="<option id="+membrei+">"+str(id)+" - "+dico[id]["nom"]+" - "+dico[id]["prenom"]+"</option>"
    return html_code

def supprimer_membre(S1="", btn_idMembre=""):
    if btn_idMembre != '':
        bdd.delete_membre(btn_idMembre)
    raise HTTP_REDIRECTION(chemin + '/python/ajouter_equipe.py')


def creer_equipe_card():
    idEquipe = str(int(bdd.count_equipes()[0]) + 1)
    cec='''<div class="card">
                <div class="card-header">
                    <div class="card-title">Créer une équipe</div>
                </div>
                <div class="card-body">
                    <form method="post" action="'''+chemin+'''/python/ajouter_equipe.py/ajouter_eq">
                        <div class="form-group">
                            <input type="text" class="form-control" name="nom_eq" placeholder="Nom de l'équipe">
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" name="idAvion" placeholder="Identifiant de l'avion">
                        </div>
                        <div class="form-group">
                        <label class="control-label">
                            L'identifiant de cette nouvelle équipe sera :
                        </label> <!----> <p class="form-control-static text-primary"> idEquipe : '''+idEquipe+'''</p> <!---->  
                        </div>
                        <div class="form-group"></div><div class="form-group"></div><div class="form-group"></div>
                        <div class="form-group"></div><div class="form-group"></div>
                        <div class="card-action">
                            <button class="btn btn-success">Créer l'équipe</button>
                        </div>	
                    </form>							
                </div>
            </div>'''
    return cec

def ajouter_eq(nom_eq='',idAvion=''):
    idEquipe = int(bdd.count_equipes()[0])+1
    if nom_eq!='' and idAvion!='':
        bdd.ajouter_equipe_bdd(idEquipe, nom_eq, idAvion)
    raise HTTP_REDIRECTION(chemin + '/python/ajouter_equipe.py')

def liste_equipe_card():
    dico_equipes = bdd.get_equipes()

    lec='''<div class="card">
                <div class="card-header">
                    <div class="card-title">Liste des équipes</div>
                </div>
                <div class="card-body">
                    <div class="form-group">
                        <label for="exampleFormControlSelect2">Id equipe - Nom equipe - Id avion</label>
                        <select multiple class="form-control" id="exampleFormControlSelect2">
                            '''+afficher_equipes(dico_equipes)+'''
                        </select>
                    </div>
                    <form action="'''+chemin+'''/python/ajouter_equipe.py/supprimer_equipe" method="POST">
                        <div class="form-group">
                            <label for="comment">Membres de l'équipe : (Id - Nom - prénom)</label>
                            <select multiple class="form-control" name="S2" onChange="AjoutOptionAuSelect(this);">
                                <option id="membre_eq1"></option>
                                <option id="membre_eq2"></option>
                                <option id="membre_eq3"></option>
                                <option id="membre_eq4"></option>
                                <option id="membre_eq5"></option>
                                <option id="membre_eq6"></option>
                                <option id="membre_eq7"></option>
                                <option id="membre_eq8"></option>
                                <option id="membre_eq9"></option>
                                <option id="membre_eq10"></option>
                            </select>
                        </div>
                        <input type="hidden" name="btn_membre_eq" id="btn_membre_eq"/>
                        <div class="card-action">
                            <button class="btn btn-danger" id="delete_team">Supprimer cette équipe</button>
                        </div>
                    </form>
                </div>
          </div>'''
    return lec

def afficher_equipes(dico={}):
    html_code=""
    for id in dico:
        equipei = "equipe"+str(id)
        html_code+="<option id="+equipei+">"+str(id)+" - "+dico[id]["nom"]+" - "+dico[id]["idAvion"]+"</option>"
    return html_code

def afficher_membres_equipe(idEq=''):
    code_html = ''
    if idEq != '':
        dico_coequipiers = bdd.get_coequipiers(idEq)
        for id in dico_coequipiers:
            code_html+="<option>"+str(id)+" - "+dico_coequipiers[id]["nom"]+" - "+dico_coequipiers[id]["prenom"]+"</option>"
    return code_html

def supprimer_equipe(S2='',btn_membre_eq=''):
    bdd.delete_equipe(btn_membre_eq)
    raise HTTP_REDIRECTION(chemin + '/python/ajouter_equipe.py')

def footer():
    f1=''
    dico_membre = bdd.get_membres()
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
                $("#btn_idMembre").val('''+str(id)+''');
                }
            </script>
        '''
    f2 = ''
    dico_equipes = bdd.get_equipes()
    for idEq in dico_equipes:
        equipei = "equipe"+str(idEq)
        dico_equipei = bdd.get_coequipiers(str(idEq))
        f2+= '''
            <script>
            document.getElementById("'''+equipei+'''").onclick = function() {myFunction'''+equipei+'''()};
            function myFunction'''+equipei+'''() {'''
        i=1
        for idMembre in dico_equipei:
            f2+='''
            document.getElementById("membre_eq'''+str(i)+'''").innerHTML = "'''+str(idMembre)+" - "+dico_equipei[idMembre]["nom"]+" - "+dico_equipei[idMembre]["prenom"]+'''";'''
            i+=1
        for k in range(i,11):
            f2 += '''document.getElementById("membre_eq''' + str(k) + '''").innerHTML = "";'''

        f2+='''
                $("#btn_membre_eq").val('''+str(idEq)+''');
                }
            </script>
        '''
    return f1+f2

def main_panel():
    dico_membres = bdd.get_membres()
    vmain_panel='''<div class="main-panel">
                        <div class="content">
                            <div class="container-fluid">
                                <h4 class="page-title">Ajouter un membre ou une équipe</h4>
                                <div class="row">
                                    <div class="col-md-6">'''
    vmain_panel+=ajouter_membre_card()
    vmain_panel+=liste_membre_card(dico_membres)
    vmain_panel+='</div> <div class="col-md-6">'
    vmain_panel+=creer_equipe_card()
    vmain_panel+=liste_equipe_card()
    vmain_panel+='</div></div></div>'
    vmain_panel+=footer()
    vmain_panel+='</div></div>'
    return vmain_panel
