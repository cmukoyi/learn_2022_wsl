
from tkinter import *

window = Tk() #instatiate an instance of a window

window.geometry("420x420")
window.title("Visight-Solutions SA")

icon = PhotoImage(file='C:/Users/Carl/Desktop/Education/Python/py3_learn_2022/.venv/gui/logo.png')
window.iconphoto(True,icon)
window.config(background="#349eeb")

window.mainloop() #this will place window on computer scree
