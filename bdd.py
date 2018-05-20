#!C:\\python34
# -*- coding: UTF-8 -*-
# enable debugging
import mysql.connector
from mysql.connector import errorcode

conf=Import('../data/config.py')
config=conf.configBD()

def connexion():
    cnx=""
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

def close_bd(cursor,cnx):
    cursor.close()
    cnx.close()

def verif_connect(login,pwd):
    sql = "SELECT membre.idMembre, membre.nom,membre.prenom FROM membre where membre.login=%s and membre.pwd= %s;"
    param = (login, pwd)

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql, param)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def verif_connect_admin(login,pwd):
    sql = "SELECT adm.idMembre, adm.nom,adm.prenom FROM administrateur as adm where adm.login=%s and adm.pwd= %s;"
    param = (login, pwd)

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql, param)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def ajouter_membre_bdd(idMembre,nom,prenom,login,pwd,idEquipe):
    sql = "INSERT INTO `membre` (`idMembre`, `nom`, `prenom`, `login`, `pwd`, `idEquipe`) VALUES(%s, %s, %s, %s, %s, %s);"
    param = (idMembre,nom,prenom,login,pwd,idEquipe)

    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql,param)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def ajouter_equipe_bdd(idEquipe,nom,idAvion):
    sql = "INSERT INTO `equipe` (`idEquipe`, `nom`, `idAvion`) VALUES (%s, %s, %s);"
    param = (idEquipe,nom,idAvion)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql,param)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def ajouter_msg(idMessage,idDestinateur,idDestinataire,msg,lu,date):
    sql = "INSERT INTO `message` (`idMessage`, `idDestinateur`, `idDestinataire`, `msg`, `lu`, `date` ) VALUES(%s, %s, %s, %s, %s, %s);"
    param = (idMessage,idDestinateur,idDestinataire,msg,lu,date)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql,param)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def count_equipes():
    sql = "SELECT COUNT(eq.idEquipe) from equipe as eq;"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def count_membre():
    sql = "SELECT COUNT(m.idMembre) from membre as m;"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def count_msg_non_lu(idMembre):
    sql = "SELECT COUNT(m.idMessage) from message as m where m.idDestinataire=%s and m.lu=0;"
    param=(idMembre,)
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql,param)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste) == 1 else None

def change_login(idMembre, login_new,admin):
    if admin == 1:
        sql = "UPDATE administrateur as ad SET ad.login = %s WHERE ad.idMembre = %s;"
    else:
        sql = "UPDATE membre as m SET m.login = %s WHERE m.idMembre = %s;"
    param = (login_new, idMembre)

    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def change_pwd(idMembre, pwd_new,admin):
    if admin == 1 :
        sql = "UPDATE administrateur as ad SET ad.pwd = %s WHERE ad.idMembre = %s;"
    else :
        sql = "UPDATE membre as m SET m.pwd = %s WHERE m.idMembre = %s;"

    param = (pwd_new, idMembre)
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, param)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def change_msg_lu(idMessage,lu):
    if lu == 1 :
        sql = "UPDATE message as m SET m.lu = 1 WHERE m.idMessage = %s;"
    elif lu == 0 :
        sql = "UPDATE message as m SET m.lu = 0 WHERE m.idMessage = %s;"
    else :
        pass
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql, (idMessage,))
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def get_idMax():
    sql = "SELECT MAX(m.idMembre) from membre as m;"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def get_idMsgMax():
    sql = "SELECT MAX(m.idMessage) from message as m;"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return 0 if liste[0][0]==None else liste[0][0]

def get_idMembre(login, nom, admin):
    if admin == 1:
        sql = "SELECT ad.idMembre FROM administrateur as ad WHERE ad.login = %s and ad.nom = %s;"
    else:
        sql = "SELECT m.idMembre FROM membre as m WHERE m.login = %s and m.nom = %s;"
    param = (login, nom)
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql,param)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def get_idEquipe(idMembre):
    sql = "SELECT m.idEquipe FROM membre as m WHERE m.idMembre = %s;"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql,idMembre)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def get_membres():
    sql = "SELECT * FROM membre"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        dict = {}
        for idMembre, nom, prenom,login,pwd,idEquipe in cursor:
            dict[idMembre] = {"nom": str(nom)[12:-2], "prenom": str(prenom)[12:-2], "login": str(login)[12:-2], "pwd": str(pwd)[12:-2], "idEquipe": str(idEquipe)}
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict


