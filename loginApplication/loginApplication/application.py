######################################
## WJEC GCE Computer Science Unit 5 ##
## Daniel Chestnutt - 71401 - 2127  ##
## application.py - Main Window(s)  ##
######################################

###########################
## Prototype Version 1.0 ##
###########################

# ***** Importing Modules ***** #

from tkinter import *
from tkinter import messagebox as ms
from tkinter import Menu
from tkinter import ttk
import sqlite3
import os

# ***** Initial Declaration of Variables ***** #

global userDetails
userDetails = []

# ***** Functions and Procedures ***** #

# Note: these need to be declared before we create any of our windows as they
#       will need to be called by these windows. Therefore, we begin by creating
#       all variables/functions which will be used before we even create the
#       window/form in which they will be utilised by the program.

# The principle behind by system is that each form will be drawn in its own pop-up 
# window (excluding some basic informational displays which will be found on the
# main program window. Therefore, each of the below functions will draw their own
# window which is called 'tempWindow'; once the user is finished with this form
# they will either exit or commit the entered details. Upon this, the window will 
# close and the user will be returned to the main application.

# Create a New User Account #
def createUser():
    tempWindow = Tk()
    tempWindow.geometry('700x300+300+100')
    tempWindow.title("Create a New User")

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
    userTypeNew = StringVar()

    def appendUser():
        conn = sqlite3.connect('Users.db')
        with conn:
            cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS UserAccounts (userID INTEGER PRIMARY KEY, username TEXT, password TEXT, title TEXT, firstname TEXT, surname TEXT, email TEXT, mobile TEXT, userType TEXT)")
        cursor.execute("INSERT INTO UserAccounts (userID, username, password, title, firstname, surname, email, mobile, userType) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (usernameNew.get(), passwordNew.get(), titleNew.get(), firstnameNew.get(), surnameNew.get(), emailNew.get(), mobileNew.get(), userTypeNew.get()))
        
        conn.commit()

        ms.showinfo("Information", "User Created Succesfully!", parent=tempWindow)

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
    comboboxTitle = ttk.Combobox(tempWindow, textvariable=titleNew)
    comboboxTitle.grid(row=7, column=1, columnspan=2)
    comboboxTitle.config(values = ('Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Prof'), width=17)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=0, column=4, rowspan=10)

    labelUserType = Label(tempWindow, 
                          text="User Type: ", 
                          font=("corbel", 10))                 
    labelUserType.grid(row=8, column=5)                   
    comboboxUserType = ttk.Combobox(tempWindow, textvariable=userTypeNew)
    comboboxUserType.grid(row=8, column=6, columnspan=2)
    comboboxUserType.config(values = ('Doctor', 'Practice Nurse', 'Treatment Nurse', 'Pharmacist', 
                                      'Councillor', 'Receptionist', 'Practice Manager', 'Administrator'), width=17)

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
    print("Edit User Function Called.")

# Change current User Account #
def changeUser():
    print("Change User Function Called.")

# Search Patient Records #
def searchPatient():
    print("Search Patient Records Function Called.")

# Edit Patient Records #
def editPatient():
    print("Edit Patient Records Function Called.")

