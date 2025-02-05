import sqlite3

sqlite3.connect('AZHSP.db')

connection = sqlite3.connect('AZHSP.db')

cur = connection.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Customer (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            EMAIL TEXT UNIQUE NOT NULL,
            PASSWORD TEXT NOT NULL,
            ADDRESS TEXT NOT NULL,
            PINCODE TEXT NOT NULL
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Professional (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NAME TEXT NOT NULL,
            EMAIL TEXT UNIQUE NOT NULL,
            PASSWORD TEXT NOT NULL,
            PHONE_NO TEXT NOT NULL,
            ADDRESS TEXT NOT NULL,
            PINCODE TEXT NOT NULL,
            INFO_DOC BLOB
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Services (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SERVICE_NAME TEXT NOT NULL,
            PROVIDED_BY INTEGER NOT NULL,
            DESCRIPTION TEXT NOT NULL,
            BASE_PRICE REAL NOT NULL,
            RATING REAL,
            FOREIGN KEY (PROVIDED_BY) REFERENCES Professional(ID)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Service_Requests(
            CUSTOMER_ID INTEGER NOT NULL,
            SERVICE_ID INTEGER NOT NULL,
            PROFESSIONAL_ID INTEGER,
            STATUS TEXT CHECK(STATUS IN ('Requested', 'Assigned', 'In Progress', 'Closed', 'Rejected')) NOT NULL,
            REQUEST_DATE DATETIME NOT NULL,
            MODIFIED_DATE DATETIME,
            FOREIGN KEY (CUSTOMER_ID) REFERENCES Customer(ID),
            FOREIGN KEY (SERVICE_ID) REFERENCES Services(ID),
            FOREIGN KEY (PROFESSIONAL_ID) REFERENCES Professional(ID)
            )''')

cur.execute('''CREATE TABLE IF NOT EXISTS Professional_Skills (
            PROFESSIONAL_ID INTEGER NOT NULL,
            SERVICE_ID INTEGER NOT NULL,
            FOREIGN KEY (PROFESSIONAL_ID) REFERENCES Professional(ID),
            FOREIGN KEY (SERVICE_ID) REFERENCES Services(ID)
            )''')

cur.close()
connection.close()