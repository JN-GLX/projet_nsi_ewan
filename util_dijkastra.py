"""
Calcul d'itinéraire à l'aide de l'algorithme Dijkstra
"""

# le fichier doit contenir les fonctions dijskstra(ville_depart),
# calcul_itineraire(ville_depart, ville_arrivéé)
from math import inf
import bibliotheque as biblio
import util_donnees as util

# JNG: Attention à nommer les variables de manière explicite:
# ça aide à la compréhension du code
# Les éditeurs de code aident à la saisie, donc il ne faut pas avoir peur
# de la longueur du nom de la variable
# par exemple: 'ville_depart', on pense que c'est la ville de départ, alors
# qu'en fait c'est la liste des gares des départements bretons...


def dijkstra(liste_villes, sommet_depart):
    """
    Implémentation de l'algorithme Dijkstra
    """
    # liste des sommets déjà explorés
    lst_sommets_explores = []
    # liste des sommets atteignable par une arête depuis un sommet déjà exploré
    # liste à traiter
    lst_sommets_atteignables = [sommet_depart]

    # liste des distances depuis le sommet de départ
    distances = {}
    # Initialisation de l'algorithme
    # La distance des sommets différents du sommet de départ est infinie
    # JNG: Refactorisation du code pour améliorer la lisibilité
    for sommet in liste_villes:
        if sommet == sommet_depart:
            distances[sommet] = {
                                "distance": 0,
                                "relais": sommet,
                                "traite": False
                                }
        else:
            distances[sommet] = {
                                "distance": inf,
                                "relais": "N",
                                "traite": False
                                }

    sommet_courant = sommet_depart
    i = 0
    while len(lst_sommets_atteignables) != 0:
        i = i + 1
        # on cherche les voisins atteignables depuis le sommet courant
        lst_voisins = liste_villes[sommet_courant]

        # on les ajoute dans la liste des sommets atteignables
        # si le sommet n'a pas déjà été traité
        # si le sommet n'est pas déjà dans la liste
        for voisin in list(lst_voisins.keys()):
            if not distances[voisin]["traite"] \
               and voisin not in lst_sommets_atteignables:
                lst_sommets_atteignables.append(voisin)

        # on met a jour les distances dans la table distances
        for voisin in list(lst_voisins.keys()):
            # on calcule d la distance entre le voisin et l'origine
            # en passant par le voisin v
            d = lst_voisins[voisin] + distances[sommet_courant]["distance"]
            if d < distances[voisin]["distance"] \
               and not distances[voisin]["traite"]:
                distances[voisin]["distance"] = d
                distances[voisin]["relais"] = sommet_courant

        # on supprime le sommet qui vient d'être exploré de la liste des
        # sommets atteignables
        lst_sommets_atteignables.pop(
                                lst_sommets_atteignables.index(sommet_courant)
                                )

        # on indique au dictionnaire distance que le sommet courant vient
        # d'être traité pour qu'on y revienne plus
        distances[sommet_courant]["traite"] = True

        # on recherche le prochain sommet dans la liste v
        d_min = inf
        for voisin in lst_sommets_atteignables:
            # JNG: utiliser 'not' plutôt que '== False'
            if voisin not in lst_sommets_explores \
               and not distances[voisin]["traite"]:
                # d est la distance entre le sommet courant et le voisin
                d = distances[voisin]["distance"] + \
                    distances[sommet_courant]["distance"]
                # d_min : distance minimale
                # v_min: voisin le plus proche?
                if d < d_min:
                    d_min = d
                    v_min = voisin

        lst_sommets_explores.append(sommet_courant)
        sommet_courant = v_min

    return distances


# distances = dijskstra(voisins, "0")
# print(distances)
table = biblio.lit_csv_dict("liste-des-gares.csv", ";", "UTF-8")

gares = util.extrait_gares_region(table, util.DEPARTEMENTS_BRETONS)
# travail d'ewan
gares_triees = biblio.projection(gares, "COMMUNE")
voisins = {}
for gare in gares_triees:  # JNG: gare
    voisins[gare["COMMUNE"]] = {}
    # JNG: il manque du code ou bien c'est voulu?
    # si c'est voulu il faut l'expliquer en commentaire

print(voisins)
