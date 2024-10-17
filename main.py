from tkinter import *
from random import choice
window = Tk()

btn1 = Button(window,text = "нажми сюда",font=(None,24))
btn1.grid(row = 0 , column= 0)

color_list = ["red","blue","black","orange","purple","gold"]
def chenge_color(event):
    color = choice(color_list)
    btn1["bg"] = color

btn1.bind('<Button-1>',chenge_color)




window.mainloop()