# Create a new Patient Record #
def addPatient():
    tempWindow = Tk()
    tempWindow.geometry('700x450+300+100')
    tempWindow.title("Register a new Patient")

    patientTitle = StringVar()
    forename = StringVar()
    surname = StringVar()
    prevSurname = StringVar()
    dateOfBirth = StringVar()
    gender = StringVar()
    country = StringVar()
    housenumber = StringVar()
    street = StringVar()
    postcode = StringVar()
    county = StringVar()
    contactnumber = StringVar()
    regType = StringVar()
    oldGP = StringVar()
    oldGPAddress = StringVar()
    oldGPPostcode = StringVar()
    hcn = StringVar()
    personnelNum = StringVar()
    enDate = StringVar()
    diDate = StringVar()
    organYN = StringVar()
    kidney = StringVar()
    heart = StringVar()
    lungs = StringVar()
    liver = StringVar() 
    corneas = StringVar()
    pancreas = StringVar()

    def appendPatient():
        patientTitle1 = patientTitle.get()
        forename1 = forename.get()
        surname1 = surname.get()
        prevSurname1 = prevSurname.get()
        dateOfBirth1 = dateOfBirth.get()
        gender1 = gender.get()
        country1 = country.get()
        housenumber1 = housenumber.get()
        street1 = street.get()
        postcode1 = postcode.get()
        county1 = county.get()
        contactnumber1 = contactnumber.get()
        regType1 = regType.get()
        oldGP1 = oldGP.get()
        oldGPAddress1 = oldGPAddress.get()
        oldGPPostcode1 = oldGPPostcode.get()
        hcn1 = hcn.get()
        personnelNum1 = personnelNum.get()
        enDate1 = enDate.get()
        diDate1 = diDate.get()
        organYN1 = organYN.get()
        kidney1 = kidney.get()
        heart1 = heart.get()
        lungs1 = lungs.get()
        liver1 = liver.get() 
        corneas1 = corneas.get()
        pancreas1 = pancreas.get()

        conn = sqlite3.connect('Patients.db')
        
        with conn:
            cursor1 = conn.cursor()
            
            cursor1.execute("CREATE TABLE IF NOT EXISTS PatientDemo (patientID INTEGER PRIMARY KEY, patientTitle TEXT, forename TEXT, surname TEXT, prevSurname TEXT, dateOfBirth TEXT, gender TEXT, country TEXT, housenumber TEXT, street TEXT, postcode TEXT, county TEXT, contactnumber TEXT, regType TEXT, oldGP TEXT, oldGPAddress TEXT, oldGPPostcode TEXT, hcn TEXT)")
            cursor1.execute("INSERT INTO PatientDemo (patientID, patientTitle, forename, surname, prevSurname, dateOfBirth, gender, country, housenumber, street, postcode, county, contactnumber, regType, oldGP, oldGPAddress, oldGPPostcode, hcn) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (patientTitle.get(), forename.get(), surname.get(), prevSurname.get(), dateOfBirth.get(), gender.get(), country.get(), housenumber.get(), street.get(), postcode.get(), county.get(), contactnumber.get(), regType.get(), oldGP.get(), oldGPAddress.get(), oldGPPostcode.get(), hcn.get(),))

            cursor2 = conn.cursor()

            cursor2.execute("CREATE TABLE IF NOT EXISTS PatientAF (patientID INTEGER PRIMARY KEY, personnelNum TEXT, enDate TEXT, diDate TEXT)")
            cursor2.execute("INSERT INTO PatientAF (patientID, personnelNum, enDate, diDate) VALUES (NULL, ?, ?, ?)", (personnelNum.get(), enDate.get(), diDate.get(),))
            
            cursor3 = conn.cursor()

            cursor3.execute("CREATE TABLE IF NOT EXISTS PatientOD (patientID INTEGER PRIMARY KEY, organYN TEXT, kidney TEXT, heart TEXT, lungs TEXT, liver TEXT, corneas TEXT, pancreas TEXT)")
            cursor3.execute("INSERT INTO PatientOD (patientID, organYN, kidney, heart, lungs, liver, corneas, pancreas) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)", (organYN.get(), kidney.get(), heart.get(), lungs.get(), liver.get(), corneas.get(), pancreas.get(),))
            
            conn.commit()

        def clearWindow():
            comboboxTitle.current([0])
            entryForename.delete(0, END)
            entrySurname.delete(0, END)
            entryPrevSurname.delete(0, END)
            entryDOB.delete(0, END)
            comboboxCountry.current([0])
            entryHousenumber.delete(0, END)
            entryStreet.delete(0, END)
            entryPostcode.delete(0, END)
            entryCounty.delete(0, END)
            entryContactNo.delete(0, END)
            comboboxRegType.current([0])
            entryOldGP.delete(0, END)
            entryOldGPAddress.delete(0, END)
            entryOldGPPostcode.delete(0, END)
            entryHCN.delete(0, END)
            entryPersonnelNum.delete(0, END)
            entryEnDate.delete(0, END)
            entryDiDate.delete(0, END)

        again = ms.askyesno("Succesful!", "Would you like to register another patient?", parent=tempWindow)

        if again == True:
            clearWindow()
        else:
            tempWindow.destroy()

    labelTitle = Label(tempWindow, text="Antrim Castle Surgery - Registration Application", font=("corbel bold", 10), anchor=N)
    labelTitle.grid(row=0, column=1, columnspan=6)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=1, column=0, columnspan=4)

    labelPatientTitle = Label(tempWindow, text="Title: ", font=("corbel", 10))
    labelPatientTitle.grid(row=2, column=0)
    comboboxTitle = ttk.Combobox(tempWindow, textvariable=patientTitle)
    comboboxTitle.grid(row=2, column=1, columnspan=2)
    comboboxTitle.config(values = ('Please Select...', 'Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Rev', 'Prof', 'Sir', 'Other'), width=17)
    comboboxTitle.current([0])

    labelForename = Label(tempWindow, text="Forename(s): ", font=("corbel", 10))
    labelForename.grid(row=3, column=0)
    entryForename = Entry(tempWindow, textvar=forename)
    entryForename.grid(row=3, column=1, columnspan=2)

    labelSurname = Label(tempWindow, text="Surname: ", font=("corbel", 10))
    labelSurname.grid(row=4, column=0)
    entrySurname = Entry(tempWindow, textvar=surname)
    entrySurname.grid(row=4, column=1, columnspan=2)

    labelPrevSurname = Label(tempWindow, text="Previous Surname: ", font=("corbel", 10))
    labelPrevSurname.grid(row=5, column=0)
    entryPrevSurname = Entry(tempWindow, textvar=prevSurname)
    entryPrevSurname.grid(row=5, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=6, column=0, columnspan=4)

    labelDOB = Label(tempWindow, text="Date of Birth: ", font=("corbel", 10))
    labelDOB.grid(row=7, column=0)
    entryDOB = Entry(tempWindow, textvar=dateOfBirth)
    entryDOB.grid(row=7, column=1, columnspan=2)

    labelGender = Label(tempWindow, text="Gender: ", font=("corbel", 10))
    labelGender.grid(row=8, column=0)
    Radiobutton(tempWindow, 
                text="Male", 
                variable=gender,
                cursor='hand2',
                value=1).grid(row=8, column=1)
    Radiobutton(tempWindow,  
                text="Female", 
                variable=gender,
                cursor='hand2',
                value=2).grid(row=8, column=2)

    labelCountry = Label(tempWindow, text="Country of Birth: ", font=("corbel", 10))
    labelCountry.grid(row=9, column=0)
    comboboxCountry = ttk.Combobox(tempWindow, textvariable=country)
    comboboxCountry.grid(row=9, column=1, columnspan=2)
    comboboxCountry.config(values = ('Please Select...',  'Australia', 'Belgium', 'Canada', 'Denmark', 'Egypt', 'France', 'Germany', 'Hungary', 'Ireland', 'Jamaica', 'Kenya', 'Lithuania', 'Macedonia', 
                                   'Norway', 'Oman', 'Poland', 'Quatar', 'Russia', 'Spain', 'Tanzania', 'United Kingdom', 'Venuzuala', 'Yugoslavia', 'Zambia'), width=17)
    comboboxCountry.current([0])

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=10, column=0, columnspan=4)

    labelHousenumber = Label(tempWindow, text="House Number: ", font=("corbel", 10))
    labelHousenumber.grid(row=11, column=0)
    entryHousenumber = Entry(tempWindow, textvar=housenumber)
    entryHousenumber.grid(row=11, column=1, columnspan=2)

    labelStreet = Label(tempWindow, text="Street: ", font=("corbel", 10))
    labelStreet.grid(row=12, column=0)
    entryStreet = Entry(tempWindow, textvar=street)
    entryStreet.grid(row=12, column=1, columnspan=2)

    labelPostcode = Label(tempWindow, text="Postcode: ", font=("corbel", 10))
    labelPostcode.grid(row=13, column=0)
    entryPostcode = Entry(tempWindow, textvar=postcode)
    entryPostcode.grid(row=13, column=1, columnspan=2)

    labelCounty = Label(tempWindow, text="County: ", font=("corbel", 10))
    labelCounty.grid(row=14, column=0)
    entryCounty = Entry(tempWindow, textvar=county)
    entryCounty.grid(row=14, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=15, column=0, columnspan=4)

    labelContactNo = Label(tempWindow, text="Contact Number: ", font=("corbel", 10))
    labelContactNo.grid(row=16, column=0)
    entryContactNo = Entry(tempWindow, textvar=contactnumber)
    entryContactNo.grid(row=16, column=1, columnspan=2)

    #########################################
    ## BEGIN SECOND COLUMN OF ENTRY LABELS ##
    #########################################

    spacerLabel = Label(tempWindow, text=" ", width=4)
    spacerLabel.grid(row=0, column=3, rowspan=18)

    labelRegType = Label(tempWindow, text="Registration Type: ", font=("corbel", 10))
    labelRegType.grid(row=2, column=4)
    comboboxRegType = ttk.Combobox(tempWindow, textvariable=regType)
    comboboxRegType.grid(row=2, column=5, columnspan=2)
    comboboxRegType.config(values = ('Please Select...', 'First ever registration with a GP Surgery', 'Moving GP Surgery'), width=17)
    comboboxRegType.current([0])

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=3, column=4, columnspan=3)

    labelOldGP = Label(tempWindow, text="Old GP: ", font=("corbel", 10))
    labelOldGP.grid(row=4, column=4)
    entryOldGP = Entry(tempWindow, textvar=oldGP)
    entryOldGP.grid(row=4, column=5, columnspan=2)

    labelOldGPAddress = Label(tempWindow, text="Address: ", font=("corbel", 10))
    labelOldGPAddress.grid(row=5, column=4)
    entryOldGPAddress = Entry(tempWindow, textvar=oldGPAddress)
    entryOldGPAddress.grid(row=5, column=5, columnspan=2)

    labelOldGPPostcode = Label(tempWindow, text="Postcode: ", font=("corbel", 10))
    labelOldGPPostcode.grid(row=6, column=4)
    entryOldGPPostcode = Entry(tempWindow, textvar=oldGPPostcode)
    entryOldGPPostcode.grid(row=6, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=7, column=4, columnspan=3)

    labelHCN = Label(tempWindow, text="Health & Care Number: ", font=("corbel", 10))
    labelHCN.grid(row=8, column=4)
    entryHCN = Entry(tempWindow, textvar=hcn)
    entryHCN.grid(row=8, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=9, column=4, columnspan=3)

    labelGender = Label(tempWindow, text="Complete the below if the patient is returning from the Armed Forces!", font=("corbel", 10))
    labelGender.grid(row=10, column=4, columnspan=4)

    labelPersonnelNum = Label(tempWindow, text="Personnel Number: ", font=("corbel", 10))
    labelPersonnelNum.grid(row=11, column=4)
    entryPersonnelNum = Entry(tempWindow, textvar=personnelNum)
    entryPersonnelNum.grid(row=11, column=5, columnspan=2)

    labelEnDate = Label(tempWindow, text="Enlistment Date: ", font=("corbel", 10))
    labelEnDate.grid(row=12, column=4)
    entryEnDate = Entry(tempWindow, textvar=enDate)
    entryEnDate.grid(row=12, column=5, columnspan=2)

    labelDiDate = Label(tempWindow, text="Discharge Date: ", font=("corbel", 10))
    labelDiDate.grid(row=13, column=4)
    entryDiDate = Entry(tempWindow, textvar=diDate)
    entryDiDate.grid(row=13, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=14, column=4, columnspan=3)

    labelOrganYN = Label(tempWindow, text="Has the Patient Consented to Organ Donation?", font=("corbel", 10))
    labelOrganYN.grid(row=15, column=4, columnspan=2)
    Radiobutton(tempWindow, 
                text="Yes", 
                variable=organYN,
                cursor='hand2',
                value='Yes').grid(row=15, column=6)
    Radiobutton(tempWindow, 
                text="No", 
                variable=organYN,
                cursor='hand2',
                value='No').grid(row=15, column=7)

    labelOrganType = Label(tempWindow, text="Organs to be donated: ", font=("corbel", 10))
    labelOrganType.grid(row=16, column=4)
    Checkbutton(tempWindow,
                cursor='hand2',
                text="Kidneys", 
                variable=kidney,
                onvalue='Yes', offvalue='No').grid(row=16, column=5, sticky='W')
    Checkbutton(tempWindow,
                cursor='hand2',
                text="Heart", 
                variable=heart,
                onvalue='Yes', offvalue='No').grid(row=16, column=6, sticky='W')
    Checkbutton(tempWindow,
                cursor='hand2',
                text="Liver", 
                variable=liver,
                onvalue='Yes', offvalue='No').grid(row=16, column=7, sticky='W')
    Checkbutton(tempWindow,
                cursor='hand2',
                text="Corneas", 
                variable=corneas,
                onvalue='Yes', offvalue='No').grid(row=17, column=5, sticky='W')
    Checkbutton(tempWindow,
                cursor='hand2',
                text="Lungs", 
                variable=lungs,
                onvalue='Yes', offvalue='No').grid(row=17, column=6, sticky='W')
    Checkbutton(tempWindow,
                cursor='hand2',
                text="Pancreas", 
                variable=pancreas,
                onvalue='Yes', offvalue='No').grid(row=17, column=7, sticky='W')

    Button(tempWindow, text='Save Data to Record', bg='darkblue', fg='white', cursor='hand2', command=appendPatient).grid(row=18, column=1, columnspan=2)
    Button(tempWindow, text='Exit', bg='darkblue', fg='white', cursor='hand2', command=tempWindow.destroy).grid(row=18, column=3, columnspan=2)

    tempWindow.mainloop()

