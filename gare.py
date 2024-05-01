# JNG: il vaudrait mieux importer sous la forme suivante:
# import tkinter as Tk
from tkinter import *

# JNG: Même remarque
# import bibliotheque as biblio
from bibliotheque import *
# Idem
from util_dijkastra import *
# Idem
from test_folium import *

# JNG: Remarques générales
# 1 - Il faudrait prendre la peine de donner
# des noms explicites aux variables (mêmes locales) pour aider à mieux
# comprendre ce que le code est censé faire.
#
# 2 - Améliorer la lisibilité du code en limitant la longueur des lignes
# à 79 caractères (les éditeurs de code peuvent afficher une règle)
# Quand le code n'est pas entre parenthèses, il faut mettre '\' à la fin
# de la ligne et continuer sur la ligne suivante
# voir exemple pour l'initialisation de self.__gares ci-dessous
#
# 3 - Améliorer la lisibilité du code, suite:
# Une fonction ne doit pas être trop longue, et ne devrait faire qu'une
# seule chose (et le faire bien :-) )
# Il faudrait découper certaines fonctions/méthodes, notamment __init__
# en plusieurs petites fonctions (avec des noms explicites):
# ça aidera à la compréhension du code et au débogage


class GUI():
    """
    Classe pour la création de l'interface graphique
    """
    # constructeur de l'interface graphique
    def __init__(self):
        self.__table = lit_csv_dict("liste-des-gares.csv",";","UTF-8")

        #on déclare des gares "bidon" - JNG: Pourquoi bidon?
        # Créer une petite fonction dont le nom permet de comprendre
        # ce qu'elle fait
        self.__gares = extrait_table(self.__table, "DEPARTEMEN", "FINISTERE") \
            + extrait_table(self.__table, "DEPARTEMEN", "COTES-D'ARMOR") \
            + extrait_table(self.__table, "DEPARTEMEN", "MORBIHAN") \
            + extrait_table(self.__table, "DEPARTEMEN", "ILLE-ET-VILAINE")

        #travail d'ewan
        # JNG: ne pas oublier d'enlever les "print" de débogage avant de
        # rendre le projet

        print("test : ",self.__gares[0])
        code_ligne = liste_lignes(self.__gares)

        print (code_ligne)

        # JNG: La variable 'e' n'est pas utilisée dans la boucle
        # Le code n'est pas très clair: on a l'impression que 'table_filtree'
        # est écrasée à chaque tour de boucle
        for e in code_ligne:
            self.table_filtree = projection(self.__gares, "COMMUNE")
            self.table_filtree_finale = []
        for elt in self.table_filtree :
            for cle, valeur in elt.items() :
                self.table_filtree_finale.append(valeur)
        print(self.table_filtree_finale)
        # initialisation de l'interface graphique
        self.fenetre = Tk()


        #on définit le premier frame avec un titre
        self.cadre1 = LabelFrame(self.fenetre,  text='Choisissez la gare de départ')
        self.cadre1.pack()

        #options1 contient la valeur sélectionnée par l'utilisateur
        self.options1 = StringVar(self.cadre1)
        #on initialise options1 vide
        self.options1.set("")

        #opt1 contient les choix possibles
        self.opt1 = OptionMenu(self.cadre1, self.options1, *self.table_filtree_finale)
        self.opt1.config(width=50)
        self.opt1.pack()

        self.cadre2 = LabelFrame(self.fenetre,  text='Choisissez la gare darrivée')
        self.cadre2.pack()

        self.options2 = StringVar(self.cadre2)
        self.options2.set("")

        self.opt2 = OptionMenu(self.cadre2, self.options2, *self.table_filtree_finale)
        self.opt2.config(width=50)
        self.opt2.pack()

        #on associe l'appui du bouton à calcule_itineraire

        self.plot_button = Button(master = self.fenetre, command = self.calcule_itineraire, height = 2, width = 20, text = "calcul de l'itinéraire")
        self.plot_button.pack()

        self.fenetre.mainloop()

#en cours marine
    # JNG: il faudrait distinguer la fonction appelée lors du clic sur le
    # bouton de celle servant effectivement à calculer l'itineraire
    # (module util_dijkastra)
    # La fonction ci-dessous pourrait par exemple s'appeller:
    # btn_calcule_itineraire_on_click
    def calcule_itineraire(self):

        ville_depart = self.options1.get()
        ville_arrivee = self.options2.get()
        #distance = ('ville_depart' - 'ville_arrivee')
        print(ville_depart, "  ", ville_arrivee)
    """
            chemin = [ville_arrivee]
            sommet  = ville_arrivee
            while sommet != ville_depart:
                sommet = distance[sommet]["relais"]
                chemin.insert(0,sommet)
            return chemin
    """


#chemin = calcule_itineraire('0', '6', distance)
        #votre code ici

# print("le resultat")
#travail d'elouan
def liste_lignes(gares):
    liste = []
    for e in gares:
        if e["CODE_LIGNE"] not in liste :
            liste.append(e["CODE_LIGNE"])
    # print(liste_lignes)
    return liste

"""#print(calcule_itineraire('0', '6', distance))
#print(chemin)"""
#trvail de marine
def dictionnaire_lignes(gares):
    dictionnaire = {}
    cle_dictionnaire = liste_lignes(gares)

    for element in cle_dictionnaire :
        dictionnaire[element]= []
        for ligne in gares :
            if ligne["CODE_LIGNE"] == element :
                dictionnaire[element].append((ligne["COMMUNE"], ligne["PK"]))
    return dictionnaire
#print(dictionnaire_lignes(gares)))

app = GUI()