def get_equipes():
    sql = "SELECT * FROM equipe"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        dict = {}
        for idEquipe,nom,idAvion in cursor:
            dict[idEquipe] = {"idEquipe": str(idEquipe)[12:-2],"nom": str(nom)[12:-2],"idAvion": str(idAvion)[12:-2] }
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict

def get_coequipiers(idEq, idMembre_connecte=''):
    sql = "SELECT * FROM membre as m WHERE m.idEquipe = %s "
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql,idEq)
        dict = {}
        for idMembre, nom, prenom,login,pwd,idEquipe in cursor:
            if idMembre_connecte!=str(idMembre):
                dict[idMembre] = {"nom": str(nom)[12:-2], "prenom": str(prenom)[12:-2], "login": str(login)[12:-2], "pwd": str(pwd)[12:-2], "idEquipe": str(idEquipe)}
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict

def get_msg_received(idMembre):
    sql = "SELECT * FROM message as m WHERE m.idDestinataire = %s "
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql,(idMembre,))
        dict = {}
        for idMessage, idDestinateur, idDestinataire,msg,lu, date in cursor:
            dict[idMessage] = {"idMessage": str(idMessage), "idDestinateur": str(idDestinateur), "msg": str(msg)[12:-2], "lu": str(lu), "date":str(date)[12:-2]}
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict

def get_msg_send(idMembre):
    sql = "SELECT * FROM message as m WHERE m.idDestinateur = %s "
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql,(idMembre,))
        dict = {}
        for idMessage, idDestinateur, idDestinataire,msg,lu,date in cursor:
            dict[idMessage] = {"idMessage": str(idMessage), "idDestinataire": str(idDestinataire), "msg": str(msg)[12:-2], "lu": str(lu), "date":str(date)[12:-2]}
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict

def get_pwd(idMembre, admin):
    if admin == 1:
        sql = "SELECT adm.pwd FROM administrateur as adm WHERE adm.idMembre = %s;"
    else :
        sql = "SELECT m.pwd FROM membre as m WHERE m.idMembre = %s;"

    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql,idMembre)
        liste = list(cursor)
    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return liste[0] if len(liste)==1 else None

def get_aerodromes():
    sql = "SELECT idAerodrome, lat, lon FROM aerodrome"
    try:
        cnx = connexion()
        cursor = cnx.cursor(prepared=True)
        cursor.execute(sql)
        dict = {}
        for idAerodrome, lat, lon in cursor:
            dict[idAerodrome] = "{lat: "+str(lat)+", lng: "+str(lon)+"}"

    except mysql.connector.Error as err:
        liste = "Failed select table test: {}".format(err)
        exit(1)
    finally:
        close_bd(cursor, cnx)
    return dict

def delete_membre(idMembre):
    sql = "DELETE FROM membre WHERE membre.idMembre = %s;"
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql,(idMembre,))
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def delete_equipe(idEq):
    sql1 = "DELETE FROM membre WHERE membre.idEquipe = %s;"
    sql2 = "DELETE FROM equipe WHERE equipe.idEquipe = %s;"
    try:
        cnx = connexion()
        cursor1 = cnx.cursor()
        cursor2 = cnx.cursor()
        try:
            cursor1.execute(sql1,(idEq,))
            cursor2.execute(sql2,(idEq,))
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None

def delete_msg(idMessage):
    sql = "DELETE FROM message WHERE message.idMessage = %s;"
    try:
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            cursor.execute(sql,(idMessage,))
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
    except mysql.connector.Error as err:
        print("Failed select table test: {}".format(err))
        exit(1)
    finally:
        if cnx:
            cnx.close()
    return None