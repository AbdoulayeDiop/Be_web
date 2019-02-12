import time
from threading import Timer
import random
from geopy.distance import great_circle
import mysql.connector
from mysql.connector import errorcode
from lxml import etree

def configBD():
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'ienac17_bouamrene_diop_lecalvez_ranem',
        'raise_on_warnings': True
    }
    return config


config = configBD()


def connexion():
    cnx = ""
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Mauvais login ou mot de passe")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La Base de données n'existe pas.")
        else:
            print(err)
    return cnx


def close_bd(cursor, cnx):
    cursor.close()
    cnx.close()


def get_aerodromes():
    sql = "SELECT idAerodrome, latitude, longitude FROM aerodrome"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        dict = {}
        for idAerodrome, lat, lon in cursor:
            dict[idAerodrome.decode("utf-8")] = (lat, lon)

    except mysql.connector.Error as err:
        dict = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict


def get_aerodromesInZone(zone):
    sql = "SELECT idAerodrome, latitude, longitude FROM aerodrome WHERE aerodrome.zone = %s"
    param = (zone,)

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql, param)
        dict = {}
        for idAerodrome, lat, lon in cursor:
            dict[idAerodrome.decode("utf-8")] = (lat, lon)

    except mysql.connector.Error as err:
        dict = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict


def get_aerodromesBetween(pos1, pos2):
    dict = {}
    for idAerodrome, (lat, lon) in get_aerodromes().items():
        if (lat, lon) != pos1:
            if min(pos1[0], pos2[0]) <= lat <= max(pos1[0], pos2[0]) and min(pos1[1], pos2[1]) <= lon <= max(pos1[1],
                                                                                                             pos2[1]):
                dict[idAerodrome] = (lat, lon)
    return dict

def delete_position(idAvion):
    sql = "DELETE FROM position WHERE idAvion = %s"
    param = (idAvion,)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

def insert_position(idAvion, lat, lon, heure):
    delete_position(idAvion)
    sql = "INSERT INTO `position` VALUES (%s, %s, %s, %s);"
    l = time.localtime(time.time())
    param = (idAvion, lon, lat, int(str(l[3]) + str(l[4]) + str(l[5])))
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()

            print(1)
        except mysql.connector.Error:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

def delete_passages(idAvion):
    sql = "DELETE FROM passage WHERE idAvion = %s"
    param = (idAvion,)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

def insert_passage(idAvion, idAerodrome):
    sql = "INSERT INTO passage VALUES (%s, %s, %s, %s, %s);"
    l = time.localtime(time.time())
    param = (idAvion, idAerodrome, int(str(l[3]) + str(l[4]) + str(l[5])), 0, 80)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error:
            cnx.rollback()

    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

def delete_trajet(idAvion):
    sql = "DELETE FROM trajets WHERE idAvion = %s;"
    param = (idAvion,)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

def insert_trajet(idAvion, trajet):
    delete_trajet(idAvion)
    sql = "INSERT INTO trajets VALUES (%s, %s);"
    s = ""
    for val in trajet.dict:
        s += val + " "
    param = (idAvion, s)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error:
            cnx.rollback()

    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

def delete_distance(idAvion):
    sql = "DELETE FROM distance WHERE idAvion = %s"
    param = (idAvion, )
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

def insert_distance(idAvion, distance):
    sql = "INSERT INTO distance VALUES (%s, %s, %s);"
    l = time.localtime(time.time())
    param = (idAvion, distance/1.852, int(str(l[3]) + str(l[4]) + str(l[5])))
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error:
            cnx.rollback()

    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        close_bd(cursor, cnx)

proxim_dict = {0: (1, 2, 3, 4, 5, 6), 1: (2, 6, 5), 2: (1, 6, 3), 3: (2, 6, 4), 4: (3, 6, 5), 5: (4, 6, 1),
               6: (1, 2, 3, 4, 5)}


