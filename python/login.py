conf=Import('../data/config.py')
bdd=Import('../data/bdd.py')
cookies=Import('../python/cookies.py')
chemin=conf.chemin()

def index():
    deconnecter()
    result='''
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>CB-Connexion</title>
            <meta charset="UTF-8">
            <!--===============================================================================================-->	
            <link rel="icon" type="image/png" href="'''+chemin+'''/login/images/icons/favicon.ico"/>
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="'''+chemin+'''/login/vendor/bootstrap/css/bootstrap.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="'''+chemin+'''/login/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
        <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="'''+chemin+'''/login/css/main.css">
        <!--===============================================================================================-->
        </head>
        <body>
            
            <div class="limiter">
                <div class="container-login100">
                    <div class="wrap-login100">
                        <div class="login100-pic js-tilt" data-tilt>
                            <img src="'''+chemin+'''/login/images/img-01.png" alt="IMG">
                        </div>
        
                        <form method="post" action="'''+chemin+'''/python/login.py/verif">
                            <span class="login100-form-title">
                                Connexion Equipage
                            </span>
        
                            <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                                <input class="input100" type="text" name="login" placeholder="email">
                                <span class="focus-input100"></span>
                                <span class="symbol-input100">
                                    <i class="fa fa-user" aria-hidden="true"></i>
                                </span>
                            </div>
        
                            <div class="wrap-input100 validate-input" data-validate = "Password is required">
                                <input class="input100" type="password" name="pwd" placeholder="Mot de passe">
                                <span class="focus-input100"></span>
                                <span class="symbol-input100">
                                    <i class="fa fa-lock" aria-hidden="true"></i>
                                </span>
                            </div>
                            
                            <div class="container-login100-form-btn"> 
                                <span class="login100-form-btn">
                                    <button class="button" type="submit">Connexion</button>
                                </span>    
                            </div>
        
                            <div class="text-center p-t-12">
                                <span class="txt1">
                                    Vous avez oublié votre
                                </span>
                                <a class="txt2" href="'''+chemin+'''/python/mdp_recup.py">
                                    Identifiant / Mot de passe?
                                </a>
                            </div>
        
                            <!-- <div class="text-center p-t-136"> -->
                                <!-- <a class="txt2" href="#"> -->
                                    <!-- Create your Account -->
                                    <!-- <i class="fa fa-long-arrow-right m-l-5" aria-hidden="true"></i> -->
                                <!-- </a> -->
                            <!-- </div> -->
                        </form>
                    </div>
                </div>
            </div>
                
        <!--===============================================================================================-->	
            <script src="'''+chemin+'''/login/vendor/jquery/jquery-3.2.1.min.js"></script>
        <!--===============================================================================================-->
            <script src="'''+chemin+'''/login/vendor/bootstrap/js/popper.js"></script>
            <script src="'''+chemin+'''/login/vendor/bootstrap/js/bootstrap.min.js"></script>
        <!--===============================================================================================-->
            <script src="'''+chemin+'''/login/vendor/tilt/tilt.jquery.min.js"></script>
            <script >
                $('.js-tilt').tilt({
                    scale: 1.1
                })
            </script>
        <!--===============================================================================================-->
            <script src="'''+chemin+'''/login/js/main.js"></script>
        
        </body>
        </html>'''
    return result

def verif(login='',pwd=''):
    resultat = bdd.verif_connect(login, pwd)
    if resultat:
        cookies.set_cookie("nom", resultat[1].decode("utf-8"))
        cookies.set_cookie("prenom", resultat[1].decode("utf-8"))
        cookies.set_cookie("login", login)
        raise HTTP_REDIRECTION(chemin + '/index.py')
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')

def verif(login='',pwd=''):
    resultat = bdd.verif_connect(login, pwd)
    resultat_admin = bdd.verif_connect_admin(login, pwd)
    cookies.set_cookie("login", login)
    if resultat_admin:
        cookies.set_cookie("idMembre", resultat_admin[0])
        cookies.set_cookie("nom", resultat_admin[1])
        cookies.set_cookie("prenom", resultat_admin[2])
        cookies.set_cookie("admin", 1)

        raise HTTP_REDIRECTION(chemin + '/index.py')
    elif resultat:
        cookies.set_cookie("idMembre", resultat[0])
        cookies.set_cookie("nom", resultat[1].decode("utf-8"))
        cookies.set_cookie("prenom", resultat[2].decode("utf-8"))
        cookies.set_cookie("admin", 0)
        cookies.set_cookie("idEquipe", resultat[3])
        cookies.set_cookie("mode", 0)
        raise HTTP_REDIRECTION(chemin + '/index.py')
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')

def deconnecter():
    if "nom" in COOKIE:
        cookies.erase("idMembre")
        cookies.erase("nom")
        cookies.erase("prenom")
        cookies.erase("login")
        cookies.erase("admin")
        cookies.erase("idEquipe")