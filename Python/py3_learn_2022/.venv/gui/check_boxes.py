
from tkinter import *

def display():
    if(x.get()==1):
        print("You Agree")
    else:
        print("You dont agree")

window =Tk()

x = IntVar()

check_box = Checkbutton(window,
                        text="I agree to TCs",
                        variable=x,
                        onvalue=1,
                        offvalue=0,
                        command=display
                       )
check_box.pack()

window.mainloop()