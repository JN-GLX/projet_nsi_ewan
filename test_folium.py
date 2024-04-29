# Créé par eleguern, le 10/04/2024 en Python 3.7
import folium
from bibliotheque import *
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

table = lit_csv_dict("liste-des-gares.csv",";","UTF-8")

itineraire = ['BREST', 'LANDERNEAU', 'LAMBALLE']

trail_coordinates = []

for ville in itineraire:
    v = extrait_table(table,'COMMUNE',ville)
    print(v)


    lat = float(v[0]['X_WGS84'])
    long = float(v[0]['Y_WGS84'])
    trail_coordinates.append((lat,long))




m = folium.Map(location=(48.400002, -4.48333))

m.save("index.html")

m = folium.Map(location=[-71.38, -73.9], zoom_start=11)


folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)


"""
m

m = folium.Map([48.400002, -4.48333], zoom_start=9)

folium.Marker(
    location=[48.387779, -4.480458],
    tooltip="Start !",
    popup="Gare de Brest",
    icon=folium.Icon(icon="Cloud"),
).add_to(m)


folium.Marker(
    location=[48.4069, -4.3936],
    tooltip="1er arrêt",
    popup="Gare du Relecq-Kerhuon",
    icon=folium.Icon(icon="Cloud"),
).add_to(m)


folium.Marker(
    location=[48.453717 , -4.256657],
    tooltip="2ème arrêt",
    popup="Gare de Landerneau",
    icon=folium.Icon(icon="Cloud"),
).add_to(m)


folium.Marker(
    location=[48.49588 , -4.082225],
    tooltip="3ème arrêt",
    popup="Gare de Landivisiau",
    icon=folium.Icon(icon="Cloud"),
).add_to(m)

48.555659 , -3.143622
folium.Marker(
    location=[48.57806 , -3.832468],
    tooltip="4ème arrêt",
    popup="Gare de Morlaix",
    icon=folium.Icon(icon="Cloud"),
).add_to(m)


folium.Marker(
    location=[48.555659 , -3.143622],
    tooltip="5ème arrêt",
    popup="Gare de Guingamp",
    icon=folium.Icon(icon="Cloud"),
).add_to(m)

"""
m.save("index.html")


