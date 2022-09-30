from tabnanny import check
import re
import ipaddress
import socket

# Regex de vérification d'une Ip
regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

# Informations des classes Ligne = Classes /// Colonnes = nbr Rés, nbr Hôt
infos_classes = [
                    ["256","16777216"],
                    ["65536","65534"],
                    ["16777216","254"]
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

# Fonction permettant d'afficher les caractéristiques d'une classe
def caracteristiquesClasse(numClasse):
    classe = ""
    nbReseaux = ""
    nbHotes = ""
    if(numClasse == 0):
        classe = "Adresse réservée"
        nbReseaux = "Cette adresse n'est pas utilisée pour l'adressage des hôtes"
        nbHotes = "Cette adresse n'est pas utilisée pour l'adressage des hôtes"
    elif(numClasse == 1):
        classe = "Adresse de classe A"
        nbReseaux = infos_classes[0][0]
        nbHotes = infos_classes[0][1]
    elif(numClasse == 2):
        classe = "Adresse de classe A (Réservée)"
        nbReseaux = infos_classes[0][0]
        nbHotes = infos_classes[0][1]
    elif(numClasse == 3):
        classe = "Adresse de classe B"
        nbReseaux = infos_classes[1][0]
        nbHotes = infos_classes[1][1]
    elif(numClasse == 4):
        classe = "Adresse de classe C"
        nbReseaux = infos_classes[2][0]
        nbHotes = infos_classes[2][1]
    elif(numClasse == 5):
        classe = "Adresse de classe D (Multicast)"
        nbReseaux = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
        nbHotes = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
    else:
        classe = "Adresse de classe E (Expériences protocoles)"
        nbReseaux = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
        nbHotes = "Cette classe n'est pas utilisée pour l'adressage des hôtes"
    
    # Retour d'un tableau contenant les caractéristiques de la classe
    # 0:classe     1:nbre réseaux     2:nbre hôtes
    carac = []
    carac.append(classe)
    carac.append(nbReseaux)
    carac.append(nbHotes)
    print("Classe : " + carac[0])
    print("Nbr réseaux : " + carac[1])
    print("Nbr hôtes : " + carac[2])
    return carac

# Fonction permettant de renvoyer les ip d'adresse et de broadcast du réseau et sous-réseau
# 0:adresse du réseau     1:adresse broadcast du réseau     2:adresse de sous-réseau     3:adresse broadcast de sous-réseau
def determinationAdresse(ip, masque):
    classeIpUtilisateur = determinationClasse(ip)
    adresse = ""
    broadcast = ""
    adresseSR = ""
    broadcastSR = ""

    if(classeIpUtilisateur >= 0 and classeIpUtilisateur < 5):
        masqueIpClasse = val_masques_classes[classeIpUtilisateur-1]
        adresse = str(calculAdresseReseau(ip,masqueIpClasse))
        broadcast = str(calculAdresseBroadcast(ip,masqueIpClasse))

        if(masque != masqueIpClasse):
            adresseSR = str(calculAdresseReseau(ip,masque))
            broadcastSR = str(calculAdresseBroadcast(ip,masque))
        else:
            adresseSR = "Il ne s'agit pas d'un sous-réseau"
            broadcastSR = "Il ne s'agit pas d'un sous-réseau"
    else:
        adresse = str(calculAdresseReseau(ip,masque))
        broadcast = str(calculAdresseBroadcast(ip,masque))
        adresseSR = "Il ne s'agit pas d'un sous-réseau"
        broadcastSR = "Il ne s'agit pas d'un sous-réseau"
    
    adresses = []
    adresses.append(adresse)
    adresses.append(broadcast)
    adresses.append(adresseSR)
    adresses.append(broadcastSR)
    print("Adresse : " + adresses[0])
    print("Adresse BC : " + adresses[1])
    print("Adresse SR : " + adresses[2])
    print("Adresse SR BC : " + adresses[3])
    return adresses

def verifEgaliteAdresse(ip, mask, adresse):
    adresseACompare = calculAdresseReseau(ip, mask)
    return str(adresseACompare) == str(adresse)

# Fonction de la première fonctionnalité
def fonctionnalite1():
    valid = False

    while(valid == False):
        ipUtilisateur = input("Veuillez entrer une adresse Ip :")
        valid = True
        if(validationIP(ipUtilisateur) == False):
            print("Adresse Ip entrée invalide")
            valid = False

    caracteristiquesClasse(determinationClasse(ipUtilisateur))

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

    determinationAdresse(ipUtilisateur,masqueUtilisateur)

def fonctionnalite3():
    validIp = False
    validMasque = False
    validAdresse = False
    ipUtilisateur = ""
    masqueUtilisateur = ""
    adresseUtilisateur = ""

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

    while(validAdresse == False):
        adresseUtilisateur = input("Veuillez entrer une adresse réseau :")
        validAdresse = True
        if(validationIP(adresseUtilisateur) == False):
            print("Adresse réseau entrée invalide")
            validAdresse = False

    if(verifEgaliteAdresse(ipUtilisateur, masqueUtilisateur, adresseUtilisateur)):
        print("Cette Ip fait partie de ce réseau")
    else:
        print("Cette Ip ne fait pas partie de ce réseau")

# fonctionnalite3()


        
    

