"""
Fichier principal du programme
"""
import tkinter as Tk

import bibliotheque as biblio
import util_dijkastra as dijk
# import test_folium as folium
import util_donnees as util


class GUI():
    """
    Classe pour la création de l'interface graphique
    """
    # constructeur de l'interface graphique
    def __init__(self):

        # travail d'ewan

        # JNG: Remplacement du code de chargement des gares bretonnes par une
        # fonction
        # La variable 'gares' n'est utilisée que comme "variable tampon".
        # Il n'est pas utile que ce soit une propriété de la classe GUI.
        # Donc 'self.__gares' n'est pas utile
        gares = util.initialisation_donnees_gares("liste-des-gares.csv")

        # Récupère la liste des communes sous la forme suivante
        # {"COMMUNE": 'nom de la commune' }
        table_communes = biblio.projection(gares, "COMMUNE")

        liste_communes = []
        # Récupération uniquement du nom de la commune (sans la clé)
        for elt in table_communes:
            for cle, valeur in elt.items():
                liste_communes.append(valeur)

        # Initialisation du graphe des gares
        self.__graphe_gares = dijk.creer_graphe_gares(gares)

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
                                  *liste_communes)
        self.opt1.config(width=50)
        self.opt1.pack()

        self.cadre2 = Tk.LabelFrame(self.fenetre,
                                    text="Choisissez la gare d'arrivée")
        self.cadre2.pack()

        self.options2 = Tk.StringVar(self.cadre2)
        self.options2.set("")

        self.opt2 = Tk.OptionMenu(self.cadre2, self.options2,
                                  *liste_communes)
        self.opt2.config(width=50)
        self.opt2.pack()

        # on associe l'appui du bouton à btn_calcule_itineraire_on_click
        self.plot_button = Tk.Button(
            master=self.fenetre, command=self.btn_calcule_itineraire_on_click,
            height=2, width=20, text="Calculer l'itinéraire"
            )
        self.plot_button.pack()

        self.fenetre.mainloop()

# en cours marine
    # JNG: proposition de distinguer la fonction déclenchée au clic
    # sur le bouton, de celle qui effectuera effectivement
    # le calcul de l'itineraire
    def btn_calcule_itineraire_on_click(self):
        """
        Traitement du clic sur le bouton 'Calculer'
        """
        ville_depart = self.options1.get()
        ville_arrivee = self.options2.get()
        # distance = ('ville_depart' - 'ville_arrivee')
        # Calcul des distances à partir de la ville de départ
        distances = dijk.dijkstra(self.__graphe_gares, ville_depart)

        print(ville_depart, "  ", ville_arrivee)
        print(distances)
        # Le code suivant (après modification) devrait être déplacé
        # dans une fonction à part 'calculer_itineraire'
        # calculer_itineraire(ville_depart, ville_arrivee, distances)
        """
            chemin = [ville_arrivee]
            sommet  = ville_arrivee
            while sommet != ville_depart:
                sommet = distance[sommet]["relais"]
                chemin.insert(0,sommet)
            return chemin
        """


app = GUI()
