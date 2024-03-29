DROP TABLE IF EXISTS TRAIN;
DROP TABLE IF EXISTS BOOKED;
DROP TABLE IF EXISTS PASSENGERS;
DROP TABLE IF EXISTS TRAIN_STATUS;
CREATE TABLE TRAIN
    (Train_Number VARCHAR(25) PRIMARY KEY, 
    Train_Name VARCHAR(25),
    Premium_Fare VARCHAR(25), 
    General_Fare VARCHAR(25), 
    Source_Station VARCHAR(25), 
    Destination_Station VARCHAR(25));
INSERT INTO TRAIN(Train_Number, Train_Name, Premium_Fare, General_Fare, Source_Station, Destination_Station)
VALUES 
(1, 'Orient Express', 800, 600, 'Paris', 'Istanbul'),
(2, 'Flying Scottsman', 4000, 3500, 'Edinburgh', 'London'),
(3, 'Golden Arrow', 980, 860, 'Victoria', 'Dover'),
(4, 'Golden Chariot', 4300, 3800, 'Bangalore', 'Goa'),
(5, 'Maharaja Express', 5980, 4510, 'Delhi', 'Mumbai');

CREATE TABLE BOOKED
(Passenger_ssn VARCHAR(25),
Train_Number VARCHAR(25),
Ticket_Types VARCHAR(25),
Status VARCHAR(25));
INSERT INTO BOOKED (Passenger_ssn, Train_Number, Ticket_Types, Status)
VALUES
(264816896, 3, 'Premium', 'Booked'),
(240471168, 2, 'General', 'Booked'),
(285200976, 4, 'Premium', 'Booked'),
(285200976, 2, 'Premium', 'Booked'),
(317434088, 2, 'Premium', 'Booked'),
(310908858, 2, 'General', 'Booked'),
(322273872, 2, 'General', 'Booked'),
(256558303, 3, 'Premium', 'WaitL'),
(302548590, 2, 'General', 'WaitL'),
(284965676, 3, 'Premium', 'WaitL'),
(277292710, 3, 'General', 'WaitL'),
(331160133, 3, 'General', 'WaitL'),
(331293204, 3, 'General', 'WaitL'),
(290123298, 3, 'General', 'WaitL'),
(286411536, 4, 'Premium', 'Booked'),
(294860856, 4, 'Premium', 'Booked'),
(317434088, 4, 'Premium', 'Booked'),
(310908858, 4, 'Premium', 'Booked'),
(322273872, 4, 'Premium', 'Booked'),
(256558303, 4, 'Premium', 'Booked'),
(302548590, 4, 'Premium', 'Booked'),
(284965676, 4, 'General', 'Booked'),
(277292710, 4, 'General', 'Booked'),
(331160133, 4, 'General', 'Booked'),
(331293204, 4, 'General', 'Booked');
CREATE TABLE PASSENGERS
(First_name VARCHAR(25),
Last_name VARCHAR(25),
Address VARCHAR(25),
City VARCHAR(25),
Country VARCHAR(25),
Phone VARCHAR(25),
Ssn VARCHAR(25) PRIMARY KEY,
Bdate date);
INSERT INTO PASSENGERS (First_name, Last_name, Address, City, Country, Phone, Ssn, Bdate)
VALUES ('James', 'Butt', '6649 N Blue Gum St', 'New Orleans', 'Orleans', '504-845-1427', '264816896', '1968-10-10'),
('Josephine', 'Darakjy', '4 B Blue Ridge Blvd', 'Brighton', 'Livingston', '810-374-9840', '240471168', '1975-11-01'),
('Art', 'Venere', '8 W Cerritos Ave #54', 'Bridgeport', 'Gloucester', '856-264-4130', '285200976', '1982-11-13'),
('Lenna', 'Paprocki', '639 Main St', 'Anchorage', 'Anchorage', '907-921-2010', '309323096', '1978-08-09'),
('Donette', 'Foller', '34 Center St', 'Hamilton', 'Butler', '513-549-4561', '272610795', '1990-06-11'),
('Simona', 'Morasca', '3 Mcauley Dr', 'Ashland', 'Ashland', '419-800-6759', '250951162', '1994-08-15'),
('Mitsue', 'Tollner', '7 Eads St', 'Chicago', 'Cook', '773-924-8565', '272913578', '1984-07-04'),
('Leota', 'Dilliard', '7 W Jackson Blvd', 'San Jose', 'Santa Clara', '408-813-1105', '268682534', '1991-05-09'),
('Sage', 'Wieser', '5 Boston Ave #88', 'Sioux Falls', 'Minnehaha', '605-794-4895', '310908858', '1982-02-25'),
('Kris', 'Marrier', '228 Runamuck Pl #2808', 'Baltimore', 'Baltimore City', '410-804-4694', '322273872', '1956-04-04'),
('Minna', 'Amigon', '2371 Jerrold Ave', 'Kulpsville', 'Montgomery', '215-422-8694', '256558303', '1995-09-09'),
('Abel', 'Maclead', '37275 St Rt 17m M', 'Middle Island', 'Suffolk', '631-677-3675', '302548590', '1960-11-05'),
('Kiley', 'Caldarera', '25 E 75th St #69', 'Los Angeles', 'Los Angeles', '310-254-3084', '284965676', '1981-05-09'),
('Graciela', 'Ruta', '98 Connecticut Ave Nw', 'Chagrin Falls', 'Geauga', '440-579-7763', '277292710', '1982-02-25'),
('Cammy', 'Albares', '56 E Morehead St', 'Laredo', 'Webb', '956-841-7216', '331160133', '1956-04-04'),
('Mattie', 'Poquette', '73 State Road 434 E', 'Phoenix', 'Maricopa', '602-953-6360', '331293204', '1995-09-09'),
('Meaghan', 'Garufi', '69734 E Carrillo St', 'Mc Minnville', 'Warren', '931-235-7959', '290123298', '1960-11-02'),
('Gladys', 'Rim', '322 New Horizon Blvd', 'Milwaukee', 'Milwaukee', '414-377-2880', '286411536', '1991-05-09'),
('Yuki', 'Whobrey', '1 State Route 27', 'Taylor', 'Wayne', '313-341-4470', '294860856', '1985-02-25'),
('Fletcher', 'Flosi', '394 Manchester Blvd', 'Rockford', 'Winnebago', '815-426-5657', '317434088', '1961-04-04');
CREATE TABLE TRAIN_STATUS
    (Train_Date DATE,
    Train_Name VARCHAR(25),
    Premium_seats_available VARCHAR(25),
    Gen_seats_available VARCHAR(25),
    Premium_seats_occupied VARCHAR(25),
    Gen_seats_occupied VARCHAR(25));
INSERT INTO TRAIN_STATUS (Train_Date, Train_Name, Premium_seats_available, Gen_seats_available, Premium_seats_occupied, Gen_seats_occupied) 
VALUES 
('2022-02-19', 'Orient Express', '10', '10', '0', '0'),
('2022-02-20', 'Flying Scottsman', '8', '5', '2', '5'),
('2022-02-21', 'Maharaja Express', '7', '6', '3', '4'),
('2022-02-21', 'Golden Chariot', '6', '3', '4', '7'),
('2022-02-22', 'Golden Arrow', '8', '7', '2', '3'),
('2022-03-10', 'Golden Arrow', '8', '5', '2', '5'),
('2022-02-21', 'Maharaja Express', '7', '6', '3', '4'),
('2022-02-21', 'Flying Scottsman', '5', '5', '5', '5');








