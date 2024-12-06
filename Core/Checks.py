#  This Module has all the required functions to perform the operations on the database
import mysql.connector as con
from mysql.connector.errors import ProgrammingError,Error
import Core.InsertData as Insert

def CheckDatabase():
    print("Checking Database Requirement..")
    db = con.connect(
        host = Host_address,
        user = Your User Name,
        database = "",
        password = Your password
        )
    cur = db.cursor()
    result = None

    try : 
        cur.execute("USE railway;")
    except ProgrammingError:
        print("Database does not exist")
        result = False
    else:
        result = True
    
    if result is True:
        print("Database Exists!")
    else:
        print("Creating Database with required Tables")
        print("Please Wait for a while")
        cur.execute("CREATE DATABASE railway;")
        cur.execute("USE railway;")
        CreateTable()
        print("Database and Tables Created")
    cur.close()
    db.close()

def CreateTable():
    db = con.connect(host = Host_address,
    user = Your User Name,
    database = "railway",
    password = Your password
        )
    cur = db.cursor()
    cur.execute("create table train_info (Train_No varchar(10) NOT NULL, Station_Code varchar(20) NOT NULL, Station_Name varchar(30) NOT NULL, Arrival_Time varchar(20) NOT NULL, Departure_Time varchar(20) NOT NULL, Distance varchar(10) NOT NULL, Source_Station_Code varchar(20) NOT NULL, Source_Station_Name varchar(70) NOT NULL, Destination_Station_Code varchar(20) NOT NULL, Destination_Station_Name varchar(60) NOT NULL);")
    cur.execute("create table bookings (Train_No int NOT NULL, Passenger_Name varchar(30) NOT NULL, Mobile_No varchar(10) NOT NULL, Passenger_Adhaar varchar(12) NOT NULL, Date_Of_Booking varchar(20) NOT NULL, Booking_ID int NOT NULL, Class varchar(20) NOT NULL,Date_Of_Travel varchar(20) NOT NULL);")
    Insert.InsertTrainData()

    cur.close()
    db.close()

def CheckConnection():
    try:
        print("Checking the Connection to the MySQL Server..")
        connection = con.connect(
            host = Host_address,
            user = Your User Name,
            database = "railway",
            password = Your password)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server Version", db_Info)
    except Error as e:
        print(e)
        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True