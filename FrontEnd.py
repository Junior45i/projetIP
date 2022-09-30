from base64 import encode
from cgi import test
from tkinter import *
from tokenize import String
import AnalyseIP
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import bcrypt


connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="ppython")
cursordb = connectiondb.cursor()


def login_verification():
    user_verification = ""
    user_verification = entry1.get()
    pass_verification = entry0.get()
    #Hash et sal
    pass_verification = pass_verification.encode('utf-8')
    saltDepart = bcrypt.gensalt(rounds=10)
    hashedDepart = bcrypt.hashpw(pass_verification, saltDepart)
    print(hashedDepart)
    # requetes sql
    # try:
    result = ""
    try:
        sql = "select mdpUtilisateur from utilisateur where nomUtilisateur = %s"
        cursordb.execute(sql,[(user_verification)])
        results = cursordb.fetchone()
        result = results[0]
        result = str(result)
        result = result.encode('utf-8')
        if results:
            if(bcrypt.checkpw(pass_verification,result)):
                connection.destroy()    
                accueil()
            else:
                messagebox.showerror("Erreur", "Combinaison LOGIN/MDP incorrecte")
        else:
            messagebox.showerror("Erreur", "Combinaison LOGIN/MDP incorrecte")
    except:
        messagebox.showerror("Erreur", "Combinaison LOGIN/MDP incorrecte")
    # except:
    #         messagebox.showerror("Erreur", "Combinaison LOGIN/MDP incorrecte")


# Créer une frame de la taille de la fenêtre
# Cela permet de ne pas supprimer la fenetre


# liste des variables
tailleEcran = "1000x600"
colorBack = "#D9D9D9"


def partie1():
    
    def btnAccueil():
        partie1.destroy()
        accueil()
        
    def btnCalcul():
        if(AnalyseIP.validationIP(entry0.get())):
            classe = AnalyseIP.caracteristiquesClasse(AnalyseIP.determinationClasse(entry0.get()))
            lClasse.config(text=str(classe[0]))
            lReseau.config(text=str(classe[1]))
            lHote.config(text=str(classe[2]))
        else:
            lClasse.config(text="IP Invalide")
            lReseau.config(text="IP Invalide")
            lHote.config(text="IP Invalide")
        
    partie1 = Tk()
    partie1.geometry("1000x600")
    partie1.configure(bg = "#ffffff")
    canvas = Canvas(
        partie1,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/partie1/background.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"./images/partie1/img_textBox0.png")
    entry0_bg = canvas.create_image(
        480.0, 239.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 282, y = 218,
        width = 396,
        height = 40)

    lClasse = Label(partie1)
    lClasse.place(
        x = 350, y = 315,
        width = 300,
        height = 30)
    lClasse['background'] = colorBack
    
    lReseau = Label(partie1)
    lReseau.place(
        x = 350, y = 390,
        width = 300,
        height = 30)
    lReseau['background'] = colorBack
    
    lHote = Label(partie1)
    lHote.place(
        x = 350, y = 462,
        width = 300,
        height = 30)
    lHote['background'] = colorBack

    img0 = PhotoImage(file = f"./images/partie1/img0.png")
    btn_calcul = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnCalcul,
        relief = "flat")

    btn_calcul.place(
        x = 693, y = 218,
        width = 191,
        height = 42)

    img1 = PhotoImage(file = f"./images/partie1/img1.png")
    btn_Accueil = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnAccueil,
        relief = "flat")

    btn_Accueil.place(
        x = 93, y = 91,
        width = 118,
        height = 109)

    partie1.resizable(False, False)
    partie1.mainloop()

