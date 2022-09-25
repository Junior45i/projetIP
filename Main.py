# Main du projet

from AnalyseIP import fonctionnalite1, fonctionnalite2


choixValid = False

print("1) Déterminer la classe d'une Ip et ses caractéristiques")
print("2) Déterminer l'adresse réseau et de broadcast d'une Ip")
print("3) Déterminer si une Ip fait partie d'un réseau")
print("4) Déterminer si deux adresses Ip font parties du même réseau")
print("5) Déterminer les caractéristiques d'un sous-réseau")

# Switch des choix du menus
while(choixValid == False):
    choix = input("Veuillez faire un choix de fonctionnalité : ")
    print(choix)
    choixValid = True

    if(choix == "1"):
        fonctionnalite1()
    elif(choix == "2"):
        fonctionnalite2()
    else:
        choixValid = False
        print("Choix invalide, veuillez réessayer")