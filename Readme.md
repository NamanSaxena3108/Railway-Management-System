# Railway Management System 

### Overview 
The Railway Management System is a comprehensive system designed to manage various aspects of a railway network, including passenger information and station management. The system aims to provide a user-friendly interface for railway staff to efficiently manage the railway network, ensuring smooth and safe operations.

### Features
1. **Book a Ticket**: Users can book tickets for their desired journey, specifying the source and destination stations, and the date of travel.
2. **Cancel a Ticket**: Users can cancel their booked tickets if needed. 
3. **Check Fares**: Users can check the fare for their specified class by specifying the source and destination stations.
4. **Show Bookings**: Users can view their current bookings.
5. **Available Trains**: Users can see a list of available trains for their journey.
6. **About Section**: Users can access information about the application.
7. **Exit Option**: Users can exit the application gracefully.

### Database Structure
The system uses a MySQL database with the following tables:

- **train_info**: Contains information about the trains.
  - Columns: `Train_No`, `Station_Code`, `Station_Name`, `Arrival_Time`, `Departure_Time`, `Distance`, `Source_Station_Code`, `Source_Station_Name`, `Destination_Station_Code`, `Destination_Station_Name`

- **bookings**: Contains information about the bookings made by users.
  - Columns: `Train_No`, `Passenger_Name`, `Mobile_No`, `Aadhaar`, `Date_Of_Booking`, `Booking_ID`, `Class`, `Date_Of_Travel`

### Folders
- **/Assets**: Contains the data that is to be inserted in the MySQL tables in CSV format.
  - Files: `Train_details.csv` -> Contains all the data about the trains in the format 
    (Train No, Station Code, Station Name, Arrival time, Departure Time, 
    Distance, Source Station, Source Station Name, Destination Station, 
    Destination Station Name)

- **/Core**: Contains all the files that are required by the project to work.
  - Files: 
    - `__init__.py`: Makes the folder recognized as a module.
    - `Checks.py`: Contains functions that verify the requirements of the project.
    - `InsertData.py`: Contains functions to insert the data into the MySQL tables.
    - `User _Functions.py`: Contains functions that allow a user to perform certain tasks.

### Installation
1. Ensure you have Python installed on your system.
2. Install the required packages using pip:
   ```bash
   pip install requirement.txt
3. Set up a MySQL database and create the necessary tables as described above.
4. To stop use `Ctrl + c`

### Usage
1. Run the application using Streamlit:
```streamlit run app.py```
2. Follow the on-screen instructions to book tickets, check fares, and manage bookings.

### About
The Railway Management System is designed to streamline the process of managing railway bookings and information, making it easier for users to navigate and utilize railway services effectively.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