# Add a new Document #
def addDocument():
    print("Add New Document Function Called.")

# View a Document #
def viewDocument():
    print("View Document Function Called.")

# Create the main Program Window #
def mainWindow():
    window = Tk()
    window.geometry('1366x768+0+0')
    window.title("Antrim Castle Surgery - Medical Informations System") 
    window.config(bg="white")
    
    def logOff():
        window.destroy()
        os.system("application.py")

    menu = Menu(window)

    dropdownUsers = Menu(menu) 

    dropdownUsers.add_command(label='Create New User', command=createUser) 
    dropdownUsers.add_command(label='Edit Existing User', command=editUser) 
    dropdownUsers.add_command(label='Change User', command=changeUser)
    dropdownUsers.add_command(label='Log-Off', command=logOff)

    menu.add_cascade(label='User Accounts', menu=dropdownUsers)

    dropdownPatients = Menu(menu) 

    dropdownPatients.add_command(label='Search Patients', command=searchPatient) 
    dropdownPatients.add_command(label='Edit Patient Details', command=editPatient) 
    dropdownPatients.add_command(label='Add a new Patient', command=addPatient)

    menu.add_cascade(label='Patient Records', menu=dropdownPatients)

    dropdownDocuments = Menu(menu) 

    dropdownDocuments.add_command(label='Add New Document', command=addDocument) 
    dropdownDocuments.add_command(label='View Saved Documents', command=viewDocument) 

    menu.add_cascade(label='Documents', menu=dropdownDocuments)

    window.config(menu=menu)

    # ***** Initial Opening Window ***** #

    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    # START. - These labels format the window by 
    # dividing it into 8 columns of equal width.
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=0, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=1, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=2, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=3, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=4, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=5, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=6, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=7, rowspan=20)
    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=0, column=8, rowspan=20)
    # END.

    labelInstructions = Label(window, 
                              text="Options Menu",
                              font=("corbel", 14),
                              bg="white")                 
    labelInstructions.grid(row=3, column=0, columnspan=2)

    Button(window, text='Search Patient Records', width=20, bg='darkblue', fg='white', command=searchPatient).grid(row=5, column=0, columnspan=2)
    Button(window, text='Register New Patients', width=20, bg='darkblue', fg='white', command=addPatient).grid(row=6, column=0, columnspan=2)
    Button(window, text='Edit Patient Records', width=20, bg='darkblue', fg='white', command=editPatient).grid(row=7, column=0, columnspan=2)
    Button(window, text='Add New Documents', width=20, bg='darkblue', fg='white', command=addDocument).grid(row=8, column=0, columnspan=2)
    Button(window, text='View Saved Documents', width=20, bg='darkblue', fg='white', command=viewDocument).grid(row=9, column=0, columnspan=2)

    labelInstructions = Label(window, 
                              text="System Options",
                              font=("corbel", 14),
                              bg="white")                                  
    labelInstructions.grid(row=3, column=7, columnspan=2)

    Button(window, text='Create New Users', width=20, bg='darkblue', fg='white', command=createUser).grid(row=5, column=7, columnspan=2)
    Button(window, text='Edit User Accounts', width=20, bg='darkblue', fg='white', command=editUser).grid(row=6, column=7, columnspan=2)
    Button(window, text='Change Current User', width=20, bg='darkblue', fg='white', command=changeUser).grid(row=7, column=7, columnspan=2)
    Button(window, text='Log-Off', width=20, bg='darkblue', fg='white', command=logOff).grid(row=8, column=7, columnspan=2)

    title = userDetails[3]
    firstname = userDetails[4]
    surname = userDetails[5]
   
    welcomeText = "Welcome back " + title + " " + firstname + " " + surname + "!"

    #labelACS = Label(window, 
    #                 text="Antrim Castle Surgery",
    #                 font=("corbel bold", 18))
    #labelACS.grid(row=3, column=2, columnspan=5)

    photoLogo = PhotoImage(file="surgeryLogoSmall.png")
    logo = Label(image=photoLogo)
    logo.grid(row=2, rowspan=2, column=2, columnspan=5, sticky=N)

    spacerLabel = Label(window, text=" ", width=20, bg="white")
    spacerLabel.grid(row=5, column=0, columnspan=9)

    labelHello = Label(window, text=welcomeText,
                       font=("corbel", 14),
                       bg="white")
    labelHello.grid(row=6, column=3, columnspan=3)


    # ***** Running the Code ***** #

    window.mainloop()

