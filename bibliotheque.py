

# Créé par Utilisateur, le 27/02/2022 en Python 3.7

def lit_csv_dict(adresse, separateur=";", encoding="utf-8"):
    """
    Crée une liste de dictionnaires à partir d'un fichier csv
    paramètres d'entrée :
    - adresse est l'adresse du fichier sur le disque (string)
    - separateur est le séparateur utilisé dans le fichier csv (string) ";" par défaut
    - encoding est l'encodage. utf-8 par défaut
    paramètre de sortie :
    - Renvoie une liste de dictionnaires
    """

    tableau = []                               # Le tableau qui contiendra les dictionnaires (un par ligne)

    with open(adresse, "r", encoding=encoding) as fichier :                        # On ouvre le fichier
        cles = fichier.readline()                            # La première ligne contient les noms des clés
        cles = cles[:-1].split(separateur)                   # on sépare les différentes cles

        for ligne in fichier :                               # On parcourt les lignes suivantes
            valeurs = ligne[:-1].split(separateur)  #on sépare les différentes valeurs de la ligne
            dico = dict()                                    # On cree un dictionnaire pour la ligne
            # On remplit le dictionnaire de la ligne
            for cle, valeur in zip(cles, valeurs):
                dico[cle] = valeur
            tableau.append(dico)                           # On rajoute ce dictionnaire au tableau

    return tableau                                   # On renvoie le tableau contenant les dictionnaires




def projection(table, liste_descripteurs):
    """
    paramètres d'entrée :
        la table de dictionnaires
        la liste de descripteurs est une liste des champs à garder
    action :
        ne garde que certains champs de la table
        crée une table "projetée" suivant la liste des champs retenus ['descript1', 'descript2',... ]
    paramètre de sortie
         la table projetée
    """
    ma_liste=[]  # on déclare une nouvelle liste vide
    for ligne in table : # on parcourt la table de dictionnaire
        mon_dico = {} #  # on cree le nouveau dictionnaire
        for clé in ligne :  #pour chaque clé du dictoinnaire de départ
            if clé in liste_descripteurs :  #si la clé est dans la liste de la projection
                mon_dico[clé] = ligne[clé]  #  on ajoute l'élement dans le nouveau dictionnaire
        ma_liste.append(mon_dico)  # on ajoute le dictionnaire dans la nouvelle liste vide
    return ma_liste



def tri(table, champ, r = False):
    """
    paramètres d'entrée :
    - la table à trier
    - le champ sur lequel on doit trier
    - un boolean pour trier dans l'ordre inverse, False par défaut : par défaut la liste est triée dans l'ordre croissant

    paramètre de sortie
    - la table triée
    """

    def critere(ligne):
        return int(ligne[champ])

    ma_table_triee = sorted(table,key = critere, reverse = r)
    return ma_table_triee



def extrait_table(table, champ, valeur):
    """
    Action : garde certaines lignes de la table de départ, dont le champ est égal à valeur
    paramètres d'entrée :
        - table : la table de départ
        - champ : le nom du champ qui sert de critère
        - valeur : la valeur que doit avoir le champ pour que l'on garde la ligne
    """
    nouvelle_table = []
    for ligne in table:
        if ligne[champ] == valeur:
            nouvelle_table.append(ligne)
    return nouvelle_table


