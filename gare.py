from tkinter import *
from bibliotheque import *
from util_dijkastra import *
from test_folium import *


class GUI():
    #constructeur de l'interface graphique
    def __init__(self):
        self.__table = lit_csv_dict("liste-des-gares.csv",";","UTF-8")

        #on déclare des gares "bidon"
        self.__gares = extrait_table(self.__table, "DEPARTEMEN", "FINISTERE") + extrait_table(self.__table, "DEPARTEMEN", "COTES-D'ARMOR") +  extrait_table(self.__table, "DEPARTEMEN", "MORBIHAN") + extrait_table(self.__table, "DEPARTEMEN", "ILLE-ET-VILAINE")
        #travail d'ewan
        print("test : ",self.__gares[0])
        code_ligne = liste_lignes(self.__gares)

        print (code_ligne)

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

print("le resultat")
#travail d'elouan
def liste_lignes(gares):
    liste = []
    for e in gares:
        if e["CODE_LIGNE"] not in liste :
            liste.append(e["CODE_LIGNE"])
    print(liste_lignes)
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