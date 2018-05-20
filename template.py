c = Import('/bouamrene_diop_lecalvez_ranem/python/cookies.py')
bdd = Import('/bouamrene_diop_lecalvez_ranem/data/bdd.py')


def entete(chemin='', titre='CB'):
    ventete = '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
            <title>''' + titre + '''</title>
            <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no' name='viewport' />
            <meta charset="UTF-8" />
            <meta name="viewport" content="initial-scale=1.0">
            <meta charset="utf-8">
            <link rel="stylesheet" href=" ''' + chemin + '''/assets/css/bootstrap.min.css">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i">'''
    if int(COOKIE["mode"].value) == 1:
        ventete+='''<link rel="stylesheet" href=" ''' + chemin + '''/assets/css/ready_nuit.css">'''
    else:
        ventete+='''<link rel="stylesheet" href=" ''' + chemin + '''/assets/css/ready.css">'''

    ventete+=    '''<link rel="stylesheet" href=" ''' + chemin + '''/assets/css/demo.css">
        </head>
        <body>
        <div class="wrapper">'''

    return ventete


def sidebar(num_page, chemin=''):
    prenom = COOKIE["prenom"].value
    nom = COOKIE["nom"].value
    admin = COOKIE["admin"].value
    idMembre = COOKIE["idMembre"].value
    nb_msg_non_lu = str(bdd.count_msg_non_lu(idMembre)[0])
    add_user = ''
    l1 = [1, 2, 3, 4, 5, 6,7]
    l2 = []
    for i in l1:
        if i == num_page:
            l2.append("active")
        else:
            l2.append("")
    sb = '''
    <div class="sidebar">
        <div class="scrollbar-inner sidebar-wrapper">
            <div class="user">
                <div class="photo">
					<img src="''' + chemin + '''/img/concentric-circles.png">
                </div>
                <div class="info">
                    <a class="" data-toggle="collapse" href="#collapseExample" aria-expanded="true">
                        <span>
                            <span class="user-level">''' + prenom + " " + nom + '''</span>
                            <span class="caret"></span>
                        </span>
                    </a>
                    <div class="clearfix"></div>

                    <div class="collapse in" id="collapseExample" aria-expanded="true" style="">
                        <ul class="nav">
                            '''
    if int(admin) == 0:
        sb += '''    <li>
                                <a href="''' + chemin + '''/python/menu_equipe.py">
                                    <span class="link-collapse">Mon équipe</span>
                                </a>
                            </li>'''

    sb += '''                <li>
                                <a href=" ''' + chemin + '''/python/parametres.py">
                                    <span class="link-collapse">Paramètres</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <ul class="nav">
                <li class="nav-item ''' + l2[0] + '''">
                    <a href=" ''' + chemin + '''/index.py">
                        <i class="la la-plane"></i>
                        <p>Accueil</p>
                    </a>
                </li>'''
    if int(admin) == 0:
        sb += '''
                <li class="nav-item ''' + l2[1] + '''">
                    <a href=" ''' + chemin + '''/python/contacter.py">
                        <i class="la la-envelope"></i>
                        <p>Contacter un coéquipier</p>
                    </a>
                </li>'''
    sb += '''
                <li class="nav-item ''' + l2[2] + '''">
                    <a href=" ''' + chemin + '''/python/classement.py">
                        <i class="la la-th"></i>
                        <p>Classement</p>
                    </a>
                </li>
                <li class="nav-item ''' + l2[3] + '''">
                    <a href="''' + chemin + '''/python/notifications.py">
                        <i class="la la-bell"></i>
                        <p>Notifications</p>'''
    if nb_msg_non_lu!='0':
        sb+=         '''<span class="badge badge-success">'''+nb_msg_non_lu+'''</span>'''

    sb+=         '''</a>
                </li>'''

    if int(admin) == 1:
        add_user = '''
                <li class="nav-item ''' + l2[4] + '''">
                    <a href="''' + chemin + '''/python/ajouter_equipe.py">
                        <i class="la la-user-plus"></i>
                        <p>Ajouter membre/équipe</p>
                    </a>
				</li>'''
    sb +='''
                <li class="nav-item ''' + l2[5] + '''">
                    <a href="''' + chemin + '''/python/webmasters.py">
                        <i class="la la-pencil-square"></i>
                        <p>Webmasters</p>
                    </a>
				</li>'''
    fin = '''</ul>
        </div>
    </div>
    '''
    return sb + add_user + fin