class Aerodrome():
    def __init__(self, idAerodrome, lat, lon, zone):
        self.idAerodrome = idAerodrome
        self.lon = lon
        self.lat = lat
        self.zone = zone


class Trajet():
    def __init__(self, dep):
        self.dep = dep
        self.position = (dep.lat, dep.lon)
        self.dict = {dep.idAerodrome: self.position}

    def calcul_trajet(self):
        liste_zones = [1, 2, 3, 4, 5, 6]
        zone = self.dep.zone
        if zone in liste_zones:
            liste_zones.pop(liste_zones.index(zone))
        while liste_zones:
            liste_proxim = [val for val in liste_zones if val in proxim_dict[zone]]
            if liste_proxim:
                new_zone = random.choice(liste_proxim)
            else:
                new_zone = random.choice([val for val in liste_zones])
            liste_zones.pop(liste_zones.index(new_zone))
            idAerodrome, (lat, lon) = min(get_aerodromesInZone(new_zone).items(),
                                          key=lambda x: calcul_distance(self.position, x[1]))
            while self.position != (lat, lon):
                dict2 = get_aerodromesBetween(self.position, (lat, lon))
                new_id, self.position = min([val for val in dict2.items() if val[0] not in self.dict],
                                                key=lambda x: calcul_distance(x[1], self.position))
                self.dict[new_id] = self.position
            self.dict[idAerodrome] = (lat, lon)
            zone = new_zone
        aerodromes_dict = get_aerodromes()
        while len(self.dict) < 100:
            new_id, self.position = min([val for val in aerodromes_dict.items() if val[0] not in self.dict],
                                        key=lambda x: calcul_distance(x[1], self.position))
            self.dict[new_id] = self.position


class Simul():
    def __init__(self, step, dep, idAvion):
        self.dep = dep
        self.idAvion = idAvion
        self.position = (self.dep.lat, self.dep.lon)
        self.step = step
        self.distance = 0
        self.time_start = None
        self.time = None
        self.trajet = Trajet(dep)
        self.trajet.calcul_trajet()
        insert_trajet(self.idAvion, self.trajet)
        self.next_index = 1

    def start(self):
        delete_passages(self.idAvion)
        self.time_start = time.time()
        self.time = self.time_start
        insert_position(self.idAvion, self.dep.lat, self.dep.lon, self.time - self.time_start)
        self.advance()

    def stop(self):
        self.timer.cancel()

    def advance(self):
        if self.next_index >= len(self.trajet.dict):
            return None
        else:
            self.timer = Timer(self.step, self.update)
            self.timer.start()

    def update(self):
        self.time += self.step
        idAerodrome, next_aerodrome_pos = list(self.trajet.dict.items())[self.next_index]
        dist = calcul_distance(self.position, next_aerodrome_pos)
        step_dist = 10000 * self.step
        if step_dist < dist:
            self.distance += step_dist
            self.position = self.position[0] + (next_aerodrome_pos[0] - self.position[0]) * step_dist / dist, self.position[1] + (next_aerodrome_pos[1] - self.position[1]) * step_dist / dist
        else:
            self.distance += dist
            self.position = next_aerodrome_pos
            insert_passage(self.idAvion, idAerodrome)
            self.next_index += 1
        insert_position(self.idAvion, float(self.position[0]), float(self.position[1]), self.time - self.time_start)
        insert_distance(self.idAvion, self.distance)
        self.advance()


def calcul_distance(pos1, pos2):
    return 1e3 * great_circle(pos1, pos2).km

if __name__ == "__main__":
    dep1 = Aerodrome("LFCC", 44.3525, 1.49427, 3)
    dep2 = Aerodrome("LFAT", 50.5301,1.586 , 1)
    dep3 = Aerodrome("LFCC", 44.3525, 1.49427, 3)
    simu1 = Simul(1, dep1, "TB20")
    simu2 = Simul(1, dep2, "TB202")
    simu3 = Simul(1, dep3, "TB203")
    simu1.start()
    simu2.start()
    simu3.start()