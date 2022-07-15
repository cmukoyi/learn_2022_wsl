from tkinter import *

window = Tk()

photo = PhotoImage(file='C:/Users/Carl/Desktop/Education/Python/py3_learn_2022/.venv/gui/logo.png')

window.geometry("420x420")
label = Label(window,
              text="ViSight Software Dev",
              font=('Arial',10,'bold'),
              fg='#FFFFFF',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom'
              )

window.config(background="black")
label.pack()
#label.place(x=0,0)


window.mainloop()
