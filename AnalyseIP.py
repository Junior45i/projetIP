from tabnanny import check
import re
ip = input("Veuillez entrer l'Ip :")
regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"


# Fonction permettant la validation d'une IP sur base d'une IP
def validationIP(ip):
    # Split sur base du point
    # Vérifie que l'on à bien 4 blocs
    if(re.search(regex_ip, ip)):
        return True 
    
if(validationIP(ip) == True):
    print("valide")
else:
    print("Ip invalide")

# ipSplit = ip.split('.')  