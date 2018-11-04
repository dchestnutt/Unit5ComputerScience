####################################
## Unit 5 Computer Science 2018/9 ##
## Daniel Chestnutt [71401, 2127] ##
## Registration Application Form  ##
####################################

# Import GUI and Database
from tkinter import *
import sqlite3

# Create window, define dimensions, declare title (of the window itself)
win = Tk()
win.geometry('1200x600')
win.title("Registration Form")

# Definition of all variables (used to return the entered values) used later in the form
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
organType = StringVar()

## Database Function ##
# This function will be used to create the database (if it doesn't already exist) or append to the database if it does.
def database():
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
    organType1 = organType.get()

    conn = sqlite3.connect('Patient.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS PatientDemo (patientTitle TEXT, forename TEXT, surname TEXT, prevSurname TEXT, dateOfBirth TEXT, gender TEXT,
                                                             country TEXT, housenumber TEXT, street TEXT, postcode TEXT, county TEXT, contactnumber TEXT,
                                                             regType TEXT, oldGP TEXT, oldGPAddress TEXT, oldGPPostcode TEXT, hcn TEXT, personnelNum TEXT,
                                                             enDate TEXT, diDate TEXT, organYN TEXT, organType TEXT)""")
    cursor.execute("""INSERT INTO Patient (patientTitle, forename, surname, prevSurname, dateOfBirth, gender, country, housenumber, street, postcode, county,
                                            contactnumber, regType, oldGP, oldGPAddress, oldGPPostcode, hcn, personnelNum, enDate, diDate, organYN, organType)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (patientTitle1, forename1, surname1, prevSurname1, dateOfBirth1, gender1, country1, housenumber1, street1, postcode1, county1, contactnumber1, regType1, oldGP1, oldGPAddress1, oldGPPostcode1, hcn1, personnelNum1, enDate1, diDate1, organYN1, organType1))
    conn.commit()

# This label will act as the title at the top of our window.
labelTitle = Label(win, text="Antrim Castle Surgery - Registration Form", width=50, font=("bold", 20))
labelTitle.place(x=300, y=10)

labelPatientTitle = Label(win, text="Title", width=20, font=("bold", 10))
labelPatientTitle.place(x=-15, y=70)
titleList = ['Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Rev', 'Prof', 'Sir', 'Other'];
droplist = OptionMenu(win, patientTitle, *titleList)
droplist.config(width=20)
patientTitle.set('Select your Title')
droplist.place(x=130, y=65)

labelForename = Label(win, text="Forename(s)", width=20, font=("bold", 10))
labelForename.place(x=-15, y=100)
entryForename = Entry(win, textvar=forename)
entryForename.place(x=130, y=100)

labelSurname = Label(win, text="Surname", width=20, font=("bold", 10))
labelSurname.place(x=-15, y=130)
entrySurname = Entry(win, textvar=surname)
entrySurname.place(x=130, y=130)

labelPrevSurname = Label(win, text="Previous Surname", width=20, font=("bold", 10))
labelPrevSurname.place(x=-15, y=160)
entryPrevSurname = Entry(win, textvar=prevSurname)
entryPrevSurname.place(x=130, y=160)

labelDOB = Label(win, text="Date of Birth", width=20, font=("bold", 10))
labelDOB.place(x=-15, y=190)
entryDOB = Entry(win, textvar=dateOfBirth)
entryDOB.place(x=130, y=190)

labelGender = Label(win, text="Gender", width=20, font=("bold", 10))
labelGender.place(x=-15, y=220)
Radiobutton(win, text="Male", padx = 5, variable=gender, value='Male').place(x=125, y=220)
Radiobutton(win, text="Female", padx = 5, variable=gender, value='Female').place(x=180, y=220)

labelCountry = Label(win, text="Country of Birth", width=20, font=("bold", 10))
labelCountry.place(x=-15, y=250)
countryList = ['Australia', 'Belgium', 'Canada', 'Denmark', 'Egypt', 'France', 'Germany', 'Hungary', 'Ireland', 'Jamaica', 'Kenya', 'Lithuania', 'Macedonia', 'Norway', 'Oman', 'Poland', 'Quatar', 'Russia', 'Spain', 'Tanzania', 'United Kingdom', 'Venuzuala', 'Yugoslavia', 'Zambia'];
droplist = OptionMenu(win, country, *countryList)
droplist.config(width=20)
country.set('Select your Country')
droplist.place(x=130, y=245)

labelHousenumber = Label(win, text="House Number", width=20, font=("bold", 10))
labelHousenumber.place(x=-15, y=310)
entryHousenumber = Entry(win, textvar=housenumber)
entryHousenumber.place(x=130, y=310)

