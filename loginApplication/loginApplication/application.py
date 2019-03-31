######################################
## WJEC GCE Computer Science Unit 5 ##
## Daniel Chestnutt - 71401 - 2127  ##
######################################


###################################
## Software Development Solution ##
###################################


# ***** Importing Modules ***** #

# Date-time modules
import datetime
from datetime import date

# API modules - (printer interfacing)
import win32api
import win32print
import tempfile

# tKinter modules - (graphics)
from tkinter import *
from tkinter import messagebox as ms
from tkinter import Menu
from tkinter import ttk

# SQLite modules - (databases)
import sqlite3

# Other modules
import os

# SMPTP Libraries - (email)
import smtplib

# Document modules (mail-merge & microsoft word interfacing)
from mailmerge import MailMerge


# ***** Initial Declaration of Global Variables ***** #

global userDetails
userDetails = []

currentPatientDetails = []


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

# Mail Merge Data into Documents #
# Status: FULL WORKING
def newDoc():
    searchTerm = StringVar()
    docType = StringVar()
    dobDay = StringVar()
    dobMonth = StringVar()
    dobYear = StringVar()
    firstname = StringVar()
    lastname = StringVar()

    tempWindow = Tk()
    tempWindow.geometry('460x140')
    tempWindow.title("Create a New Document")

    center(tempWindow)
    
    def searchUser():       
        def getValues():
            firstname = entryFirstname.get()
            lastname = entryLastname.get()
            dobDay = comboboxDOBDay.get()
            dobMonth = comboboxDOBMonth.get()
            dobYear = comboboxDOBYear.get()

            values = [firstname, lastname, dobDay, dobMonth, dobYear]

            return values

        values = getValues()
        
        firstname = values[0]
        lastname = values[1]
        dobDay = values[2]
        dobMonth = values[3]
        dobYear = values[4]
        
        dob = str(dobDay) + "/" + str(dobMonth) + "/" + str(dobYear)

        fullname = str(firstname) + " " + str(lastname)

        conn = sqlite3.connect('Patients.db')
        
        with conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM PatientDemo WHERE forename = ? and surname = ? and dateOfBirth = ?", (firstname, lastname, dob))

            result = cursor.fetchall()
            
            if result:
                tupleDetails2 = ""
                stringDetails2 = ""
                currentPatientDetails = []

                cursor.execute('SELECT * FROM PatientDemo WHERE forename = ? and surname =  ? and dateOfBirth = ?', (firstname, lastname, dob))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetails.append(detail)

                ms.showinfo('Succesful!', 'The record of ' + fullname + ' has been loaded.', parent=tempWindow)

                tempWindow.destroy()
                createDoc(currentPatientDetails)
            else:
                ms.showerror('Patient Not Found', 'No patients with these matching details have been found.')
                entryFirstname.delete(0, END)
                entryLastname.delete(0, END)
                comboboxDOBDay.current(0)
                comboboxDOBMonth.current(0)
                comboboxDOBYear.current(0)
       
    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=0, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=6, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=2, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=8, rowspan=9)

    labelFirstname = Label(tempWindow, 
                        text="Patient Firstname: ",
                        font=("corbel bold", 10))
    labelFirstname.grid(row=1, column=1)
    entryFirstname = Entry(tempWindow, 
                        textvar=firstname)
    entryFirstname.grid(row=1, column=3, columnspan=3, sticky=E+W)

    labelLastname = Label(tempWindow, 
                        text="Patient Lastname: ",
                        font=("corbel bold", 10))
    labelLastname.grid(row=2, column=1)
    entryLastname = Entry(tempWindow, 
                        textvar=lastname)
    entryLastname.grid(row=2, column=3, columnspan=3, sticky=E+W)

    labelDocType = Label(tempWindow, 
                              text="Patient Date of Birth: ", 
                              font=("corbel bold", 10))
    labelDocType.grid(row=3, column=1)
    
    comboboxDOBDay = ttk.Combobox(tempWindow, 
                                   textvariable=dobDay)
    comboboxDOBDay.grid(row=3, column=3, sticky=E+W)
    comboboxDOBDay.config(values = ('DD', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                                     '30', '31'), width=4)
    comboboxDOBDay.current([0])

    comboboxDOBMonth = ttk.Combobox(tempWindow, 
                                   textvariable=dobMonth)
    comboboxDOBMonth.grid(row=3, column=4, sticky=E+W)
    comboboxDOBMonth.config(values = ('MM', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12'), width=4)
    comboboxDOBMonth.current([0])

    comboboxDOBYear = ttk.Combobox(tempWindow, 
                                   textvariable=dobYear)
    comboboxDOBYear.grid(row=3, column=5, sticky=E+W)
    comboboxDOBYear.config(values = ('YYYY', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909',
                                     '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', 
                                     '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', 
                                     '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', 
                                     '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', 
                                     '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', 
                                     '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
                                     '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                                     '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', 
                                     '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                                     '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'), width=9)
    comboboxDOBYear.current([0])

    searchButton = Button(tempWindow, 
                          text='Search', 
                          bg='darkblue', 
                          fg='white', 
                          command=searchUser).grid(row=2, column=7)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=4, column=0, columnspan=5)

    def createDoc(currentPatientDetails):
        enteredCorrOrigin = ''
        
        tempWindow2 = Tk()
        tempWindow2.geometry('460x200')
        tempWindow2.title("Create a New Document")

        center(tempWindow2)

        spacerLabel = Label(tempWindow2, 
                        text=" ")
        spacerLabel.grid(row=0, column=0, columnspan=8)

        spacerLabel = Label(tempWindow2, 
                        text=" ")
        spacerLabel.grid(row=2, column=0, columnspan=8)

        spacerLabel = Label(tempWindow2, 
                        text=" ")
        spacerLabel.grid(row=8, column=0, columnspan=8)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=0, rowspan=9)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=2, rowspan=9)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=5, rowspan=9)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=7, rowspan=9)

        labelDocType = Label(tempWindow2, 
                              text="Document Type: ", 
                              font=("corbel", 10))
        labelDocType.grid(row=1, column=1)
        comboboxDocType = ttk.Combobox(tempWindow2, 
                                    textvariable=docType)
        comboboxDocType.grid(row=1, column=3, columnspan=2, sticky=E+W)
        comboboxDocType.config(values = ('Please Select...', 'Attend RE Tests', 'Attend RE Correspondence', 'Attend Annual Clinic', 'Repeat Tests'), width=17)
        comboboxDocType.current([0])

        def getCombobox(currentPatientDetails):
            def mergeTT1(currentPatientDetails):
                longDate = "DATE AS POSTMARK"

                userTitle = userDetails[3]
                userFirstname = userDetails[4]
                userFirstInitial = userFirstname[0]
                userSurname = userDetails[5]

                patientTitle = currentPatientDetails[1]
                patientFirstname = currentPatientDetails[2]
                patientSurname = currentPatientDetails[3]
                patientDOB = currentPatientDetails[5]
                patientCountry = currentPatientDetails[7]
                patientCounty = currentPatientDetails[11]
                patientHouseNum = currentPatientDetails[8]
                patientStreet = currentPatientDetails[9]
                patientPostcode = currentPatientDetails[10]

                patientFirstInitial = patientFirstname[0]

                with MailMerge(r'.\templates\attendReTests.docx') as document:

                    document.merge(Title=patientTitle,
                               First_Initial=patientFirstInitial,
                               Surname=patientSurname,
                               Housenumber=patientHouseNum,
                               Street_Name=patientStreet,
                               Postcode=patientPostcode,
                               County=patientCounty,
                               Country=patientCountry,
                               Long_Date=longDate,
                               Firstname=patientFirstname,
                               Staff_Title=userTitle,
                               Staff_First_Initial=userFirstInitial,
                               Staff_Surname=userSurname)

                    document.write(r'.\documentOutput\TEMPattendReTests.docx')
                    
                    currentPatientDetails = []

                    printQuery = ms.askyesno("Succesful!", "Would you like to print the document?", parent=tempWindow2)

                    if printQuery == True:
                        filename = (r'.\documentOutput\TEMPattendReTests.docx')
                        win32api.ShellExecute (
                          0,
                          "print",
                          filename,
                          '/d:"%s"' % win32print.GetDefaultPrinter (),
                          ".",
                          0
                        )
                    else:
                        tempWindow.destroy()
            
            def mergeTT2(corrOrigin, currentPatientDetails):
                longDate = "DATE AS POSTMARK"
                  
                userTitle = userDetails[3]
                userFirstname = userDetails[4]
                userFirstInitial = userFirstname[0]
                userSurname = userDetails[5]

                patientTitle = currentPatientDetails[1]
                patientFirstname = currentPatientDetails[2]
                patientSurname = currentPatientDetails[3]
                patientDOB = currentPatientDetails[5]
                patientCountry = currentPatientDetails[7]
                patientCounty = currentPatientDetails[11]
                patientHouseNum = currentPatientDetails[8]
                patientStreet = currentPatientDetails[9]
                patientPostcode = currentPatientDetails[10]

                patientFirstInitial = patientFirstname[0]

                with MailMerge(r'.\templates\attendReCorrespondence.docx') as document:

                    document.merge(Title=patientTitle,
                                   First_Initial=patientFirstInitial,
                                   Surname=patientSurname,
                                   Housenumber=patientHouseNum,
                                   Street_Name=patientStreet,
                                   Postcode=patientPostcode,
                                   County=patientCounty,
                                   Country=patientCountry,
                                   Long_Date=longDate,
                                   Firstname=patientFirstname,
                                   Staff_Title=userTitle,
                                   Staff_First_Initial=userFirstInitial,
                                   Staff_Surname=userSurname,
                                   Correspondence_Origin=corrOrigin)

                    document.write(r'.\documentOutput\TEMPattendReCorrespondence.docx')

                    currentPatientDetails = []

                    printQuery = ms.askyesno("Succesful!", "Would you like to print the document?", parent=tempWindow2)

                    if printQuery == True:
                        filename = (r'.\documentOutput\TEMPattendReCorrespondence.docx')
                        win32api.ShellExecute (
                          0,
                          "print",
                          filename,
                          '/d:"%s"' % win32print.GetDefaultPrinter (),
                          ".",
                          0
                        )
                    else:
                        tempWindow.destroy()

            def mergeTT3(clinicYear, clinicName, appDate, appTime, clinicianName, currentPatientDetails):
                longDate = "DATE AS POSTMARK"
                  
                userTitle = userDetails[3]
                userFirstname = userDetails[4]
                userFirstInitial = userFirstname[0]
                userSurname = userDetails[5]

                patientTitle = currentPatientDetails[1]
                patientFirstname = currentPatientDetails[2]
                patientSurname = currentPatientDetails[3]
                patientDOB = currentPatientDetails[5]
                patientCountry = currentPatientDetails[7]
                patientCounty = currentPatientDetails[11]
                patientHouseNum = currentPatientDetails[8]
                patientStreet = currentPatientDetails[9]
                patientPostcode = currentPatientDetails[10]

                patientFirstInitial = patientFirstname[0]

                with MailMerge(r'.\templates\attendAnnualClinic.docx') as document:

                    document.merge(Title=patientTitle,
                                   First_Initial=patientFirstInitial,
                                   Surname=patientSurname,
                                   Housenumber=patientHouseNum,
                                   Street_Name=patientStreet,
                                   Postcode=patientPostcode,
                                   County=patientCounty,
                                   Country=patientCountry,
                                   Long_Date=longDate,
                                   Firstname=patientFirstname,
                                   Staff_Title=userTitle,
                                   Staff_First_Initial=userFirstInitial,
                                   Staff_Surname=userSurname,
                                   Year=clinicYear,
                                   Clinic_Name=clinicName,
                                   Appointment_Date=appDate,
                                   Appointment_Time=appTime,
                                   Clinician_Full_Name=clinicianName)

                    document.write(r'.\documentOutput\TEMPattendAnnualClinic.docx')

                    currentPatientDetails = []

                    printQuery = ms.askyesno("Succesful!", "Would you like to print the document?", parent=tempWindow2)

                    if printQuery == True:
                        filename = (r'.\documentOutput\TEMPattendAnnualClinic.docx')
                        win32api.ShellExecute (
                          0,
                          "print",
                          filename,
                          '/d:"%s"' % win32print.GetDefaultPrinter (),
                          ".",
                          0
                        )
                    else:
                        tempWindow.destroy()

            def mergeTT4(testReq, currentPatientDetails):
                longDate = "DATE AS POSTMARK"
                  
                userTitle = userDetails[3]
                userFirstname = userDetails[4]
                userFirstInitial = userFirstname[0]
                userSurname = userDetails[5]

                patientTitle = currentPatientDetails[1]
                patientFirstname = currentPatientDetails[2]
                patientSurname = currentPatientDetails[3]
                patientDOB = currentPatientDetails[5]
                patientCountry = currentPatientDetails[7]
                patientCounty = currentPatientDetails[11]
                patientHouseNum = currentPatientDetails[8]
                patientStreet = currentPatientDetails[9]
                patientPostcode = currentPatientDetails[10]

                patientFirstInitial = patientFirstname[0]

                with MailMerge(r'.\templates\repeatTests.docx') as document:

                    document.merge(Title=patientTitle,
                                   First_Initial=patientFirstInitial,
                                   Surname=patientSurname,
                                   Housenumber=patientHouseNum,
                                   Street_Name=patientStreet,
                                   Postcode=patientPostcode,
                                   County=patientCounty,
                                   Country=patientCountry,
                                   Long_Date=longDate,
                                   Firstname=patientFirstname,
                                   Staff_Title=userTitle,
                                   Staff_First_Initial=userFirstInitial,
                                   Staff_Surname=userSurname,
                                   Tests_Required=testReq)

                    document.write(r'.\documentOutput\TEMPrepeatTests.docx')

                    currentPatientDetails = []

                    printQuery = ms.askyesno("Succesful!", "Would you like to print the document?", parent=tempWindow2)

                    if printQuery == True:
                        filename = (r'.\documentOutput\TEMPrepeatTests.docx')
                        win32api.ShellExecute (
                          0,
                          "print",
                          filename,
                          '/d:"%s"' % win32print.GetDefaultPrinter (),
                          ".",
                          0
                        )
                    else:
                        tempWindow.destroy()
            
            templateType = IntVar()
            result = comboboxDocType.current()

            if result == 1: #Attend RE Tests
                mergeTT1(currentPatientDetails)
                tempWindow2.destroy()

            elif result == 2: # Attend RE Correspondence
                corrOrigin = StringVar()
                
                def getCorrOrigin():
                    corrOrigin = entryCorrOrigin.get()
                    
                    mergeTT2(corrOrigin, currentPatientDetails)
                    tempWindow2.destroy()

                labelCorrOrigin = Label(tempWindow2, 
                                      text="Correspondence Origin: ",
                                      font=("corbel bold", 10))
                labelCorrOrigin.grid(row=5, column=1)
                entryCorrOrigin = Entry(tempWindow2, 
                                    textvar=corrOrigin)
                entryCorrOrigin.grid(row=5, column=3, columnspan=2, sticky=E+W)

                createButton = Button(tempWindow2, 
                                      text='Create',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getCorrOrigin).grid(row=5, column=6, sticky=E+W)
            
            elif result == 3: # Attend Annual Clinic
                data1 = StringVar()
                data2 = StringVar()
                data3 = StringVar()
                data4 = StringVar()
                data5 = StringVar()
                
                def getDataResults():
                    clinicYear = entryClinYear.get()
                    clinicName = entryClinName.get()
                    appDate = entryAppDate.get()
                    appTime = entryAppTime.get()
                    clinicianName = entryClinicianName.get()

                    mergeTT3(clinicYear, clinicName, appDate, appTime, clinicianName, currentPatientDetails)
                    tempWindow2.destroy()

                labelClinYear = Label(tempWindow2, 
                                      text="Clinic Year: ",
                                      font=("corbel bold", 10))
                labelClinYear.grid(row=3, column=1)
                entryClinYear = Entry(tempWindow2, 
                                    textvar=data1)
                entryClinYear.grid(row=3, column=3, columnspan=2, sticky=E+W)

                labelClinName = Label(tempWindow2, 
                                      text="Clinic Name: ",
                                      font=("corbel bold", 10))
                labelClinName.grid(row=4, column=1)
                entryClinName = Entry(tempWindow2, 
                                    textvar=data2)
                entryClinName.grid(row=4, column=3, columnspan=2, sticky=E+W)

                labelAppDate = Label(tempWindow2, 
                                      text="Appointment Date: ",
                                      font=("corbel bold", 10))
                labelAppDate.grid(row=5, column=1)
                entryAppDate = Entry(tempWindow2, 
                                    textvar=data3)
                entryAppDate.grid(row=5, column=3, columnspan=2, sticky=E+W)

                labelAppTime = Label(tempWindow2, 
                                      text="Appointment Time: ",
                                      font=("corbel bold", 10))
                labelAppTime.grid(row=6, column=1)
                entryAppTime = Entry(tempWindow2, 
                                    textvar=data4)
                entryAppTime.grid(row=6, column=3, columnspan=2, sticky=E+W)

                labelClinicianName = Label(tempWindow2, 
                                      text="Clinician Name: ",
                                      font=("corbel bold", 10))
                labelClinicianName.grid(row=7, column=1)
                entryClinicianName = Entry(tempWindow2, 
                                    textvar=data5)
                entryClinicianName.grid(row=7, column=3, columnspan=2, sticky=E+W)

                createButton = Button(tempWindow2, 
                                      text='Create',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getDataResults).grid(row=5, column=6, sticky=E+W)

            elif result == 4: # Repeat Tests
                
                testsReqData = StringVar()
                
                def getTestsReq():
                    testsReq = entryTestsReq.get()
                    
                    mergeTT4(testsReq, currentPatientDetails)
                    tempWindow2.destroy()

                labelTestsReq = Label(tempWindow2, 
                                      text="Tests Required: ",
                                      font=("corbel bold", 10))
                labelTestsReq.grid(row=5, column=1)
                entryTestsReq = Entry(tempWindow2, 
                                    textvar=testsReqData)
                entryTestsReq.grid(row=5, column=3, columnspan=2, sticky=E+W)

                createButton = Button(tempWindow2, 
                                      text='Create',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getTestsReq).grid(row=5, column=6, sticky=E+W)

            else:
                print("ERROR LINE 405")

        loadButton = Button(tempWindow2, 
                            text='Load',
                            bg='darkblue', 
                            fg='white', 
                            command= lambda: getCombobox(currentPatientDetails)).grid(row=1, column=6, sticky=E+W)

