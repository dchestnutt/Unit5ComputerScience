from tkinter import *
from tkinter import messagebox as ms
from tkinter import Menu
import sqlite3

window = Tk()
window.geometry('1000x500+0+0')
window.title("Example Code")          

usernameNew = StringVar()
passwordNew = StringVar()

# ***** Defining Functions ***** #

# Create a New User Account #
def createUser():
    tempWindow = Tk()
    tempWindow.geometry('500x300+100+100')
    tempWindow.title("Create a New User")

    #labelInstructions = Label(tempWindow, 
    #                         text="Please enter new user details below.", 
    #                         width=20, 
    #                         font=("Century Gothic", 10),
    #                         anchor=CENTER)                 
    #labelInstructions.pack(side=LEFT, padx=5, pady=5)
    #labelInstructions.grid(row=0, column=0, columnspan=3) 

    #spacerLabel = Label(tempWindow, text=" ", width=20)
    #spacerLabel.pack(side=LEFT, padx=5, pady=5)
    #spacerLabel.grid(row=1, column=0, columnspan=3)

    labelUsername = Label(tempWindow, 
                          text="Username: ", 
                          width=4, 
                          font=("Century Gothic", "bold", 10))                 
    labelUsername.pack(side=LEFT, padx=5, pady=5)
    #labelUsername.grid(row=2, column=0)                   
    entryUsername = Entry(tempWindow, textvar=usernameNew) 
    entryUsername.pack(fill=X, padx=5, expand=True)
    #entryUsername.grid(row=2, column=1, columnspan=2)            
    
    labelPassword = Label(tempWindow, 
                          text="Username: ", 
                          width=4, 
                          font=("Century Gothic", "bold", 10))                 
    labelPassword.pack(side=LEFT, padx=5, pady=5)
    #labelPassword.grid(row=3, column=0)                   
    entryPassword = Entry(tempWindow, textvar=passwordNew) 
    entryPassword.pack(fill=X, padx=5, expand=True)
    #entryPassword.grid(row=3, column=1, columnspan=2)

# Edit an Existing User Account #
def editUser():
    print("Doing Nothing.")

# Change current User Account #
def changeUser():
    print("Doing Nothing.")

# Log-out of the System #
def logOff():
    print("Doing Nothing.")

# ***** The Menu Bar ***** #

menu = Menu(window)

dropdownUsers = Menu(menu) 

dropdownUsers.add_command(label='Create New User', command=createUser) 
dropdownUsers.add_command(label='Edit Existing User', command=editUser) 
dropdownUsers.add_command(label='Change User', command=changeUser)
dropdownUsers.add_command(label='Log-Off', command=logOff)

menu.add_cascade(label='User Accounts', menu=dropdownUsers)

window.config(menu=menu)

window.mainloop()