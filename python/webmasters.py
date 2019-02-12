template = Import('template.py')
conf = Import('../data/config.py')
cookies = Import('../python/cookies.py')
chemin = conf.chemin()

def index():
    if "nom" in COOKIE :
        result = template.entete(chemin,'CB - Webmasters')
        result += template.main_header(chemin)
        result += template.sidebar(6, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


def video_card():
    return ''' '''

def cv_card():
    code_html ='''  
                    <div class="row">
                        <div class="col-md-6">    
                            <div class="card" style="width:400px">
                              <img class="card-img-top" src="'''+chemin+'''/cv_webmaster/photo_nadir.png" alt="Card image">
                              <div class="card-body">
                                <h4 class="card-title">Nadir RANEM</h4>
                                <p class="card-text">Nadir RANEM, élève ENAC et responsable de la gestion de base de donnée ainsi que de la partie responsive</p>
                                <a href="'''+chemin+'''/cv_webmaster/cv_nadir.py" class="btn btn-primary" target="_blank">Version html</a>
                                <a href="'''+chemin+'''/cv_webmaster/cv_nadir.pdf" class="btn btn-primary" target="_blank">Version pdf</a>
                              </div>
                            </div>
                            <div class="card" style="width:400px">
                              <img class="card-img-top" src="'''+chemin+'''/cv_webmaster/photo_amine.jpg" height="440" alt="Card image">
                              <div class="card-body">
                                <h4 class="card-title">Amine Bouamrene</h4>
                                <p class="card-text">Amine Bouamrene, élève ENAC et responsable de la gestion de base de donnée ainsi que de la partie responsive</p>
                                <a href="'''+chemin+'''/cv_webmaster/cv_amine.py" class="btn btn-primary" target="_blank">Version html</a>
                                <a href="'''+chemin+'''/cv_webmaster/cv_amine.pdf" class="btn btn-primary" target="_blank">Version pdf</a>
                              </div>
                            </div>
                        </div>
                        <div class="col-md-6">    
                            <div class="card" style="width:400px">
                              <img class="card-img-top" src="'''+chemin+'''/cv_webmaster/photo_aymeric.jpg" height="440" alt="Card image">
                              <div class="card-body">
                                <h4 class="card-title">Aymeric Lecalvez</h4>
                                <p class="card-text">Aymeric Lecalvez, élève ENAC et responsable de la gestion de base de donnée ainsi que de la partie responsive</p>
                                <a href="'''+chemin+'''/cv_webmaster/cv_abdoulaye.py" class="btn btn-primary" target="_blank">Version html</a>
                                <a href="'''+chemin+'''/cv_webmaster/cv_aymeric.pdf" class="btn btn-primary" target="_blank">Version pdf</a>
                              </div>
                            </div> 
                            <div class="card" style="width:400px">
                              <img class="card-img-top" src="'''+chemin+'''/cv_webmaster/photo_abdoulaye.jpg" height="440" alt="Card image">
                              <div class="card-body">
                                <h4 class="card-title">Abdoulaye Diop</h4>
                                <p class="card-text">Abdoulaye Diop, élève ENAC et responsable de la gestion de base de donnée ainsi que de la partie responsive</p>
                                <a href="'''+chemin+'''/cv_webmaster/cv_abdoulaye.py" class="btn btn-primary" target="_blank">Version html</a>
                                <a href="'''+chemin+'''/cv_webmaster/cv_abdoulaye.pdf" class="btn btn-primary" target="_blank">Version pdf</a>
                              </div>
                            </div>
                        </div>
                    </div>'''
    return code_html


def footer():
    f1=''''''
    return f1

def main_panel():
    vmain_panel='''<div class="main-panel">
                        <div class="content">
                            <div class="container-fluid">
                                <h4 class="page-title">Webmasters</h4>'''
    vmain_panel+=video_card()
    vmain_panel+=cv_card()
    vmain_panel+=footer()
    vmain_panel+='</div></div></div>'
    return vmain_panel
