bdd = Import('/bouamrene_diop_lecalvez_ranem/data/bdd.py')
simulation = Import('/bouamrene_diop_lecalvez_ranem/python/simulation.py')

if COOKIE["admin"].value == '0':
    idAvion = bdd.get_idAvion(COOKIE['idEquipe'].value)
else:
    idAvion = ""

def map():
    v = '''
    <div class="mapcontainer">
        <div  id="map"></div>
    </div>
    <script>
    var pos = {lat:45, lng:1};
    var positions=[];
    var markers = [];
    var map;
    function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          zoom: 6,
          center: {lat: 46.5, lng: 1},
          mapTypeId: 'roadmap',
          minZoom: 4
        });
    
        ''' + zone1() + zone2() + zone3() + zone4() + zone5() + zone6() + add_aerodrome() + add_trajet() +add_aeronef()+ '''
    
        '''
    for id in bdd.get_avions():
        v += '''
        
        function getPosition'''+str(id)+'''(str) {
            var link = "/bouamrene_diop_lecalvez_ranem/data/bdd.py/get_position";
            //Make the actual connection.
            var xmlHttpReq = false;
            var self = this;
            self.name = "idAvion"
            // Mozilla/Safari
            if (window.XMLHttpRequest) {
                self.xmlHttpReq = new XMLHttpRequest();
            }
            // IE
            else if (window.ActiveXObject) {
                self.xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
            }
            self.xmlHttpReq.open('POST', link, true);
            self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            self.xmlHttpReq.onreadystatechange = function() {
                if (self.xmlHttpReq.readyState == 4) { //ready state 4 means its complete.
                    var l = self.xmlHttpReq.responseText;
                    change_result(result, l);
                }
            }
            self.xmlHttpReq.send('idAvion=' +str);
        };'''

    v +='''
        var iDInterval1 = setInterval(function() {
            //d = new Date()
            //if( d.getMinutes() >= 22){
                moveMarker'''+str(idAvion)+'''(map, marker);
                clearInterval(iDInterval1);
            //}
        }, 500);
            
        var iDInterval2 = setInterval(function() {
             getDistance(idAvion);
        }, 1000);
    };

    function change_result(result, str){
        result[0] = str
    };
    
    function getDistance(str) {
        var link = "/bouamrene_diop_lecalvez_ranem/data/bdd.py/get_distance";
        //Make the actual connection.
        var xmlHttpReq = false;
        var self = this;
        self.name = "idAvion"
        // Mozilla/Safari
        if (window.XMLHttpRequest) {
            self.xmlHttpReq = new XMLHttpRequest();
        }
        // IE
        else if (window.ActiveXObject) {
            self.xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
        }
        self.xmlHttpReq.open('POST', link, true);
        self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        self.xmlHttpReq.onreadystatechange = function() {
            if (self.xmlHttpReq.readyState == 4) { //ready state 4 means its complete.
                var l = self.xmlHttpReq.responseText;
                if (l!=""){
                    document.getElementById("distance_shower").innerHTML = l + " Nm";
                }
            }
        }
        self.xmlHttpReq.send('idAvion=' +str);
    };
    
    function getZones(str) {
        var link = "/bouamrene_diop_lecalvez_ranem/data/bdd.py/get_zones";
        //Make the actual connection.
        var xmlHttpReq = false;
        var self = this;
        self.name = "idAvion"
        // Mozilla/Safari
        if (window.XMLHttpRequest) {
            self.xmlHttpReq = new XMLHttpRequest();
        }
        // IE
        else if (window.ActiveXObject) {
            self.xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
        }
        self.xmlHttpReq.open('POST', link, true);
        self.xmlHttpReq.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        self.xmlHttpReq.onreadystatechange = function() {
            if (self.xmlHttpReq.readyState == 4) { //ready state 4 means its complete.
                var l = self.xmlHttpReq.responseText;
                if (l!=""){
                    var l2 = l.split(",");
                    var zones = ["1", "2", "3", "4", "5", "6"];
                    var visited = "";
                    var not_visited = "";
                    zones.forEach(function(zone){
                        if (zone in l2){
                            visited += zone+","
                        }else{
                            not_visited += zone+","
                        }
                    });
                    document.getElementById("a_visiter").innerHTML = not_visited;
                    document.getElementById("visite").innerHTML = visited;
                }
            }
        }
        self.xmlHttpReq.send('idAvion=' +str);
    };

    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyC5BN2p1aX9BM44_17YoiN8J2tqTuRNKlk&libraries=geometry&callback=initMap"
        async defer></script>

        '''
    return v


def construct_zone():
    return '''// Construct the polygon.
    var zone = new google.maps.Polygon({
      paths: zonecoords,
      strokeColor: '#FF50CB',
      strokeOpacity: 0.4,
      strokeWeight: 2,
      fillColor: '#FF50CB',
      fillOpacity: 0.20
    });
    zone.setMap(map);
    '''


def zone6():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 48, lng: 1},
        {lat: 48, lng: 4},
        {lat: 45.5, lng: 4},
        {lat: 45.5, lng: 1}

    ];

    ''' + construct_zone()
    return v


def zone2():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 49, lng: -1.67},
        {lat: 46, lng: -1.67},
        {lat: 47.2, lng: -3},
        {lat: 48, lng: -5},
        {lat: 48.5, lng: -5},
        {lat: 49, lng: -4}

    ];

    ''' + construct_zone()
    return v


