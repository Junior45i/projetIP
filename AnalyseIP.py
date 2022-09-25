from tabnanny import check
import re
import ipaddress
import socket

# Regex de vérification d'une Ip
regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

# Informations des classes Ligne = Classes /// Colonnes = nbr Rés, nbr Hôt
infos_classes = [
                    ["256","2exp24"],
                    ["2exp16","2exp16-2"],
                    ["2exp24","2exp8-2"]
                ]

# Valeurs possibles des octets de masques
val_masque = ("128","192","224","240","248","252","254","255")

# Valeurs possibles des masques des classes
val_masques_classes = ("255.0.0.0","255.0.0.0","255.255.0.0","255.255.255.0")

# Fonction permettant la validation d'une IP
def validationIP(ip):
    if(re.search(regex_ip, ip)):
        return True
    else:
        return False

# Fonction permettant la validation d'un masque
def validationMasque(masque):
    if(masque != "255.255.255.255"):
        if(re.search(regex_ip, masque)):
            array_masque = masque.split(".")
            for i in range(3,0,-1):
                if(array_masque[i] in val_masque):
                    if(array_masque[i-1] != "255"):
                        return False
                else:
                    if(array_masque[i] == "0"):
                        if(array_masque[i-1] != "0" and not(array_masque[i-1] in val_masque)):
                            return False
                    else:
                        return False
            return True
        else:
            return False
    else:
        return False
    
# Fonction permettant de déterminer la classe d'une Ip
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
       
# Fonction récuperant l'adresse réseau d'une Ip et d'un masque    
def calculAdresseReseau(ip, mask):
    host = ipaddress.IPv4Address(ip)
    net = ipaddress.IPv4Network(ip + '/' + mask, False)
    adresseReseau = ipaddress.IPv4Address(int(host) & int(net.netmask))
    return adresseReseau

# Fonction récuperant l'adresse broadcast d'une Ip et d'un masque 
def calculAdresseBroadcast(ip, mask):
    host = ipaddress.IPv4Address(ip)
    net = ipaddress.IPv4Network(ip + '/' + mask, False)
    adresseBroadcast = net.broadcast_address
    return adresseBroadcast

# Fonction de la première fonctionnalité
def fonctionnalite1():
    valid = False
    classe = ""
    nbReseaux = ""
    nbHotes = ""

    while(valid == False):
        ipUtilisateur = input("Veuillez entrer une adresse Ip :")
        valid = True
        if(validationIP(ipUtilisateur) == False):
            print("Adresse Ip entrée invalide")
            valid = False
    
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
    
    print("Classe de l'adresse Ip : " + classe)
    print("Nombre de réseaux de la classe : " + nbReseaux)
    print("Nombre d'hôtes que peut fournir le réseau : " + nbHotes)

# Fonction de la deuxième fonctionnalité
def fonctionnalite2():
    validIp = False
    validMasque = False
    ipUtilisateur = ""
    masqueUtilisateur = ""

    while(validIp == False):
        ipUtilisateur = input("Veuillez entrer une adresse Ip :")
        validIp = True
        if(validationIP(ipUtilisateur) == False):
            print("Adresse Ip entrée invalide")
            validIp = False

    while(validMasque == False):
        masqueUtilisateur = input("Veuillez entrer un masque de réseau :")
        validMasque = True
        if(validationMasque(masqueUtilisateur) == False):
            print("Masque entré invalide")
            validMasque = False

    classeIpUtilisateur = determinationClasse(ipUtilisateur)
    if(classeIpUtilisateur > 0 and classeIpUtilisateur < 5):
        masqueIpClasse = val_masques_classes[classeIpUtilisateur-1]
        print("Adresse de réseau : " + str(calculAdresseReseau(ipUtilisateur,masqueIpClasse)))
        print("Adresse de broadcast du réseau : " + str(calculAdresseBroadcast(ipUtilisateur,masqueIpClasse)))
        if(masqueUtilisateur != masqueIpClasse):
            print("Adresse de sous-réseau : " + str(calculAdresseReseau(ipUtilisateur,masqueUtilisateur)))
            print("Adresse de broadcast du sous-réseau : " + str(calculAdresseBroadcast(ipUtilisateur,masqueUtilisateur)))
    else:
        print("Adresse de réseau : " + str(calculAdresseReseau(ipUtilisateur,masqueUtilisateur)))
        print("Adresse de broadcast du réseau : " + str(calculAdresseBroadcast(ipUtilisateur,masqueUtilisateur)))


        
    

