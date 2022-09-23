from tabnanny import check
import re
import ipaddress
import socket

regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
infos_classes = [
                    ["256","2exp24"],
                    ["2exp16","2exp16-2"],
                    ["2exp24","2exp8-2"]
                ]

# Fonction permettant la validation d'une IP sur base d'une IP
def validationIP(ip):
    if(re.search(regex_ip, ip)):
        return True
    else:
        return False
    
def determinationClasse(ip):
    # Rajouter pour 0
    ipSplit = ip.split('.')
    if(int(ipSplit[0]) == 0):
        return 0
    elif(int(ipSplit[0]) > 0 and int(ipSplit[0]) < 127) :
        return 1
    elif(int(ipSplit[0]) == 127):
        return 2
    elif(int(ipSplit[0]) > 127 and int(ipSplit[0]) < 192):
        return 3
    elif(int(ipSplit[0]) > 191 and int(ipSplit[0]) < 224):
        return 4
    elif(int(ipSplit[0]) > 223 and int(ipSplit[0]) < 240):
        return 5
    else :
        return 6
    
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
    return True

def fct1():
    valid = False
    classe = ""
    nbReseaux = ""
    nbHotes = ""
    while(valid == False):
        ipUtilisateur = input("Veuillez entrer une adresse Ip :")
        valid = True
        if(validationIP(ipUtilisateur)):
            if(determinationClasse(ipUtilisateur) == 0):
                classe = "Adresse réservée"
                nbReseaux = "Cette adresse n'est pas utilisée pour l'adressage des hôtes"
                nbHotes = "Cette adresse n'est pas utilisée pour l'adressage des hôtes"
            elif(determinationClasse(ipUtilisateur) == 1):
                classe = "Adresse de classe A"
                nbReseaux = infos_classes[0][0]
                nbHotes = infos_classes[0][1]
            elif(determinationClasse(ipUtilisateur) == 2):
                classe = "Adresse de classe A (Réservée)"
                nbReseaux = infos_classes[0][0]
                nbHotes = infos_classes[0][1]
            elif(determinationClasse(ipUtilisateur) == 3):
                classe = "Adresse de classe B"
                nbReseaux = infos_classes[1][0]
                nbHotes = infos_classes[1][1]
            elif(determinationClasse(ipUtilisateur) == 4):
                classe = "Adresse de classe C"
                nbReseaux = infos_classes[2][0]
                nbHotes = infos_classes[2][1]
            elif(determinationClasse(ipUtilisateur) == 5):
                classe = "Adresse de classe D (Multicast)"
                nbReseaux = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
                nbHotes = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
            else:
                classe = "Adresse de classe E (Expériences protocoles)"
                nbReseaux = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
                nbHotes = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
        else:
            print("Adresse Ip entrée invalide")
            valid = False
    
    print("Classe de l'adresse Ip : " + classe)
    print("Nombre de réseaux de la classe : " + nbReseaux)
    print("Nombre d'hôtes que peut fournir le réseau : " + nbHotes)

fct1()
        
    

