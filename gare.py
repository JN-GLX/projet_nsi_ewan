# JNG: correction de l'import
import tkinter as Tk

import bibliotheque as biblio
import util_dijkastra as dijk
import test_folium as folium
import util_donnees as util

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
        self.__table = biblio.lit_csv_dict("liste-des-gares.csv", ";", "UTF-8")

        # JNG: Remplacement du code de chargement des gares bretonnes par une
        # fonction
        # La variable 'gares' n'est utilisée que comme "variable tampon".
        # Il n'est pas utile que ce soit une propriété de la classe GUI.
        # Donc 'self.__gares' n'est pas utile
        gares = util.extrait_gares_region(self.__table,
                                          util.DEPARTEMENTS_BRETONS)

        # travail d'Ewan
        code_ligne = util.liste_lignes(gares)

        print(code_ligne)

        # JNG: La variable 'e' n'est pas utilisée dans la boucle
        # Et la boucle sur code_ligne ne sert à rien
        # Utilisation de variables locales (sans 'self.')
#        for e in code_ligne:
        # Récupère la liste des communes sous la forme suivante
        # {"COMMUNE": 'nom de la commune' }
        table_filtree = biblio.projection(gares, "COMMUNE")

        table_filtree_finale = []
        # Récupération uniquement du nom de la commune (sans la clé)
        for elt in table_filtree:
            for cle, valeur in elt.items():
                table_filtree_finale.append(valeur)
#        print(table_filtree_finale)

        # initialisation de l'interface graphique
        self.fenetre = Tk.Tk()

        # on définit le premier frame avec un titre
        self.cadre1 = Tk.LabelFrame(self.fenetre,
                                    text='Choisissez la gare de départ')
        self.cadre1.pack()

        # options1 contient la valeur sélectionnée par l'utilisateur
        self.options1 = Tk.StringVar(self.cadre1)
        # on initialise options1 vide
        self.options1.set("")

        # opt1 contient les choix possibles
        self.opt1 = Tk.OptionMenu(self.cadre1, self.options1,
                                  *table_filtree_finale)
        self.opt1.config(width=50)
        self.opt1.pack()

        self.cadre2 = Tk.LabelFrame(self.fenetre,
                                    text="Choisissez la gare d'arrivée")
        self.cadre2.pack()

        self.options2 = Tk.StringVar(self.cadre2)
        self.options2.set("")

        self.opt2 = Tk.OptionMenu(self.cadre2, self.options2,
                                  *table_filtree_finale)
        self.opt2.config(width=50)
        self.opt2.pack()

        # on associe l'appui du bouton à calcule_itineraire
        self.plot_button = Tk.Button(master=self.fenetre,
                                     command=self.calcule_itineraire,
                                     height=2, width=20,
                                     text="calcul de l'itinéraire")
        self.plot_button.pack()

        self.fenetre.mainloop()

# en cours marine
    # JNG: il faudrait distinguer la fonction appelée lors du clic sur le
    # bouton de celle servant effectivement à calculer l'itineraire
    # (module util_dijkastra)
    # La fonction ci-dessous pourrait par exemple s'appeller:
    # btn_calcule_itineraire_on_click
    def calcule_itineraire(self):

        ville_depart = self.options1.get()
        ville_arrivee = self.options2.get()
        # distance = ('ville_depart' - 'ville_arrivee')
        print(ville_depart, "  ", ville_arrivee)
    """
            chemin = [ville_arrivee]
            sommet  = ville_arrivee
            while sommet != ville_depart:
                sommet = distance[sommet]["relais"]
                chemin.insert(0,sommet)
            return chemin
    """

# chemin = calcule_itineraire('0', '6', distance)
# votre code ici

# print("le resultat")

app = GUI()
