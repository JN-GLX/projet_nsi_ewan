# le fichier doit contenir les fonctions dijskstra(ville_depart), calcul_itineraire(ville_depart, ville_arrivéé)
from math import inf
from bibliotheque import *

def dijskstra(ville_depart, sommet_depart):
    #liste des sommets déjà explorés
    lst_e = []

    #liste des sommets atteignable par une arête depuis un sommet déjà exploré
    #liste à traiter
    lst_v = [sommet_depart]


    #liste des distances depuis le sommet de départ
    distances = {}
    for s in ville_depart:
        if s == sommet_depart:
            distances[s] = {"distance":0,   "relais":s, "traite":False}
        else:
            distances[s] = {"distance":inf,   "relais":"N", "traite":False}


    sommet_courant = sommet_depart
    i = 0
    while len(lst_v) != 0:
        i = i + 1

        #on cherche les voisins atteignables depuis le sommet courant
        vois = ville_depart[sommet_courant]


        #on les ajoute dans la liste des voisins
        #si le sommet n'a pas déjà été traité
        #si le sommet n'est pas déjà dans la liste
        for v in list(vois.keys()):

            if distances[v]["traite"] == False and v not in lst_v:
                lst_v.append(v)
        #on met a jour les distances dans la table distances
        for v in list(vois.keys()):
            #on calcule d la distance entre le voisin et l'origine
            #en passant par le voisin v
            d = vois[v] + distances[sommet_courant]["distance"]
            if d < distances[v]["distance"] and distances[v]["traite"] == False:
                distances[v]["distance"] = d
                distances[v]["relais"] = sommet_courant



        #on supprime le sommet qui vient d'être exploré de la liste des sommets à explorer
        lst_v.pop(lst_v.index(sommet_courant))

        #on indique au dictionnaire distance que le sommet courant vient d'être traité pour qu'on y revienne plus
        distances[sommet_courant]["traite"] = True

        #on recherche le prochain sommet dans la liste v
        d_min = inf
        for v in lst_v:
            if v not in lst_e and distances[v]["traite"] == False:

                #d est la distance entre le sommet courant et le voisin
                d = distances[v]["distance"] + distances[sommet_courant]["distance"]

                if  d < d_min:
                    d_min = d
                    v_min = v

        lst_e.append(sommet_courant)
        sommet_courant = v_min

    return distances





#distances = dijskstra(voisins, "0")
#print(distances)
table = lit_csv_dict("liste-des-gares.csv",";","UTF-8")

gares = extrait_table(table, "DEPARTEMEN", "FINISTERE") + extrait_table(table, "DEPARTEMEN", "COTES-D'ARMOR") +  extrait_table(table, "DEPARTEMEN", "MORBIHAN") + extrait_table(table, "DEPARTEMEN", "ILLE-ET-VILAINE")
        #travail d'ewan
gares_triees = projection(gares, "COMMUNE")
voisins = {}
for g in gares_triees :
    voisins[g["COMMUNE"]] = { }

print(voisins)