# Center the Window on the Monitor # 
# Status: FULLY WORKING
def center(toplevel):
    toplevel.update_idletasks()

    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2

    toplevel.geometry("+%d+%d" % (x, y)) 

# Enter new Patient Medical Data #
# Status: FULLY WORKING
def newMed():
    searchTerm = StringVar()
    docType = StringVar()
    dobDay = StringVar()
    dobMonth = StringVar()
    dobYear = StringVar()
    firstname = StringVar()
    lastname = StringVar()

    tempWindow = Tk()
    tempWindow.geometry('480x160')
    tempWindow.title("Add new Medical Data")

    center(tempWindow)
    
    def getData(currentPatientDetails):        
        tempWindow2 = Tk()
        tempWindow2.geometry('460x200')
        tempWindow2.title("Add new Medical Data")

        center(tempWindow2)

        spacerLabel = Label(tempWindow2, 
                        text=" ")
        spacerLabel.grid(row=0, column=0, columnspan=8)

        spacerLabel = Label(tempWindow2, 
                        text=" ")
        spacerLabel.grid(row=2, column=0, columnspan=8)

        spacerLabel = Label(tempWindow2, 
                        text=" ")
        spacerLabel.grid(row=8, column=0, columnspan=8)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=0, rowspan=9)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=2, rowspan=9)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=5, rowspan=9)

        spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
        spacerLabel.grid(row=0, column=7, rowspan=9)

        labelDocType = Label(tempWindow2, 
                              text="Data Type to be Entered: ", 
                              font=("corbel", 10))
        labelDocType.grid(row=1, column=1)
        comboboxDocType = ttk.Combobox(tempWindow2, 
                                    textvariable=docType)
        comboboxDocType.grid(row=1, column=3, columnspan=2, sticky=E+W)
        comboboxDocType.config(values = ('Please Select...', 'Height', 'Weight', 'Blood Pressure', 'Blood Glucose', 'Serum HCG', 'Urinalysis', 'Smoking Status'), width=17)
        comboboxDocType.current([0])

        def getCombobox(currentPatientDetails):
            def saveData(value, dataType, currentPatientDetails):
                    currentDT = datetime.datetime.now()

                    currentY = currentDT.year
                    currentM = currentDT.month
                    currentD = currentDT.day
                    currentH = currentDT.hour
                    currentMin = currentDT.minute

                    currentDate = str(currentD) + "/" + str(currentM) + "/" + str(currentY)
                    currentTime = str(currentH) + ":" + str(currentMin)

                    patientID = currentPatientDetails[0]
                    userID = userDetails[0]
                
                    with sqlite3.connect('Patients.db') as patientsDB:
                        cursorPatient = patientsDB.cursor()
       
                    insertData = '''INSERT INTO PatientMed (entryID, patientID, userID, time, date, dataType, value) 
                                    VALUES (NULL, ?, ?, ?, ?, ?, ?)'''
                    cursorPatient.execute(insertData,[(patientID), (userID), (currentTime), (currentDate), (dataType), (value)])

                    patientsDB.commit()

                    global lastPatientID
                    lastPatientID = patientID

                    ms.showinfo('Success!', 'Data Entry Saved.')
            
            templateType = IntVar()
            result = comboboxDocType.current()

            if result == 1: # Height
                heightVal = DoubleVar()
                
                def getHeightVal():
                    heightVal = entryHeightVal.get()
                    dataType = "Height"

                    saveData(heightVal, dataType, currentPatientDetails)
                    tempWindow2.destroy()

                labelHeightVal = Label(tempWindow2, 
                                      text="Height (m): ",
                                      font=("corbel bold", 10))
                labelHeightVal.grid(row=5, column=1)
                entryHeightVal = Entry(tempWindow2, 
                                    textvar=heightVal)
                entryHeightVal.grid(row=5, column=3, columnspan=2, sticky=E+W)

                createButton = Button(tempWindow2, 
                                      text='Save',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getHeightVal).grid(row=5, column=6, sticky=E+W)

            elif result == 2: # Weight
                weightVal = DoubleVar()
                
                def getWeightVal():
                    weightVal = entryWeightVal.get()
                    dataType = "Height"

                    saveData(weightVal, dataType, currentPatientDetails)
                    tempWindow2.destroy()

                labelWeightVal = Label(tempWindow2, 
                                      text="Weight (kg): ",
                                      font=("corbel bold", 10))
                labelWeightVal.grid(row=5, column=1)
                entryWeightVal = Entry(tempWindow2, 
                                    textvar=weightVal)
                entryWeightVal.grid(row=5, column=3, columnspan=2, sticky=E+W)

                createButton = Button(tempWindow2, 
                                      text='Save',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getWeightVal).grid(row=5, column=6, sticky=E+W)
            
            elif result == 3: # Blood Pressure
                bpVal = StringVar()
                diastolicVal = IntVar()
                systolicVal = IntVar()
                
                def getBPVal():
                    diastolicVal = entrydiaBPVal.get()
                    systolicVal = entrysysBPVal.get()
                    dataType = "Blood Pressure"

                    bpVal = systolicVal + "/" + diastolicVal

                    saveData(bpVal, dataType, currentPatientDetails)
                    tempWindow2.destroy()

                labelsysBPVal = Label(tempWindow2, 
                                      text="Systolic BP: ",
                                      font=("corbel bold", 10))
                labelsysBPVal.grid(row=4, column=1)
                entrysysBPVal = Entry(tempWindow2, 
                                    textvar=systolicVal)
                entrysysBPVal.grid(row=4, column=3, columnspan=2, sticky=E+W)

                labeldiaBPVal = Label(tempWindow2, 
                                      text="Diastolic BP: ",
                                      font=("corbel bold", 10))
                labeldiaBPVal.grid(row=6, column=1)
                entrydiaBPVal = Entry(tempWindow2, 
                                    textvar=diastolicVal)
                entrydiaBPVal.grid(row=6, column=3, columnspan=2, sticky=E+W)

                createButton = Button(tempWindow2, 
                                      text='Save',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getBPVal).grid(row=5, column=6, sticky=E+W)

            elif result == 4: # Blood Glucose
                bgVal = DoubleVar()
                
                def getBGVal():
                    bgVal = entryBGVal.get()
                    dataType = "Blood Glucose"

                    saveData(bgVal, dataType, currentPatientDetails)
                    tempWindow2.destroy()

                labelBGVal = Label(tempWindow2, 
                                      text="Blood Glucose: ",
                                      font=("corbel bold", 10))
                labelBGVal.grid(row=5, column=1)
                entryBGVal = Entry(tempWindow2, 
                                    textvar=bgVal)
                entryBGVal.grid(row=5, column=3, columnspan=2, sticky=E+W)

                createButton = Button(tempWindow2, 
                                      text='Save',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getBGVal).grid(row=5, column=6, sticky=E+W)

            elif result == 5: # Serum HCG
                hcgVal = StringVar()
                
                def getHCGVal():
                    hcgVal = comboboxHCGVal.current()
                    dataType = "Serum HCG"

                    if hcgVal == 1:
                        hcgVal = "Positive"
                    elif hcgVal == 2:
                        hcgVal = "Negative"

                    saveData(hcgVal, dataType, currentPatientDetails)
                    tempWindow2.destroy()

                labelHCGVal = Label(tempWindow2, 
                                      text="Result: ",
                                      font=("corbel bold", 10))
                labelHCGVal.grid(row=5, column=1)
                comboboxHCGVal = ttk.Combobox(tempWindow2, 
                                            textvariable=hcgVal)
                comboboxHCGVal.grid(row=5, column=3, columnspan=2, sticky=E+W)
                comboboxHCGVal.config(values = ('Please Select...', 'Positive', 'Negative'), width=17)
                comboboxHCGVal.current([0])

                createButton = Button(tempWindow2, 
                                      text='Save',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getHCGVal).grid(row=5, column=6, sticky=E+W)

            elif result == 6: # Urinalysis 
                data1 = StringVar()
                data2 = StringVar()
                data3 = StringVar()
                data4 = StringVar()
                data5 = StringVar()
                
                def getDataResults():
                    LEU = entryLEU.get()
                    BLD = entryBLD.get()
                    ERY = entryERY.get()
                    PRO = comboboxPRO.current()
                    KET = comboboxKET.current()
                    
                    dataType = "Urinalysis"

                    if PRO == 1:
                        PRO = "Positive"
                    elif PRO == 2:
                        PRO = "Negative"

                    if PRO == 1:
                        PRO = "Positive"
                    elif PRO == 2:
                        PRO = "Negative"

                    urinalysisVal = "LEU" + LEU +", BLD" + BLD + ", ERY" + ERY + ", PRO " + PRO + ", KET " + KET
                    
                    saveData(urinalysisValue, dataType, currentPatientDetails)
                    tempWindow2.destroy()

                labelLEU = Label(tempWindow2, 
                                      text="Leucocytes (LEU): ",
                                      font=("corbel bold", 10))
                labelLEU.grid(row=3, column=1)
                entryLEU = Entry(tempWindow2, 
                                    textvar=data1)
                entryLEU.grid(row=3, column=3, columnspan=2, sticky=E+W)

                labelBLD = Label(tempWindow2, 
                                      text="Blood (BLD): ",
                                      font=("corbel bold", 10))
                labelBLD.grid(row=4, column=1)
                entryBLD = Entry(tempWindow2, 
                                    textvar=data2)
                entryBLD.grid(row=4, column=3, columnspan=2, sticky=E+W)

                labelERY = Label(tempWindow2, 
                                      text="Erythrocyte (ERY): ",
                                      font=("corbel bold", 10))
                labelERY.grid(row=5, column=1)
                entryERY = Entry(tempWindow2, 
                                    textvar=data3)
                entryERY.grid(row=5, column=3, columnspan=2, sticky=E+W)

                labelPRO = Label(tempWindow2, 
                                      text="Proteins (PRO): ",
                                      font=("corbel bold", 10))
                labelPRO.grid(row=6, column=1)
                comboboxPRO = ttk.Combobox(tempWindow2, 
                                            textvariable=data4)
                comboboxPRO.grid(row=6, column=3, columnspan=2, sticky=E+W)
                comboboxPRO.config(values = ('Please Select...', 'Positive', 'Negative'), width=17)
                comboboxPRO.current([0])

                labelKET = Label(tempWindow2, 
                                      text="Ketones (KET): ",
                                      font=("corbel bold", 10))
                labelKET.grid(row=7, column=1)
                comboboxKET = ttk.Combobox(tempWindow2, 
                                            textvariable=data5)
                comboboxKET.grid(row=7, column=3, columnspan=2, sticky=E+W)
                comboboxKET.config(values = ('Please Select...', 'Positive', 'Negative'), width=17)
                comboboxKET.current([0])

                createButton = Button(tempWindow2, 
                                      text='Create',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getDataResults).grid(row=5, column=6, sticky=E+W)

            elif result == 7: # Smoking Status
                ssVal = StringVar()
                
                def getSSVal():
                    ssVal = comboboxSSVal.current()

                    dataType = "Smoking Status"

                    if ssVal == 1:
                        ssVal = "Never Smoked Tobacco"
                    elif ssVal == 2:
                        ssVal = "Ex-Smoker"
                    elif ssVal == 3:
                        ssVal = "Current Smoker (<10 a day)"
                    elif ssVal == 4:
                        ssVal = "Current Smoker (>10 a day)"

                    saveData(ssVal, dataType, currentPatientDetails)
                    tempWindow2.destroy()

                labelSSVal = Label(tempWindow2, 
                                      text="Smoking Status: ",
                                      font=("corbel bold", 10))
                labelSSVal.grid(row=5, column=1)
                comboboxSSVal = ttk.Combobox(tempWindow2, 
                                            textvariable=ssVal)
                comboboxSSVal.grid(row=5, column=3, columnspan=2, sticky=E+W)
                comboboxSSVal.config(values = ('Please Select...', 'Never Smoked Tobacco', 'Ex-Smoker', 'Current Smoker (<10 a day)', 'Current Smoker (>10 a day)'), width=17)
                comboboxSSVal.current([0])

                createButton = Button(tempWindow2, 
                                      text='Save',
                                      bg='darkblue', 
                                      fg='white', 
                                      command=getSSVal).grid(row=5, column=6, sticky=E+W)

            else:
                print("ERROR LINE 405")

        loadButton = Button(tempWindow2, 
                            text='Load',
                            bg='darkblue', 
                            fg='white', 
                            command= lambda: getCombobox(currentPatientDetails)).grid(row=1, column=6, sticky=E+W)

    def searchUser():       
        def getValues():
            firstname = entryFirstname.get()
            lastname = entryLastname.get()
            dobDay = comboboxDOBDay.get()
            dobMonth = comboboxDOBMonth.get()
            dobYear = comboboxDOBYear.get()

            values = [firstname, lastname, dobDay, dobMonth, dobYear]

            return values

        values = getValues()
        
        firstname = values[0]
        lastname = values[1]
        dobDay = values[2]
        dobMonth = values[3]
        dobYear = values[4]
        
        dob = str(dobDay) + "/" + str(dobMonth) + "/" + str(dobYear)

        fullname = str(firstname) + " " + str(lastname)

        conn = sqlite3.connect('Patients.db')
        
        with conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM PatientDemo WHERE forename = ? and surname = ? and dateOfBirth = ?", (firstname, lastname, dob))

            result = cursor.fetchall()
            
            if result:
                tupleDetails2 = ""
                stringDetails2 = ""
                currentPatientDetails = []

                cursor.execute('SELECT * FROM PatientDemo WHERE forename = ? and surname =  ? and dateOfBirth = ?', (firstname, lastname, dob))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetails.append(detail)

                ms.showinfo('Succesful!', 'The record of ' + fullname + ' has been loaded.', parent=tempWindow)

                tempWindow.destroy()
                getData(currentPatientDetails)
            else:
                ms.showerror('Patient Not Found', 'No patients with these matching details have been found.')
                entryFirstname.delete(0, END)
                entryLastname.delete(0, END)
                comboboxDOBDay.current(0)
                comboboxDOBMonth.current(0)
                comboboxDOBYear.current(0)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=0, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=6, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=2, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=8, rowspan=9)

    labelFirstname = Label(tempWindow, 
                        text="Patient Firstname: ",
                        font=("corbel bold", 10))
    labelFirstname.grid(row=1, column=1)
    entryFirstname = Entry(tempWindow, 
                        textvar=firstname)
    entryFirstname.grid(row=1, column=3, columnspan=3, sticky=E+W)

    labelLastname = Label(tempWindow, 
                        text="Patient Lastname: ",
                        font=("corbel bold", 10))
    labelLastname.grid(row=2, column=1)
    entryLastname = Entry(tempWindow, 
                        textvar=lastname)
    entryLastname.grid(row=2, column=3, columnspan=3, sticky=E+W)

    labelDocType = Label(tempWindow, 
                              text="Patient Date of Birth: ", 
                              font=("corbel bold", 10))
    labelDocType.grid(row=3, column=1)
    
    comboboxDOBDay = ttk.Combobox(tempWindow, 
                                   textvariable=dobDay)
    comboboxDOBDay.grid(row=3, column=3, sticky=E+W)
    comboboxDOBDay.config(values = ('DD', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                                     '30', '31'), width=4)
    comboboxDOBDay.current([0])

    comboboxDOBMonth = ttk.Combobox(tempWindow, 
                                   textvariable=dobMonth)
    comboboxDOBMonth.grid(row=3, column=4, sticky=E+W)
    comboboxDOBMonth.config(values = ('MM', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12'), width=4)
    comboboxDOBMonth.current([0])

    comboboxDOBYear = ttk.Combobox(tempWindow, 
                                   textvariable=dobYear)
    comboboxDOBYear.grid(row=3, column=5, sticky=E+W)
    comboboxDOBYear.config(values = ('YYYY', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909',
                                     '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', 
                                     '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', 
                                     '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', 
                                     '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', 
                                     '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', 
                                     '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
                                     '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                                     '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', 
                                     '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                                     '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'), width=9)
    comboboxDOBYear.current([0])

    searchButton = Button(tempWindow, 
                          text='Search', 
                          bg='#09425A', 
                          fg='#FFFFFF', 
                          command=searchUser).grid(row=2, column=7)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=4, column=0, columnspan=9)

    def lastUser():
        if lastPatientID:
            conn = sqlite3.connect('Patients.db')
                
            patientID = str(lastPatientID)

            with conn:
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM PatientDemo WHERE patientID = ?", (patientID))

                result = cursor.fetchall()
            
                if result:
                    tupleDetails2 = ""
                    stringDetails2 = ""
                    currentPatientDetails = []

                    cursor.execute('SELECT * FROM PatientDemo WHERE patientID = ?', (patientID))
            
                    tupleDetails2 = cursor.fetchall()

                    for stringDetails2 in tupleDetails2:
                        for detail in stringDetails2:
                            currentPatientDetails.append(detail)

                    ms.showinfo('Succesful!', 'The previous record has been loaded.', parent=tempWindow)

                    tempWindow.destroy()
                    getData(currentPatientDetails)
                else:
                    ms.showerror('Patient Not Found', 'No patients with these matching details have been found.')
                    entryFirstname.delete(0, END)
                    entryLastname.delete(0, END)
                    comboboxDOBDay.current(0)
                    comboboxDOBMonth.current(0)
                    comboboxDOBYear.current(0)
        else:
            ms.showerror('No Patient Selected', 'No patients have been previously selected.')

    searchButton = Button(tempWindow, 
                          text='Use Previous Patient Record', 
                          bg='#09425A', 
                          fg='#FFFFFF', 
                          command=lastUser).grid(row=5, column=3, columnspan=3)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=4, column=0, columnspan=5)

# Create a New User Account # 
# Status: FULLY WORKING
def createUser():  
    tempWindow = Tk()
    tempWindow.geometry('700x300')
    tempWindow.title("Create a New User")

    center(tempWindow)
    
    accountType = userDetails[8]
    
    print(userDetails)

    print(accountType)

    if accountType == "Doctor" or accountType == "Practice Nurse" or accountType == "Pharmacist" or accountType == "Councillor" or accountType == "Receptionist":
        ms.showerror("Access Denied", 
                     "You do not have access to this feature. If this is in error please contact the systems administrator.", 
                     parent=tempWindow)
        tempWindow.destroy()

    elif accountType == "Administrator" or accountType == "Practice Manager":
        usernameNew = StringVar()
        passwordNew = StringVar()
        titleNew = StringVar()
        firstnameNew = StringVar()
        surnameNew = StringVar()
        emailNew = StringVar()
        mobileNew = StringVar()
        userTypeNew = StringVar()
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

        def clearWindow():
            entryUsername.delete(0, END)
            entryPassword.delete(0, END)
            entryFirstname.delete(0, END)
            entrySurname.delete(0, END)
            comboboxTitle.current([0])
            comboboxUserType.current([0])
            entryEmail.delete(0, END)
            entryMobile.delete(0, END)

        def appendUser(username, password, title, firstname, surname, email, mobile, userType):
            with sqlite3.connect('Users.db') as usersDB:
                cursorUser = usersDB.cursor()
       
            insertUser = '''INSERT INTO UserAccounts (userID, username, password, title, firstname, surname, email, mobile, userType) 
                            VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)'''
            cursorUser.execute(insertUser,[(username), (password), (title), (firstname), (surname), (email), (mobile), (userType)])

            usersDB.commit()

            again = ms.askyesno("Succesful!", 
                                "Would you like to create another user?", 
                                parent=tempWindow)

            if again == True:
                clearWindow()
            else:
                tempWindow.destroy()

        def getValues():
            username = entryUsername.get()
            password = entryPassword.get()
            title = comboboxTitle.get()
            firstname = entryFirstName.get()
            surname = entrySurname.get()
            email = entryEmail.get()
            mobile = entryMobile.get()
            userType = comboboxUserType.get()

            appendUser(username, password, title, firstname, surname, email, mobile, userType)

        labelInstructions = Label(tempWindow, 
                                 text="Antrim Castle Surgery - Administration Portal (Create a User)",
                                 font=("corbel bold", 14),
                                 anchor=N)                 
        labelInstructions.grid(row=0, column=1, columnspan=8) 

        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=20)
        spacerLabel.grid(row=1, column=0, columnspan=8)

        labelUsername = Label(tempWindow, 
                              text="Username: ", 
                              font=("corbel", 10))                 
        labelUsername.grid(row=2, column=0)                   
        entryUsername = Entry(tempWindow, 
                              textvariable=usernameNew) 
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
        entryFirstName = Entry(tempWindow, 
                               textvar=firstnameNew) 
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
        comboboxTitle = ttk.Combobox(tempWindow, 
                                     textvariable=titleNew)
        comboboxTitle.grid(row=7, column=1, columnspan=2)
        comboboxTitle.config(values = ('Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Prof'), width=17)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=0, column=4, rowspan=10)

        labelUserType = Label(tempWindow, 
                              text="User Type: ", 
                              font=("corbel", 10))                 
        labelUserType.grid(row=8, column=5)                   
        comboboxUserType = ttk.Combobox(tempWindow, 
                                        textvariable=userTypeNew)
        comboboxUserType.grid(row=8, column=6, columnspan=2)
        comboboxUserType.config(values = ('Doctor', 'Practice Nurse', 'Treatment Nurse', 'Pharmacist', 
                                          'Councillor', 'Receptionist', 'Practice Manager', 'Administrator'), width=17)

        labelEmail = Label(tempWindow,
                           text="E-mail: ",
                           font=("corbel", 10))
        labelEmail.grid(row=9, column=0)
        entryEmail = Entry(tempWindow, 
                           textvar=emailNew)
        entryEmail.grid(row=9, column=1, columnspan=2)

        labelMobile = Label(tempWindow,
                           text="Mobile: ",
                           font=("corbel", 10))
        labelMobile.grid(row=10, column=0)
        entryMobile = Entry(tempWindow, 
                            textvar=mobileNew)
        entryMobile.grid(row=10, column=1, columnspan=2)

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
                    onvalue='Yes', 
                    offvalue='No').grid(row=3, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="View Patient Consultation Notes", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canViewConsultations,
                    onvalue='Yes', 
                    offvalue='No').grid(row=4, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Edit Patient Consultation Notes", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canEditConsultations,
                    onvalue='Yes', 
                    offvalue='No').grid(row=5, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Communicate with Patients", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canCommunicatePatients,
                    onvalue='Yes', 
                    offvalue='No').grid(row=6, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="View Patient Statistics", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canViewStatistics,
                    onvalue='Yes', 
                    offvalue='No').grid(row=2, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="View Patient Appointments", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canViewAppointments,
                    onvalue='Yes', 
                    offvalue='No').grid(row=3, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Cancel Patient Appointments", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canCancelAppointments,
                    onvalue='Yes', 
                    offvalue='No').grid(row=4, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Create New User Accounts", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canCreateUsers,
                    onvalue='Yes', 
                    offvalue='No').grid(row=5, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Edit User Accounts", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canEditUsers,
                    onvalue='Yes', 
                    offvalue='No').grid(row=6, column=8, sticky='W',)

        Button(tempWindow, 
               text='Create User', 
               width=20, 
               bg='darkblue', 
               fg='white', 
               command=getValues).grid(row=12, column=5, columnspan=3)
        Button(tempWindow, 
               text='Exit', 
               width=20, 
               bg='darkblue', 
               fg='white', 
               command=tempWindow.destroy).grid(row=12, column=8, columnspan=2)

        tempWindow.mainloop()

    else:
        ms.showerror("Permissions Error", 
                     "ERROR CODE 001 - Please report this error to your systems administrator.", 
                     parent=tempWindow)
        tempWindow.destroy()

