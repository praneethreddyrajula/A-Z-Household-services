# Orm
# Schema of the db

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Professional(db.Model):
#     ID = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     EMAIL = db.Column(db.String(255),unique=True, nullable=False)
#     PASSWORD = db.Column(db.Text,nullable=False)
#     FULLNAME = db.Column(db.String(255), nullable=False)
#     SERVICENAME = db.Column(db.String(255))
#     EXPERIENCE = db.Column(db.Integer)
#     ADDRESS = db.Column(db.Text)
#     OINCODE = db.Column(db.Integer)
#     ROOTUSER = db.Column(db.Boolean, default=False)

# class Customers(db.Model):
#     ID = db.Column(db.Integer,primary_key=True,autoincrement=True)
#     EMAIL = db.Column(db.String(255),unique=True, nullable=False)
#     PASSWORD = db.Column(db.Text,nullable=False)
#     FULLNAME = db.Column(db.String(255), nullable=False)
#     ADDRESS = db.Column(db.String(255))
#     CITY = db.Column(db.String(255))
#     STATE = db.Column(db.String(255))
#     PINCODE = db.Column(db.Integer)
#     ROOTUSER = db.Column(db.Boolean, default=False)
# from sqlalchemy import create_engine, MetaData, Table
# from sqlalchemy.orm import mapper, sessionmaker
# class Bookmarks(object):
#     pass
# #----------------------------------------------------------------------
# def loadSession():
#     """"""    
#     dbPath = 'AZHS.db'
#     engine = create_engine('sqlite:///%s' % dbPath, echo=True)
    
#     metadata = MetaData(engine)
#     moz_bookmarks = Table('Users', metadata, autoload=True)
#     mapper(Bookmarks, moz_bookmarks)
    
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session
# if __name__ == "__main__":
#     session = loadSession()
#     res = session.query(Bookmarks).all()
#     res[1].title

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker,registry

class Users(object):
    pass

def loadSession():
    """Initialize the database session"""
    dbPath = 'C:/Users/prajula/Desktop/Project/A-Z-Household-services/AZHS.db'  # Path to the SQLite database
    engine = create_engine(f'sqlite:///{dbPath}', echo=True)  # Use the SQLite URL format
    
    metadata = MetaData()
    users_table = Table('Users', metadata, autoload_with=engine)  # `metadata` should be used here, not `engine`
    
    registry.map_imperatively(Users, users_table)  # Map the Users class to the Users table
    
    Session = sessionmaker(bind=engine)  # Create a session factory bound to the engine
    session = Session()  # Instantiate a session
    return session

if __name__ == "__main__":
    session = loadSession()
    try:
        res = session.query(Users).all()  # Query all records from the Users table
        if len(res) > 1:
            print(res[1].name)  # Assuming 'name' is a column in the Users table
        else:
            print("Not enough records in the Users table")
    except Exception as e:
        print(f"An error occurred: {e}")
