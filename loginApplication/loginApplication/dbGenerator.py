import sqlite3

conn1 = sqlite3.connect('Patients.db')

with conn1:
    cursor1 = conn1.cursor()

    cursor1.execute('''CREATE TABLE IF NOT EXISTS PatientMed (entryID INTEGER PRIMARY KEY, patientID TEXT, 
                      userID TEXT, time TEXT, date TEXT, dataType TEXT, value TEXT)''')

    cursor1.execute('''CREATE TABLE IF NOT EXISTS PatientCons (consultationID INTEGER PRIMARY KEY, patientID TEXT, 
                      userID TEXT, time TEXT, date TEXT, complaint TEXT, examination TEXT, history TEXT,
                      treatment TEXT, diagnosis TEXT, comments TEXT)''')
    
    conn1.commit()

conn2 = sqlite3.connect('Appointments.db')

with conn2:
    cursor2 = conn2.cursor()

    cursor2.execute('''CREATE TABLE IF NOT EXISTS AppointmentBook (appointmentID INTEGER PRIMARY KEY, patientID TEXT, 
                      userID TEXT, time TEXT, date TEXT, type TEXT, status TEXT, reason TEXT)''')

    conn2.commit()

conn3 = sqlite3.connect('Stocks.db')

with conn3:
    cursor3 = conn3.cursor()

    cursor3.execute('''CREATE TABLE IF NOT EXISTS Stocks (itemID INTEGER PRIMARY KEY, name TEXT, 
                      category TEXT, brand TEXT, quantity TEXT)''')

    conn3.commit()
