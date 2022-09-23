from tkinter import *
from tkinter.tix import COLUMN

# Création de la fenêtre
window = Tk()

# Titre de la fenêtre
window.title("Boulogne la meilleur")
window.geometry("1080x720")
window.minsize(480,360)
window.iconbitmap("./images/logo.ico")
window.config(background='#82CEF9')

#Création du frame
frame = Frame(window, bg='#82CEF9',)

#Ajout du texte titre
label_title = Label(frame, text="Informations sur les IP", font=("Courrier", 40), bg='#82CEF9')
label_title.pack()

#Ajout d'un second titre
label_subtitle = Label(frame, text="Test", font=("Courrier", 20), bg='#82CEF9')
label_subtitle.pack()

#Ajouter un bouton
file_menu=Menu(menu_bar, tearoff=0)
menu_bar = Menu(window)
menu_bar.add(label="Test")
window.config(menu=menu_bar)

# ajouter
frame.pack(expand=YES)

# Affichage de la fenêtre
window.mainloop()