def main_header(chemin=''):
    prenom = COOKIE["prenom"].value
    nom = COOKIE["nom"].value
    login = COOKIE["login"].value
    admin = COOKIE["admin"].value
    mh = '''
    <div class="main-header">
        <div class="logo-header">
            <a href="''' + chemin + '''" class="logo">
                Coupe Breitling
            </a>
            <button class="navbar-toggler sidenav-toggler ml-auto" type="button" data-toggle="collapse"
                    data-target="collapse" aria-controls="sidebar" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <button class="topbar-toggler more"><i class="la la-ellipsis-v"></i></button>
        </div>
        <nav class="navbar navbar-header navbar-expand-lg">
            <div class="container-fluid">
                <ul class="navbar-nav topbar-nav ml-md-auto align-items-center">
                    <li class="nav-item dropdown">
                        <a class="dropdown-toggle profile-pic" data-toggle="dropdown" href="#" aria-expanded="false">
                            <i class="la la-user la-2x"></i><span>''' + prenom + " " + nom + '''</span></a>
                        <ul class="dropdown-menu dropdown-user">
                            <li>
                                <div class="user-box">
                                    <div class="u-text">
                                        <h4>''' + prenom + " " + nom + '''</h4>
                                        <p class="text-muted">''' + login + '''</p>
                                    </div>
                                </div>
                            </li>
                            <div class="dropdown-divider"></div>'''
    if int(admin) == 0:
        mh += '''             <a class="dropdown-item" href="''' + chemin + '''/python/menu_equipe.py"><i class="ti-team"></i> Mon Equipe</a>
                            <div class="dropdown-divider"></div>'''
    mh += '''
                            <a class="dropdown-item" href="''' + chemin + '''/python/parametres.py"><i class="ti-settings"></i> Paramètres</a>
                            <div class="dropdown-divider"></div>
                            <form action="'''+chemin+'''/python/template.py/change_mode" method="GET">
                                <button class="dropdown-item"><i class="ti-settings"></i> Mode Nuit/Jour</button>
                            </form>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item" href="''' + chemin + '''/python/login.py" ><i class="fa fa-power-off"></i> Déconnexion</a>
                        </ul>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
    '''
    return mh

def change_mode():
    if int(COOKIE["mode"].value)==1:
        c.set_cookie("mode",0)
    else:
        c.set_cookie("mode",1)
    raise HTTP_REDIRECTION('/bouamrene_diop_lecalvez_ranem/python/contacter.py')


def footer(chemin=''):
    vfooter = '''        
        <footer class="footer" >&ALl right reserved ENAC</footer>
    </div>
    <script src=" ''' + chemin + '''/assets/js/core/jquery.3.2.1.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/jquery-ui-1.12.1.custom/jquery-ui.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/core/popper.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/core/bootstrap.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/chartist/chartist.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/chartist/plugin/chartist-plugin-tooltip.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/bootstrap-toggle/bootstrap-toggle.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/jquery-mapael/jquery.mapael.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/jquery-mapael/maps/world_countries.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/chart-circle/circles.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/plugin/jquery-scrollbar/jquery.scrollbar.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/ready.min.js"></script>
    <script src=" ''' + chemin + '''/assets/js/demo.js"></script>
    <script src=" ''' + chemin + '''/assets/js/ajouter_eq.js"></script>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC5BN2p1aX9BM44_17YoiN8J2tqTuRNKlk&callback=initMap"
    async defer></script>

    </body>
    </html>
        '''
    return vfooter

# <script src=" ''' + chemin + '''/assets/js/plugin/bootstrap-notify/bootstrap-notify.min.js"></script>
