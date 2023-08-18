import tkinter as tk
from tkinter import Tk,Frame,Canvas
from PIL import ImageTk, Image
t = Tk()
t.title("Transparency")

frame = Frame(t)

frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)

canvas.pack()

photoimage = ImageTk.PhotoImage(file="image\开始界面.png")
photoimage2 = ImageTk.PhotoImage(file="image\圈.png")

canvas.create_image(150, 150, image=photoimage)
canvas.create_image(50, 50, image=photoimage2)
t.mainloop()
