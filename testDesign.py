from tkinter import *


def btn_clicked():
    print("Button Clicked")


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
    command = btn_clicked,
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
    command = btn_clicked,
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
    command = btn_clicked,
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
    command = btn_clicked,
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
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 578, y = 266,
    width = 253,
    height = 54)

accueil.resizable(False, False)
accueil.mainloop()
