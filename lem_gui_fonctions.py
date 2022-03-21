import mysql.connector
#VARIABLE MENU

def Menu_Lemgui_Dict():
    dict_requete = {
        "1": "Lister les tous les agences",  
        "2": "Lister tous les caissiers par ordre croissant de leur nom",
        "3": "Lister toutes les adresses des agences",
        "4": "Lister les comptes de transaction de l'agence 21, Dunning Halley par ordre croissant du solde",
        "5": "Lister la somme des montants déposés par le caissier Winton dans un compte de transaction de l’agence dont le chef est Chilver par ordre croissant du montant",
        "6": "Lister les utilisateurs de 21, Dunning Halley",
        "7": "Lister le nombre de compte par agence",
        "8": "Lister les comptes affectés à l’utilisateur Veeler durant le mois de Mai 2021",
        "9": "Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
        "10": "Lister le montant des transactions effectué par l'utilisateur Veller et par date dans l’agence dont le numéro est 001",
        "11": "Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
        "12": "Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est Jolly par ordre croissant du montant",
        "13": "Lister les montants de transactions et les frais associés effectués par l’utilisateur Mouan dans l’agence dont le chef est moussa diop.",
        "14": "Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.",
        "15": "Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
        "16": "Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
        "17": "Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
        "18": "Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
        "19": "Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
        "20": "Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
        "21": "Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 221",
        "22": "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
        "23": "Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
        "24": "Lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.",
        "25": "Lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop",
        "Q": "Tapper Q pour quitter",
        "R": "Taper R pour Rétablir les requêtes",
        "E": "Tapez H pour voir l'historique des requêtes",
    }
    return dict_requete
#AFFICHER MENU
def Menu_Lemgui():
    print("1) Lister les tous les agences")
    print("2) Lister tous les caissiers par ordre croissant de leur nom")
    print("3) Lister toutes les adresses des agences")
    print("4) Lister les comptes de transaction d'une agence par ordre croissant du solde")
    print("5) Lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est moussa dop par ordre croissant du montant")
    print("6) Lister les utilisateurs de l’agence Plateau")
    print("7) Lister le nombre de compte par agence")
    print("8) Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021")
    print("9) Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021")
    print("10) Lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 001")
    print("11) Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001")
    print("12) Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussa diop par ordre croissant du montant")
    print("13) Lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop.")
    print("14) Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.")
    print("15) Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021")
    print("16) Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021")
    print("17) Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021")
    print("18) Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221")
    print("19) Lister les agences qui n’ont pas fait de dépôt le 10-08-2021")
    print("20) Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221")
    print("21) Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 221")
    print("22) Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221")
    print("23) Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021")
    print("24) Lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.")
    print("25) Lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop")
    print("Tapper Q pour quitter")
    print("Taper R pour Rétablir les requêtes")
    print("Tapez E pour voir l'historique des requêtes")

#Connecter BASE
db = mysql.connector.connect(
    host="localhost",
    user="marieme",
    password="marieme",
    database="DB_LemGUI"   
)
mycursor = db.cursor()
def Recuperation_Query(request):
    with db.cursor() as r:
        r.execute(request)
        sql_reponse = r.fetchall()
        return sql_reponse
# FONCTIONS DES REQUETES
def Requete_1():
    request = "SELECT adresse_AGENCE FROM AGENCE"
    sql_reponse = Recuperation_Query(request)
    l_r =[]
    for i in sql_reponse:
        l_r.append(i[0])
    return l_r
def Requete_2():
    request = "SELECT nom_USER FROM USERS WHERE id_PROFIL_PROFIL = 3"
    sql_reponse = Recuperation_Query(request)
    l_r =[]
    for i in sql_reponse:
        l_r.append(i[0])
    return l_r
def Requete_3():
    request = "SELECT nom_USER,adresse_AGENCE FROM USERS JOIN AGENCE ON (USERS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE) where id_PROFIL_PROFIL = 1"
    sql_reponse = Recuperation_Query(request)
    for row in sql_reponse:
        row = row[0]    
    return sql_reponse
def Requete_4():
    request = "SELECT COMPTE_TRANSACTION.numero FROM COMPTE_TRANSACTION JOIN TRANSACTIONS ON (COMPTE_TRANSACTION.numero = TRANSACTIONS.numero_COMPTE_TRANSACTION) WHERE TRANSACTIONS.numero_AGENCE_AGENCE = 1 ORDER BY solde_COMPTE_TRANSACTION"
    sql_reponse = Recuperation_Query(request)
    l_r =[]
    for i in sql_reponse:
        l_r.append(i[0])
    return l_r