# Edit an Existing User Account # 
# Status: FULLY WORKING
def editUser():
    searchTerm = StringVar()
    docType = StringVar()
    dobDay = StringVar()
    dobMonth = StringVar()
    dobYear = StringVar()
    firstname = StringVar()
    lastname = StringVar()

    tempWindow = Tk()
    tempWindow.geometry('460x100')
    tempWindow.title("Add new Medical Data")

    center(tempWindow)

    def getAccount():
        def getValues():
            userSearch = entryEditUsername.get()
            adminPassword = entryAdminPassword.get()
            
            values = [userSearch, adminPassword]

            return values

        values = getValues()
        
        userSearch = values[0]
        adminPassword = values[1]
        
        conn = sqlite3.connect('Users.db')
        
        with conn:
            cursor = conn.cursor()

            adminCorrect = ""
            adminString = ""
            userID = "1"

            cursor.execute('SELECT password FROM UserAccounts WHERE userID = ?', (userID))

            adminCorrect = cursor.fetchall()

            for adminString in adminCorrect:
                for detail in adminString:
                    adminCorrect = detail

            getUser = "SELECT * FROM UserAccounts WHERE username = ?"
            cursor.execute(getUser,[(userSearch)])

            result = cursor.fetchall()
            
            if result:
                if adminPassword == adminCorrect:
                    tupleDetails2 = ""
                    stringDetails2 = ""
                    searchedUserDetails = []

                    getUser = "SELECT * FROM UserAccounts WHERE username = ?"
                    cursor.execute(getUser,[(userSearch)])
            
                    tupleDetails2 = cursor.fetchall()

                    for stringDetails2 in tupleDetails2:
                        for detail in stringDetails2:
                            searchedUserDetails.append(detail)

                    ms.showinfo('Succesful!', 'The user account of ' + userSearch + ' has been loaded.', parent=tempWindow)

                    tempWindow.destroy()
                    setWindow(searchedUserDetails)
                else:
                    ms.showerror('Error', 'The admin password entered is incorrect.')
                    entryEditUsername.delete(0, END)
                    entryAdminPassword.delete(0, END)
            else:
                ms.showerror('Error', 'No user accounts were found with that username. Please try again.')
                entryEditUsername.delete(0, END)
                entryAdminPassword.delete(0, END)
       
    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=0, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=6, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=2, rowspan=9)

    spacerLabel = Label(tempWindow, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=8, rowspan=9)

    labelEditUsername = Label(tempWindow, 
                        text="Username to Edit: ",
                        font=("corbel bold", 10))
    labelEditUsername.grid(row=1, column=1)
    entryEditUsername = Entry(tempWindow, 
                        textvar=firstname)
    entryEditUsername.grid(row=1, column=3, columnspan=3, sticky=E+W)

    labelAdminPassword = Label(tempWindow, 
                        text="Admin Password: ",
                        font=("corbel bold", 10))
    labelAdminPassword.grid(row=2, column=1)
    entryAdminPassword = Entry(tempWindow, 
                        textvar=lastname)
    entryAdminPassword.grid(row=2, column=3, columnspan=3, sticky=E+W)

    searchButton = Button(tempWindow, 
                          text='Load Account', 
                          bg='darkblue', 
                          fg='white', 
                          command=getAccount).grid(row=2, column=7)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=4, column=0, columnspan=5)

    def setWindow(searchedUserDetails):
        tempWindow = Tk()
        tempWindow.geometry('700x300')
        tempWindow.title("Edit an Existing User")
        
        center(tempWindow)
        
        usernameNew = StringVar()
        passwordNew = StringVar()
        titleNew = StringVar()
        firstnameNew = StringVar()
        surnameNew = StringVar()
        emailNew = StringVar()
        mobileNew = StringVar()
        userTypeNew = StringVar()
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

        def fillData(searchedUserDetails):
            entryUsername.delete(0, END)
            entryUsername.insert(0, searchedUserDetails[1])
        
            entryPassword.delete(0, END)
            entryPassword.insert(0, searchedUserDetails[2])

            currentTitle = searchedUserDetails[3]
            comboboxTitle.set(currentTitle)

            entryFirstName.delete(0, END)
            entryFirstName.insert(0, searchedUserDetails[4])

            entrySurname.delete(0, END)
            entrySurname.insert(0, searchedUserDetails[5])
        
            entryEmail.delete(0, END)
            entryEmail.insert(0, searchedUserDetails[6])
        
            entryMobile.delete(0, END)
            entryMobile.insert(0, searchedUserDetails[7])

            currentUserType = searchedUserDetails[8]
            comboboxUserType.set(currentUserType)
        
        def appendUser(username, password, title, firstname, surname, email, mobile, userType, userID):
            with sqlite3.connect('Users.db') as usersDB:
                cursorUser = usersDB.cursor()
       
                updateUser = "UPDATE UserAccounts SET username = ?, password = ?, title = ?, firstname = ?, surname = ?, email = ?, mobile = ?, userType = ? WHERE userID = ?"
                updateValues = (username), (password), (title), (firstname), (surname), (email), (mobile), (userType), (userID)

                cursorUser.execute(updateUser, updateValues)

                usersDB.commit()

                again = ms.askyesno("Succesful!", "Would you like to edit another account?", parent=tempWindow)

                if again == True:
                    tempWindow.destroy()
                    editUser()
                else:
                    tempWindow.destroy()

        def getValues(searchedUserDetails):
            username = entryUsername.get()
            password = entryPassword.get()
            title = comboboxTitle.get()
            firstname = entryFirstName.get()
            surname = entrySurname.get()
            email = entryEmail.get()
            mobile = entryMobile.get()
            userType = comboboxUserType.get()
            userID = searchedUserDetails[0]

            appendUser(username, password, title, firstname, surname, email, mobile, userType, userID)

        labelInstructions = Label(tempWindow, 
                             text="Antrim Castle Surgery - Administration Portal (Edit User Accounts)",
                             font=("corbel bold", 14),
                             anchor=N)                 
        labelInstructions.grid(row=0, column=1, columnspan=8) 

        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=20)
        spacerLabel.grid(row=1, column=0, columnspan=8)

        labelUsername = Label(tempWindow, 
                              text="Username: ", 
                              font=("corbel", 10))                 
        labelUsername.grid(row=2, column=0)                   
        entryUsername = Entry(tempWindow, 
                              textvariable=usernameNew) 
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
        entryFirstName = Entry(tempWindow, 
                               textvar=firstnameNew) 
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
        comboboxTitle = ttk.Combobox(tempWindow, 
                                     textvariable=titleNew)
        comboboxTitle.grid(row=7, column=1, columnspan=2)
        comboboxTitle.config(values = ('Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Prof'), width=17)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=0, column=4, rowspan=10)

        labelUserType = Label(tempWindow, 
                              text="User Type: ", 
                              font=("corbel", 10))                 
        labelUserType.grid(row=8, column=5)                   
        comboboxUserType = ttk.Combobox(tempWindow, 
                                        textvariable=userTypeNew)
        comboboxUserType.grid(row=8, column=6, columnspan=2)
        comboboxUserType.config(values = ('Doctor', 'Practice Nurse', 'Pharmacist', 
                                          'Councillor', 'Receptionist', 'Practice Manager', 'Administrator'), width=17)

        labelEmail = Label(tempWindow,
                           text="E-mail: ",
                           font=("corbel", 10))
        labelEmail.grid(row=9, column=0)
        entryEmail = Entry(tempWindow, 
                           textvar=emailNew)
        entryEmail.grid(row=9, column=1, columnspan=2)

        labelMobile = Label(tempWindow,
                           text="Mobile: ",
                           font=("corbel", 10))
        labelMobile.grid(row=10, column=0)
        entryMobile = Entry(tempWindow, 
                            textvar=mobileNew)
        entryMobile.grid(row=10, column=1, columnspan=2)

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
                    onvalue='Yes', 
                    offvalue='No').grid(row=3, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="View Patient Consultation Notes", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canViewConsultations,
                    onvalue='Yes', 
                    offvalue='No').grid(row=4, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Edit Patient Consultation Notes", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canEditConsultations,
                    onvalue='Yes', 
                    offvalue='No').grid(row=5, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Communicate with Patients", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canCommunicatePatients,
                    onvalue='Yes', 
                    offvalue='No').grid(row=6, column=7, sticky='W',)
        Checkbutton(tempWindow, 
                    text="View Patient Statistics", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canViewStatistics,
                    onvalue='Yes', 
                    offvalue='No').grid(row=2, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="View Patient Appointments", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canViewAppointments,
                    onvalue='Yes', 
                    offvalue='No').grid(row=3, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Cancel Patient Appointments", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canCancelAppointments,
                    onvalue='Yes', 
                    offvalue='No').grid(row=4, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Create New User Accounts", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canCreateUsers,
                    onvalue='Yes', 
                    offvalue='No').grid(row=5, column=8, sticky='W',)
        Checkbutton(tempWindow, 
                    text="Edit User Accounts", 
                    cursor='hand2',
                    font=("corbel", 10),
                    variable=canEditUsers,
                    onvalue='Yes', 
                    offvalue='No').grid(row=6, column=8, sticky='W',)

        Button(tempWindow, 
               text='Save Changes', 
               width=20, 
               bg='darkblue', 
               fg='white', 
               command= lambda: getValues(searchedUserDetails)).grid(row=12, column=5, columnspan=3)
        Button(tempWindow, 
               text='Exit', 
               width=20, 
               bg='darkblue', 
               fg='white', 
               command=tempWindow.destroy).grid(row=12, column=8, columnspan=2)

        fillData(searchedUserDetails)
        tempWindow.mainloop()

