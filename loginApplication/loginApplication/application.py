######################################
## WJEC GCE Computer Science Unit 5 ##
## Daniel Chestnutt - 71401 - 2127  ##
## application.py - Main Window(s)  ##
######################################

# ***** Importing Modules ***** #

from tkinter import *
from tkinter import messagebox as ms
from tkinter import Menu
import sqlite3

# ***** Creating the Window ***** #

window = Tk()
window.geometry('1000x500+0+0')
window.title("Example Code")          

# ***** Defining Variables ***** #

usernameNew = StringVar()
passwordNew = StringVar()
canViewPatientData = StringVar()
canEditPatientData = StringVar()
canViewConsultations = StringVar()
canEditConsultations = StringVar()
canCommunicatePatients = StringVar()
canViewStatistics = StringVar()
canViewAppointments = StringVar()
canCancelAppointments = StringVar()
canCreateUsers = StringVar()
canEditUsers = StringVar()
titleNew = StringVar()
firstnameNew = StringVar()
surnameNew = StringVar()
emailNew = StringVar()
mobileNew = StringVar()

# ***** Defining Functions ***** #

# Create a New User Account #
def createUser():
    tempWindow = Tk()
    tempWindow.geometry('700x300+100+100')
    tempWindow.title("Create a New User")

    def appendUser():
        usernameNew1 = usernameNew.get()
        passwordNew1 = passwordNew.get()
        canViewPatientData1 = canViewPatientData.get()
        canEditPatientData1 = canEditPatientData.get()
        canViewConsultations1 = canViewConsultations.get()
        canEditConsultations1 = canEditConsultations.get()
        canCommunicatePatients1 = canCommunicatePatients.get()
        canViewStatistics1 = canViewStatistics.get()
        canViewAppointments1 =  canViewAppointments.get()
        canCancelAppointments1 =  canCancelAppointments.get()
        canCreateUsers1 = canCreateUsers.get()
        canEditUsers1 = canEditUsers.get()
        titleNew1 = titleNew.get()
        firstnameNew1 = firstnameNew.get()
        surnameNew1 = surnameNew.get()
        emailNew1 = emailNew.get()
        mobileNew1 = mobileNew.get()

        conn = sqlite3.connect('Users.db')
        with conn:
            cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS UserAccounts (username TEXT, password TEXT, ViewPatientData TEXT, EditPatientData TEXT, ViewConsultations TEXT, EditConsultations TEXT, CommunicatePatients TEXT, ViewStatistics TEXT, ViewAppointments TEXT, CancelAppointments TEXT, CreateUsers TEXT, EditUsers TEXT, title TEXT, firstname TEXT, surname TEXT, email TEXT, mobile TEXT)")
        cursor.execute("INSERT INTO UserAccounts (username, password, ViewPatientData, EditPatientData, ViewConsultations, EditConsultations, CommunicatePatients, ViewStatistics, ViewAppointments, CancelAppointments, CreateUsers, EditUsers, title, firstname, surname, email, mobile) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (usernameNew1, passwordNew1, canViewPatientData1, canEditPatientData1, canViewConsultations1, canEditConsultations1, canCommunicatePatients1, canViewStatistics1, canViewAppointments1, canCancelAppointments1, canCreateUsers1, canEditUsers1, titleNew1, firstnameNew1, surnameNew1, emailNew1, mobileNew1))
        conn.commit()

        print("Data Appended.")

        ms.showinfo("Information", "User Created Succesfully!")

        return

    labelInstructions = Label(tempWindow, 
                             text="Antrim Castle Surgery - Administration Portal (Create a User)",
                             font=("corbel bold", 10),
                             anchor=N)                 
    labelInstructions.grid(row=0, column=1, columnspan=8) 

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=1, column=0, columnspan=8)

    labelUsername = Label(tempWindow, 
                          text="Username: ", 
                          font=("corbel", 10))                 
    labelUsername.grid(row=2, column=0)                   
    entryUsername = Entry(tempWindow, textvar=usernameNew) 
    entryUsername.grid(row=2, column=1, columnspan=2)            
    
    labelPassword = Label(tempWindow, 
                          text="Password: ", 
                          font=("corbel", 10))                 
    labelPassword.grid(row=3, column=0)                   
    entryPassword = Entry(tempWindow, textvar=passwordNew) 
    entryPassword.grid(row=3, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=4, column=0, columnspan=3)
    
    labelFirstName = Label(tempWindow, 
                          text="Forename: ", 
                          font=("corbel", 10))                 
    labelFirstName.grid(row=5, column=0)                   
    entryFirstName = Entry(tempWindow, textvar=firstnameNew) 
    entryFirstName.grid(row=5, column=1, columnspan=2)            
    
    labelSurname = Label(tempWindow, 
                          text="Surname: ", 
                          font=("corbel", 10))                 
    labelSurname.grid(row=6, column=0)                   
    entrySurname = Entry(tempWindow, textvar=surnameNew) 
    entrySurname.grid(row=6, column=1, columnspan=2)

    labelTitle = Label(tempWindow, 
                          text="Title: ", 
                          font=("corbel", 10))                 
    labelTitle.grid(row=7, column=0)                   
    entryTitle = Entry(tempWindow, textvar=titleNew) 
    entryTitle.grid(row=7, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=0, column=4, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=8, column=0, columnspan=8)

    labelEmail = Label(tempWindow,
                       text="E-mail: ",
                       font=("corbel", 10))
    labelEmail.grid(row=9, column=0)
    entryEmail = Entry(tempWindow, textvar=emailNew)
    entryEmail.grid(row=9, column=1, columnspan=2)

    labelEmail = Label(tempWindow,
                       text="Mobile: ",
                       font=("corbel", 10))
    labelEmail.grid(row=10, column=0)
    entryEmail = Entry(tempWindow, textvar=mobileNew)
    entryEmail.grid(row=10, column=1, columnspan=2)

    labelPermissions = Label(tempWindow,    
                             text="User Permissions: ",  
                             font=("corbel", 10))
    labelPermissions.grid(row=2, column=5, columnspan=2)                                                    
    Checkbutton(tempWindow, 
                text="View Patient Data", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canViewPatientData,
                onvalue='Yes', offvalue='No').grid(row=2, column=7, sticky='W',)  
    Checkbutton(tempWindow, 
                text="Edit Patient Data", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canEditPatientData,
                onvalue='Yes', offvalue='No').grid(row=3, column=7, sticky='W',)
    Checkbutton(tempWindow, 
                text="View Patient Consultation Notes", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canViewConsultations,
                onvalue='Yes', offvalue='No').grid(row=4, column=7, sticky='W',)
    Checkbutton(tempWindow, 
                text="Edit Patient Consultation Notes", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canEditConsultations,
                onvalue='Yes', offvalue='No').grid(row=5, column=7, sticky='W',)
    Checkbutton(tempWindow, 
                text="Communicate with Patients", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canCommunicatePatients,
                onvalue='Yes', offvalue='No').grid(row=6, column=7, sticky='W',)
    Checkbutton(tempWindow, 
                text="View Patient Statistics", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canViewStatistics,
                onvalue='Yes', offvalue='No').grid(row=2, column=8, sticky='W',)
    Checkbutton(tempWindow, 
                text="View Patient Appointments", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canViewAppointments,
                onvalue='Yes', offvalue='No').grid(row=3, column=8, sticky='W',)
    Checkbutton(tempWindow, 
                text="Cancel Patient Appointments", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canCancelAppointments,
                onvalue='Yes', offvalue='No').grid(row=4, column=8, sticky='W',)
    Checkbutton(tempWindow, 
                text="Create New User Accounts", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canCreateUsers,
                onvalue='Yes', offvalue='No').grid(row=5, column=8, sticky='W',)
    Checkbutton(tempWindow, 
                text="Edit User Accounts", 
                cursor='hand2',
                font=("corbel", 10),
                variable=canEditUsers,
                onvalue='Yes', offvalue='No').grid(row=6, column=8, sticky='W',)

    Button(tempWindow, text='Create User', width=20, bg='darkblue', fg='white', command=appendUser).grid(row=12, column=5, columnspan=3)
    Button(tempWindow, text='Exit', width=20, bg='darkblue', fg='white', command=tempWindow.destroy).grid(row=12, column=8, columnspan=2)

    tempWindow.mainloop()

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