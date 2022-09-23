from pickle import FALSE, TRUE
from tabnanny import check
import re
import ipaddress
import socket
ip = input("Veuillez entrer l'Ip :")
ip = input("Mask")
regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
infos_classes = [["256","2exp24"],
                ["2exp16","2exp16 -2"],
                ["2exp24","2exp8 -2"]]

# Fonction permettant la validation d'une IP sur base d'une IP
def validationIP(ip):
    try: 
        socket.inet_aton(ip)
        print("vrai")
        return TRUE
    except socket.error:
        print("faux")
        return FALSE
    
def determinationClasse(ip):
    # Rajouter pour 0
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
    
def calculReseau_broadcast(ip, mask):
    host = ipaddress.IPv4Address(ip)
    net = ipaddress.IPv4Network(mask + '/' + mask, False)
    print('Réseau ou Sous-Réseau:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
    print('Broadcast:', net.broadcast_address)
    
def determinationSiMemeReseau(ip,mask,reseau):
    return TRUE

# if(determinationClasse(ip) == True):
#     print("valide")
# else:
#     print("Ip invalide")

