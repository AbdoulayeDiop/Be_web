template = Import('template.py')
monEq = Import('menu_equipe.py')
bdd = Import('../data/bdd.py')
conf = Import('../data/config.py')
cookies = Import('../python/cookies.py')
chemin = conf.chemin()
import datetime as dt


def index():
    if "nom" in COOKIE :
        result = template.entete(chemin,'CB - Contacter')
        result += template.main_header(chemin)
        result += template.sidebar(2, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')

def contacter_card():

    cc = '''<div class="card">
                    <div class="card-header">
                        <div class="card-title">Envoyer un message</div>
                    </div>
                    <form action="'''+chemin+'''/python/contacter.py/send_msg" method="POST">
                        <div class="card-body">
                    '''
    if "notif_msg" in COOKIE :
        cc+= COOKIE["notif_msg"].value

    cc+=   '''     
                            <div class="form-group">
                                <label for="comment" id="membre_msg">Selectionner un membre à contacter dans la liste </label>
                            </div>
                            <div class="form-group">
                                <label for="message-text" class="col-form-label">Message</label>
                                <textarea class="form-control" name="msg" id="msg">
                                </textarea>
                            </div>
                            <input type="hidden" name="btn_idcoeq_msg" id="btn_idcoeq_msg" />
                            <div class="card-action">
                                <button class="btn btn-success">Envoyer</button>
                            </div>
                        </div>
                    </form>
                </div>
                '''
    cookies.erase("notif_msg")
    return cc

def send_msg(msg='',btn_idcoeq_msg=''):
    if (msg!='' and btn_idcoeq_msg!=''):
        idMessage = str(bdd.get_idMsgMax()+1)
        idDestinateur = COOKIE["idMembre"].value
        date = str(dt.datetime.now())[:19]
        bdd.ajouter_msg(idMessage,idDestinateur,btn_idcoeq_msg,msg,'0', date)
        cookies.set_cookie("notif_msg", '<div class="alert alert-success" role="alert"> Message envoyé avec succés </div>')
    else:
        cookies.set_cookie("notif_msg", '<div class="alert alert-warning" role="alert"> Message non envoyé, veuillez selectionner un membre </div>')
    raise HTTP_REDIRECTION(chemin + '/python/contacter.py')


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
                document.getElementById("membre_msg").innerHTML = "Membre à contacter : '''+dico_membre[id]["nom"]+" "+dico_membre[id]["prenom"]+'''";
                $("#btn_idcoeq_msg").val('''+str(id)+''');
                }
            </script>
        '''
    return f1

def main_panel():
    vmain_panel='''<div class="main-panel">
                        <div class="content">
                            <div class="container-fluid">
                                <h4 class="page-title">Contacter un coéquipier</h4>
                                <div class="row">
                                    <div class="col-md-6">'''
    vmain_panel+=monEq.liste_coeq_card()
    vmain_panel+='</div> <div class="col-md-6">'
    vmain_panel+=contacter_card()
    vmain_panel+='</div></div></div>'
    vmain_panel+=footer()
    vmain_panel+='</div></div>'
    return vmain_panel
