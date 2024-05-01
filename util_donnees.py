"""
Module regroupant des fonctions de traitement des données du fichier
'liste-des-gares.csv'
"""

import bibliotheque as biblio

DEPARTEMENTS_BRETONS = ["FINISTERE",
                        "COTES-D'ARMOR",
                        "MORBIHAN",
                        "ILLE-ET-VILAINE"]


def extrait_gares_region(table, departements):
    """
    Extrait les gares de 'table' en fonction des 'departements'
    """
    gares = []
    for departement in departements:
        gares += biblio.extrait_table(table, "DEPARTEMEN", departement)

    return gares


# travail d'elouan
def liste_lignes(gares):
    """
    Extrait les lignes de 'gares'
    """
    liste = []
    for e in gares:
        if e["CODE_LIGNE"] not in liste:
            liste.append(e["CODE_LIGNE"])
    # print(liste_lignes)
    return liste


# travail de marine
def dictionnaire_lignes(gares):
    """
    Crée un dictionnaire des lignes avec les communes qui les composent
    et la distance (point kilométrique)
    """
    dictionnaire = {}
    cle_dictionnaire = liste_lignes(gares)

    for element in cle_dictionnaire:
        dictionnaire[element] = []
        for ligne in gares:
            if ligne["CODE_LIGNE"] == element:
                dictionnaire[element].append((ligne["COMMUNE"], ligne["PK"]))
    return dictionnaire

