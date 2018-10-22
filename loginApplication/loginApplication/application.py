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

# Search Patient Records #
def searchPatient():
    print("Doing Nothing.")

# Edit Patient Records #
def editPatient():
    print("Doing Nothing.")

# Create a new Patient Record #
def addPatient():
    tempWindow = Tk()
    tempWindow.geometry('700x500+100+100')
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
            cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS PatientDemo (patientTitle TEXT, forename TEXT, surname TEXT, prevSurname TEXT, dateOfBirth TEXT, gender TEXT,
                                                                 country TEXT, housenumber TEXT, street TEXT, postcode TEXT, county TEXT, contactnumber TEXT,
                                                                 regType TEXT, oldGP TEXT, oldGPAddress TEXT, oldGPPostcode TEXT, hcn TEXT, personnelNum TEXT,
                                                                 enDate TEXT, diDate TEXT, organYN TEXT, kidney TEXT, heart TEXT, lungs TEXT, liver TEXT, 
                                                                 corneas TEXT, pancreas TEXT)""")
        cursor.execute("""INSERT INTO PatientDemo (patientTitle, forename, surname, prevSurname, dateOfBirth, gender, country, housenumber, street, postcode, county,
                                                   contactnumber, regType, oldGP, oldGPAddress, oldGPPostcode, hcn, personnelNum, enDate, diDate, organYN, kidney, 
                                                   heart, lungs, liver, corneas, pancreas)
                                                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                      (patientTitle1, forename1, surname1, prevSurname1, dateOfBirth1, gender1, country1, housenumber1, street1, postcode1, county1, contactnumber1, 
                       regType1, oldGP1, oldGPAddress1, oldGPPostcode1, hcn1, personnelNum1, enDate1, diDate1, organYN1, kidney1, heart1, lungs1, liver1, corneas1, pancreas1))
        conn.commit()

        ms.showinfo("Information", "Registration Succesful!", parent=tempWindow)

        return

    labelTitle = Label(tempWindow, text="Antrim Castle Surgery - Registration Application", font=("corbel bold", 10), anchor=N)
    labelTitle.grid(row=0, column=1, columnspan=6)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=1, column=0, columnspan=4)

    labelPatientTitle = Label(tempWindow, text="Title", font=("corbel", 10))
    labelPatientTitle.grid(row=2, column=0)
    titleList = ['Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Rev', 'Prof', 'Sir', 'Other'];
    droplist = OptionMenu(tempWindow, patientTitle, *titleList)
    droplist.config(width=14)
    patientTitle.set('Select your Title')
    droplist.grid(row=2, column=1, columnspan=2)

    labelForename = Label(tempWindow, text="Forename(s)", font=("corbel", 10))
    labelForename.grid(row=3, column=0)
    entryForename = Entry(tempWindow, textvar=forename)
    entryForename.grid(row=3, column=1, columnspan=2)

    labelSurname = Label(tempWindow, text="Surname", font=("corbel", 10))
    labelSurname.grid(row=4, column=0)
    entrySurname = Entry(tempWindow, textvar=surname)
    entrySurname.grid(row=4, column=1, columnspan=2)

    labelPrevSurname = Label(tempWindow, text="Previous Surname", font=("corbel", 10))
    labelPrevSurname.grid(row=5, column=0)
    entryPrevSurname = Entry(tempWindow, textvar=prevSurname)
    entryPrevSurname.grid(row=5, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=6, column=0, columnspan=4)

    labelDOB = Label(tempWindow, text="Date of Birth", font=("corbel", 10))
    labelDOB.grid(row=7, column=0)
    entryDOB = Entry(tempWindow, textvar=dateOfBirth)
    entryDOB.grid(row=7, column=1, columnspan=2)

    labelGender = Label(tempWindow, text="Gender", font=("corbel", 10))
    labelGender.grid(row=8, column=0)
    Radiobutton(tempWindow, 
                text="Male", 
                variable=gender, 
                value=1).grid(row=8, column=1)
    Radiobutton(tempWindow,  
                text="Female", 
                variable=gender, 
                value=2).grid(row=8, column=2)

    labelCountry = Label(tempWindow, text="Country of Birth", font=("corbel", 10))
    labelCountry.grid(row=9, column=0)
    countryList = ['Australia', 'Belgium', 'Canada', 'Denmark', 'Egypt', 'France', 'Germany', 'Hungary', 'Ireland', 'Jamaica', 'Kenya', 'Lithuania', 'Macedonia', 'Norway', 'Oman', 'Poland', 'Quatar', 'Russia', 'Spain', 'Tanzania', 'United Kingdom', 'Venuzuala', 'Yugoslavia', 'Zambia'];
    droplist = OptionMenu(tempWindow, country, *countryList)
    droplist.config(width=14)
    country.set('Select your Country')
    droplist.grid(row=9, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=10, column=0, columnspan=4)

    labelHousenumber = Label(tempWindow, text="House Number", font=("corbel", 10))
    labelHousenumber.grid(row=11, column=0)
    entryHousenumber = Entry(tempWindow, textvar=housenumber)
    entryHousenumber.grid(row=11, column=1, columnspan=2)

    labelStreet = Label(tempWindow, text="Street", font=("corbel", 10))
    labelStreet.grid(row=12, column=0)
    entryStreet = Entry(tempWindow, textvar=street)
    entryStreet.grid(row=12, column=1, columnspan=2)

    labelPostcode = Label(tempWindow, text="Postcode", font=("corbel", 10))
    labelPostcode.grid(row=13, column=0)
    entryPostcode = Entry(tempWindow, textvar=postcode)
    entryPostcode.grid(row=13, column=1, columnspan=2)

    labelCounty = Label(tempWindow, text="County", font=("corbel", 10))
    labelCounty.grid(row=14, column=0)
    entryCounty = Entry(tempWindow, textvar=county)
    entryCounty.grid(row=14, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=15, column=0, columnspan=4)

    labelContactNo = Label(tempWindow, text="Contact Number", font=("corbel", 10))
    labelContactNo.grid(row=16, column=0)
    entryContactNo = Entry(tempWindow, textvar=contactnumber)
    entryContactNo.grid(row=16, column=1, columnspan=2)

    #########################################
    ## BEGIN SECOND COLUMN OF ENTRY LABELS ##
    #########################################

    spacerLabel = Label(tempWindow, text=" ", width=4)
    spacerLabel.grid(row=0, column=3, rowspan=18)

    labelRegType = Label(tempWindow, text="Registration Type", font=("corbel", 10))
    labelRegType.grid(row=2, column=4)
    regTypeList = ['First ever registration with a GP Surgery', 'Moving GP Surgery'];
    droplist = OptionMenu(tempWindow, regType, *regTypeList)
    droplist.config(width=14)
    regType.set('Please select...')
    droplist.grid(row=2, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=3, column=4, columnspan=3)

    labeloldGP = Label(tempWindow, text="Old GP", font=("corbel", 10))
    labeloldGP.grid(row=4, column=4)
    entryoldGP = Entry(tempWindow, textvar=oldGP)
    entryoldGP.grid(row=4, column=5, columnspan=2)

    labelOldGPAddress = Label(tempWindow, text="Address", font=("corbel", 10))
    labelOldGPAddress.grid(row=5, column=4)
    entryOldGPAddress = Entry(tempWindow, textvar=oldGPAddress)
    entryOldGPAddress.grid(row=5, column=5, columnspan=2)

    labelOldGPPostcode = Label(tempWindow, text="Postcode", font=("corbel", 10))
    labelOldGPPostcode.grid(row=6, column=4)
    entryOldGPPostcode = Entry(tempWindow, textvar=oldGPPostcode)
    entryOldGPPostcode.grid(row=6, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=7, column=4, columnspan=3)

    labelHCN = Label(tempWindow, text="Health & Care Number", font=("corbel", 10))
    labelHCN.grid(row=8, column=4)
    entryHCN = Entry(tempWindow, textvar=hcn)
    entryHCN.grid(row=8, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=9, column=4, columnspan=3)

    labelGender = Label(tempWindow, text="Complete the below if the patient is returning from the Armed Forces", font=("corbel", 10))
    labelGender.grid(row=10, column=4, columnspan=4)

    labelPersonnelNum = Label(tempWindow, text="Personnel Number", font=("corbel", 10))
    labelPersonnelNum.grid(row=11, column=4)
    entryPersonnelNum = Entry(tempWindow, textvar=personnelNum)
    entryPersonnelNum.grid(row=11, column=5, columnspan=2)

    labelEnDate = Label(tempWindow, text="Enlistment Date", font=("corbel", 10))
    labelEnDate.grid(row=12, column=4)
    entryEnDate = Entry(tempWindow, textvar=enDate)
    entryEnDate.grid(row=12, column=5, columnspan=2)

    labelDiDate = Label(tempWindow, text="Discharge Date", font=("corbel", 10))
    labelDiDate.grid(row=13, column=4)
    entryDiDate = Entry(tempWindow, textvar=diDate)
    entryDiDate.grid(row=13, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, text=" ")
    spacerLabel.grid(row=14, column=4, columnspan=3)

    labelOrganYN = Label(tempWindow, text="Has the Patient Consented to Organ Donation", font=("corbel", 10))
    labelOrganYN.grid(row=15, column=4, columnspan=2)
    Radiobutton(tempWindow, 
                text="Yes", 
                variable=organYN, 
                value='Yes').grid(row=15, column=6)
    Radiobutton(tempWindow, 
                text="No", 
                variable=organYN, 
                value='No').grid(row=15, column=7)

    labelOrganType = Label(tempWindow, text="Organs", font=("corbel", 10))
    labelOrganType.grid(row=16, column=4)
    Checkbutton(tempWindow, 
                text="Kidneys", 
                variable=kidney,
                onvalue='Yes', offvalue='No').grid(row=16, column=5, sticky='W')
    Checkbutton(tempWindow, 
                text="Heart", 
                variable=heart,
                onvalue='Yes', offvalue='No').grid(row=16, column=6, sticky='W')
    Checkbutton(tempWindow, 
                text="Liver", 
                variable=liver,
                onvalue='Yes', offvalue='No').grid(row=16, column=7, sticky='W')
    Checkbutton(tempWindow, 
                text="Corneas", 
                variable=corneas,
                onvalue='Yes', offvalue='No').grid(row=17, column=5, sticky='W')
    Checkbutton(tempWindow, 
                text="Lungs", 
                variable=lungs,
                onvalue='Yes', offvalue='No').grid(row=17, column=6, sticky='W')
    Checkbutton(tempWindow, 
                text="Pancreas", 
                variable=pancreas,
                onvalue='Yes', offvalue='No').grid(row=17, column=7, sticky='W')

    Button(tempWindow, text='Save Data to Record', bg='darkblue', fg='white', command=appendPatient).grid(row=18, column=1, columnspan=2)
    Button(tempWindow, text='Exit', bg='darkblue', fg='white', command=tempWindow.destroy).grid(row=18, column=3, columnspan=2)

    tempWindow.mainloop()

# ***** The Menu Bar ***** #

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

window.config(menu=menu)

window.mainloop()