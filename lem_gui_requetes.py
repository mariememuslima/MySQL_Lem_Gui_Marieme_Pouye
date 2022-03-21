from lem_gui_fonctions import*

#Menu_Lemgui()
# AFFICHAGE
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

dict_requete = Menu_Lemgui_Dict()
#requete_input = (input("Saisissez vote choix ici_"))
def afficher_dict():
    choice = 0
    #-> BOUCLE AFFICHER
    print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    print("#    BIENVENUE SUR LEM_GUI, VOICI LE MENU                 #")
    print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    for key,value in dict_requete.items():
            print(key,"->",value)
    print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    print("#                    FAITE VOTRE CHOIX                    #")
    print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
    requete_input = "0"
    while requete_input != "Q" or requete_input !="q":
        historique_requete = {}
        #-CHOIX
        requete_input = (input("Saisissez votre choix ici_"))
        #* TRAITEMENT CHOIX
        if requete_input in liste_requete:
            print("Vous avez choisi la requête ", requete_input)
            rep=dict_fonction[requete_input]()
            print(rep)
            recuperation_historique = dict_requete.pop(requete_input)
            historique_requete[requete_input]=recuperation_historique
            requete_input = (input("Saisissez votre choix ici_"))
            for va,ke in dict_requete.items():
                print(va,"->",ke)    
            while requete_input != "Q" or requete_input !="q":
                if requete_input in liste_requete:
                    print("Vous avez choisi la requête ", requete_input)
                    rep=dict_fonction[requete_input]()
                    print(rep)
                    recuperation_historique = dict_requete.pop(requete_input)
                    historique_requete[requete_input]=recuperation_historique
                    requete_input = (input("Saisissez votre choix ici_"))
                elif requete_input == "r" or requete_input == "R":
                    for i,k in historique_requete:
                        dict_requete[i]=k
        elif requete_input == "r" or requete_input == "R":
            print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
            print("#          VOUS N'AVEZ PAS ENCORE FAIT DE CHOIX           #")
            print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
        elif requete_input == "q" or requete_input == "Q":
            print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
            print("#                        A BIENTOT                        #")
            print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#")
            break
        else:
            print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
            print("#  Votre choix n'est pas pris en compte, choisissez à nouveau #")
            print("#*#*#*#*#*#**#**#*#**#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#")
afficher_dict()
