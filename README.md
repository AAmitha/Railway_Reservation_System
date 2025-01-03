Railway Reservation System

Overview:
This project is a simple railway reservation system implemented using Python and SQLite for data storage. The system includes a graphical user interface (GUI) built with Tkinter to facilitate user interaction. Additionally, the back-end is designed using SQL queries for data manipulation and management.

Technologies Used:
1. Python: Programming language for implementing the application logic.
2. SQLite: Lightweight, serverless, and easy-to-use database for storing reservation data.
3. Tkinter: GUI library for creating a user-friendly interface.
4. SQL: Language for managing and querying database tables and data.

Features:
1. Passenger Query (Query1): Fetch train details based on passenger names.
2. Train Date Query (Query2): Show records of booked tickets on a specific train date.
3. Age-based Query (Query3): Retrieve records of passengers within a specified age range.
4. Train Count Query (Query4): Count and display the number of passengers for each train.
5. Train Name Query (Query5): Fetch passenger details for a specific train.
6. Passenger Deletion and Status Update (Query6): Delete a booking and update the status of a specific passenger.

Database Schema
The .sql file contains SQL queries to create and manage tables along with sample data. The tables and queries include:
1. TRAIN: Stores train-related information.
2. BOOKED: Records passenger bookings linked to trains.
3. PASSENGERS: Contains personal details of passengers.
4. TRAIN_STATUS: Tracks the status of train operations on specific dates.

Getting Started
Prerequisites:
  Python 3.x
  SQLite3
  Tkinter

Installation:
Clone the repository: git clone [repo link]
Navigate to the project directory: cd RailwayReservationSystem
Run the Python script: python railway_reservation.py

Usage:
  Input Fields:
    First Name
    Last Name
    Train Date
    Train Name
    Age
    Passenger SSN

  Queries:
    Query1: Show records based on First Name and Last Name.
    Query2: Show records based on Train Date.
    Query3: Show records based on Age.
    Query4: Show train-wise passenger counts.
    Query5: Show detailed records based on Train Name.
    Query6: Delete booking and update passenger status.

SQL Data
  The .sql file includes all necessary SQL queries to initialize the database, creating tables and inserting sample data for demonstration purposes.

Contributions
  Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

