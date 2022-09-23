from tabnanny import check
import re
ip = input("Veuillez entrer l'Ip :")
regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
infos_classes = [["256","2exp24"],
                ["2exp16","2exp16 -2"],
                ["2exp24","2exp8 -2"]]

# Fonction permettant la validation d'une IP sur base d'une IP
def validationIP(ip):
    # Split sur base du point 
    # Vérifie que l'on à bien 4 blocs
    if(re.search(regex_ip, ip)):
        print ("IP BONNE")
        return True
    
def determinationClasse(ip):
    ipSplit = ip.split('.')
    if (int(ipSplit[0]) > 0 and int(ipSplit[0]) <127) :
        print("Classe A")
        return 1
    elif (int(ipSplit[0]) == 127):
        print("Classe A (Réservé)")
        return 2
    elif (int(ipSplit[0]) > 127 and int(ipSplit[0]) <192):
        print("Classe B")
        return 3
    elif (int(ipSplit[0]) > 191 and int(ipSplit[0]) <224):
        print("Classe C")
        return 4
    elif (int(ipSplit[0]) > 223 and int(ipSplit[0]) <240):
        print("Classe D")
        return 5
    elif (int(ipSplit[0]) > 239 and int(ipSplit[0]) <256):
        print("Classe E (expériences protocoles)")
        return 6
    else: 
        print("La classe n'existe pas")
        return 0
    
def infoClasse(classe):
    # Vérifie si une recherche des infos de la classe est nécessaire
    if(classe < 5):
        return True
    else: 
        return False
    

if(determinationClasse(ip) == True):
    print("valide")
else:
    print("Ip invalide")