# Check User Details for Validity #
def checkUser():
    conn = sqlite3.connect('Users.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserAccounts WHERE username = ? and password = ?", (username.get(), password.get()))

        result = cursor.fetchall()

        if result:
            tupleDetails = StringVar()

            cursorUser = conn.cursor()

            cursorUser.execute('SELECT * FROM UserAccounts WHERE username = ?', (username.get(),))
            tupleDetails = cursorUser.fetchall()

            for stringDetails in tupleDetails:
                for detail in stringDetails:
                    userDetails.append(detail)

            tempWindow.destroy()
            mainWindow() 
        else:
            ms.showerror('User Not Found', 'Username or Password not Found.')
            entryUsername.delete(0, END)
            entryPassword.delete(0, END)

ignoreThis = 1

# ***** Creating an Admin User Account ***** #


# Note: This code should be commented out. It is only needed to create the initial user
#       account which is used to log-in for the first time and therefore create 
#       subsequent user accounts and access levels etc. 

#conn = sqlite3.connect('Users.db')
#with conn:
#    cursor = conn.cursor()
#
#    cursor.execute("CREATE TABLE IF NOT EXISTS UserAccounts (userID INTEGER PRIMARY KEY, username TEXT, password TEXT, title TEXT, firstname TEXT, surname TEXT, email TEXT, mobile TEXT, userType TEXT)")
#    cursor.execute("INSERT INTO UserAccounts (userID, username, password, title, firstname, surname, email, mobile, userType) VALUES (NULL, 'admin', 'Password1', 'Mr', 'System', 'Administrator', 'systemadmin@acs.com', '02894413910', 'Administrator')")
#    
#    conn.commit()

# ***** Drawing the Login Window ***** #

# This window will be used to initialise our program by asking the user for their
# login details and checking this against the details which are stored in our
# "Users" database. This allows for us to ensure confidentiality & security.

tempWindow = Tk()
tempWindow.geometry('160x180+580+250')
tempWindow.title("Antrim Castle Surgery - Medical Informations System")

username = StringVar()
password = StringVar()

spacerLabel = Label(tempWindow, text=" ")
spacerLabel.pack()

labelUsername = Label(tempWindow, 
                        text="Username: ", 
                        font=("corbel", 10),
                        padx=5)                                   
labelUsername.pack()
entryUsername = Entry(tempWindow, textvar=username)            
entryUsername.pack()

labelPassword = Label(tempWindow, 
                        text="Password: ", 
                        font=("corbel", 10),
                        padx=5)                                  
labelPassword.pack()
entryPassword = Entry(tempWindow, textvar=password, show = '•') 
entryPassword.pack()

spacerLabel = Label(tempWindow, text=" ")
spacerLabel.pack()

logedIn = Button(tempWindow, text='Log-In', bg='darkblue', fg='white', command=checkUser).pack()

tempWindow.mainloop()