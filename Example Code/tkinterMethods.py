from tkinter import *

window = Tk()

window.geometry("500x500+0+0")
window.title("tKinter Methods")

def label(text, row, column):
    Label(window, 
          text=text,
          width=20, 
          font=("bold", 10),
          bg='#202C4F')                    
    label.grid(row=row, column=column) 
    
label("Test", 0, 0)