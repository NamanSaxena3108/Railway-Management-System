# This module contain all the functions that can be performed by the user to do some task's.
import mysql.connector
import datetime
from mysql.connector import DataError
import random

sleeper_charge = int(1.5)
third_ac_charge = int(2)
second_ac_charge = int(3)
first_ac_charge = int(4)

current_date = datetime.date.today()

max_date = current_date + datetime.timedelta(days=120)

def AvailableTrains(start,final,date_user):
    mn = mysql.connector.connect(host=my_sql_config["host"], user=my_sql_config["user"],
                                 password=my_sql_config["password"], database=my_sql_config["database"])
    cur = mn.cursor()
    cur.execute(
        'SELECT Train_No, Source_Station_Code, Source_Station_Name, Station_Name, Destination_Station_Code, Destination_Station_Name, Arrival_Time, Departure_Time from train_info where Source_Station_Code="{}" AND Destination_Station_Code="{}";'.format(
            start, final))
    result = cur.fetchall()
    cur.close()
    mn.close()
    if len(result) == 0:
        print("No Train Available!")
    else:
        trains = []
        for train in result:
            trains.append({
                "Train Number": train[0],
                "Source Station": train[2],
                "Station": train[3],
                "Destination Station": train[5],
                "Arrival Time": train[6],
                "Departure Time": train[7]
            })
        return trains
    

def CheckFare(start, final):
    mn = mysql.connector.connect(host=my_sql_config["host"], user=my_sql_config["user"],
                                 password=my_sql_config["password"], database=my_sql_config["database"])
    cur = mn.cursor()

    # Execute the SQL query to get the distance and fare information along with station names
    cur.execute(
        '''
        SELECT 
            Train_No, 
            Distance, 
            Source_Station_Name, 
            Destination_Station_Name,
            Station_Name 
        FROM 
            train_info 
        WHERE 
            Source_Station_Code = %s AND Destination_Station_Code = %s;
        ''', (start, final))
    
    result_fare = cur.fetchall()
    cur.close()
    mn.close()

    # Prepare fare information
    fare_info = []
    if len(result_fare) == 0:
        return "No Available Train"
    else:
        for y in result_fare:
            fare_info.append({
                "Train Number": y[0],
                "Distance": y[1],
                "Source Station": y[2],  # Include Source Station Name
                "Destination Station": y[3],  # Include Destination Station Name
                "Station Name": y[4],  # Include Station Name if needed
                "Sleeper Fare": int(y[1]) * sleeper_charge,
                "Third AC Fare": int(y[1]) * third_ac_charge,
                "Second AC Fare": int(y[1]) * second_ac_charge,
                "First AC Fare": int(y[1]) * first_ac_charge
            })
        return fare_info
    
def ShowBookings(mobile_no):
    mn = mysql.connector.connect(host=my_sql_config["host"], user=my_sql_config["user"],
                                 password=my_sql_config["password"], database=my_sql_config["database"])
    cur = mn.cursor()

    cur.execute('SELECT Train_No, Passenger_Name, Mobile_No, Date_Of_Booking, Booking_ID, Class, Date_Of_Travel FROM bookings WHERE Mobile_No="{}"'.format(mobile_no))
    result = cur.fetchall()
    if len(result) == 0:
        return "No Record Found!"
    else:
        bookings = []
        for x in result:
            bookings.append({
                "Train Number": x[0],
                "Passenger Name": x[1],
                "Mobile Number": x[2],
                "Date of Booking": x[3],
                "Booking ID": x[4],
                "Class": x[5],
                "Date of Travel": x[6]  # Include Date of Travel
            })
        return bookings
    
def BookTrain(train_no, name, mobile, adhaar, booking_class, travel_date):
    mn = mysql.connector.connect(host=my_sql_config["host"], user=my_sql_config["user"],
                                 password=my_sql_config["password"], database=my_sql_config["database"])
    cur = mn.cursor()

    Time_of_Booking = datetime.datetime.now()
    date = Time_of_Booking.date()
    date = date.strftime("%d-%m-%y")

    id = random.randint(1, 10000)
    cur.execute("SELECT Booking_ID FROM bookings")
    result = cur.fetchall()
    Used_ID = [x[0] for x in result]

    while id in Used_ID:
        id = random.randint(1, 10000)

    try:
        # Use parameterized query to prevent SQL injection and handle data types
        cur.execute("INSERT INTO bookings (Train_No, Passenger_Name, Mobile_No, Passenger_Adhaar, Date_Of_Booking, Booking_ID, Class, Date_Of_Travel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                    (train_no, name, mobile, adhaar, date, id, booking_class, travel_date))
        mn.commit()
        return id  # Return only the booking ID
    except mysql.connector.Error as err:
        return f"Error in Booking: {err}"  # Return error message
    finally:
        cur.close()
        mn.close()
        
def CancelBooking(unique_id):
    mn = mysql.connector.connect(host=my_sql_config["host"], user=my_sql_config["user"],
                                 password=my_sql_config["password"], database=my_sql_config["database"])
    cur = mn.cursor()

    # Check if the booking exists
    cur.execute("SELECT * FROM bookings WHERE Booking_ID={}".format(unique_id))
    result = cur.fetchall()
    
    if len(result) == 0:
        return "No Booking Found!"
    
    # If booking exists, delete it
    cur.execute("DELETE FROM bookings WHERE Booking_ID={}".format(unique_id))
    mn.commit()
    cur.close()
    mn.close()
    
    return "Booking cancelled successfully!"