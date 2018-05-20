template = Import('python/template.py')
google_map = Import('python/google_map.py')
conf = Import('data/config.py')
chemin = conf.chemin()


def index():
    if "nom" in COOKIE:
        result = template.entete(chemin,'CB - Accueil')
        result += template.main_header(chemin)
        result += template.sidebar(1, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


def map_view():
    vmap_view = '''
    <div class="row">
        <div class="col-md-3">
            <div class="card card-stats card-warning">
                <div class="card-body ">
                    <div class="row">
                        <div class="col-5">
                            <div class="icon-big text-center">
                                <i class="la la-users"></i>
                            </div>
                        </div>
                        <div class="col-7 d-flex align-items-center">
                            <div class="numbers">
                                <p class="card-category"> Equipes</p>
                                <h4 class="card-title">17</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card card-stats card-success">
                <div class="card-body ">
                    <div class="row">
                        <div class="col-5">
                            <div class="icon-big text-center">
                                <i class="la la-bar-chart"></i>
                            </div>
                        </div>
                        <div class="col-7 d-flex align-items-center">
                            <div class="numbers">
                                <p class="card-category">Rang</p>
                                <h4 class="card-title">6 ème</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card card-stats card-danger">
                <div class="card-body">
                    <div class="row">
                        <div class="col-5">
                            <div class="icon-big text-center">
                                <i class="la la-certificate"></i>
                            </div>
                        </div>
                        <div class="col-7 d-flex align-items-center">
                            <div class="numbers">
                                <p class="card-category">Meilleurs score</p>
                                <h4 class="card-title">32</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card card-stats card-primary">
                <div class="card-body ">
                    <div class="row">
                        <div class="col-5">
                            <div class="icon-big text-center">
                                <i class="la la-clock-o"></i>
                            </div>
                        </div>
                        <div class="col-7 d-flex align-items-center">
                            <div class="numbers">
                                <p class="card-category">Temps restant</p>
                                <h4 class="card-title">18:09:11</h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header">
                    <h4 class="card-title">Suivi de la trajectoire</h4>
                </div>
                '''+ google_map.map() +'''
            </div>
        </div>
    </div>'''
    return vmap_view


def info_bar():
    ib = '''
        <div class="row row-card-no-pd">
            <div class="col-md-4">
                <div class="card">
                    <div class="card-body">
                        <!-- <p class="fw-bold mt-1">Distance Parcourue</p> -->
                        <h4><b>Distance parcourue<i class="la la-map-pin"></i></b></h4>
                    </div> 
                    <div class="card-footer text-primary">
                        </br><h2><b> 2000 Nm</b></h4>
                    </div>
                </div>
            </div>
            <div class="col-md-5">
                <div class="card">
                    <div class="card-body"></div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card card-stats">
                    <div class="card-body">
                        <p class="fw-bold mt-1">ZONES</p>
                        <div class="row">
                            <div class="col-5">
                                <div class="icon-big text-center icon-warning">
                                    <i class="la la-crosshairs text-danger"></i>
                                </div>
                            </div>
                            <div class="col-7 d-flex align-items-center">
                                <div class="numbers">
                                    <p class="card-category">à visiter</p>
                                    <h4 class="card-title">5,6</h4>
                                </div>
                            </div>
                        </div>
                        <hr/>
                        <div class="row">
                            <div class="col-5">
                                <div class="icon-big text-center">
                                    <i class="la la-check-circle text-success"></i>
                                </div>
                            </div>
                            <div class="col-7 d-flex align-items-center">
                                <div class="numbers">
                                    <p class="card-category">visitée(s)</p>
                                    <h4 class="card-title">1,2,3,4</h4>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    '''
    return ib


def global_stat():
    vglobal_stat = '''
    <div class="row">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h4 class="card-title">Distance parcourue</h4>
                </div>
                <div class="card-body">
                    <div id="salesChart" class="chart"></div>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h4 class="card-title">Distance parcourue</h4>
                </div>
                <div class="card-body">
                    <div id="salesChart" class="chart"></div>
                </div>
            </div>
        </div>
    </div>
    '''
    return vglobal_stat


def main_panel():
    vmain_panel = '''
    <div class="main-panel">
        <div class="content">
            <div class="container-fluid">
                <h4 class="page-title">Accueil</h4>'''
    vmain_panel += map_view()
    vmain_panel += info_bar()
    vmain_panel += global_stat()
    vmain_panel += '''
            </div>
        </div>
    </div>
    '''
    return vmain_panel