def zone1():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 49.75, lng: 5.5},
        {lat: 49.75, lng: 0},
        {lat: 50.2, lng: 1.2},
        {lat: 51, lng: 1.4},
        {lat: 51.2, lng: 2.5},
        {lat: 50.2, lng: 5}

    ];

    ''' + construct_zone()
    return v


def zone3():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 44.5, lng: 2},
        {lat: 42.1, lng: 2},
        {lat: 43, lng: -2},
        {lat: 44.5, lng: -1.2}

    ];

    ''' + construct_zone()
    return v


def zone4():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 44.5, lng: 5},
        {lat: 43.2, lng: 5},
        {lat: 42.9, lng: 6.1},
        {lat: 43.5, lng: 8},
        {lat: 44.5, lng: 7.3}

    ];

    ''' + construct_zone()
    return v


def zone5():
    v = '''
    // Define the LatLng coordinates for the polygon.
    var zonecoords = [
        {lat: 49.6, lng: 6},
        {lat: 46.5, lng: 6},
        {lat: 47.3, lng: 7.5},
        {lat: 49, lng: 8.5},
        {lat: 49.6, lng: 6.5}

    ];

    ''' + construct_zone()
    return v


def add_aerodrome():
    v = '''
    var aerodromes = [];
    var image = {
        // Adresse de l'icône personnalisée
        url: '/bouamrene_diop_lecalvez_ranem/assets/img/concentric-circles.png',
        // Taille de l'icône personnalisée
        size: new google.maps.Size(16, 16),
        // Origine de l'image, souvent (0, 0)
        origin: new google.maps.Point(0,0),
        // L'ancre de l'image. Correspond au point de l'image que l'on raccroche à la carte.
        anchor: new google.maps.Point(8, 8)
        };'''
    dict = bdd.get_aerodromes()
    for idAerodrome, (lat, lon) in dict.items():
        v += '''
    aerodromes.push({idAerodrome:"''' + idAerodrome + '''",position:{lat:''' + str(lat) + ''',lng:''' + str(lon) + '''}});
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(''' + str(lat) + "," + str(lon) + '''),
        map: map,
        icon: image,
        title: "''' + str(idAerodrome) + '''"
    });
        '''

    return v


def add_trajet():
    strTrajet = bdd.get_trajet(idAvion)
    v = '''
    var idAvion = "'''+ idAvion +'''";
    var trajet = ['''
    for id in strTrajet.strip().split():
        v+= '''"'''+id+'''",'''
    v+= '''];
    var flightPlanCoordinates = [];
    trajet.forEach(function(id){
        aerodromes.forEach(function(aerodrome){
            if (aerodrome.idAerodrome==id){
                flightPlanCoordinates.push(aerodrome.position)
            }
        });
    });
    var flightPath = new google.maps.Polyline({
        path: flightPlanCoordinates,
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 0.6,
        strokeWeight: 2
        });
    flightPath.setMap(map);
    var idAvions =[ '''
    for val in bdd.get_avions():
        v+= '''"'''+val+'''",'''
    v+= '''];
    '''
    return v


def add_aeronef():
    v = '''
    var pathIcon = 'm105.67322,-78l-124.03125,53.625c-10.38228,-6.92107 -34.20059,-21.27539 -38.90546,-23.44898c-39.44003,-18.22079 -36.9454,14.73107 -20.34924,24.6052c4.53917,2.70065 27.72351,17.17823 43.47345, 26.37502l17.90625,133.93749l22.21875,13.15625l11.53125,-120.93749l71.53125, 36.68749l3.84372,39.21875l14.53128,8.625l11.09372,-42.40625l0.12503,0.0625l30.8125,-31.53123l-14.875,-8.00001l-35.625,16.90626l-68.28125,-42.43751l97.6875,-72.18749l-22.6875,-12.25z'
    var result = [""];
    var i = 0;'''
    for id in bdd.get_avions():
        if id == idAvion:
            v += '''
    var marker'''+str(id)+''' = new google.maps.Marker({
        position: map.center,
        map: map,
        icon: { path:pathIcon,
            scale: 0.1,
            strokeColor: '#000099',
            strokeOpacity: 1.0,
            strokeWeight: 1,
            fillColor: '#000099',
            fillOpacity: 0.6,
            rotation:150
        },
        anchor : (0.5, 0.5),
        title : "'''+str(id)+'''"
    });
    var currentPosition = ""
    var rotation = 150;
    function moveMarker'''+str(id)+'''(map, marker){
        setInterval(function(){
            if (currentPosition!=""){
                getPosition'''+str(id)+'''("'''+str(id)+'''");
                if (result[0]!=""){
                    m = result[0].split(",");
                    var nextPosition = {lat: parseFloat(m[0]), lng: parseFloat(m[1])};
                    marker'''+str(id)+'''.setPosition(nextPosition)
                    if (nextPosition.lat != currentPosition.lat){
                        rotation = 150 - Math.atan2((nextPosition.lat - currentPosition.lat),(nextPosition.lng - currentPosition.lng))*180/Math.PI
                    }
                    marker'''+str(id)+'''.setIcon({ 
                        path:pathIcon,
                        scale: 0.1,
                        strokeColor: '#000099',
                        strokeOpacity: 1.0,
                        strokeWeight: 1,
                        fillColor: '#000099',
                        fillOpacity: 0.6,
                        rotation:rotation
                    });
                    currentPosition = nextPosition
                }
            } else {
                getPosition'''+str(id)+'''("'''+str(id)+'''");
                if (result[0]!=""){
                    var m = result[0].split(",");
                    currentPosition = {lat: parseFloat(m[0]), lng: parseFloat(m[1])};
                    marker.setPosition(currentPosition)
                }
            }
        }, 1000)
    };
    '''
    return v

