template = Import('template.py')
conf = Import('../data/config.py')
bdd = Import('../data/bdd.py')
cookies = Import('cookies.py')
chemin = conf.chemin()


def index():
    if "nom" in COOKIE:
        result = template.entete(chemin,'CB - Paramètres')
        result += template.main_header(chemin)
        result += template.sidebar(7, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')

def modif_login_card():
    amc='''     <div class="card">
                    <div class="card-header">
                        <div class="card-title">Email</div>
                    </div>
                    <div class="card-body">
                         <form method="post" action="'''+chemin+'''/python/parametres.py/modif_login">'''

    if "notif_login" in COOKIE :
        amc+= COOKIE["notif_login"].value

    amc+= '''
                            <div class="form-group">
                                <input type="email" class="form-control" name="login_entered" placeholder="Ancien Email">
                            </div>
                            <div class="form-group">
                                <input type="email" class="form-control" name="login_new" placeholder="Nouvel Email">
                            </div>
                            <div class="card-action">
                                <button class="btn btn-success">Modifier mon Email</button>
                            </div>
                        </form>
                    </div>
                </div>'''
    cookies.erase("notif_login")
    return amc

def modif_login(login_entered='',login_new=''):
    login_true = str(COOKIE["login"].value)
    nom = str(COOKIE["nom"].value)
    admin = int(COOKIE["admin"].value)
    idMembre = str(int(bdd.get_idMembre(login_true,nom, admin)[0]))
    if login_true == login_entered:
        cookies.set_cookie("login", login_new)
        bdd.change_login(idMembre,login_new, admin)
        cookies.set_cookie("notif_login",'<div class="alert alert-success" role="alert"> Email changé </div>')
        raise HTTP_REDIRECTION(chemin + '/python/parametres.py')
    else:
        cookies.set_cookie("notif_login",'<div class="alert alert-danger" role="alert"> Ancien email incorrect </div>')
        raise HTTP_REDIRECTION(chemin + '/python/parametres.py')

def modif_pwd_card():
    cec='''<div class="card">
                <div class="card-header">
                    <div class="card-title">Mot de passe</div>
                </div>
                <div class="card-body">
                    <form method="post" action="'''+chemin+'''/python/parametres.py/modif_pwd">'''
    if "notif_pwd" in COOKIE :
        cec+= COOKIE["notif_pwd"].value
                        
    cec+= '''           <div class="form-group">
                            <input type="password" class="form-control" name="pwd_entered" placeholder="Ancien Mot de passe">
                        </div>
                        <div class="form-group">
                            <input type="password" class="form-control" name="pwd_new" placeholder="Nouveau Mot de passe">
                        </div>
                        <div class="card-action">
                            <button class="btn btn-success">Modifier mon Mot de passe</button>
                        </div>	
                    </form>							
                </div>
            </div>'''
    cookies.erase("notif_pwd")
    return cec

def modif_pwd(pwd_entered='',pwd_new=''):
    login_true = str(COOKIE["login"].value)
    nom = str(COOKIE["nom"].value)
    admin = int(COOKIE["admin"].value)
    idMembre = str(int(bdd.get_idMembre(login_true, nom, admin )[0]))
    if bdd.verif_connect(login_true,pwd_entered):
        bdd.change_pwd(idMembre, pwd_new,admin)
        cookies.set_cookie("notif_pwd", '<div class="alert alert-success" role="alert"> Mot de passe changé </div>')
        raise HTTP_REDIRECTION(chemin + '/python/parametres.py')
    else:
        cookies.set_cookie("notif_pwd", '<div class="alert alert-danger" role="alert"> Ancien mot de passe incorrect </div>')
        raise HTTP_REDIRECTION(chemin + '/python/parametres.py')

def footer():
    f=''' '''
    return f

def main_panel():
    vmain_panel='''<div class="main-panel">
                        <div class="content">
                            <div class="container-fluid">
                                <h4 class="page-title">Modifier mes identifiants personnels</h4>
                                <div class="row">
                                    <div class="col-md-6">'''
    vmain_panel+=modif_login_card()
    vmain_panel+='</div> <div class="col-md-6">'
    vmain_panel+=modif_pwd_card()
    vmain_panel+='</div></div></div>'
    vmain_panel+=footer()
    vmain_panel+='</div></div>'
    return vmain_panel