# Search Patient Records # 
# Status: NOT FINISHED - add recent consultations
def searchPatient():
    tempWindow2 = Tk()
    tempWindow2.geometry('470x120')
    tempWindow2.title("Search Patient Records")

    center(tempWindow2)

    dobDay = StringVar()
    dobMonth = StringVar()
    dobYear = StringVar()
    firstname = StringVar()
    lastname = StringVar()

    def mainWindow(currentPatientDetails, currentPatientDetailsOD, currentPatientDetailsAF, recentPatientMed):
        tempWindow = Tk()
        tempWindow.geometry('425x380')
        tempWindow.title("Patient Registration Overview")

        center(tempWindow)

        patientID = currentPatientDetails[0]

        def viewOD(currentPatientDetailsOD):
            tempWindow3 = Tk()
            tempWindow3.geometry('425x380')
            tempWindow3.title("Organ Donation Status")

            center(tempWindow3)

            # BEGIN FORMATTING #
            spacerLabel = Label(tempWindow3, text=" ", width=5)
            spacerLabel.grid(row=0, column=0, rowspan=13)

            spacerLabel = Label(tempWindow3, text=" ", width=20)
            spacerLabel.grid(row=0, column=1, rowspan=13)

            spacerLabel = Label(tempWindow3, text=" ", width=5)
            spacerLabel.grid(row=0, column=2, rowspan=13)

            spacerLabel = Label(tempWindow3, text=" ", width=20)
            spacerLabel.grid(row=0, column=3, rowspan=13)
        
            spacerLabel = Label(tempWindow3, text=" ", width=5)
            spacerLabel.grid(row=0, column=4, rowspan=13)

            i = 0

            while i < 13:
                spacerLabel = Label(tempWindow3, text=" ", width=10)
                spacerLabel.grid(row=i, column=0, columnspan=5)
            
                i += 1
            # END FORMATTING #

            consent = currentPatientDetailsOD[1]
            kidney = currentPatientDetailsOD[2]
            heart = currentPatientDetailsOD[3]
            lungs = currentPatientDetailsOD[4]
            liver = currentPatientDetailsOD[5]
            corneas = currentPatientDetailsOD[6]
            pancreas = currentPatientDetailsOD[7]

            if consent == "Yes":
                consent = "Consent Given"
            else:
                consent = "Consent Denied"

            labelTitle = Label(tempWindow3, 
                               text="Organ Donation Status", 
                               font=("corbel bold", 14))                 
            labelTitle.grid(row=1, column=1, columnspan=3)     

            labelConsent = Label(tempWindow3, 
                                 text=consent, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=3, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=kidney, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=4, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=heart, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=5, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=lungs, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=6, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=liver, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=7, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=corneas, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=8, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=pancreas, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=9, column=3)

            ## DIV

            labelConsent = Label(tempWindow3, 
                                 text="Consent Status:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=3, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Kidney:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=4, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Heart:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=5, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Lungs:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=6, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Liver:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=7, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Corneas:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=8, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Pancreas:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=9, column=1)

            navButton = Button(tempWindow3, 
                               text='Close', 
                               bg='#09425A', 
                               fg='#FFFFFF',
                               width=20,
                               command=tempWindow3.destroy).grid(row=11, column=1)

            navButton = Button(tempWindow3, 
                               text='Edit', 
                               bg='#09425A', 
                               fg='#FFFFFF',
                               width=20,
                               command=editPatient).grid(row=11, column=3)

        def viewAF(currentPatientDetailsAF):
            tempWindow4 = Tk()
            tempWindow4.geometry('425x380')
            tempWindow4.title("Armed Forces Records")

            center(tempWindow4)

            # BEGIN FORMATTING #
            spacerLabel = Label(tempWindow4, text=" ", width=5)
            spacerLabel.grid(row=0, column=0, rowspan=9)

            spacerLabel = Label(tempWindow4, text=" ", width=20)
            spacerLabel.grid(row=0, column=1, rowspan=9)

            spacerLabel = Label(tempWindow4, text=" ", width=5)
            spacerLabel.grid(row=0, column=2, rowspan=9)

            spacerLabel = Label(tempWindow4, text=" ", width=20)
            spacerLabel.grid(row=0, column=3, rowspan=9)
        
            spacerLabel = Label(tempWindow4, text=" ", width=5)
            spacerLabel.grid(row=0, column=4, rowspan=9)

            i = 0

            while i < 9:
                spacerLabel = Label(tempWindow4, text=" ", width=10)
                spacerLabel.grid(row=i, column=0, columnspan=5)
            
                i += 1
            # END FORMATTING #

            personnelNum = currentPatientDetailsAF[1]
            enDate = currentPatientDetailsAF[2]
            diDate = currentPatientDetailsAF[3]

            labelTitle = Label(tempWindow4, 
                               text="Armed Forces Records", 
                               font=("corbel bold", 14))                 
            labelTitle.grid(row=1, column=1, columnspan=3)     

            labelConsent = Label(tempWindow4, 
                                 text=personnelNum, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=3, column=3)

            labelConsent = Label(tempWindow4, 
                                 text=enDate, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=4, column=3)

            labelConsent = Label(tempWindow4, 
                                 text=diDate, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=5, column=3)

            ## DIV

            labelConsent = Label(tempWindow4, 
                                 text="Personnel Number:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=3, column=1)

            labelConsent = Label(tempWindow4, 
                                 text="Enlistment Date:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=4, column=1)

            labelConsent = Label(tempWindow4, 
                                 text="Discharge Date:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=5, column=1)

            navButton = Button(tempWindow4, 
                               text='Close', 
                               bg='#09425A', 
                               fg='#FFFFFF',
                               width=20,
                               command=tempWindow4.destroy).grid(row=7, column=1)

            navButton = Button(tempWindow4, 
                               text='Edit', 
                               bg='#09425A', 
                               fg='#FFFFFF',
                               width=20,
                               command=editPatient).grid(row=7, column=3)

        def viewCons():
            print("View Recent Consultations Function Called.")

        def viewMed(recentPatientMed):
            tempWindow3 = Tk()
            tempWindow3.geometry('425x500')
            tempWindow3.title("Recent Medical Data")

            center(tempWindow3)

            # BEGIN FORMATTING #
            spacerLabel = Label(tempWindow3, text=" ", width=5)
            spacerLabel.grid(row=0, column=0, rowspan=23)

            spacerLabel = Label(tempWindow3, text=" ", width=20)
            spacerLabel.grid(row=0, column=1, rowspan=23)

            spacerLabel = Label(tempWindow3, text=" ", width=5)
            spacerLabel.grid(row=0, column=2, rowspan=23)

            spacerLabel = Label(tempWindow3, text=" ", width=20)
            spacerLabel.grid(row=0, column=3, rowspan=23)
        
            spacerLabel = Label(tempWindow3, text=" ", width=5)
            spacerLabel.grid(row=0, column=4, rowspan=23)

            i = 0

            while i < 23:
                spacerLabel = Label(tempWindow3, text=" ", width=10)
                spacerLabel.grid(row=i, column=0, columnspan=5)
            
                i += 1
            # END FORMATTING #

            # GET VALS FROM LIST

            user1 = recentPatientMed[2]
            time1 = recentPatientMed[3]
            date1 = recentPatientMed[4]
            data1 = recentPatientMed[5]
            value1 = recentPatientMed[6]

            user2 = recentPatientMed[9]
            time2 = recentPatientMed[10]
            date2 = recentPatientMed[11]
            data2 = recentPatientMed[12]
            value2 = recentPatientMed[13]

            user3 = recentPatientMed[16]
            time3 = recentPatientMed[17]
            date3 = recentPatientMed[18]
            data3 = recentPatientMed[19]
            value3 = recentPatientMed[20]

            # Get User Names

            conn = sqlite3.connect('Users.db')
        
            with conn:
                cursor = conn.cursor()

                user1details = []
                user2details = []
                user3details = []

                tupleDetails2 = ""
                stringDetails2 = ""

                cursor.execute("SELECT title, firstname, surname FROM UserAccounts WHERE userID = ?", (user1))

                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        user1details.append(detail)

                tupleDetails2 = ""
                stringDetails2 = ""

                cursor.execute("SELECT title, firstname, surname FROM UserAccounts WHERE userID = ?", (user2))

                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        user2details.append(detail)

                tupleDetails2 = ""
                stringDetails2 = ""

                cursor.execute("SELECT title, firstname, surname FROM UserAccounts WHERE userID = ?", (user3))

                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        user3details.append(detail)

            user1title = user1details[0]
            user1firstname = user1details[1]
            user1surname = user1details[2]

            user1fullname = user1title + " " + user1firstname + " " + user1surname

            user2title = user2details[0]
            user2firstname = user2details[1]
            user2surname = user2details[2]

            user2fullname = user2title + " " + user2firstname + " " + user2surname

            user3title = user3details[0]
            user3firstname = user3details[1]
            user3surname = user3details[2]

            user3fullname = user3title + " " + user3firstname + " " + user3surname

            labelTitle = Label(tempWindow3, 
                               text="Recent Medical Data Entries", 
                               font=("corbel bold", 14))                 
            labelTitle.grid(row=1, column=1, columnspan=3)

            # SET 1 LABELS   

            labelConsent = Label(tempWindow3, 
                                 text="Staff Member:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=3, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Entry Time:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=4, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Entry Date:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=5, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Data Type:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=6, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Data Value:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=7, column=1)    

            # SET 2 LABELS

            labelConsent = Label(tempWindow3, 
                                 text="Staff Member:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=9, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Entry Time:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=10, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Entry Date:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=11, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Data Type:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=12, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Data Value:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=13, column=1)

            # SET 3 LABELS

            labelConsent = Label(tempWindow3, 
                                 text="Staff Member:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=15, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Entry Time:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=16, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Entry Date:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=17, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Data Type:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=18, column=1)

            labelConsent = Label(tempWindow3, 
                                 text="Data Value:", 
                                 font=("corbel bold", 10))                 
            labelConsent.grid(row=19, column=1)

            # SET 1 VALUES    

            labelConsent = Label(tempWindow3, 
                                 text=user1fullname, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=3, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=time1, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=4, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=date1, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=5, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=data1, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=6, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=value1, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=7, column=3)    

            # SET 2 VALUES

            labelConsent = Label(tempWindow3, 
                                 text=user2fullname, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=9, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=time2, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=10, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=date2, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=11, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=data2, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=12, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=value2, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=13, column=3)

            # SET 3 VALUES

            labelConsent = Label(tempWindow3, 
                                 text=user3fullname, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=15, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=time3, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=16, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=date3, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=17, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=data3, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=18, column=3)

            labelConsent = Label(tempWindow3, 
                                 text=value3, 
                                 font=("corbel", 10))                 
            labelConsent.grid(row=19, column=3)

            navButton = Button(tempWindow3, 
                               text='Close', 
                               bg='#09425A', 
                               fg='#FFFFFF',
                               width=20,
                               command=tempWindow3.destroy).grid(row=21, column=1)

            navButton = Button(tempWindow3, 
                               text='Add New', 
                               bg='#09425A', 
                               fg='#FFFFFF',
                               width=20,
                               command=newMed).grid(row=21, column=3)

        patientTitle = currentPatientDetails[1]
        firstName = currentPatientDetails[2]
        lastName = currentPatientDetails[3]

        fullName = patientTitle + " " + firstName + " " + lastName

        dateOfBirth = currentPatientDetails[5]

        houseNum = currentPatientDetails[8]
        street = currentPatientDetails[9]
        postcode = currentPatientDetails[10]
        county = currentPatientDetails[11]

        address1 = houseNum + " " + street
        address2 = county
        address3 = postcode

        patientHCN = currentPatientDetails[17]

        contactNum = currentPatientDetails[12]

        # BEGIN FORMATTING #
        spacerLabel = Label(tempWindow, text=" ", width=5)
        spacerLabel.grid(row=0, column=0, rowspan=15)

        spacerLabel = Label(tempWindow, text=" ", width=20)
        spacerLabel.grid(row=0, column=1, rowspan=15)

        spacerLabel = Label(tempWindow, text=" ", width=5)
        spacerLabel.grid(row=0, column=2, rowspan=15)

        spacerLabel = Label(tempWindow, text=" ", width=20)
        spacerLabel.grid(row=0, column=3, rowspan=15)
        
        spacerLabel = Label(tempWindow, text=" ", width=5)
        spacerLabel.grid(row=0, column=4, rowspan=15)

        i = 0

        while i < 15:
            spacerLabel = Label(tempWindow, text=" ", width=10)
            spacerLabel.grid(row=i, column=0, columnspan=5)
            
            i += 1
        # END FORMATTING #

        labelTitle = Label(tempWindow, 
                           text="PATIENT OVERVIEW", 
                           font=("corbel bold", 14))                 
        labelTitle.grid(row=1, column=1, columnspan=3)                   
        
        labelName = Label(tempWindow, 
                           text="Full Name:", 
                           font=("corbel bold", 10))                 
        labelName.grid(row=3, column=1)
        
        labelDOB = Label(tempWindow, 
                           text="Date of Birth:", 
                           font=("corbel bold", 10))                 
        labelDOB.grid(row=4, column=1)

        labelAdd = Label(tempWindow, 
                           text="Address:", 
                           font=("corbel bold", 10))                 
        labelAdd.grid(row=6, column=1)

        labelHCN = Label(tempWindow, 
                           text="H&C Number:", 
                           font=("corbel bold", 10))                 
        labelHCN.grid(row=8, column=1)

        labelContact = Label(tempWindow, 
                           text="Contact Number:", 
                           font=("corbel bold", 10))                 
        labelContact.grid(row=9, column=1)

        ## DIV

        labelName = Label(tempWindow, 
                           text=fullName, 
                           font=("corbel", 10))                 
        labelName.grid(row=3, column=3)
        
        labelDOB = Label(tempWindow, 
                           text=dateOfBirth, 
                           font=("corbel", 10))                 
        labelDOB.grid(row=4, column=3)

        labelAdd = Label(tempWindow, 
                           text=address1, 
                           font=("corbel", 10))                 
        labelAdd.grid(row=5, column=3)

        labelAdd = Label(tempWindow, 
                           text=address2, 
                           font=("corbel", 10))                 
        labelAdd.grid(row=6, column=3)

        labelAdd = Label(tempWindow, 
                           text=address3, 
                           font=("corbel", 10))                 
        labelAdd.grid(row=7, column=3)

        labelHCN = Label(tempWindow, 
                           text=patientHCN, 
                           font=("corbel", 10))                 
        labelHCN.grid(row=8, column=3)

        labelContact = Label(tempWindow, 
                           text=contactNum, 
                           font=("corbel", 10))                 
        labelContact.grid(row=9, column=3)
        
        navButton = Button(tempWindow, 
                           text='Medical History', 
                           bg='#09425A', 
                           fg='#FFFFFF',
                           width=20,
                           command= lambda: viewMed(recentPatientMed)).grid(row=11, column=1)

        navButton = Button(tempWindow, 
                           text='Organ Donor Status', 
                           bg='#09425A', 
                           fg='#FFFFFF',
                           width=20,
                           command= lambda: viewOD(currentPatientDetailsOD)).grid(row=11, column=3)

        navButton = Button(tempWindow, 
                           text='Consultations', 
                           bg='#09425A', 
                           fg='#FFFFFF',
                           width=20,
                           command=viewCons).grid(row=13, column=1)

        navButton = Button(tempWindow, 
                           text='Armed Forces Records', 
                           bg='#09425A', 
                           fg='#FFFFFF',
                           width=20,
                           command= lambda: viewAF(currentPatientDetailsAF)).grid(row=13, column=3)
        
    def searchUser():       
        def getValues():
            firstname = entryFirstname.get()
            lastname = entryLastname.get()
            dobDay = comboboxDOBDay.get()
            dobMonth = comboboxDOBMonth.get()
            dobYear = comboboxDOBYear.get()

            values = [firstname, lastname, dobDay, dobMonth, dobYear]

            return values

        values = getValues()
        
        firstname = values[0]
        lastname = values[1]
        dobDay = values[2]
        dobMonth = values[3]
        dobYear = values[4]
        
        dob = str(dobDay) + "/" + str(dobMonth) + "/" + str(dobYear)

        fullname = str(firstname) + " " + str(lastname)

        conn = sqlite3.connect('Patients.db')
        
        with conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM PatientDemo WHERE forename = ? and surname = ? and dateOfBirth = ?", (firstname, lastname, dob))

            result = cursor.fetchall()
            
            if result:
                tupleDetails2 = ""
                stringDetails2 = ""
                currentPatientDetails = []
                currentPatientDetailsOD = []
                currentPatientDetailsAF = []
                recentPatientMed = []
                recentPatientCons = []

                cursor.execute('SELECT * FROM PatientDemo WHERE forename = ? and surname =  ? and dateOfBirth = ?', (firstname, lastname, dob))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetails.append(detail)

                patientID = str(currentPatientDetails[0])

                cursor.execute('SELECT * FROM PatientOD WHERE patientID = ?', (patientID))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetailsOD.append(detail)

                cursor.execute('SELECT * FROM PatientAF WHERE patientID = ?', (patientID))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetailsAF.append(detail)

                cursor.execute('''SELECT * 
                                  FROM PatientMed 
                                  WHERE patientID = ?
                                  ORDER BY entryID ASC
                                  LIMIT 3;''', 
                                  (patientID))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        recentPatientMed.append(detail)

                ms.showinfo('Succesful!', 'The record of ' + fullname + ' has been loaded.', parent=tempWindow2)

                tempWindow2.destroy()
                mainWindow(currentPatientDetails, currentPatientDetailsOD, currentPatientDetailsAF, recentPatientMed)
            else:
                ms.showerror('Patient Not Found', 'No patients with these matching details have been found.')
                entryFirstname.delete(0, END)
                entryLastname.delete(0, END)
                comboboxDOBDay.current(0)
                comboboxDOBMonth.current(0)
                comboboxDOBYear.current(0)
       
    spacerLabel = Label(tempWindow2, 
                        text=" ")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=0, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=6, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=2, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=8, rowspan=9)

    labelFirstname = Label(tempWindow2, 
                        text="Patient Firstname: ",
                        font=("corbel bold", 10))
    labelFirstname.grid(row=1, column=1)
    entryFirstname = Entry(tempWindow2, 
                        textvar=firstname)
    entryFirstname.grid(row=1, column=3, columnspan=3, sticky=E+W)

    labelLastname = Label(tempWindow2, 
                        text="Patient Lastname: ",
                        font=("corbel bold", 10))
    labelLastname.grid(row=2, column=1)
    entryLastname = Entry(tempWindow2, 
                        textvar=lastname)
    entryLastname.grid(row=2, column=3, columnspan=3, sticky=E+W)

    labelDocType = Label(tempWindow2, 
                              text="Patient Date of Birth: ", 
                              font=("corbel bold", 10))
    labelDocType.grid(row=3, column=1)
    
    comboboxDOBDay = ttk.Combobox(tempWindow2, 
                                   textvariable=dobDay)
    comboboxDOBDay.grid(row=3, column=3, sticky=E+W)
    comboboxDOBDay.config(values = ('DD', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                                     '30', '31'), width=4)
    comboboxDOBDay.current([0])

    comboboxDOBMonth = ttk.Combobox(tempWindow2, 
                                   textvariable=dobMonth)
    comboboxDOBMonth.grid(row=3, column=4, sticky=E+W)
    comboboxDOBMonth.config(values = ('MM', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12'), width=4)
    comboboxDOBMonth.current([0])

    comboboxDOBYear = ttk.Combobox(tempWindow2, 
                                   textvariable=dobYear)
    comboboxDOBYear.grid(row=3, column=5, sticky=E+W)
    comboboxDOBYear.config(values = ('YYYY', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909',
                                     '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', 
                                     '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', 
                                     '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', 
                                     '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', 
                                     '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', 
                                     '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
                                     '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                                     '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', 
                                     '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                                     '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'), width=9)
    comboboxDOBYear.current([0])

    searchButton = Button(tempWindow2, 
                          text='Search', 
                          bg='darkblue', 
                          fg='white', 
                          command=searchUser).grid(row=2, column=7)

    spacerLabel = Label(tempWindow2, 
                        text=" ")
    spacerLabel.grid(row=4, column=0, columnspan=5)

    tempWindow2.mainloop()

# Edit Patient Records #
# Status: BROKEN - does not fill in values of checkboxes or radiobuttons
def editPatient():
    tempWindow2 = Tk()
    tempWindow2.geometry('460x140')
    tempWindow2.title("Create a New Document")

    center(tempWindow2)

    dobDay = StringVar()
    dobMonth = StringVar()
    dobYear = StringVar()
    firstname = StringVar()
    lastname = StringVar()

    def mainWindow(currentPatientDetails, currentPatientDetailsOD, currentPatientDetailsAF):
        tempWindow = Tk()
        tempWindow.geometry('700x450')
        tempWindow.title("Register a new Patient")

        center(tempWindow)

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

        def appendPatient(title, forename, surname, prevSurname, dob, genderNew, country, 
                      housenumber, street, postcode, county, contactNo, regType, oldGP, oldGPAddress, 
                      oldGPPostcode, hcn, personnelNum, enDate, diDate, organYNNew, kidneyNew, heartNew, 
                      lungsNew, liverNew, corneasNew, pancreasNew):
        
            conn = sqlite3.connect('Patients.db')
        
            with conn:
                cursor = conn.cursor()
            
                insertPatientDemo = '''UPDATE PatientDemo 
                                       SET patientTitle = ?, forename = ?, surname = ?, prevSurname = ?, dateOfBirth = ?, 
                                           gender = ?, country = ?, housenumber = ?, street = ?, postcode = ?, county = ?, 
                                           contactnumber = ?, regType = ?, oldGP = ?, oldGPAddress = ?, oldGPPostcode = ?, 
                                           hcn = ? 
                                       WHERE patientID = ?''' 
                insertPatientDemoValues = (title), (forename), (surname), (prevSurname), (dob), (genderNew), (country), (housenumber), (street), (postcode), (county), (contactNo), (regType), (oldGP), (oldGPAddress), (oldGPPostcode), (hcn)
                cursor.execute(insertPatientDemo, insertPatientDemoValues)
        
                insertPatientAF = "UPDATE PatientAF SET personnelNum = ?, enDate = ?, diDate = ? WHERE patientID = ?"
                insertPatientAFValues = (personnelNum), (enDate), (diDate)
                cursor.execute(insertPatientAF, insertPatientAFValues)
            
                insertPatientOD = '''UPDATE PatientOD 
                                     SET patientID = ?, organYN = ?, kidney = ?, heart = ?, lungs = ?, liver = ?, corneas = ?, pancreas = ? 
                                     WHERE patientID = ?'''
                insertPatientODValues = (organYNNew), (kidneyNew), (heartNew), (lungsNew), (liverNew), (corneasNew), (pancreasNew)
                cursor.execute(insertPatientOD, insertPatientODValues)
            
                conn.commit()

            again = ms.askyesno("Succesful!", "Would you like to edit another patient record?", parent=tempWindow)

            if again == True:
                tempWindow.destroy()
                editPatient()
            else:
                tempWindow.destroy()
        
        def getPatientValues(genderNew):
            title = comboboxTitle.get()
            forename = entryForename.get()
            surname = entrySurname.get()
            prevSurname = entryPrevSurname.get()
            dob = entryDOB.get()

            print("genderNew", genderNew)

            country = comboboxCountry.get()
            housenumber = entryHousenumber.get()
            street = entryStreet.get()
            postcode = entryPostcode.get()
            county = entryCounty.get()
            contactNo = entryContactNo.get()
            regType = comboboxRegType.get()
            oldGP = entryOldGP.get()
            oldGPAddress = entryOldGPAddress.get()
            oldGPPostcode = entryOldGPPostcode.get()
            hcn = entryHCN.get()

            personnelNum = entryPersonnelNum.get()
            enDate = entryEnDate.get()
            diDate = entryDiDate.get()

            organYNNew = organYN.get()
            kidneyNew = kidney.get()
            heartNew = heart.get()
            liverNew = liver.get()
            corneasNew = corneas.get()
            lungsNew = lungs.get()
            pancreasNew = pancreas.get()
        
            appendPatient(title, forename, surname, prevSurname, dob, genderNew, country, 
                          housenumber, street, postcode, county, contactNo, regType, oldGP, oldGPAddress, 
                          oldGPPostcode, hcn, personnelNum, enDate, diDate, organYNNew, kidneyNew, heartNew, 
                          lungsNew, liverNew, corneasNew, pancreasNew)

        labelTitle = Label(tempWindow, 
                           text="Antrim Castle Surgery - Registration Application", 
                           font=("corbel bold", 14), 
                           anchor=N)
        labelTitle.grid(row=0, column=1, columnspan=6)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=1, column=0, columnspan=4)

        labelPatientTitle = Label(tempWindow, 
                                  text="Title: ", 
                                  font=("corbel", 10))
        labelPatientTitle.grid(row=2, column=0)
        comboboxTitle = ttk.Combobox(tempWindow, 
                                     textvariable=patientTitle)
        comboboxTitle.grid(row=2, column=1, columnspan=2)
        comboboxTitle.config(values = ('Please Select...', 'Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Rev', 'Prof', 'Sir', 'Other'), width=17)
        comboboxTitle.current([0])

        labelForename = Label(tempWindow, 
                              text="Forename(s): ", 
                              font=("corbel", 10))
        labelForename.grid(row=3, column=0)
        entryForename = Entry(tempWindow, 
                              textvar=forename)
        entryForename.grid(row=3, column=1, columnspan=2)

        labelSurname = Label(tempWindow, 
                             text="Surname: ", 
                             font=("corbel", 10))
        labelSurname.grid(row=4, column=0)
        entrySurname = Entry(tempWindow, 
                             textvar=surname)
        entrySurname.grid(row=4, column=1, columnspan=2)

        labelPrevSurname = Label(tempWindow, 
                                 text="Previous Surname: ", 
                                 font=("corbel", 10))
        labelPrevSurname.grid(row=5, column=0)
        entryPrevSurname = Entry(tempWindow, 
                                 textvar=prevSurname)
        entryPrevSurname.grid(row=5, column=1, columnspan=2)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=6, column=0, columnspan=4)

        labelDOB = Label(tempWindow, 
                         text="Date of Birth: ", 
                         font=("corbel", 10))
        labelDOB.grid(row=7, column=0)
        entryDOB = Entry(tempWindow, 
                         textvar=dateOfBirth)
        entryDOB.grid(row=7, column=1, columnspan=2)

        labelGender = Label(tempWindow, 
                            text="Gender: ", 
                            font=("corbel", 10))
        labelGender.grid(row=8, column=0)
        rbMale = Radiobutton(tempWindow, 
                            text="Male",
                            variable=gender,
                            value="Male").grid(row=8, column=1)
        rbFemale = Radiobutton(tempWindow,  
                            text="Female",
                            variable=gender,
                            value="Female").grid(row=8, column=2)

        labelCountry = Label(tempWindow, 
                             text="Country of Birth: ", 
                             font=("corbel", 10))
        labelCountry.grid(row=9, column=0)
        comboboxCountry = ttk.Combobox(tempWindow, 
                                       textvariable=country)
        comboboxCountry.grid(row=9, column=1, columnspan=2)
        comboboxCountry.config(values = ('Please Select...',  'Australia', 'Belgium', 'Canada', 'Denmark', 'Egypt', 'France', 
                                         'Germany', 'Hungary', 'Ireland', 'Jamaica', 'Kenya', 'Lithuania', 'Macedonia', 'Norway', 
                                         'Oman', 'Poland', 'Quatar', 'Russia', 'Spain', 'Tanzania', 'United Kingdom', 'Venuzuala', 
                                         'Yugoslavia', 'Zambia'), width=17)
        comboboxCountry.current([0])

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=10, column=0, columnspan=4)

        labelHousenumber = Label(tempWindow, 
                                 text="House Number: ", 
                                 font=("corbel", 10))
        labelHousenumber.grid(row=11, column=0)
        entryHousenumber = Entry(tempWindow, 
                                 textvar=housenumber)
        entryHousenumber.grid(row=11, column=1, columnspan=2)

        labelStreet = Label(tempWindow, 
                            text="Street: ", 
                            font=("corbel", 10))
        labelStreet.grid(row=12, column=0)
        entryStreet = Entry(tempWindow, 
                            textvar=street)
        entryStreet.grid(row=12, column=1, columnspan=2)

        labelPostcode = Label(tempWindow, 
                              text="Postcode: ", 
                              font=("corbel", 10))
        labelPostcode.grid(row=13, column=0)
        entryPostcode = Entry(tempWindow, 
                              textvar=postcode)
        entryPostcode.grid(row=13, column=1, columnspan=2)

        labelCounty = Label(tempWindow, 
                            text="County: ", 
                            font=("corbel", 10))
        labelCounty.grid(row=14, column=0)
        entryCounty = Entry(tempWindow, 
                            textvar=county)
        entryCounty.grid(row=14, column=1, columnspan=2)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=15, column=0, columnspan=4)

        labelContactNo = Label(tempWindow, 
                               text="Contact Number: ", 
                               font=("corbel", 10))
        labelContactNo.grid(row=16, column=0)
        entryContactNo = Entry(tempWindow, 
                               textvar=contactnumber)
        entryContactNo.grid(row=16, column=1, columnspan=2)

        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=4)
        spacerLabel.grid(row=0, column=3, rowspan=18)

        labelRegType = Label(tempWindow, 
                             text="Registration Type: ", 
                             font=("corbel", 10))
        labelRegType.grid(row=2, column=4)
        comboboxRegType = ttk.Combobox(tempWindow, 
                                       textvariable=regType)
        comboboxRegType.grid(row=2, column=5, columnspan=2)
        comboboxRegType.config(values = ('Please Select...', 'First ever registration with a GP Surgery', 
                                         'Moving GP Surgery'), width=17)
        comboboxRegType.current([0])

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=3, column=4, columnspan=3)

        labelOldGP = Label(tempWindow, 
                           text="Old GP: ", 
                           font=("corbel", 10))
        labelOldGP.grid(row=4, column=4)
        entryOldGP = Entry(tempWindow, 
                           textvar=oldGP)
        entryOldGP.grid(row=4, column=5, columnspan=2)

        labelOldGPAddress = Label(tempWindow, 
                                  text="Address: ", 
                                  font=("corbel", 10))
        labelOldGPAddress.grid(row=5, column=4)
        entryOldGPAddress = Entry(tempWindow, 
                                  textvar=oldGPAddress)
        entryOldGPAddress.grid(row=5, column=5, columnspan=2)

        labelOldGPPostcode = Label(tempWindow, 
                                   text="Postcode: ", 
                                   font=("corbel", 10))
        labelOldGPPostcode.grid(row=6, column=4)
        entryOldGPPostcode = Entry(tempWindow, 
                                   textvar=oldGPPostcode)
        entryOldGPPostcode.grid(row=6, column=5, columnspan=2)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=7, column=4, columnspan=3)

        labelHCN = Label(tempWindow, 
                         text="Health & Care Number: ", 
                         font=("corbel", 10))
        labelHCN.grid(row=8, column=4)
        entryHCN = Entry(tempWindow, 
                         textvar=hcn)
        entryHCN.grid(row=8, column=5, columnspan=2)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=9, column=4, columnspan=3)

        labelGender = Label(tempWindow, 
                            text="Complete the below if the patient is returning from the Armed Forces!", 
                            font=("corbel", 10))
        labelGender.grid(row=10, column=4, columnspan=4)

        labelPersonnelNum = Label(tempWindow, 
                                  text="Personnel Number: ", 
                                  font=("corbel", 10))
        labelPersonnelNum.grid(row=11, column=4)
        entryPersonnelNum = Entry(tempWindow, 
                                  textvar=personnelNum)
        entryPersonnelNum.grid(row=11, column=5, columnspan=2)

        labelEnDate = Label(tempWindow, 
                            text="Enlistment Date: ", 
                            font=("corbel", 10))
        labelEnDate.grid(row=12, column=4)
        entryEnDate = Entry(tempWindow, 
                            textvar=enDate)
        entryEnDate.grid(row=12, column=5, columnspan=2)

        labelDiDate = Label(tempWindow, 
                            text="Discharge Date: ", 
                            font=("corbel", 10))
        labelDiDate.grid(row=13, column=4)
        entryDiDate = Entry(tempWindow, 
                            textvar=diDate)
        entryDiDate.grid(row=13, column=5, columnspan=2)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=14, column=4, columnspan=3)

        labelOrganYN = Label(tempWindow, 
                             text="Has the Patient Consented to Organ Donation?", 
                             font=("corbel", 10))
        labelOrganYN.grid(row=15, column=4, columnspan=2)
        organButtonYes = Radiobutton(tempWindow, 
                                   text="Yes", 
                                   variable=organYN,
                                   cursor='hand2',
                                   value=1).grid(row=15, column=6)
        organButtonNo = Radiobutton(tempWindow, 
                                   text="No", 
                                   variable=organYN,
                                   cursor='hand2',
                                   value=0).grid(row=15, column=7)

        labelOrganType = Label(tempWindow, 
                               text="Organs to be donated: ", 
                               font=("corbel", 10))
        labelOrganType.grid(row=16, column=4)
        kidneyBox = Checkbutton(tempWindow,
                                   cursor='hand2',
                                   text="Kidneys", 
                                   variable=kidney,
                                   onvalue="Yes",
                                   offvalue="No").grid(row=16, column=5, sticky='W')
        heartBox = Checkbutton(tempWindow,
                                  cursor='hand2',
                                  text="Heart", 
                                  variable=heart,
                                  onvalue="Yes",
                                  offvalue="No").grid(row=16, column=6, sticky='W')
        liverBox = Checkbutton(tempWindow,
                                  cursor='hand2',
                                  text="Liver", 
                                  variable=liver,
                                  onvalue="Yes",
                                  offvalue="No").grid(row=16, column=7, sticky='W')
        corneasBox = Checkbutton(tempWindow,
                                    cursor='hand2',
                                    text="Corneas", 
                                    variable=corneas,
                                    onvalue="Yes",
                                    offvalue="No").grid(row=17, column=5, sticky='W')
        lungsBox = Checkbutton(tempWindow,
                                  cursor='hand2',
                                  text="Lungs",
                                  variable=lungs,
                                  onvalue="Yes",
                                  offvalue="No").grid(row=17, column=6, sticky='W')
        pancreasBox = Checkbutton(tempWindow,
                                     cursor='hand2',
                                     text="Pancreas", 
                                     variable=pancreas,
                                     onvalue="Yes",
                                     offvalue="No").grid(row=17, column=7, sticky='W')
        
        def updateValues(currentPatientDetails, currentPatientDetailsOD, currentPatientDetailsAF):
            entryForename.delete(0, END)
            entryForename.insert(0, currentPatientDetails[2])

            entrySurname.delete(0, END)
            entrySurname.insert(0, currentPatientDetails[3])

            if currentPatientDetails[4] is not None:
                entryPrevSurname.delete(0, END)
                entryPrevSurname.insert(0, currentPatientDetails[4])

            entryDOB.delete(0, END)
            entryDOB.insert(0, currentPatientDetails[5])

            entryHousenumber.delete(0, END)
            entryHousenumber.insert(0, currentPatientDetails[8])

            entryStreet.delete(0, END)
            entryStreet.insert(0, currentPatientDetails[9])

            entryPostcode.delete(0, END)
            entryPostcode.insert(0, currentPatientDetails[10])

            entryCounty.delete(0, END)
            entryCounty.insert(0, currentPatientDetails[11])

            entryContactNo.delete(0, END)
            entryContactNo.insert(0, currentPatientDetails[12])

            if currentPatientDetails[14] is not None:
                entryOldGP.delete(0, END)
                entryOldGP.insert(0, currentPatientDetails[14])

            if currentPatientDetails[15] is not None:
                entryOldGPAddress.delete(0, END)
                entryOldGPAddress.insert(0, currentPatientDetails[15])
       
            if currentPatientDetails[16] is not None:
                entryOldGPPostcode.delete(0, END)
                entryOldGPPostcode.insert(0, currentPatientDetails[16])

            entryHCN.delete(0, END)
            entryHCN.insert(0, currentPatientDetails[17])

            titleReturn = currentPatientDetails[1]
            countryReturn = currentPatientDetails[7]
            regTypeReturn = currentPatientDetails[13]

            comboboxTitle.set(titleReturn)
            comboboxCountry.set(countryReturn)
            comboboxRegType.set(regTypeReturn)

            if currentPatientDetails[6] == 'Female':
                gender.set("Female")
            elif currentPatientDetails[6] == 'Male':
                gender.set("Male")
            else:
                print("ERROR IN GENDER SELECTION LINE 1018")

            if currentPatientDetailsAF[1] is not None:
                entryPersonnelNum.delete(0, END)
                entryPersonnelNum.insert(0, currentPatientDetailsAF[1])

            if currentPatientDetailsAF[2] is not None:
                entryEnDate.delete(0, END)
                entryEnDate.insert(0, currentPatientDetailsAF[2])

            if currentPatientDetails[3] is not None:
                entryDiDate.delete(0, END)
                entryDiDate.insert(0, currentPatientDetailsAF[3])

            if currentPatientDetailsOD[1] == "Yes":
                organYN.set(1)
            else:
                organYN.set(0)
        
            if currentPatientDetailsOD[2] == "Yes": 
                kidney.set("Yes")
            if currentPatientDetailsOD[3] == "Yes":
                heart.set("Yes")
            if currentPatientDetailsOD[5] == "Yes": 
                liver.set("Yes")
            if currentPatientDetailsOD[6] == "Yes":
                corneas.set("Yes")
            if currentPatientDetailsOD[4] == "Yes":
                lungs.set("Yes")
            if currentPatientDetailsOD[7] == "Yes": 
                pancreas.set("Yes")

        Button(tempWindow, 
               text='Save Data to Record', 
               bg='darkblue', 
               fg='white', 
               cursor='hand2', 
               command= lambda: getPatientValues(gender.get())).grid(row=18, column=1, columnspan=2)
        Button(tempWindow, 
               text='Exit', 
               bg='darkblue', 
               fg='white', 
               cursor='hand2', 
               command=tempWindow.destroy).grid(row=18, column=3, columnspan=2)

        updateValues(currentPatientDetails, currentPatientDetailsOD, currentPatientDetailsAF)
        tempWindow.mainloop()

    def searchUser():       
        def getValues():
            firstname = entryFirstname.get()
            lastname = entryLastname.get()
            dobDay = comboboxDOBDay.get()
            dobMonth = comboboxDOBMonth.get()
            dobYear = comboboxDOBYear.get()

            values = [firstname, lastname, dobDay, dobMonth, dobYear]

            return values

        values = getValues()
        
        firstname = values[0]
        lastname = values[1]
        dobDay = values[2]
        dobMonth = values[3]
        dobYear = values[4]
        
        dob = str(dobDay) + "/" + str(dobMonth) + "/" + str(dobYear)

        fullname = str(firstname) + " " + str(lastname)

        conn = sqlite3.connect('Patients.db')
        
        with conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM PatientDemo WHERE forename = ? and surname = ? and dateOfBirth = ?", (firstname, lastname, dob))

            result = cursor.fetchall()
            
            if result:
                tupleDetails2 = ""
                stringDetails2 = ""
                currentPatientDetails = []
                currentPatientDetailsOD = []
                currentPatientDetailsAF = []

                cursor.execute('SELECT * FROM PatientDemo WHERE forename = ? and surname =  ? and dateOfBirth = ?', (firstname, lastname, dob))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetails.append(detail)

                patientID = str(currentPatientDetails[0])

                cursor.execute('SELECT * FROM PatientOD WHERE patientID = ?', (patientID))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetailsOD.append(detail)

                cursor.execute('SELECT * FROM PatientAF WHERE patientID = ?', (patientID))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetailsAF.append(detail)

                ms.showinfo('Succesful!', 'The record of ' + fullname + ' has been loaded.', parent=tempWindow2)

                tempWindow2.destroy()
                mainWindow(currentPatientDetails, currentPatientDetailsOD, currentPatientDetailsAF)
            else:
                ms.showerror('Patient Not Found', 'No patients with these matching details have been found.')
                entryFirstname.delete(0, END)
                entryLastname.delete(0, END)
                comboboxDOBDay.current(0)
                comboboxDOBMonth.current(0)
                comboboxDOBYear.current(0)
       
    spacerLabel = Label(tempWindow2, 
                        text=" ")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=0, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=6, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=2, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=8, rowspan=9)

    labelFirstname = Label(tempWindow2, 
                        text="Patient Firstname: ",
                        font=("corbel bold", 10))
    labelFirstname.grid(row=1, column=1)
    entryFirstname = Entry(tempWindow2, 
                        textvar=firstname)
    entryFirstname.grid(row=1, column=3, columnspan=3, sticky=E+W)

    labelLastname = Label(tempWindow2, 
                        text="Patient Lastname: ",
                        font=("corbel bold", 10))
    labelLastname.grid(row=2, column=1)
    entryLastname = Entry(tempWindow2, 
                        textvar=lastname)
    entryLastname.grid(row=2, column=3, columnspan=3, sticky=E+W)

    labelDocType = Label(tempWindow2, 
                              text="Patient Date of Birth: ", 
                              font=("corbel bold", 10))
    labelDocType.grid(row=3, column=1)
    
    comboboxDOBDay = ttk.Combobox(tempWindow2, 
                                   textvariable=dobDay)
    comboboxDOBDay.grid(row=3, column=3, sticky=E+W)
    comboboxDOBDay.config(values = ('DD', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                                     '30', '31'), width=4)
    comboboxDOBDay.current([0])

    comboboxDOBMonth = ttk.Combobox(tempWindow2, 
                                   textvariable=dobMonth)
    comboboxDOBMonth.grid(row=3, column=4, sticky=E+W)
    comboboxDOBMonth.config(values = ('MM', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12'), width=4)
    comboboxDOBMonth.current([0])

    comboboxDOBYear = ttk.Combobox(tempWindow2, 
                                   textvariable=dobYear)
    comboboxDOBYear.grid(row=3, column=5, sticky=E+W)
    comboboxDOBYear.config(values = ('YYYY', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909',
                                     '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', 
                                     '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', 
                                     '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', 
                                     '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', 
                                     '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', 
                                     '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
                                     '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                                     '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', 
                                     '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                                     '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'), width=9)
    comboboxDOBYear.current([0])

    searchButton = Button(tempWindow2, 
                          text='Search', 
                          bg='darkblue', 
                          fg='white', 
                          command=searchUser).grid(row=2, column=7)

    spacerLabel = Label(tempWindow2, 
                        text=" ")
    spacerLabel.grid(row=4, column=0, columnspan=5)

    tempWindow2.mainloop()

# Create a new Patient Record #
# Status: BROKEN :(
def addPatient():
    tempWindow = Tk()
    tempWindow.geometry('700x450')
    tempWindow.title("Register a new Patient")

    center(tempWindow)

    patientTitle = StringVar()
    forename = StringVar()
    surname = StringVar()
    prevSurname = StringVar()
    dateOfBirth = StringVar()
    
    global gender
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

    def appendPatient(title, forename, surname, prevSurname, dob, genderNew, country, 
                      housenumber, street, postcode, county, contactNo, regType, oldGP, oldGPAddress, 
                      oldGPPostcode, hcn, personnelNum, enDate, diDate, organYNNew, kidneyNew, heartNew, 
                      lungsNew, liverNew, corneasNew, pancreasNew):
        conn = sqlite3.connect('Patients.db')
        
        with conn:
            cursor = conn.cursor()
        
        insertPatientDemo = '''INSERT INTO PatientDemo (patientID, patientTitle, forename, surname, prevSurname, dateOfBirth, 
                            gender, country, housenumber, street, postcode, county, contactnumber, regType, oldGP, oldGPAddress, 
                            oldGPPostcode, hcn) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''' 
        cursor.execute(insertPatientDemo, [(title), (forename), (surname), (prevSurname), (dob), (genderNew), (country), 
                                           (housenumber), (street), (postcode), (county), (contactNo), (regType), (oldGP), (oldGPAddress), 
                                           (oldGPPostcode), (hcn)])
        
        insertPatientAF = "INSERT INTO PatientAF (patientID, personnelNum, enDate, diDate) VALUES (NULL, ?, ?, ?)"
        cursor.execute(insertPatientAF, [(personnelNum), (enDate), (diDate)])
            
        cursor.execute('''CREATE TABLE IF NOT EXISTS PatientOD (patientID INTEGER PRIMARY KEY, organYN TEXT, kidney TEXT, 
                          heart TEXT, lungs TEXT, liver TEXT, corneas TEXT, pancreas TEXT)''')
        
        insertPatientOD = '''INSERT INTO PatientOD (patientID, organYN, kidney, heart, lungs, liver, corneas, pancreas) 
                             VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insertPatientOD, [(organYNNew), (kidneyNew), (heartNew), (lungsNew), (liverNew), (corneasNew), (pancreasNew)])
            
        conn.commit()

        again = ms.askyesno("Succesful!", "Would you like to register another patient?", parent=tempWindow)

        if again == True:
            clearWindow()
        else:
            tempWindow.destroy()

    def getPatientValues(genderNew):
        title = comboboxTitle.get()
        forename = entryForename.get()
        surname = entrySurname.get()
        prevSurname = entryPrevSurname.get()
        dob = entryDOB.get()
        country = comboboxCountry.get()
        housenumber = entryHousenumber.get()
        street = entryStreet.get()
        postcode = entryPostcode.get()
        county = entryCounty.get()
        contactNo = entryContactNo.get()
        regType = comboboxRegType.get()
        oldGP = entryOldGP.get()
        oldGPAddress = entryOldGPAddress.get()
        oldGPPostcode = entryOldGPPostcode.get()
        hcn = entryHCN.get()

        personnelNum = entryPersonnelNum.get()
        enDate = entryEnDate.get()
        diDate = entryDiDate.get()

        organYNNew = organYN.get()
        kidneyNew = kidney.get()
        heartNew = heart.get()
        liverNew = liver.get()
        corneasNew = corneas.get()
        lungsNew = lungs.get()
        pancreasNew = pancreas.get()
        
        appendPatient(title, forename, surname, prevSurname, dob, genderNew, country, 
                      housenumber, street, postcode, county, contactNo, regType, oldGP, oldGPAddress, 
                      oldGPPostcode, hcn, personnelNum, enDate, diDate, organYNNew, kidneyNew, heartNew, 
                      lungsNew, liverNew, corneasNew, pancreasNew)

    labelTitle = Label(tempWindow, 
                       text="Antrim Castle Surgery - Registration Application", 
                       font=("corbel bold", 14), 
                       anchor=N)
    labelTitle.grid(row=0, column=1, columnspan=6)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=1, column=0, columnspan=4)

    labelPatientTitle = Label(tempWindow, 
                              text="Title: ", 
                              font=("corbel", 10))
    labelPatientTitle.grid(row=2, column=0)
    comboboxTitle = ttk.Combobox(tempWindow, 
                                 textvariable=patientTitle)
    comboboxTitle.grid(row=2, column=1, columnspan=2)
    comboboxTitle.config(values = ('Please Select...', 'Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Rev', 'Prof', 'Sir', 'Other'), width=17)
    comboboxTitle.current([0])

    labelForename = Label(tempWindow, 
                          text="Forename(s): ", 
                          font=("corbel", 10))
    labelForename.grid(row=3, column=0)
    entryForename = Entry(tempWindow, 
                          textvar=forename)
    entryForename.grid(row=3, column=1, columnspan=2)

    labelSurname = Label(tempWindow, 
                         text="Surname: ", 
                         font=("corbel", 10))
    labelSurname.grid(row=4, column=0)
    entrySurname = Entry(tempWindow, 
                         textvar=surname)
    entrySurname.grid(row=4, column=1, columnspan=2)

    labelPrevSurname = Label(tempWindow, 
                             text="Previous Surname: ", 
                             font=("corbel", 10))
    labelPrevSurname.grid(row=5, column=0)
    entryPrevSurname = Entry(tempWindow, 
                             textvar=prevSurname)
    entryPrevSurname.grid(row=5, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=6, column=0, columnspan=4)

    labelDOB = Label(tempWindow, 
                     text="Date of Birth: ", 
                     font=("corbel", 10))
    labelDOB.grid(row=7, column=0)
    entryDOB = Entry(tempWindow, 
                     textvar=dateOfBirth)
    entryDOB.grid(row=7, column=1, columnspan=2)

    labelGender = Label(tempWindow, 
                        text="Gender: ", 
                        font=("corbel", 10))
    labelGender.grid(row=8, column=0)
    Radiobutton(tempWindow, 
                text="Male",
                variable=gender,
                value="Male").grid(row=8, column=1)
    Radiobutton(tempWindow,  
                text="Female",
                variable=gender,
                value="Female").grid(row=8, column=2)

    labelCountry = Label(tempWindow, 
                         text="Country of Birth: ", 
                         font=("corbel", 10))
    labelCountry.grid(row=9, column=0)
    comboboxCountry = ttk.Combobox(tempWindow, 
                                   textvariable=country)
    comboboxCountry.grid(row=9, column=1, columnspan=2)
    comboboxCountry.config(values = ('Please Select...',  'Australia', 'Belgium', 'Canada', 'Denmark', 'Egypt', 'France', 
                                     'Germany', 'Hungary', 'Ireland', 'Jamaica', 'Kenya', 'Lithuania', 'Macedonia', 'Norway', 
                                     'Oman', 'Poland', 'Quatar', 'Russia', 'Spain', 'Tanzania', 'United Kingdom', 'Venuzuala', 
                                     'Yugoslavia', 'Zambia'), width=17)
    comboboxCountry.current([0])

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=10, column=0, columnspan=4)

    labelHousenumber = Label(tempWindow, 
                             text="House Number: ", 
                             font=("corbel", 10))
    labelHousenumber.grid(row=11, column=0)
    entryHousenumber = Entry(tempWindow, 
                             textvar=housenumber)
    entryHousenumber.grid(row=11, column=1, columnspan=2)

    labelStreet = Label(tempWindow, 
                        text="Street: ", 
                        font=("corbel", 10))
    labelStreet.grid(row=12, column=0)
    entryStreet = Entry(tempWindow, 
                        textvar=street)
    entryStreet.grid(row=12, column=1, columnspan=2)

    labelPostcode = Label(tempWindow, 
                          text="Postcode: ", 
                          font=("corbel", 10))
    labelPostcode.grid(row=13, column=0)
    entryPostcode = Entry(tempWindow, 
                          textvar=postcode)
    entryPostcode.grid(row=13, column=1, columnspan=2)

    labelCounty = Label(tempWindow, 
                        text="County: ", 
                        font=("corbel", 10))
    labelCounty.grid(row=14, column=0)
    entryCounty = Entry(tempWindow, 
                        textvar=county)
    entryCounty.grid(row=14, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=15, column=0, columnspan=4)

    labelContactNo = Label(tempWindow, 
                           text="Contact Number: ", 
                           font=("corbel", 10))
    labelContactNo.grid(row=16, column=0)
    entryContactNo = Entry(tempWindow, 
                           textvar=contactnumber)
    entryContactNo.grid(row=16, column=1, columnspan=2)

    spacerLabel = Label(tempWindow, 
                        text=" ", 
                        width=4)
    spacerLabel.grid(row=0, column=3, rowspan=18)

    labelRegType = Label(tempWindow, 
                         text="Registration Type: ", 
                         font=("corbel", 10))
    labelRegType.grid(row=2, column=4)
    comboboxRegType = ttk.Combobox(tempWindow, 
                                   textvariable=regType)
    comboboxRegType.grid(row=2, column=5, columnspan=2)
    comboboxRegType.config(values = ('Please Select...', 'First ever registration with a GP Surgery', 
                                     'Moving GP Surgery'), width=17)
    comboboxRegType.current([0])

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=3, column=4, columnspan=3)

    labelOldGP = Label(tempWindow, 
                       text="Old GP: ", 
                       font=("corbel", 10))
    labelOldGP.grid(row=4, column=4)
    entryOldGP = Entry(tempWindow, 
                       textvar=oldGP)
    entryOldGP.grid(row=4, column=5, columnspan=2)

    labelOldGPAddress = Label(tempWindow, 
                              text="Address: ", 
                              font=("corbel", 10))
    labelOldGPAddress.grid(row=5, column=4)
    entryOldGPAddress = Entry(tempWindow, 
                              textvar=oldGPAddress)
    entryOldGPAddress.grid(row=5, column=5, columnspan=2)

    labelOldGPPostcode = Label(tempWindow, 
                               text="Postcode: ", 
                               font=("corbel", 10))
    labelOldGPPostcode.grid(row=6, column=4)
    entryOldGPPostcode = Entry(tempWindow, 
                               textvar=oldGPPostcode)
    entryOldGPPostcode.grid(row=6, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=7, column=4, columnspan=3)

    labelHCN = Label(tempWindow, 
                     text="Health & Care Number: ", 
                     font=("corbel", 10))
    labelHCN.grid(row=8, column=4)
    entryHCN = Entry(tempWindow, 
                     textvar=hcn)
    entryHCN.grid(row=8, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=9, column=4, columnspan=3)

    labelGender = Label(tempWindow, 
                        text="Complete the below if the patient is returning from the Armed Forces!", 
                        font=("corbel", 10))
    labelGender.grid(row=10, column=4, columnspan=4)

    labelPersonnelNum = Label(tempWindow, 
                              text="Personnel Number: ", 
                              font=("corbel", 10))
    labelPersonnelNum.grid(row=11, column=4)
    entryPersonnelNum = Entry(tempWindow, 
                              textvar=personnelNum)
    entryPersonnelNum.grid(row=11, column=5, columnspan=2)

    labelEnDate = Label(tempWindow, 
                        text="Enlistment Date: ", 
                        font=("corbel", 10))
    labelEnDate.grid(row=12, column=4)
    entryEnDate = Entry(tempWindow, 
                        textvar=enDate)
    entryEnDate.grid(row=12, column=5, columnspan=2)

    labelDiDate = Label(tempWindow, 
                        text="Discharge Date: ", 
                        font=("corbel", 10))
    labelDiDate.grid(row=13, column=4)
    entryDiDate = Entry(tempWindow, 
                        textvar=diDate)
    entryDiDate.grid(row=13, column=5, columnspan=2)

    spacerLabel = Label(tempWindow, 
                        text=" ")
    spacerLabel.grid(row=14, column=4, columnspan=3)

    labelOrganYN = Label(tempWindow, 
                         text="Has the Patient Consented to Organ Donation?", 
                         font=("corbel", 10))
    labelOrganYN.grid(row=15, column=4, columnspan=2)
    organButton1 = Radiobutton(tempWindow, 
                               text="Yes", 
                               variable=organYN,
                               cursor='hand2',
                               value=1).grid(row=15, column=6)
    organButton2 = Radiobutton(tempWindow, 
                               text="No", 
                               variable=organYN,
                               cursor='hand2',
                               value=0).grid(row=15, column=7)

    labelOrganType = Label(tempWindow, 
                           text="Organs to be donated: ", 
                           font=("corbel", 10))
    labelOrganType.grid(row=16, column=4)
    kidneyButton = Checkbutton(tempWindow,
                               cursor='hand2',
                               text="Kidneys", 
                               variable=kidney,
                               onvalue="Yes",
                               offvalue="No").grid(row=16, column=5, sticky='W')
    heartButton = Checkbutton(tempWindow,
                              cursor='hand2',
                              text="Heart", 
                              variable=heart,
                              onvalue="Yes",
                              offvalue="No").grid(row=16, column=6, sticky='W')
    liverButton = Checkbutton(tempWindow,
                              cursor='hand2',
                              text="Liver", 
                              variable=liver,
                              onvalue="Yes",
                              offvalue="No").grid(row=16, column=7, sticky='W')
    corneasButton = Checkbutton(tempWindow,
                                cursor='hand2',
                                text="Corneas", 
                                variable=corneas,
                                onvalue="Yes",
                                offvalue="No").grid(row=17, column=5, sticky='W')
    lungsButton = Checkbutton(tempWindow,
                              cursor='hand2',
                              text="Lungs",
                              variable=lungs,
                              onvalue="Yes",
                              offvalue="No").grid(row=17, column=6, sticky='W')
    pancreasButton = Checkbutton(tempWindow,
                                 cursor='hand2',
                                 text="Pancreas", 
                                 variable=pancreas,
                                 onvalue="Yes",
                                 offvalue="No").grid(row=17, column=7, sticky='W')

    Button(tempWindow, 
           text='Save Data to Record', 
           bg='darkblue', 
           fg='white', 
           cursor='hand2', 
           command= lambda: getPatientValues(gender.get())).grid(row=18, column=1, columnspan=2)

    Button(tempWindow, 
           text='Exit', 
           bg='darkblue', 
           fg='white', 
           cursor='hand2', 
           command=tempWindow.destroy).grid(row=18, column=3, columnspan=2)

    tempWindow.mainloop()

# View Item Stocks List #
# Status: FULLY WORKING
def viewStock():
    tempWindow = Tk()
    tempWindow.geometry('700x450')
    tempWindow.title("View Stock Lists")

    center(tempWindow)

    conn = sqlite3.connect('Stocks.db')
        
    with conn:
        cursor = conn.cursor()

        tupleDetails2 = ""
        stringDetails2 = ""
        stocksList = []

        cursor.execute("SELECT * FROM Stocks LIMIT 3;")

        tupleDetails2 = cursor.fetchall()

        for stringDetails2 in tupleDetails2:
            for detail in stringDetails2:
                stocksList.append(detail)

    print(stocksList)

    item1name = stocksList[1]
    item1type = stocksList[2]
    item1brand = stocksList[3]
    item1quantity = stocksList[4]

    item2name = stocksList[6]
    item2type = stocksList[7]
    item2brand = stocksList[8]
    item2quantity = stocksList[9]

    item3name = stocksList[11]
    item3type = stocksList[12]
    item3brand = stocksList[13]
    item3quantity = stocksList[14]

    # BEGIN FORMATTING #
    spacerLabel = Label(tempWindow, text=" ", width=5)
    spacerLabel.grid(row=0, column=0, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=0, column=1, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=0, column=2, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=0, column=3, rowspan=10)
        
    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=0, column=4, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=5)
    spacerLabel.grid(row=0, column=5, rowspan=10)

    i = 0

    while i < 10:
        spacerLabel = Label(tempWindow, text=" ", width=10)
        spacerLabel.grid(row=i, column=0, columnspan=6)
            
        i += 1
    # END FORMATTING #

    labelTitle = Label(tempWindow, 
                       text="Antrim Castle Surgery - Stock Lists", 
                       font=("corbel bold", 14))                 
    labelTitle.grid(row=1, column=1, columnspan=4)  

    labelHeading = Label(tempWindow, 
                        text="Item Name",
                        font=("corbel bold", 12))
    labelHeading.grid(row=3, column=1)

    labelHeading = Label(tempWindow, 
                        text="Item Type",
                        font=("corbel bold", 12))
    labelHeading.grid(row=3, column=2)

    labelHeading = Label(tempWindow, 
                        text="Brand Name",
                        font=("corbel bold", 12))
    labelHeading.grid(row=3, column=3)

    labelHeading = Label(tempWindow, 
                        text="Quantity",
                        font=("corbel bold", 12))
    labelHeading.grid(row=3, column=4)

    # ITEM 1

    labelItem1 = Label(tempWindow, 
                       text=item1name,
                       font=("corbel", 10))
    labelItem1.grid(row=4, column=1)

    labelItem1 = Label(tempWindow, 
                       text=item1type,
                       font=("corbel", 10))
    labelItem1.grid(row=4, column=2)

    labelItem1 = Label(tempWindow, 
                       text=item1brand,
                       font=("corbel", 10))
    labelItem1.grid(row=4, column=3)

    labelItem1 = Label(tempWindow, 
                       text=item1quantity,
                       font=("corbel", 10))
    labelItem1.grid(row=4, column=4)

    # ITEM 2

    labelItem2 = Label(tempWindow, 
                       text=item2name,
                       font=("corbel", 10))
    labelItem2.grid(row=5, column=1)

    labelItem2 = Label(tempWindow, 
                       text=item2type,
                       font=("corbel", 10))
    labelItem2.grid(row=5, column=2)

    labelItem2 = Label(tempWindow, 
                       text=item2brand,
                       font=("corbel", 10))
    labelItem2.grid(row=5, column=3)

    labelItem2 = Label(tempWindow, 
                       text=item2quantity,
                       font=("corbel", 10))
    labelItem2.grid(row=5, column=4)

    # ITEM 3

    labelItem3 = Label(tempWindow, 
                       text=item3name,
                       font=("corbel", 10))
    labelItem3.grid(row=6, column=1)

    labelItem3 = Label(tempWindow, 
                       text=item3type,
                       font=("corbel", 10))
    labelItem3.grid(row=6, column=2)

    labelItem3 = Label(tempWindow, 
                       text=item3brand,
                       font=("corbel", 10))
    labelItem3.grid(row=6, column=3)

    labelItem3 = Label(tempWindow, 
                       text=item3quantity,
                       font=("corbel", 10))
    labelItem3.grid(row=6, column=4)

    navButton = Button(tempWindow, 
                       text='Close', 
                       bg='#09425A', 
                       fg='#FFFFFF',
                       width=20,
                       command=tempWindow.destroy).grid(row=8, column=1)

    navButton = Button(tempWindow, 
                       text='Edit', 
                       bg='#09425A', 
                       fg='#FFFFFF',
                       width=20,
                       command=editStock).grid(row=8, column=4)

# Edit Item Stocks List #
# Status: BROKEN - not updating new quanitity values
def editStock():
    tempWindow = Tk()
    tempWindow.geometry('700x450')
    tempWindow.title("Add/Edit Stock Lists")

    center(tempWindow)

    itemType = StringVar()
    itemBrand = StringVar()
    itemName = StringVar()
    itemQuan = StringVar()

    def editCurrentStock():
        def showDetails():
            def updateStocks():
                itemQuan = entryQuan.get()

                conn = sqlite3.connect('Stocks.db')
        
                with conn:
                    cursor = conn.cursor()

                    cursor.execute("UPDATE Stocks SET quantity = ? WHERE itemID = ?", (itemQuan,), (itemID,))

                    conn.commit()

                ms.showinfo('Succesful!', 'The stock list has been updated.', parent=tempWindow)
            
            itemID = comboboxType.get()

            conn = sqlite3.connect('Stocks.db')
        
            with conn:
                cursor = conn.cursor()

                tupleDetails2 = ""
                stringDetails2 = ""
                currentStocks = []
            
                cursor.execute("SELECT quantity FROM Stocks WHERE itemID = ?", (itemID,))

                itemQuan = cursor.fetchall()

            labelQuan = Label(tempWindow, 
                               text="Quantity:",
                               font=("corbel bold", 12))
            labelQuan.grid(row=6, column=1)

            entryQuan = Entry(tempWindow, 
                              textvar=itemQuan)
            entryQuan.grid(row=6, column=3, sticky=E+W)

            navButton = Button(tempWindow, 
                               text='Update', 
                               bg='#09425A', 
                               fg='#FFFFFF',
                               width=20,
                               command=updateStocks).grid(row=8, column=3)

        labelName = Label(tempWindow, 
                          text="Item Name:",
                          font=("corbel bold", 12))
        labelName.grid(row=3, column=1)

        conn = sqlite3.connect('Stocks.db')
        
        with conn:
            cursor = conn.cursor()

            tupleDetails2 = ""
            stringDetails2 = ""
            currentStocks = []
            
            cursor.execute("SELECT * FROM Stocks LIMIT 5;")

            tupleDetails2 = cursor.fetchall()

            for stringDetails2 in tupleDetails2:
                for detail in stringDetails2:
                    currentStocks.append(detail)

        item1 = currentStocks[1]
        item2 = currentStocks[6]
        item3 = currentStocks[11]
        item4 = currentStocks[16]
        item5 = currentStocks[21]

        comboboxType = ttk.Combobox(tempWindow, 
                                    textvariable=itemType)
        comboboxType.grid(row=3, column=3, sticky=E+W)
        comboboxType.config(values = ('Please Select...', item1, item2, item3, item4, item5), width=4)
        comboboxType.current([0])

        navButton = Button(tempWindow, 
                           text='Load Selection', 
                           bg='#09425A', 
                           fg='#FFFFFF',
                           width=20,
                           command=showDetails).grid(row=4, column=3)

    def addNewStock():
        def insertStocks():
            itemName = entryName.get()
            itemType = comboboxType.get()
            itemBrand = entryBrand.get()
            itemQuan = entryBrand.get()

            conn = sqlite3.connect('Stocks.db')
        
            with conn:
                cursor = conn.cursor()
                               
                insertStock = '''INSERT INTO Stocks (itemID, name, category, brand, quantity) 
                                 VALUES (NULL, ?, ?, ?, ?)'''
                cursor.execute(insertStock,[(itemName), (itemType), (itemBrand), (itemQuan)])

                conn.commit()

            ms.showinfo('Succesful!', 'The stock list has been updated.', parent=tempWindow)

        labelName = Label(tempWindow, 
                           text="Item Name:",
                           font=("corbel bold", 12))
        labelName.grid(row=3, column=1)

        labelType = Label(tempWindow, 
                           text="Item Type:",
                           font=("corbel bold", 12))
        labelType.grid(row=4, column=1)

        labelBrand = Label(tempWindow, 
                           text="Brand Name:",
                           font=("corbel bold", 12))
        labelBrand.grid(row=5, column=1)

        labelQuan = Label(tempWindow, 
                           text="Quantity:",
                           font=("corbel bold", 12))
        labelQuan.grid(row=6, column=1)

        entryName = Entry(tempWindow, 
                          textvar=itemName)
        entryName.grid(row=3, column=3, sticky=E+W)
    
        comboboxType = ttk.Combobox(tempWindow, 
                                    textvariable=itemType)
        comboboxType.grid(row=4, column=3, sticky=E+W)
        comboboxType.config(values = ('Please Select...', 'Medication', 'Dressings', 'Creams', 'Devices'), width=4)
        comboboxType.current([0])

        entryBrand = Entry(tempWindow, 
                          textvar=itemBrand)
        entryBrand.grid(row=5, column=3, sticky=E+W)

        entryQuan = Entry(tempWindow, 
                          textvar=itemQuan)
        entryQuan.grid(row=6, column=3, sticky=E+W)

        navButton = Button(tempWindow, 
                           text='Save', 
                           bg='#09425A', 
                           fg='#FFFFFF',
                           width=20,
                           command=insertStocks).grid(row=8, column=3)

    # BEGIN FORMATTING #
    spacerLabel = Label(tempWindow, text=" ", width=5)
    spacerLabel.grid(row=0, column=0, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=0, column=1, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=5)
    spacerLabel.grid(row=0, column=2, rowspan=10)

    spacerLabel = Label(tempWindow, text=" ", width=20)
    spacerLabel.grid(row=0, column=3, rowspan=10)
        
    spacerLabel = Label(tempWindow, text=" ", width=5)
    spacerLabel.grid(row=0, column=4, rowspan=10)

    i = 0

    while i < 10:
        spacerLabel = Label(tempWindow, text=" ", width=10)
        spacerLabel.grid(row=i, column=0, columnspan=5)
            
        i += 1
    # END FORMATTING # 

    navButton = Button(tempWindow, 
                       text='Add New', 
                       bg='#09425A', 
                       fg='#FFFFFF',
                       width=20,
                       command=addNewStock).grid(row=1, column=1)

    navButton = Button(tempWindow, 
                       text='Edit', 
                       bg='#09425A', 
                       fg='#FFFFFF',
                       width=20,
                       command=editCurrentStock).grid(row=1, column=3)

# Begin a new Consultation #
# Status: BROKEN - does not save data to database
def newCons():
    searchTerm = StringVar()
    docType = StringVar()
    dobDay = StringVar()
    dobMonth = StringVar()
    dobYear = StringVar()
    firstname = StringVar()
    lastname = StringVar()

    tempWindow2 = Tk()
    tempWindow2.geometry('460x140')
    tempWindow2.title("Select Patient Record")

    center(tempWindow2)

    def searchUser():       
        def getValues():
            firstname = entryFirstname.get()
            lastname = entryLastname.get()
            dobDay = comboboxDOBDay.get()
            dobMonth = comboboxDOBMonth.get()
            dobYear = comboboxDOBYear.get()

            values = [firstname, lastname, dobDay, dobMonth, dobYear]

            return values

        values = getValues()
        
        firstname = values[0]
        lastname = values[1]
        dobDay = values[2]
        dobMonth = values[3]
        dobYear = values[4]
        
        dob = str(dobDay) + "/" + str(dobMonth) + "/" + str(dobYear)

        fullname = str(firstname) + " " + str(lastname)

        conn = sqlite3.connect('Patients.db')
        
        with conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM PatientDemo WHERE forename = ? and surname = ? and dateOfBirth = ?", (firstname, lastname, dob))

            result = cursor.fetchall()
            
            if result:
                tupleDetails2 = ""
                stringDetails2 = ""
                currentPatientDetails = []

                cursor.execute('SELECT * FROM PatientDemo WHERE forename = ? and surname =  ? and dateOfBirth = ?', (firstname, lastname, dob))
            
                tupleDetails2 = cursor.fetchall()

                for stringDetails2 in tupleDetails2:
                    for detail in stringDetails2:
                        currentPatientDetails.append(detail)

                ms.showinfo('Succesful!', 'The record of ' + fullname + ' has been loaded.', parent=tempWindow2)

                tempWindow2.destroy()
                dataEntry(currentPatientDetails)
            else:
                ms.showerror('Patient Not Found', 'No patients with these matching details have been found.')
                entryFirstname.delete(0, END)
                entryLastname.delete(0, END)
                comboboxDOBDay.current(0)
                comboboxDOBMonth.current(0)
                comboboxDOBYear.current(0)

    spacerLabel = Label(tempWindow2, 
                        text=" ")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=0, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=6, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=2, rowspan=9)

    spacerLabel = Label(tempWindow2, 
                        text=" ",
                        width=4)
    spacerLabel.grid(row=0, column=8, rowspan=9)

    labelFirstname = Label(tempWindow2, 
                        text="Patient Firstname: ",
                        font=("corbel bold", 10))
    labelFirstname.grid(row=1, column=1)
    entryFirstname = Entry(tempWindow2, 
                        textvar=firstname)
    entryFirstname.grid(row=1, column=3, columnspan=3, sticky=E+W)

    labelLastname = Label(tempWindow2, 
                        text="Patient Lastname: ",
                        font=("corbel bold", 10))
    labelLastname.grid(row=2, column=1)
    entryLastname = Entry(tempWindow2, 
                        textvar=lastname)
    entryLastname.grid(row=2, column=3, columnspan=3, sticky=E+W)

    labelDocType = Label(tempWindow2, 
                              text="Patient Date of Birth: ", 
                              font=("corbel bold", 10))
    labelDocType.grid(row=3, column=1)
    
    comboboxDOBDay = ttk.Combobox(tempWindow2, 
                                   textvariable=dobDay)
    comboboxDOBDay.grid(row=3, column=3, sticky=E+W)
    comboboxDOBDay.config(values = ('DD', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12', '13', '14',
                                     '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                                     '30', '31'), width=4)
    comboboxDOBDay.current([0])

    comboboxDOBMonth = ttk.Combobox(tempWindow2, 
                                   textvariable=dobMonth)
    comboboxDOBMonth.grid(row=3, column=4, sticky=E+W)
    comboboxDOBMonth.config(values = ('MM', '01', '02', '03', '04', '05', '05', '07', '08', '09', '10', '11', '12'), width=4)
    comboboxDOBMonth.current([0])

    comboboxDOBYear = ttk.Combobox(tempWindow2, 
                                   textvariable=dobYear)
    comboboxDOBYear.grid(row=3, column=5, sticky=E+W)
    comboboxDOBYear.config(values = ('YYYY', '1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909',
                                     '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', 
                                     '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', 
                                     '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', 
                                     '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', 
                                     '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', 
                                     '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975',
                                     '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
                                     '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', 
                                     '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
                                     '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'), width=9)
    comboboxDOBYear.current([0])

    searchButton = Button(tempWindow2, 
                          text='Search', 
                          bg='darkblue', 
                          fg='white', 
                          command=searchUser).grid(row=2, column=7)

    spacerLabel = Label(tempWindow2, 
                        text=" ")
    spacerLabel.grid(row=4, column=0, columnspan=5)

    def dataEntry(currentPatientDetails):
        tempWindow = Tk()
        tempWindow.geometry('740x670+300+20')
        tempWindow.title("Antrim Castle Surgery - Medical Informations System")

        center(tempWindow)

        def saveCons(complaint, examination, history, treatment, diagnosis, comments):
            currentDT = datetime.datetime.now()

            currentY = currentDT.year
            currentM = currentDT.month
            currentD = currentDT.day
            currentH = currentDT.hour
            currentM = currentDT.minute

            currentDate = str(currentD) + "/" + str(currentM) + "/" + str(currentY)
            currentTime = str(currentH) + ":" + str(currentM)

            patientID = currentPatientDetails[0]
            userID = userDetails[0]

            with sqlite3.connect('Patients.db') as patientsDB:
                cursorCons = patientsDB.cursor()
       
                insertCons = '''INSERT INTO PatientCons (consultationID, patientID, userID, time, date, complaint, examination, history, treatment, diagnosis, comments) 
                                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                cursorCons.execute(insertUser,[(patientID), (userID), (currentTime), (currentDate), (complaint), (examination), (history), (treatment), (diagnosis), (comments)])

                patientsDB.commit()

                again = ms.askyesno("Succesful!", "Would you like to create another user?", parent=tempWindow)

                if again == True:
                    clearWindow()
                else:
                    tempWindow.destroy()

        def getValues():
            complaint = entryPC.get('1.0', 'end')
            examination = entryOE.get('1.0', 'end')
            history = entryHX.get('1.0', 'end')
            treatment = entryPX.get('1.0', 'end')
            diagnosis = entryDX.get('1.0', 'end')
            comments = entryCom.get('1.0', 'end')

            saveCons(complaint, examination, history, treatment, diagnosis, comments)

        def delCons():
            tempWindow.destroy()

        def viewDetails(currentPatientDetails):
            print("View Details Function Called.")

        searchTerm = StringVar()
        scrollbar1 = Scrollbar(tempWindow)
        scrollbar2 = Scrollbar(tempWindow)
        scrollbar3 = Scrollbar(tempWindow)
        scrollbar4 = Scrollbar(tempWindow)
        scrollbar5 = Scrollbar(tempWindow)

        # Define Columns #
        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=2)
        spacerLabel.grid(row=0, column=0)
        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=30)
        spacerLabel.grid(row=0, column=1)
        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=30)
        spacerLabel.grid(row=0, column=2)
        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=30)
        spacerLabel.grid(row=0, column=3)
        spacerLabel = Label(tempWindow, 
                            text=" ", 
                            width=2)
        spacerLabel.grid(row=0, column=4)
        # END.

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=0, column=0, columnspan=5)

        patientTitle = currentPatientDetails[1]
        patientFirstName = currentPatientDetails[2]
        patientLastName = currentPatientDetails[3]
        patientDOB = currentPatientDetails[5]
        patientHCN = currentPatientDetails[17]

        textData = (patientTitle + " " + patientFirstName + " " + patientLastName + ", Date of Birth: " + patientDOB + ", Health & Care Number: " + patientHCN)

        spacerLabel = Label(tempWindow, 
                            text="Patient Selected: ",
                            font=("corbel bold", 10))
        spacerLabel.grid(row=1, column=1, sticky=E)

        spacerLabel = Label(tempWindow, 
                            text=textData)
        spacerLabel.grid(row=1, column=2, columnspan=3, sticky=W)

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=2, column=0, columnspan=4)

        labelPC = Label(tempWindow, 
                        text="Presenting Complaint (PC)", 
                        font=("corbel bold", 10))
        labelPC.grid(row=3, column=1, columnspan=3)
        entryPC = Text(tempWindow, 
                       height=3, 
                       width=86)
        entryPC.grid(row=4, column=1, columnspan=3)
        #entryPC.config(yscrollcommand=scrollbar1.set)
        #scrollbar1.grid(row=4, column=4, sticky=N+S)
        #scrollbar1.config(command=entryPC.yview)

        entryPC.insert('1.0', 'N/A')

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=5, column=0, columnspan=4)

        labelOE = Label(tempWindow, 
                        text="On Examination (O/E)", 
                        font=("corbel bold", 10))
        labelOE.grid(row=6, column=1, columnspan=3)
        entryOE = Text(tempWindow, 
                       height=3, 
                       width=86)
        entryOE.grid(row=7, column=1, columnspan=3)
        #entryOE.config(yscrollcommand=scrollbar2.set)
        #scrollbar2.grid(row=7, column=4, sticky=N+S)
        #scrollbar2.config(command=entryOE.yview)

        entryOE.insert('1.0', 'N/A')

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=8, column=0, columnspan=4)

        labelHX = Label(tempWindow, 
                        text="History - Medical & Social (Hx)", 
                        font=("corbel bold", 10))
        labelHX.grid(row=9, column=1, columnspan=3)
        entryHX = Text(tempWindow, 
                       height=3, 
                       width=86)
        entryHX.grid(row=10, column=1, columnspan=3)
        #entryHX.config(yscrollcommand=scrollbar3.set)
        #scrollbar3.grid(row=10, column=4, sticky=N+S)
        #scrollbar3.config(command=entryHX.yview)

        entryHX.insert('1.0', 'N/A')

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=11, column=0, columnspan=4)

        labelPX = Label(tempWindow, 
                        text="Treatment Plan/Medications (Px)", 
                        font=("corbel bold", 10))
        labelPX.grid(row=12, column=1, columnspan=3)
        entryPX = Text(tempWindow, 
                       height=3, 
                       width=86)
        entryPX.grid(row=13, column=1, columnspan=3)
        #entryPX.config(yscrollcommand=scrollbar4.set)
        #scrollbar4.grid(row=13, column=4, sticky=N+S)
        #scrollbar4.config(command=entryPX.yview)

        entryPX.insert('1.0', 'N/A')

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=14, column=0, columnspan=4)

        labelDX = Label(tempWindow, 
                        text="Diagnosis (Dx)", 
                        font=("corbel bold", 10))
        labelDX.grid(row=15, column=1, columnspan=3)
        entryDX = Text(tempWindow, 
                       height=1, 
                       width=86)
        entryDX.grid(row=16, column=1, columnspan=3)

        entryDX.insert('1.0', 'N/A')

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=17, column=0, columnspan=4)

        labelCom = Label(tempWindow, 
                         text="Comments", 
                         font=("corbel bold", 10))
        labelCom.grid(row=18, column=1, columnspan=3)
        entryCom = Text(tempWindow, 
                        height=3, 
                        width=86)
        entryCom.grid(row=19, column=1, columnspan=3)
        #entryCom.config(yscrollcommand=scrollbar5.set)
        #scrollbar5.grid(row=19, column=4, sticky=N+S)
        #scrollbar5.config(command=entryCom.yview)

        entryCom.insert('1.0', 'N/A')

        spacerLabel = Label(tempWindow, 
                            text=" ")
        spacerLabel.grid(row=20, column=0, columnspan=4)

        saveCons = Button(tempWindow, 
                          text='Save Consultation', 
                          bg='darkblue', 
                          fg='white', 
                          command=getValues).grid(row=21, column=1)
        delCons = Button(tempWindow, 
                         text='Delete Consultation', 
                         bg='darkblue', 
                         fg='white', 
                         command=delCons).grid(row=21, column=2)
        viewDetails = Button(tempWindow, 
                             text='View Patient Details', 
                             bg='darkblue', 
                             fg='white', 
                             command= lambda: viewDetails(currentPatientDetails)).grid(row=21, column=3)

        tempWindow.mainloop()

