bdd = Import('/bouamrene_diop_lecalvez_ranem/data/bdd.py')
template = Import('/bouamrene_diop_lecalvez_ranem/python/template.py')
conf = Import('/bouamrene_diop_lecalvez_ranem/data/config.py')
chemin = conf.chemin()
google_map = Import('/bouamrene_diop_lecalvez_ranem/python/google_map.py')


def index():
    if "nom" in COOKIE:
        result = template.entete(chemin,'CB-Accueil')
        result += template.main_header(chemin)
        result += template.sidebar(2, chemin)
        result += main_panel()
        result += template.footer(chemin)
        return result
    else:
        raise HTTP_REDIRECTION(chemin + '/python/login.py')


def main_panel():
    d = calcul_classement()
    i = 0
    v = '''
    <div class="main-panel">
        <div class="content">
            <div class="container-fluid">
                <h4 class="page-title">Classement</h4>
                <div class="row">
                    <div class="col-md-12">
                        <div class="card">
                            <div class="card-header">
                                <div class="card-title">Classement par équipes</div>
                            </div>
                            <div class="card-body">
                                <table class="table table-head-bg-primary mt-4">
                                    <thead>
                                        <tr>
                                            <th scope="col">#</th>
                                            <th scope="col">Equipe</th>
                                            <th scope="col">Posés décollés</th>
                                            <th scope="col">Distance franchie</th>
                                            <th scope="col">Deduction bonus</th>
                                        </tr>
                                    </thead>
                                    <tbody>'''
    for idAvion, n, dist, dist_bonus in d:
        i += 1
        v += '''
                                        <tr onclick='drawTrajet("'''+bdd.get_trajet(idAvion)+'''");'>
                                            <td>'''+str(i)+'''</td>
                                            <td >'''+bdd.get_name(bdd.get_idEquipe2(idAvion))+'''</td>
                                            <td>'''+str(n)+'''</td>
                                            <td>'''+str(dist)+'''</td>
                                            <td>'''+str(dist_bonus)+'''</td>
                                        </tr>
                                        <tr>
                                        '''
    v+='''
                                    </tbody>
                                </table>
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
                </div>
            </div>
        </div>
    </div>
    '''
    return v

def calcul_classement():
    liste_bonus = ["LFRQ","LFAT","LFTH","LFBZ","LFLB"]
    d = []
    d2 = []
    for idAvion in bdd.get_avions():
        n = 0
        bonus = 0
        zones = []
        for idAerodrome in bdd.get_passages(idAvion):
            n += 1
            j = 0
            if idAerodrome in liste_bonus:
                bonus += 80
            lat, lon, zone = bdd.get_aerodrome(idAerodrome)
            if zone != 0:
                zones.append(zone)
            if lat <= 43.5 and lon >= 8:
                bonus += 80
                j += 1
            if j > 0:
                bonus += 208
        if len(zones)>= 6:
            d.append((idAvion, n, bdd.get_distance(idAvion), float(bdd.get_distance(idAvion)) - bonus))
        else:
            d2.append((idAvion, n, bdd.get_distance(idAvion), float(bdd.get_distance(idAvion)) - bonus))
    d.sort(key= lambda x: x[1], reverse=True)
    d2.sort(key=lambda x: x[1], reverse=True)
    return d+d2