def Requete_5():
    request = "SELECT SUM(montant_TRANSACTION) FROM TRANSACTIONS JOIN USERS ON (USERS.id_USER = TRANSACTIONS.id_USER_USER) JOIN COMPTE_TRANSACTION ON (TRANSACTIONS.numero_COMPTE_TRANSACTION = COMPTE_TRANSACTION.numero) WHERE USERS.ID_PROFIL_PROFIL = 3 AND TRANSACTIONS.numero_COMPTE_TRANSACTION = 311"
    sql_reponse = Recuperation_Query(request)
    return sql_reponse[0]
def Requete_6():
    request = "SELECT nom_USER FROM USERS JOIN AGENCE ON (USERS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE) WHERE numero_AGENCE = 1"
    sql_reponse = Recuperation_Query(request)
    return sql_reponse
def Requete_7():
    request = "SELECT numero_AGENCE_AGENCE,COUNT(numero_COMPTE_TRANSACTION) FROM AGENCE JOIN USERS ON (id_USER_USER = id_USER) JOIN ASSOCIER ON (USERS.id_USER = ASSOCIER.id_USER_USER) GROUP BY numero_AGENCE_AGENCE"
    sql_reponse = Recuperation_Query(request)
    print(sql_reponse)
    for i in range(len(sql_reponse)):
        re = sql_reponse[i]
        re = ("L'agence %s a eu %s compte de transaction" %(re[0],re[-1]))
        sql_reponse[i] = re
    return sql_reponse
def Requete_8():
    request = "SELECT COUNT(COMPTE_TRANSACTION.numero) FROM ASSOCIER JOIN COMPTE_TRANSACTION ON (ASSOCIER.numero_COMPTE_TRANSACTION = COMPTE_TRANSACTION.numero) WHERE (date_debut BETWEEN '2020-05-01' AND '2020-05-31' AND id_USER_USER = 0)"
    sql_reponse = Recuperation_Query(request)
    sql_reponse = sql_reponse[0]
    sql_reponse = sql_reponse[0]
    sql_reponse = ("Le nombre de compte est égal à %s" %sql_reponse )
    return sql_reponse
def Requete_9():
    request = "SELECT nom_USER FROM AGENCE JOIN USERS ON (id_USER_USER = id_USER) JOIN ASSOCIER ON (USERS.id_USER = ASSOCIER.id_USER_USER) WHERE (YEAR(date_debut) = 2020 AND numero_COMPTE_TRANSACTION = 75)"
    sql_reponse = Recuperation_Query(request)
    for i in range(len(sql_reponse)):
        re = sql_reponse[i]
        re = re[0]
        sql_reponse[i] = re
    return sql_reponse
def Requete_10():
    request = "SELECT SUM(montant_TRANSACTION) FROM AGENCE JOIN USERS ON (id_USER_USER = id_USER) JOIN ASSOCIER ON (USERS.id_USER = ASSOCIER.id_USER_USER) JOIN TRANSACTIONS ON (TRANSACTIONS.id_USER_USER = USERS.id_USER) GROUP BY USERS.id_USER"
    sql_reponse = Recuperation_Query(request)
    for i in range(len(sql_reponse)):
        re = sql_reponse[i]
        re = re[0]
        sql_reponse[i] = re
    return sql_reponse
def Requete_11():
    reponse_11 =0
    sortie = (print("Le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001", reponse_11))
    return sortie
def Requete_12():
    request = "SELECT SUM(montant_TRANSACTION) FROM TRANSACTIONS JOIN TYPE ON (id_TYPE = id_TYPE_TYPE) JOIN USERS ON (USERS.id_USER = TRANSACTIONS.id_USER_USER) WHERE USERS.nom_USER = 'Jolly' GROUP BY date_TRANSACTION ORDER BY SUM(montant_TRANSACTION) ASC"
    sql_reponse = Recuperation_Query(request)
    l_r =[]
    for row in sql_reponse:
        row = row[0]
        l_r.append(row)
    return l_r
