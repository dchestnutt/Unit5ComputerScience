######################################################
## Example tKinkter Code for use in GUI Development ##
######################################################

from tkinter import *
from tkinter import Menu

window = Tk()
window.geometry('500x500')
window.title("Example Code")

menu = Menu(window)

dropdown1 = Menu(menu) 
dropdown1.add_command(label='New')
menu.add_cascade(label='File', menu=dropdown1)

window.config(menu=menu)

window.mainloop()