# Search Consultations #
# Status: NOT YET IMPLEMENTED (copy code from search patients)
def searchCons():
    print("Search Consultations Function Called.")

# Create a New Appointment #
# Status: NOT YET IMPLEMENTED
def newApp():
    print("Create a New Appointment Function Called.")

# Edit Patient Appointments #
# Status: NOT YET IMPLEMENTED
def editApp():
    print("Edit Appointment Function Called.")

# Reset Password #
# Status: FULLY WORKING
def resetPassword():
    tempWindow2 = Tk()
    tempWindow2.geometry('350x200')
    tempWindow2.title("Password Reset Widget")
    tempWindow2.config(bg="white")

    center(tempWindow2)

    currentUsername = StringVar()

    def getEmail():
        conn = sqlite3.connect('Users.db') # Establish the database connection by designating which db file to connect to

        with conn:                         # Use the databse connection established to carry out the following
            userEmail = StringVar()     # Set the datatype for the coming fetch statement

            cursorUser = conn.cursor()

            cursorUser.execute('SELECT email FROM UserAccounts WHERE username = ?', (entryUsername.get(),))
            # ^ since the user has been authenticated above, the username is now used (as it is a
            # unique value - to pull all of the user details and save them to a list

            userEmail = cursorUser.fetchall()    
            # The user details are at first returned as a tuple in "tupleDetails"

            if userEmail:
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                
                smtpObj.ehlo()

                smtpObj.starttls()

                smtpObj.login('dchestnutt4@gmail.com', 'victoriacricket')

                subject = 'Temporary Password'
                mainMessage = 'Your temporary password is: AntrimCastleSurgery'

                emailBody="""Subject:%s 

                          %s
                          """ %(subject,mainMessage)

                smtpObj.sendmail('dchestnutt4@gmail.com', userEmail, emailBody)

                smtpObj.quit()

                with sqlite3.connect('Users.db') as usersDB:
                    cursorUser = usersDB.cursor()
                    newPassword = 'AntrimCastleSurgery'

                    updateUser = "UPDATE UserAccounts SET password = ? WHERE username = ?"
                    updateValues = (newPassword), (entryUsername.get())

                    cursorUser.execute(updateUser, updateValues)

                    usersDB.commit()

                    again = ms.showinfo("Succesful!", "Your password has been changed. Please check your email.", parent=tempWindow2)

                tempWindow2.destroy()    # Close this window
            else:                
                ms.showerror('User Not Found', 'Username not recognised. Please try again.') 
                # ^ Show error message if no user account has been found with that username
                # and password combination
                entryUsername.delete(0, END) # Clear entry fields for a second attempt
                entryPassword.delete(0, END)

    username = StringVar()

    spacerLabel = Label(tempWindow2, 
                        text=" ", 
                        bg="white")
    spacerLabel.grid(row=0, column=0, columnspan=2)

    spacerLabel = Label(tempWindow2, 
                        text="Please enter your username below.",
                        font=("corbel bold", 12),
                        bg="white")
    spacerLabel.grid(row=1, column=0, columnspan=2)

    spacerLabel = Label(tempWindow2, 
                        text="An email will be sent with a temporary password.",
                        font=("corbel bold", 12),
                        bg="white")
    spacerLabel.grid(row=2, column=0, columnspan=2)

    spacerLabel = Label(tempWindow2, 
                        text=" ", 
                        bg="white")
    spacerLabel.grid(row=3, column=0, columnspan=2)

    labelUsername = Label(tempWindow2, 
                          text="Username: ", 
                          font=("corbel", 10),
                          bg="white",
                          padx=5)                                   
    labelUsername.grid(row=4, column=0, sticky=E)
    entryUsername = Entry(tempWindow2, 
                          textvar=currentUsername)            
    entryUsername.grid(row=4, column=1, sticky=W)

    spacerLabel = Label(tempWindow2, 
                        text=" ", 
                        bg="white")
    spacerLabel.grid(row=5, column=0, columnspan=2)

    logedIn = Button(tempWindow2, 
                     text='Send Temporary Password', 
                     bg='darkblue', 
                     fg='white',
                     width=20,
                     command=getEmail).grid(row=6, column=0, columnspan=2)

    spacerLabel = Label(tempWindow2, 
                        text=" ", 
                        bg="white")
    spacerLabel.grid(row=7, column=0, columnspan=2)

