# -*- coding: utf8 -*-
template = Import('template.py')
monEq = Import('menu_equipe.py')
bdd = Import('../data/bdd.py')
conf = Import('../data/config.py')
cookies = Import('../python/cookies.py')
chemin = conf.chemin()



def index():
    if "nom" in COOKIE :
        result = template.entete(chemin,'CB - Notification')
        result += template.main_header(chemin)
        result += template.sidebar(4, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')

def received_card():
    idMembre = COOKIE["idMembre"].value
    dico_msg = bdd.get_msg_received(idMembre)
    nc= '''<div class="card">
                <div class="card-header">
                    <div class="card-title">Messages reçus</div>
                </div>
                <div class="card-body">
                    <div class="list-group">'''+msg_recus(dico_msg)+'''</div>
                </div>
            </div>'''
    return nc

def send_card():
    idMembre = COOKIE["idMembre"].value
    dico_msg = bdd.get_msg_send(idMembre)
    sc= '''<div class="card">
                <div class="card-header">
                    <div class="card-title">Messages envoyés</div>
                </div>
                <div class="card-body">
                    <div class="list-group">'''+msg_envoyes(dico_msg)+'''</div>
                </div>
            </div>'''
    return sc

def msg_recus(dico_msg):
    code_html = '''<table>'''
    for idMessage in dico_msg:
        idDestinateur = int(dico_msg[idMessage]["idDestinateur"])
        dico_membres = bdd.get_membres()
        nom_dest, prenom_dest, date = dico_membres[idDestinateur]["nom"], dico_membres[idDestinateur]["prenom"],dico_msg[idMessage]["date"]
        description_msg = date+' ) par : '+nom_dest+" "+prenom_dest
        color='info'
        if int(dico_msg[idMessage]["lu"])==0:
            color = "default"
        modal_button = '''  
                            <button type="button" id="btn_msg_received'''+str(idMessage)+'''" class="btn btn-'''+color+'''"  data-toggle="modal" data-target="#exampleModalCenter'''+str(idMessage)+'''">
                              <i class="la la-envelope"></i>'''+" ( "+description_msg+'''
                            </button>              
                            <div class="modal fade" id="exampleModalCenter'''+str(idMessage)+'''" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle'''+str(idMessage)+'''" aria-hidden="true">
                              <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                  <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalCenterTitle'''+str(idMessage)+'''">Message</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">&times;</span>
                                    </button>
                                  </div>
                                  <div id="'''+str(idMessage)+'''" class="modal-body">Message reçu par '''+nom_dest+" "+prenom_dest+' : '+dico_msg[idMessage]["msg"]+'''
                                  </div>
                                  <form action="'''+chemin+'''/python/notifications.py/msg_lu" method="POST">
                                      <input type="hidden" name="input_msg_received" id="input_msg_received'''+str(idMessage)+'''" />
                                      <div class="modal-footer">
                                        <a class="btn btn-primary" href="'''+chemin+'''/python/contacter.py">Répondre</a>
                                        <button class="btn btn-secondary">Close</button>
                                      </div>
                                  </form>
                                </div>
                              </div>
                            </div>'''
        code_html+='''<tr>
                        <td>'''+modal_button+'''</td>
                        <td>
                        <div class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Action</a>
                            <div class="dropdown-menu">
                              <a class="dropdown-item" href="'''+chemin+'''/python/contacter.py">Répondre</a>'''
        code_html+='''        <form action="'''+chemin+'''/python/notifications.py/msg_non_lu" method="POST">
                                    <button id="button_lu_msg" class="dropdown-item" name="idMessage_received" value="'''+str(idMessage)+'''" href="#">Marquer comme non lu</button>
                              </form>
                              <div class="dropdown-divider"></div>
                              <form action="'''+chemin+'''/python/notifications.py/supprimer_msg_received" method="POST">
                                    <button id="button_delete_msg_received'''+str(idMessage)+'''" class="dropdown-item" name="idMessage_received" value="'''+str(idMessage)+'''">Supprimer</button>
                              </form>
                            </div>
                        </div>
                        </td>
                        </tr>'''
    code_html+= '''</table>'''
    return code_html

def msg_non_lu(idMessage_received=''):
    bdd.change_msg_lu(idMessage_received,0)
    raise HTTP_REDIRECTION(chemin + '/python/notifications.py')

def msg_lu(input_msg_received=''):
    bdd.change_msg_lu(input_msg_received,1)
    raise HTTP_REDIRECTION(chemin + '/python/notifications.py')

def msg_envoyes(dico_msg):
    code_html = '''<table>'''
    for idMessage in dico_msg:
        idDestinataire = int(dico_msg[idMessage]["idDestinataire"])
        dico_membres = bdd.get_membres()
        nom_dest, prenom_dest, date = dico_membres[idDestinataire]["nom"], dico_membres[idDestinataire]["prenom"],dico_msg[idMessage]["date"]
        description_msg = date+' ) pour : '+nom_dest+" "+prenom_dest
        color = 'info'
        modal_button = '''  
                            <button type="button" class="btn btn-''' + color + '''"  data-toggle="modal" data-target="#exampleModalCenter_send''' + str(idMessage) + '''">
                              <i class="la la-envelope"></i>''' " ( "+ description_msg + '''
                            </button>              
                            <div class="modal fade" id="exampleModalCenter_send''' + str(idMessage) + '''" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle_send''' + str(idMessage) + '''" aria-hidden="true">
                              <div class="modal-dialog modal-dialog-centered" role="document">
                                <div class="modal-content">
                                  <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalCenterTitle_send''' + str(idMessage) + '''">Message</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">&times;</span>
                                    </button>
                                  </div>
                                  <div id="''' + str(idMessage) + '''" class="modal-body">Message envoyé à ''' + nom_dest + " " + prenom_dest + ' : ' + dico_msg[idMessage]["msg"] + '''
                                  </div>
                                  <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                  </div>
                                </div>
                              </div>
                            </div>'''
        code_html += '''<tr>
                        <td>''' + modal_button + '''</td>
                        <td>
                        <div class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Action</a>
                            <div class="dropdown-menu">
                              <a class="dropdown-item" href="''' + chemin + '''/python/contacter.py">Répondre</a>'''
        code_html += '''      <div class="dropdown-divider"></div>
                              <form action="''' + chemin + '''/python/notifications.py/supprimer_msg_send" method="POST">
                                    <button id="button_delete_msg_send''' + str(idMessage) + '''" class="dropdown-item" name="idMessage_send" value="''' + str(idMessage) + '''">Supprimer</button>
                              </form>
                            </div>
                        </div>
                        </td>
                        </tr>'''
    code_html += '''</table>'''
    return code_html

def supprimer_msg_send(idMessage_send=''):
    bdd.delete_msg(idMessage_send)
    raise HTTP_REDIRECTION(chemin + '/python/notifications.py')

def supprimer_msg_received(idMessage_received=''):
    bdd.delete_msg(idMessage_received)
    raise HTTP_REDIRECTION(chemin + '/python/notifications.py')

def footer():
    f1=''
    idMembre = COOKIE["idMembre"].value
    dico_msg = bdd.get_msg_received(idMembre)
    for id in dico_msg:
        msgi = "msg_received_"+str(id)
        btn_msg = "btn_msg_received"+ str(id)
        f1+='''
            <script>
            document.getElementById("'''+btn_msg+'''").onclick = function() {myFunction'''+msgi+'''()};
            function myFunction'''+msgi+'''() {
                $("#input_msg_received'''+str(id)+'''").val('''+str(id)+''');
                }
            </script>
        '''
    return f1

def main_panel():
    vmain_panel='''<div class="main-panel">
                        <div class="content">
                            <div class="container-fluid">
                                <h4 class="page-title">Notifications</h4>
                                <div class="row">
                                    <div class="col-md-6">'''
    vmain_panel+=received_card()
    vmain_panel+='</div> <div class="col-md-6">'
    vmain_panel+=send_card()
    vmain_panel+='</div></div></div>'
    vmain_panel+=footer()
    vmain_panel+='</div></div>'
    return vmain_panel
