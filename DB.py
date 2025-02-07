import sqlite3

connection = sqlite3.connect('AZHS.db')

# User(professional,customers) tables
connection.execute(
'''CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    role TEXT CHECK(role IN ('Admin', 'Customer', 'Professional')) NOT NULL,
    info_doc BLOB,
    pin_code TEXT NOT NULL
)''')

# Services table
connection.execute('''CREATE TABLE IF NOT EXISTS Services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT UNIQUE NOT NULL,
    description TEXT NOT NULL,
    base_price REAL NOT NULL,
    created_by INTEGER NOT NULL,
    FOREIGN KEY (created_by) REFERENCES Users(user_id)
)''')

#Service Requests Table
connection.execute('''CREATE TABLE IF NOT EXISTS Service_Requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    professional_id INTEGER,
    status TEXT CHECK(status IN ('Requested', 'Assigned', 'In Progress', 'Closed', 'Rejected')) NOT NULL,
    request_date DATETIME NOT NULL,
    completion_date DATETIME,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    FOREIGN KEY (service_id) REFERENCES Services(service_id),
    FOREIGN KEY (customer_id) REFERENCES Users(user_id),
    FOREIGN KEY (professional_id) REFERENCES Users(user_id)
)''')

# Professional_Skills
connection.execute('''CREATE TABLE IF NOT EXISTS Professional_Skills (
    skill_id INTEGER PRIMARY KEY AUTOINCREMENT,
    professional_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    FOREIGN KEY (professional_id) REFERENCES Users(user_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
)''')

# Packages Table
connection.execute('''CREATE TABLE IF NOT EXISTS Packages (
    package_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_name TEXT NOT NULL,
    description TEXT NOT NULL,
    price REAL NOT NULL,
    created_by INTEGER NOT NULL,
    FOREIGN KEY (created_by) REFERENCES Users(user_id)
)''')

# Package Inclusions Table
connection.execute('''CREATE TABLE IF NOT EXISTS Package_Inclusions (
    inclusion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    package_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    FOREIGN KEY (package_id) REFERENCES Packages(package_id),
    FOREIGN KEY (service_id) REFERENCES Services(service_id)
)''')

# Service Feedback Table
connection.execute('''CREATE TABLE IF NOT EXISTS Service_Feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    request_id INTEGER NOT NULL,
    feedback_text TEXT,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    submitted_date DATETIME NOT NULL,
    FOREIGN KEY (request_id) REFERENCES Service_Requests(request_id)
)''')

# Statistics Table (For Dashboard)
connection.execute('''CREATE TABLE IF NOT EXISTS Statistics (
    stat_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    total_requests INTEGER NOT NULL,
    total_completed_requests INTEGER NOT NULL,
    total_ratings INTEGER NOT NULL,
    average_rating REAL NOT NULL
)''')

# Insert Admin Credentials into Users Table
connection.execute('''INSERT INTO Users (email, password, name, address, role, pin_code)
VALUES ('admin@example.com', 'admin123', 'Admin User', '123 Admin Street', 'Admin', '00000')''')

connection.commit()

connection.close()