# Create the main Program Window #
# Status: FULLY WORKING
def mainWindow():
    window = Tk()
    window.geometry('1366x768')
    window.title("Antrim Castle Surgery - Medical Informations System") 
    window.config(bg="#FFFFFF")
    window.iconbitmap('surgeryWindowLogo.ico')

    center(window)

    def logOff():
        window.destroy()
        os.system("application.py")

    def changeUser():
        window.destroy()
        os.system("application.py")

    menu = Menu(window)

    dropdownUsers = Menu(menu) 

    menu.config(bg='#07C9BB')

    dropdownUsers.add_command(label='Create New User', 
                              command=createUser) 
    dropdownUsers.add_command(label='Edit Existing User', 
                              command=editUser) 
    dropdownUsers.add_command(label='Change User', 
                              command=changeUser)
    dropdownUsers.add_command(label='Log-Off', 
                              command=logOff)

    menu.add_cascade(label='User Accounts', 
                     menu=dropdownUsers)

    dropdownPatients = Menu(menu) 

    dropdownPatients.add_command(label='Search Patients', 
                                 command=searchPatient) 
    dropdownPatients.add_command(label='Edit Patient Details', 
                                 command=editPatient) 
    dropdownPatients.add_command(label='Register a new Patient', 
                                 command=addPatient)
    dropdownPatients.add_command(label='Add new Medical Data', 
                                 command=newMed)

    menu.add_cascade(label='Patient Records', 
                     menu=dropdownPatients)

    dropdownDocuments = Menu(menu) 
 
    dropdownDocuments.add_command(label='Create a New Document', 
                                  command=newDoc) 

    menu.add_cascade(label='Documents', 
                     menu=dropdownDocuments)

    dropdownOther = Menu(menu) 

    dropdownOther.add_command(label='View Item Stock List', 
                              command=viewStock) 
    dropdownOther.add_command(label='Edit Item Stock List', 
                              command=editStock) 

    menu.add_cascade(label='Other', 
                     menu=dropdownOther)

    dropdownConsultations = Menu(menu) 

    dropdownConsultations.add_command(label='Begin a new Consultation', 
                                      command=newCons) 
    dropdownConsultations.add_command(label='Search Consultations', 
                                      command=searchCons) 

    menu.add_cascade(label='Consultations', 
                     menu=dropdownConsultations)
    
    dropdownAppointments = Menu(menu) 

    dropdownAppointments.add_command(label='Book a new Appointment', 
                                     command=newApp) 
    dropdownAppointments.add_command(label='Change Appointments', 
                                     command=editApp) 

    menu.add_cascade(label='Appointments', 
                     menu=dropdownAppointments)

    window.config(menu=menu)

    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=0, columnspan=9)

    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, bg="#FFFFFF")
    spacerLabel.grid(row=0, column=0, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=1, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=2, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=3, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=4, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=5, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=6, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=7, rowspan=20)
    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=0, column=8, rowspan=20)

    labelInstructions = Label(window, 
                              text="Options Menu",
                              font=("Helvetica", 14, "bold"),
                              relief=RIDGE,
                              bg="#FFFFFF")                 
    labelInstructions.grid(row=3, column=0, columnspan=2)

    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=4, column=0, columnspan=2)

    Button(window, 
           text='Search Patient Records', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=searchPatient).grid(row=5, column=0, columnspan=2)
    Button(window, 
           text='Register New Patients', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=addPatient).grid(row=6, column=0, columnspan=2)
    Button(window, 
           text='Edit Patient Records', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=editPatient).grid(row=7, column=0, columnspan=2)
    Button(window, 
           text='View Item Stock List', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=viewStock).grid(row=8, column=0, columnspan=2)
    Button(window, 
           text='Edit Item Stock List', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=editStock).grid(row=9, column=0, columnspan=2)
    Button(window, 
           text='Add New Medical Data', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=newMed).grid(row=10, column=0, columnspan=2)
    Button(window, 
           text='Begin a new Consultation', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=newCons).grid(row=11, column=0, columnspan=2)
    Button(window, 
           text='Search Consultations', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=searchCons).grid(row=12, column=0, columnspan=2)
    Button(window, 
           text='Create a New Document', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=newDoc).grid(row=13, column=0, columnspan=2)
    Button(window, 
           text='Book a new Appointment', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=newApp).grid(row=14, column=0, columnspan=2)
    Button(window, 
           text='Change Appointments', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=editApp).grid(row=15, column=0, columnspan=2)

    labelInstructions = Label(window, 
                              text="System Options",
                              font=("Helvetica", 14, "bold"),
                              relief=RIDGE,
                              bg="#FFFFFF")                                  
    labelInstructions.grid(row=3, column=7, columnspan=2)

    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=4, column=7, columnspan=2)

    Button(window, 
           text='Create New Users', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=createUser).grid(row=5, column=7, columnspan=2)
    Button(window, 
           text='Edit User Accounts', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=editUser).grid(row=6, column=7, columnspan=2)
    Button(window, 
           text='Change Current User', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', command=changeUser).grid(row=7, column=7, columnspan=2)
    Button(window, 
           text='Log-Off', 
           width=20, 
           bg='#09425A', 
           fg='#FFFFFF', 
           command=logOff).grid(row=8, column=7, columnspan=2)

    title = userDetails[3]
    firstname = userDetails[4]
    surname = userDetails[5]
   
    welcomeText = "Welcome back " + title + " " + firstname + " " + surname + "!"

    photoLogo = PhotoImage(file="surgeryLogoSmall.png")
    logo = Label(image=photoLogo)
    logo.grid(row=1, rowspan=2, column=2, columnspan=5, sticky=N)

    spacerLabel = Label(window, 
                        text=" ", 
                        width=20, 
                        bg="#FFFFFF")
    spacerLabel.grid(row=5, column=0, columnspan=9)

    labelHello = Label(window, 
                       text=welcomeText,
                       font=("Helvetica", 14, "bold italic"),
                       bg="#FFFFFF")
    labelHello.grid(row=4, column=3, columnspan=3, rowspan=2)

    window.mainloop()

# Check User Details for Validity #
# Status: FULLY WORKING
def checkUser():
    conn = sqlite3.connect('Users.db') # Establish the database connection by designating which db file to connect to

    with conn:                         # Use the databse connection established to carry out the following
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM UserAccounts WHERE username = ? and password = ?", (username.get(), password.get()))
        # ^ will take the user-entered username and password and find a user-record where both the username and password match

        result = cursor.fetchall()  # Get all values returned from the database SELECT query

        if result:
            tupleDetails = StringVar() # Set the datatype for the coming fetch statement

            cursorUser = conn.cursor()

            cursorUser.execute('SELECT * FROM UserAccounts WHERE username = ?', (username.get(),))
            # ^ since the user has been authenticated above, the username is now used (as it is a
            # unique value - to pull all of the user details and save them to a list

            tupleDetails = cursorUser.fetchall()    

            # The user details are at first returned as a tuple in "tupleDetails"

            for stringDetails in tupleDetails:      # Add each value pulled from the database to
                for detail in stringDetails:        # a global list to allow them to be used later
                    userDetails.append(detail)      # in the program when needed

            tempWindow.destroy()    # Close this window
            mainWindow()            # Re-open the main menu
        else:               # If no user details found - 
            ms.showerror('User Not Found', 'Username or Password not Found.') 
            # ^ Show error message if no user account has been found with that username
            # and password combination
            entryUsername.delete(0, END) # Clear entry fields for a second attempt
            entryPassword.delete(0, END)

ignoreThis = 1


# ***** Log-in Window Generation ***** #

# Note: This code below serves as the first and main program loop. The window generated
#       will allow the user to authenticate themselves within the system and allows for
#       access levels and access rights to be implemented. It also serves as the root of
#       all following (tKinter) window loops.
#
# This window will be used to initialise our program by asking the user for their
# login details and checking this against the details which are stored in our
# "Users" database. This allows for us to ensure confidentiality & security

tempWindow = Tk()
tempWindow.geometry('500x300+580+250')
tempWindow.title("Antrim Castle Surgery - Medical Informations System")
tempWindow.config(bg="white")

center(tempWindow)

username = StringVar()
password = StringVar()

photoLogo = PhotoImage(file="surgeryLogoSmall.png")
logo = Label(image=photoLogo)
logo.grid(row=0, column=0, columnspan=2, rowspan=2)

spacerLabel = Label(tempWindow, 
                    text=" ", 
                    bg="white")
spacerLabel.grid(row=2, column=0, columnspan=2)

spacerLabel = Label(tempWindow, 
                    text="Welcome! Please login to continue.",
                    font=("corbel bold", 12),
                    bg="white")
spacerLabel.grid(row=3, column=0, columnspan=2)

spacerLabel = Label(tempWindow, 
                    text=" ", 
                    bg="white")
spacerLabel.grid(row=4, column=0, columnspan=2)

labelUsername = Label(tempWindow, 
                      text="Username: ", 
                      font=("corbel", 10),
                      bg="white",
                      padx=5)                                   
labelUsername.grid(row=5, column=0, sticky=E)
entryUsername = Entry(tempWindow, 
                      textvar=username)            
entryUsername.grid(row=5, column=1, sticky=W)

labelPassword = Label(tempWindow, 
                      text="Password: ", 
                      font=("corbel", 10),
                      bg="white",
                      padx=5)                                  
labelPassword.grid(row=6, column=0, sticky=E)
entryPassword = Entry(tempWindow, 
                      textvar=password, 
                      show = '•') 
entryPassword.grid(row=6, column=1, sticky=W)

spacerLabel = Label(tempWindow, 
                    text=" ", 
                    bg="white")
spacerLabel.grid(row=7, column=0, columnspan=2)

logedIn = Button(tempWindow, 
                 text='Log-In', 
                 bg='darkblue', 
                 fg='white',
                 width=20,
                 command=checkUser).grid(row=8, column=0, columnspan=2)

spacerLabel = Label(tempWindow, 
                    text=" ", 
                    bg="white")
spacerLabel.grid(row=9, column=0, columnspan=2)

passwordReset = Button(tempWindow, 
                       text='Forgot your password?', 
                       bg='#09425A', 
                       fg='#FFFFFF',
                       width=20,
                       command=resetPassword).grid(row=10, column=0, columnspan=2)

tempWindow.mainloop()

## EOF ##