from tkinter import *


def btn_clicked():
    print("Button Clicked")

    
    window = Tk()
    window.geometry("881x605")
    window.configure(bg = "#ffffff")
    window.iconbitmap('./images/logo.ico')
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 605,
        width = 881,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"./images/accueil/background.png")
    background = canvas.create_image(
        440.5, 296.5,
        image=background_img)

    img0 = PhotoImage(file = f"./images/accueil/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 524, y = 185,
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
        x = 524, y = 289,
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
        x = 524, y = 391,
        width = 253,
        height = 54)

    window.resizable(False, False)
    window.mainloop()
