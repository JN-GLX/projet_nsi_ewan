"""
Calcul d'itinéraire à l'aide de l'algorithme Dijkstra
"""

# le fichier doit contenir les fonctions dijskstra(ville_depart),
# calcul_itineraire(ville_depart, ville_arrivée)
from math import inf
import bibliotheque as biblio
import util_donnees as util

# JNG: Modification de certains noms de variables pour les rendre plus
# explicites et améliorer la lecture et la compréhension du code


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


def creer_graphe_gares(gares):
    """
    Création d'un graphe à partir de la liste des gares sous la forme d'un
    dictionnaire, dont les clés sont les villes et les valeurs sont les
    voisins avec le PK associé.
    """

    # travail d'ewan
    # Extraction des gares avec le code ligne associé et la valeur du point
    # kilométrique
    gares_triees = biblio.projection(gares, ["COMMUNE", "CODE_LIGNE", "PK"])

    # Création d'un dictionnaire des lignes avec les gares et PK associés
    dico_lignes = util.dictionnaire_lignes(gares)

    voisins = {}
    for gare in gares_triees:
        ville = gare["COMMUNE"]
        # Le PK de la ville devient le point de référence pour le calcul
        # des distances
        point_km_ref = float(util.format_point_km(gare["PK"]))

        # Liste des gares appartenant à la même ligne
        gares_ligne = dico_lignes[gare["CODE_LIGNE"]]

        voisins[ville] = {}
        for ville_ligne, point_km in gares_ligne:
            if ville_ligne != ville:
                # Calcul de la distance à partir du point de référence
                distance = abs(point_km_ref -
                               float(util.format_point_km(point_km)))
                # ajout du voisin
                voisins[ville][ville_ligne] = distance

    return voisins
