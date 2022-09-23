import re
ip = input("Veuillez entrer l'Ip :")
masque = input("Veuillez entrer le masque :")

regex_ip = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
val_masque = ("128","192","224","240","248","252","254","255")

def checkIp(ip):
    if(re.search(regex_ip, ip)):
        return True

def checkMasque(masque):
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

def create_sr(ip,masque):
    array_ip = ip.split(".")
    array_masque = masque.split(".")
    array_et_sr = []
    for i in range(len(array_ip)):
        array_et_sr.append(str(int(array_ip[i]) & int(array_masque[i])))
    et_sr = ".".join(array_et_sr)
    return et_sr

if(checkIp(ip) == True):
    if(checkMasque(masque) == True):
        print("Ip sous-réseau :" + create_sr(ip,masque))
    else:
        print("Masque invalide")     
else:
    print("Ip invalide")