labelStreet = Label(win, text="Street", width=20, font=("bold", 10))
labelStreet.place(x=-15, y=340)
entryStreet = Entry(win, textvar=street)
entryStreet.place(x=130, y=340)

labelPostcode = Label(win, text="Postcode", width=20, font=("bold", 10))
labelPostcode.place(x=-15, y=370)
entryPostcode = Entry(win, textvar=postcode)
entryPostcode.place(x=130, y=370)

labelCounty = Label(win, text="County", width=20, font=("bold", 10))
labelCounty.place(x=-15, y=400)
entryCounty = Entry(win, textvar=county)
entryCounty.place(x=130, y=400)

labelContactNo = Label(win, text="Contact Number", width=20, font=("bold", 10))
labelContactNo.place(x=-15, y=430)
entryContactNo = Entry(win, textvar=contactnumber)
entryContactNo.place(x=130, y=430)

#########################################
## BEGIN SECOND COLUMN OF ENTRY LABELS ##
#########################################

labelRegType = Label(win, text="Registration Type", width=20, font=("bold", 10))
labelRegType.place(x=300, y=70)
regTypeList = ['First ever registration with a GP Surgery', 'Moving GP Surgery'];
droplist = OptionMenu(win, regType, *regTypeList)
droplist.config(width=35)
regType.set('Please select...')
droplist.place(x=460, y=65)

labeloldGP = Label(win, text="Old GP", width=20, font=("bold", 10))
labeloldGP.place(x=300, y=100)
entryoldGP = Entry(win, textvar=oldGP)
entryoldGP.place(x=460, y=100)

labelOldGPAddress = Label(win, text="Address", width=20, font=("bold", 10))
labelOldGPAddress.place(x=300, y=130)
entryOldGPAddress = Entry(win, textvar=oldGPAddress)
entryOldGPAddress.place(x=460, y=130)

labelOldGPPostcode = Label(win, text="Postcode", width=20, font=("bold", 10))
labelOldGPPostcode.place(x=300, y=160)
entryOldGPPostcode = Entry(win, textvar=oldGPPostcode)
entryOldGPPostcode.place(x=460, y=160)

labelHCN = Label(win, text="Health & Care Number", width=20, font=("bold", 10))
labelHCN.place(x=300, y=190)
entryHCN = Entry(win, textvar=hcn)
entryHCN.place(x=460, y=190)

labelGender = Label(win, text="Complete the below if you are returning from the Armed Forces", width=50, font=("bold", 10))
labelGender.place(x=300, y=250)

labelPersonnelNum = Label(win, text="Personnel Number", width=20, font=("bold", 10))
labelPersonnelNum.place(x=300, y=280)
entryPersonnelNum = Entry(win, textvar=personnelNum)
entryPersonnelNum.place(x=460, y=280)

labelEnDate = Label(win, text="Enlistment Date", width=20, font=("bold", 10))
labelEnDate.place(x=300, y=310)
entryEnDate = Entry(win, textvar=enDate)
entryEnDate.place(x=460, y=310)

labelDiDate = Label(win, text="Discharge Date", width=20, font=("bold", 10))
labelDiDate.place(x=300, y=340)
entryDiDate = Entry(win, textvar=diDate)
entryDiDate.place(x=460, y=340)

labelOrganYN = Label(win, text="I want to donate my organs", width=20, font=("bold", 10))
labelOrganYN.place(x=300, y=370)
Radiobutton(win, text="Yes", padx = 5, variable=organYN, value='Yes').place(x=470, y=370)
Radiobutton(win, text="No", padx = 5, variable=organYN, value='No').place(x=520, y=370)

labelOrganType = Label(win, text="Organs", width=20, font=("bold", 10))
labelOrganType.place(x=300, y=400)
Checkbutton(win, text="Kidneys", variable='kidney').place(x=460,y=400)
Checkbutton(win, text="Heart", variable='heart').place(x=530,y=400)
Checkbutton(win, text="Liver", variable='liver').place(x=590,y=400)
Checkbutton(win, text="Corneas", variable='cornea').place(x=460,y=430)
Checkbutton(win, text="Lungs", variable='lung').place(x=530,y=430)
Checkbutton(win, text="Pancreas", variable='pancreas').place(x=590,y=430)

# This button will trigger the entered data to be saved to the database
# It does this by calling the databse function which we declared on line 42
Button(win, text='Save Data to Record', width=20, bg='brown', fg='white', command=database).place(x=180, y=500)

win.mainloop()