def partie2():
    def btn_clicked():
        partie2.destroy()
        accueil()
        
    def btnCalcul():
        if(AnalyseIP.validationIP(entry0.get())):
            if(AnalyseIP.validationMasque(entry1.get())):
                adresses = AnalyseIP.determinationAdresse(entry0.get(),entry1.get())
                lAdresse.config(text=str(adresses[0]))
                lBroadcast.config(text=str(adresses[1]))
                lAdresseSR.config(text=str(adresses[2]))
                lBroadcastSR.config(text=str(adresses[3]))
            else:
                lAdresse.config(text="Masque Invalide")
                lBroadcast.config(text="Masque Invalide")
                lAdresseSR.config(text="Masque Invalide")
                lBroadcastSR.config(text="Masque Invalide")
        else:
                lAdresse.config(text="IP invalide")
                lBroadcast.config(text="IP invalide")
                lAdresseSR.config(text="IP invalide")
                lBroadcastSR.config(text="IP invalide")
        
        
    partie2 = Tk()
    partie2.geometry("1000x600")
    partie2.configure(bg = "#ffffff")
    canvas = Canvas(
        partie2,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/partie2/background.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"./images/partie2/img_textBox0.png")
    entry0_bg = canvas.create_image(
        477.0, 225.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 279, y = 204,
        width = 396,
        height = 40)

    img0 = PhotoImage(file = f"./images/partie2/img0.png") 
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnCalcul,
        relief = "flat")

    b0.place(
        x = 689, y = 228,
        width = 191,
        height = 42)

    img1 = PhotoImage(file = f"./images/partie2/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 93, y = 91,
        width = 118,
        height = 109)

    entry1_img = PhotoImage(file = f"./images/partie2/img_textBox1.png")
    entry1_bg = canvas.create_image(
        477.0, 281.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1.place(
        x = 279, y = 260,
        width = 396,
        height = 40)

    # Liste des labels d'affichage
    lAdresse = Label(partie2, text="")
    lAdresse.place(
        x = 600, y = 330,
        width = 300,
        height = 30)
    lAdresse['background'] = colorBack
    
    lBroadcast = Label(partie2,text="")
    lBroadcast.place(
        x = 600, y = 373,
        width = 300,
        height = 30)
    lBroadcast['background'] = colorBack
    
    lAdresseSR = Label(partie2,text="")
    lAdresseSR.place(
        x = 600, y = 415,
        width = 300,
        height = 30)
    lAdresseSR['background'] = colorBack
    
    lBroadcastSR = Label(partie2,text="")
    lBroadcastSR.place(
        x = 600, y = 459,
        width = 300,
        height = 30)
    lBroadcastSR['background'] = colorBack

    partie2.resizable(False, False)
    partie2.mainloop()

def partie3():
    def btnAccueil():
        partie3.destroy()
        accueil()
        
    def btnCalcul():
        if(AnalyseIP.validationIP(entry0.get())):
            if(AnalyseIP.validationMasque(entry1.get())):
                if(AnalyseIP.validationIP(entry2.get())):
                    if(AnalyseIP.verifEgaliteAdresse(entry0.get(), entry1.get(), entry2.get())):
                        lResult.config(text="Cette Ip fait partie de ce réseau")
                    else:
                        lResult.config(text="Cette Ip ne fait pas partie de ce réseau")
                else:
                    lResult.config(text="Ip réseau invalide")
            else:
                lResult.config(text="Masque invalide")
        else: 
            lResult.config(text="IP invalide")
    
    partie3 = Tk()
    partie3.geometry("1000x600")
    partie3.configure(bg = "#ffffff")
    canvas = Canvas(
        partie3,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/partie3/background.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"./images/partie3/img_textBox0.png")
    entry0_bg = canvas.create_image(
        500.0, 231.0,
        image = entry0_img)

    lResult = Label(partie3, text="")
    lResult.place(
        x = 400, y = 430,
        width = 300,
        height = 30)
    lResult['background'] = colorBack

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 302, y = 210,
        width = 396,
        height = 40)

    entry1_img = PhotoImage(file = f"./images/partie3/img_textBox1.png")
    entry1_bg = canvas.create_image(
        500.0, 295.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1.place(
        x = 302, y = 274,
        width = 396,
        height = 40)

    entry2_img = PhotoImage(file = f"./images/partie3/img_textBox2.png")
    entry2_bg = canvas.create_image(
        500.0, 358.0,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry2.place(
        x = 302, y = 337,
        width = 396,
        height = 40)

    img0 = PhotoImage(file = f"./images/partie3/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnCalcul,
        relief = "flat")

    b0.place(
        x = 139, y = 420,
        width = 191,
        height = 42)

    img1 = PhotoImage(file = f"./images/partie3/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnAccueil,
        relief = "flat")

    b1.place(
        x = 93, y = 91,
        width = 118,
        height = 109)

    partie3.resizable(False, False)
    partie3.mainloop()

def partie4():
    def btnAccueil():
        partie4.destroy()
        accueil()
    
    def btnCalcul():
        if(AnalyseIP.validationIP(entry0.get())):
            if(AnalyseIP.validationMasque(entry1.get())):
                if(AnalyseIP.validationIP(entry2.get())):
                    if(AnalyseIP.validationMasque(entry3.get())):
                        if(AnalyseIP.verifEgaliteAdresseDeuxIp(entry0.get(), entry1.get(), entry2.get(), entry3.get())):
                              lResult.config(text="Les deux machines considère l'autre comme faisant partie de son réseau")
                        else:
                            lResult.config(text="Les deux machines ne considère pas l'autre comme faisant partie de son réseau")
                    else:
                        lResult.config(text="Le masque 2 est invalide")
                else:
                    lResult.config(text="L'IP 2 est invalide")
            else:
                lResult.config(text="Le masque 1 est invalide")
        else: 
            lResult.config(text="L'IP 1 est invalide")
    
    partie4 = Tk()

    partie4.geometry("1000x600")
    partie4.configure(bg = "#ffffff")
    canvas = Canvas(
        partie4,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/partie4/background.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"./images/partie4/img_textBox0.png")
    entry0_bg = canvas.create_image(
        480.0, 239.0,
        image = entry0_img)

    lResult = Label(partie4,text="")
    lResult.place(
        x = 250, y = 459,
        width = 500,
        height = 30)
    lResult['background'] = colorBack

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 282, y = 218,
        width = 396,
        height = 40)

    img0 = PhotoImage(file = f"./images/partie4/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnCalcul,
        relief = "flat")

    b0.place(
        x = 707, y = 298,
        width = 191,
        height = 42)

    img1 = PhotoImage(file = f"./images/partie4/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnAccueil,
        relief = "flat")

    b1.place(
        x = 93, y = 91,
        width = 118,
        height = 109)

    entry1_img = PhotoImage(file = f"./images/partie4/img_textBox1.png")
    entry1_bg = canvas.create_image(
        480.0, 291.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry1.place(
        x = 282, y = 270,
        width = 396,
        height = 40)

    entry2_img = PhotoImage(file = f"./images/partie4/img_textBox2.png")
    entry2_bg = canvas.create_image(
        480.0, 361.0,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry2.place(
        x = 282, y = 340,
        width = 396,
        height = 40)

    entry3_img = PhotoImage(file = f"./images/partie4/img_textBox3.png")
    entry3_bg = canvas.create_image(
        479.0, 413.0,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry3.place(
        x = 281, y = 392,
        width = 396,
        height = 40)

    partie4.resizable(False, False)
    partie4.mainloop()
    
# MAIN

def accueil():
    
    def btnParti1():
        accueil.destroy()
        partie1()
        
    def btnParti2():
        accueil.destroy()
        partie2()
    
    def btnParti3():
        accueil.destroy()
        partie3()
    
    def btnParti4():
        accueil.destroy()
        partie4()
        
    accueil = Tk()
    accueil.geometry("1000x600")
    accueil.configure(bg = "#ffffff")
    canvas = Canvas(
        accueil,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/accueil/background.png")
    background = canvas.create_image(
        500.0, 300.0,
        image=background_img)

    img0 = PhotoImage(file = f"./images/accueil/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnParti1,
        relief = "flat")

    b0.place(
        x = 578, y = 100,
        width = 253,
        height = 54)

    img1 = PhotoImage(file = f"./images/accueil/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnParti2,
        relief = "flat")

    b1.place(
        x = 578, y = 183,
        width = 253,
        height = 54)

    img2 = PhotoImage(file = f"./images/accueil/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnParti4,
        relief = "flat")

    b2.place(
        x = 578, y = 349,
        width = 253,
        height = 54)

    img3 = PhotoImage(file = f"./images/accueil/img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnParti1,
        relief = "flat")

    b3.place(
        x = 578, y = 432,
        width = 253,
        height = 54)

    img4 = PhotoImage(file = f"./images/accueil/img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btnParti3,
        relief = "flat")

    b4.place(
        x = 578, y = 266,
        width = 253,
        height = 54)

    accueil.resizable(False, False)
    accueil.mainloop()

def btn_clicked():
    if(entry1.get()=="test" and entry0.get()=="test2"):
        connection.destroy()
        accueil()
    else:
        messagebox.showerror("Erreur", "Combinaison LOGIN/MDP incorrecte")

connection = Tk()
connection.geometry("1000x600")
connection.configure(bg = "#FFFFFF")
# essayer de créer une frame
canvas = Canvas(
    connection,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"./images/connection/background.png")
background = canvas.create_image(
    500.0, 300.0,
    image=background_img)

entry0_img = PhotoImage(file = f"./images/connection/img_textBox0.png")
entry0_bg = canvas.create_image(
    262.5, 325.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#1094cb",
    highlightthickness = 0,
    show='*'
    )

entry0.place(
    x = 138.0, y = 313,
    width = 249.0,
    height = 22)

entry1_img = PhotoImage(file = f"./images/connection/img_textBox1.png")
entry1_bg = canvas.create_image(
    263.0, 273.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#1094cb",
    highlightthickness = 0)

entry1.place(
    x = 139.0, y = 261,
    width = 248.0,
    height = 22)

img0 = PhotoImage(file = f"./images/connection/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = login_verification,
    relief = "flat")

b0.place(
    x = 156, y = 410,
    width = 244,
    height = 42)

connection.resizable(False, False)
connection.mainloop()