def Requete_13():
    request = "SELECT TRANSACTIONS.montant_TRANSACTION,libelle_PART FROM AGENCE JOIN USERS ON (AGENCE.id_USER_USER = USERS.id_USER) JOIN TRANSACTIONS ON (TRANSACTIONS.numero_AGENCE_AGENCE = AGENCE.numero_AGENCE) JOIN POSSEDR ON (POSSEDR.num_TRANSACTION_TRANSACTIONS = TRANSACTIONS.num_TRANSACTION) JOIN PART ON (POSSEDR.id_PART_PART = id_PART) WHERE AGENCE.numero_AGENCE = 1 AND USERS.id_USER = 3;"
    sql_reponse = Recuperation_Query(request)
    return sql_reponse
def Requete_14():
    reponse_14 =0
    sortie = (print("La somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001", reponse_14))
    return sortie
def Requete_15():
    reponse_15 =0
    sortie = (print("La somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021", reponse_15))
    return sortie
def Requete_16():
    reponse_16 =0
    sortie = (print("L’agence qui a fait le plus de transfert durant le mois de Juin 2021", reponse_16))
    return sortie
def Requete_17():
    reponse_17 =0
    sortie = (print("L’agence qui a fait le moins de transfert de dépôt le 10-08-2021", reponse_17))
    return sortie
def Requete_18():
    reponse_18 =0
    sortie = (print("L’agence qui a fait le retrait le plus grand durant le mois de MAI 2021", reponse_18))
    return sortie
def Requete_19():
    reponse_19 =0
    sortie = (print("Les agences qui n’ont pas fait de dépôt le 10-08-2021", reponse_19))
    return sortie
def Requete_20():
    reponse_20 =0
    sortie = (print("Les noms utilisés par l’agence numéro 001 durant le mois de MAI 2021", reponse_20))
    return sortie
def Requete_21():
    reponse_21 =0
    sortie = (print("Le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 2021", reponse_21))
    return sortie
def Requete_22():
    reponse_22 =0
    sortie = (print("Le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 2021", reponse_22))
    return sortie
def Requete_23():
    reponse_23 =0
    sortie = (print("Les 5 agences qui ont effectué le plus de transactions durant l’année 2021", reponse_23))
    return sortie
def Requete_24():
    reponse_24 =0
    sortie = (print("Les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021", reponse_24))
    return sortie
def Requete_25():
    reponse_25 =0
    sortie = (print("L’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop", reponse_25))
    return sortie
def Requete_Quitter():
    reponse_q =0
    sortie = (print("Tapper Q pour quitter", reponse_q))
    return sortie
def Requete_Reset(requete_input):
    reponse_r =0
    sortie = (print("Taper R pour Rétablir les requêtes", reponse_r))
    return sortie
def Requete_Historique(requete_input):
    reponse_h =0
    sortie = (print("Tapez H pour voir l'historique des requêtes", reponse_h))
    return sortie
#
historique_requete = {}
liste_historique_requete =[]
requete_input = 0
c = 1
liste_requete = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","R","E","r","e"]
#LISTE ET DICTIONNAIRE DES FONCTIONS
liste_fonction = [Requete_1,Requete_2,Requete_3,Requete_4,Requete_5,Requete_6,Requete_7,Requete_8,Requete_9,Requete_10,Requete_11,Requete_12,Requete_13,Requete_14,Requete_15,Requete_16,Requete_17,Requete_18,Requete_19,Requete_20,Requete_21,Requete_22,Requete_23,Requete_24,Requete_25,Requete_Quitter,Requete_Reset,Requete_Historique]
dict_fonction = {
    "1":Requete_1,
    "2":Requete_2,
    "3":Requete_3,
    "4":Requete_4,
    "5":Requete_5,
    "6":Requete_6,
    "7":Requete_1,
    "8":Requete_8,
    "9":Requete_9,
    "10":Requete_10,
    "11":Requete_11,
    "12":Requete_12,
    "13":Requete_13,
    "14":Requete_14,
    "15":Requete_15,
    "16":Requete_16,
    "17":Requete_17,
    "18":Requete_18,
    "19":Requete_19,
    "20":Requete_20,
    "21":Requete_21,
    "22":Requete_22,
    "23":Requete_23,
    "24":Requete_24,
    "25":Requete_25,
    "Q":Requete_Quitter,
    "R":Requete_Reset,
    "H":Requete_Historique,
}





