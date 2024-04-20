# Importing the libraries
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk

# creating an object
root = tkinter.Tk()

# setting title and geomerty
root.title("BMI Calculator")
root.geometry("470x580+300+200")

# background color for window
root.config(bg="lightgrey")


def bmi():
    Height = float(h.get())
    Weight = float(w.get())
    m = Height / 100  # converting height into meter
    B = round(float(Weight / m ** 2), 1)  # calculating
    label.config(text=B)  # displaying


    if B <= 18.5:
        label1.config(text="Underweight")
    elif (B > 18.5) and (B <= 25):
        label1.config(text="Normal")
    elif (B > 25) and (B <= 30):
        label1.config(text="Overweight")
    else:
        label1.config(text="Health is at risk!\n Need to lose")


top = tkinter.Label(root, text="BMI CALCULATOR", font=("arial", 25, "bold"), width=25, bd=5, bg="white")
top.place(x=300, y=0)

tkinter.Label(root, width=72, height=18, bg="lightcyan").pack(side="bottom")

box = tkinter.PhotoImage(file="bo.png")
tkinter.Label(root, image=box).place(x=20, y=100)
tkinter.Label(root, image=box).place(x=500, y=100)

current = tkinter.DoubleVar()


def get_current():
    return '{: .2f}'.format(current.get())


def slider_c(event):
    height.set(get_current())
    size = int(float(get_current()))
    img = (Image.open("man.png"))
    resize = img.resize((50, 10 + size))
    p = ImageTk.PhotoImage(resize)
    man.config(image=p)
    man.place(x=100, y=600 - size)
    man.image = p
style_h = ttk.Style()
style_h.configure("TScale", background="white")

slider_h = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale", command=slider_c, variable=current)
slider_h.place(x=120, y=250)
current2 = tkinter.DoubleVar()


def get_current2():
    return '{: .2f}'.format(current2.get())


def slider_c2(event):
    weight.set(get_current2())

style_w = ttk.Style()
style_w.configure("TScale", background="white")

slider_w = ttk.Scale(root, from_=0, to=200, orient="horizontal", style="TScale", command=slider_c2, variable=current2)
slider_w.place(x=600, y=250)


height = tkinter.StringVar()
weight = tkinter.StringVar()
h = tkinter.Entry(root, textvariable=height, width=5, font=("arial", 50), bg="white", fg="black", bd=0,
                  justify="center")
h.place(x=80, y=160)
height.set(get_current())

w = tkinter.Entry(root, textvariable=weight, width=5, font=("arial", 50), bg="white", fg="black", bd=0,
                  justify="center")
w.place(x=555, y=160)
weight.set(get_current2())

man = tkinter.Label(root, bg="lightcyan")
man.place(x=70, y=530)

tkinter.Button(root, text="Report", width=15, height=2, font=("Arial", 10, "bold"), bg="#1f6e68", fg="white",
               command=bmi).place(x=1000, y=340)
label = tkinter.Label(root, font=("arial", 30, "bold"), bg="lightcyan", fg="black")
label.place(x=450, y=450)

label1 = tkinter.Label(root, font=("arial", 10, "bold"), bg="lightcyan", fg="black", width=50)
label1.place(x=300, y=500)

root.mainloop()