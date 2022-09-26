from cgi import test
from tkinter import *
from tokenize import String
import AnalyseIP


def partie1():
    
    texte = "test"
    
    def btnAccueil():
        partie1.destroy()
        accueil()
        
    def btnCalcul():
        classe = AnalyseIP.determinationClasse(entry0.get())
        print(classe)
        return classe
        
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



    lClasse = Label(partie1, text = texte )
    lClasse.place(
        x = 350, y = 315,
        width = 300,
        height = 30)
    lClasse['background'] = '#D9D9D9'
    
    lReseau = Label(partie1, text = texte )
    lReseau.place(
        x = 350, y = 390,
        width = 300,
        height = 30)
    lReseau['background'] = '#D9D9D9'
    
    lHote = Label(partie1, text = texte )
    lHote.place(
        x = 350, y = 462,
        width = 300,
        height = 30)
    lHote['background'] = '#D9D9D9'

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
        command = btn_clicked,
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

    partie2.resizable(False, False)
    partie2.mainloop()

    
# MAIN

def accueil():
    
    def btnParti1():
        accueil.destroy()
        partie1()
        
    def btnParti2():
        accueil.destroy()
        partie2()
        
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
        command = btnParti1,
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
        command = btnParti1,
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
    

connection = Tk()
connection.geometry("1000x600")
connection.configure(bg = "#FFFFFF")
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
    highlightthickness = 0)

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
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 156, y = 410,
    width = 244,
    height = 42)

connection.resizable(False, False)
connection.mainloop()

