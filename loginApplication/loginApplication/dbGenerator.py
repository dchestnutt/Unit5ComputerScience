######################################
## WJEC GCE Computer Science Unit 5 ##
## Daniel Chestnutt - 71401 - 2127  ##
######################################

## This code will be used to generate the blank databases.
## It will also fill the database with an administrator account and
## some example patient details to allow the system to function for
## testing purposes.

# ***** Importing Modules ***** #
import sqlite3


## Patients.db Creation
conn1 = sqlite3.connect('Patients.db')

with conn1:
    cursor1 = conn1.cursor()

    ## PatientDemo Entity
    cursor1.execute('''CREATE TABLE IF NOT EXISTS PatientDemo (patientID INTEGER PRIMARY KEY, patientTitle TEXT, 
                       forename TEXT , surname TEXT, prevSurname TEXT, dateOfBirth TEXT, gender TEXT, country TEXT, 
                       housenumber TEXT, street TEXT, postcode TEXT, county TEXT, contactnumber TEXT, regType TEXT, 
                       oldGP TEXT, oldGPAddress TEXT, oldGPPostcode TEXT, hcn TEXT)''')

    ## Pushing Example Patients to the PatientDemo Entity
    cursor1.execute('''INSERT INTO PatientDemo (patientID, patientTitle, forename, surname, prevSurname, dateOfBirth, 
                       gender, country, housenumber, street, postcode, county, contactnumber, regType, oldGP, oldGPAddress, 
                       oldGPPostcode, hcn) 
                       VALUES (NULL, 'Miss', 'Zoe', 'Davies', NULL, '13/03/2001', 'Female', 'United Kingdom', '29', 'Meadowlands', 
                       'BT41 4EU', 'Antrim', '07923030234', 'First Ever Registration with a GP Surgery', NULL, NULL, NULL, '320 300 2860')''')

    ## PatientAF Entity
    cursor1.execute('''CREATE TABLE IF NOT EXISTS PatientAF (patientID INTEGER PRIMARY KEY, personnelNum TEXT, 
                       enDate TEXT, diDate TEXT)''')

    ## PatientOD Entity
    cursor1.execute('''CREATE TABLE IF NOT EXISTS PatientOD (patientID INTEGER PRIMARY KEY, organYN TEXT, kidney TEXT, 
                       heart TEXT, lungs TEXT, liver TEXT, corneas TEXT, pancreas TEXT)''')

    ## PatientMed Entity
    cursor1.execute('''CREATE TABLE IF NOT EXISTS PatientMed (entryID INTEGER PRIMARY KEY, patientID TEXT, 
                      userID TEXT, time TEXT, date TEXT, dataType TEXT, value TEXT)''')

    ## PatientCons Entity
    cursor1.execute('''CREATE TABLE IF NOT EXISTS PatientCons (consultationID INTEGER PRIMARY KEY, patientID TEXT, 
                      userID TEXT, time TEXT, date TEXT, complaint TEXT, examination TEXT, history TEXT,
                      treatment TEXT, diagnosis TEXT, comments TEXT)''')
    
    conn1.commit()

## Appointments.db Creation
conn2 = sqlite3.connect('Appointments.db')

with conn2:
    cursor2 = conn2.cursor()

    ## AppointmentBook Entity
    cursor2.execute('''CREATE TABLE IF NOT EXISTS AppointmentBook (appointmentID INTEGER PRIMARY KEY, patientID TEXT, 
                      userID TEXT, time TEXT, date TEXT, type TEXT, status TEXT, reason TEXT)''')

    conn2.commit()

## Stocks.db Creation
conn3 = sqlite3.connect('Stocks.db')
 
with conn3:
    cursor3 = conn3.cursor()

    ## Stocks Entity
    cursor3.execute('''CREATE TABLE IF NOT EXISTS Stocks (itemID INTEGER PRIMARY KEY, name TEXT, 
                      category TEXT, brand TEXT, quantity TEXT)''')

    conn3.commit()

## Users.db Creation
conn4 = sqlite3.connect('Users.db')

with conn4:
    cursor4 = conn4.cursor()

    ## User Accounts Entity
    cursor4.execute('''CREATE TABLE IF NOT EXISTS UserAccounts (userID INTEGER PRIMARY KEY, username TEXT, 
                      password TEXT, title TEXT, firstname TEXT, surname TEXT, email TEXT, mobile TEXT, userType TEXT)''')
    
    ## Pushing Administrator Account Details to UserAccounts Entity
    cursor4.execute('''INSERT INTO UserAccounts (userID, username, password, title, firstname, surname, email, mobile, 
                      userType) VALUES (NULL, 'admin', 'Password1', 'Mr', 'System', 'Administrator', 'systemadmin@acs.com', 
                      '02894413910', 'Administrator')''')
    
    conn4.commit()