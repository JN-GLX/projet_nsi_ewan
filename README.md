# COMMENTAIRES JNG SUR CODE

## 1 - Nommage des variables

Il faudrait prendre la peine de donner
des noms explicites aux variables (mêmes locales) pour aider à mieux
comprendre ce que le code est censé faire.
Les éditeurs de code aident à la saisie, donc il ne faut pas avoir peur
de la longueur du nom de la variable

## 2 - Longueur des lignes de code

Améliorer la lisibilité du code en limitant la longueur des lignes
à 79 caractères (les éditeurs de code peuvent afficher une règle)
Quand le code n'est pas entre parenthèses, il faut mettre '\' à la fin
de la ligne et continuer sur la ligne suivante

## 3 - Longueur et rôle des fonctions

Une fonction ne doit pas être trop longue, et ne devrait faire qu'une
seule chose (et le faire bien :-))
Il faudrait découper certaines fonctions/méthodes, notamment __init__
en plusieurs petites fonctions (avec des noms explicites):
ça aidera à la compréhension du code et au débogage

