from flask import Flask, render_template
from flask_mysqldb import MySQL
import mysql.connector
import csv
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="bbmsh899",
  auth_plugin='mysql_native_password'
)

mysql = MySQL(app)

# creating database_cursor to perform SQL operation to run queries
db_cursor = db_connection.cursor(buffered=True)

# executing cursor with execute method and pass SQL query
db_cursor.execute("CREATE DATABASE IF NOT EXISTS hospital")

db_cursor.execute("USE hospital")

def populate_table(db_connection, db_cursor, insert_query, file_path):
    with open(file_path, mode='r') as csv_data:
        reader = csv.reader(csv_data, delimiter=',')  # Update delimiter to ','
        csv_data_list = list(reader)
        for row in csv_data_list[1:]:
            row = tuple(map(lambda x: None if x == "" else x, row))  # No need for split(',') due to csv.reader
            db_cursor.execute(insert_query, row)

    db_connection.commit()

# to check if the table exists
# if the table exists, create method will not be called,
# each table is created once
def table_exists(table_name):
    db_cursor.execute("SHOW TABLES LIKE %s", (table_name,))
    return db_cursor.fetchone() is not None



########################## CREATE TABLES ##########################
# doctors table
def create_doctor_table():
    table_name = "Doctor"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Doctor( doctor_id CHAR(15) NOT NULL, 
                                                   gender CHAR(1), 
                                                   lname CHAR(50), 
                                                   specialization CHAR(50), 
                                                   fname CHAR(50), 
                                                   department_id CHAR(10), 
                                                   email CHAR(50), 
                                                   phone_number CHAR(15), 
                                                   PRIMARY KEY (doctor_id))""")
        insert_doctors = (
            "INSERT INTO Doctor(doctor_id, gender, lname, specialization, fname, department_id, email, phone_number) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_doctors, "Doctors.csv")

create_doctor_table()

# administrator table
def create_administrator_table():
    table_name = "Administrator"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Administrator( department_id CHAR(10) NOT NULL,  
                                                         adm_id CHAR(15) NOT NULL, 
                                                         phone_number CHAR(15), 
                                                         fname CHAR(50), 
                                                         lname CHAR(50), 
                                                         email CHAR(50), 
                                                         PRIMARY KEY (adm_id))""")
        insert_administrators = (
            "INSERT INTO Administrator(department_id, adm_id, phone_number, fname, lname, email) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_administrators, "Administrator.csv")

create_administrator_table()

#department table
def create_department_table():
    table_name = "Department"
    if not table_exists(table_name):
        #Create Table
        db_cursor.execute("""CREATE TABLE Department( department_id CHAR(10) NOT NULL,  
                                                      department_name VARCHAR(100) NOT NULL, 
                                                      admin_id INT,
                                                      PRIMARY KEY (department_id),
                                                      FOREIGN KEY (admin_id) REFERENCES Administrator(admin_id))
                                                       """)
        insert_departments = (
            "INSERT INTO Department(department_id, department_name, admin_id) "
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_departments, "Department.csv")

create_department_table()


#staff table
def create_staff_table():
    table_name = "Staff"
    if not table_exists(table_name):
        #Create Table
        db_cursor.execute("""CREATE TABLE Staff( staff_id INT,
                                                 fname VARCHAR(50),
                                                 lname VARCHAR(50),
                                                 sex CHAR(1),
                                                 department_id CHAR(10),
                                                 phone_number CHAR(15),
                                                 email VARCHAR(100),
                                                 PRIMARY KEY (stafF_id)
                                                 """)

        insert_staff = (
            "INSERT INTO Staff(staff_id, fname, lname, sex, department_id, phone_number, email)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_staff, "Staff.csv")

create_staff_table()


# nurse table
def create_nurse_table():
    table_name = "Nurse"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Nurse(nurse_id INT,
                                                doctor_id INT,
                                                department_id INT,
                                                FOREIGN KEY (nurse_id) REFERENCES Staff,
                                                PRIMARY KEY (doctor_id) REFERENCES Doctor)""")
        insert_nurses = (
            "INSERT INTO Doctor(nurse_id, doctor_id, department_id) "
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_nurses, "Nurse.csv")

create_nurse_table()


# patient table
def create_patient_table():
    table_name = "Patient"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Patient(patient_id INT,
                                                  fname VARCHAR(50),
                                                  lname VARCHAR(50),
                                                  email VARCHAR(50),
                                                  phone_number CHAR(15),
                                                  birth_date DATE,
                                                  age INT,
                                                  sex CHAR(1),
                                                  insurance_details VARCHAR(255),
                                                  PRIMARY KEY (patient_id)  
                                                )""")
        insert_patients = (
            "INSERT INTO Patient(patient_id , fname, lname, email, phone_number, birth_date, age, sex, insurance_details) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_patients, "Patient.csv")

create_patient_table()

# appointment table
def create_appointment_table():
    table_name = "Appointment"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Appointment(appointment_id INT,
                                                        start_time TIME,
                                                        end_time TIME,
                                                        date DATE,
                                                        doctor_id INT,
                                                        patient_id INT,
                                                        PRIMARY KEY (appointment_id),
                                                        FOREIGN KEY (patient_id) REFERENCES Patient (patient_id)
                                                    )""")
    
        
        insert_appointments = (
            "INSERT INTO Appointment(appointment_id , start_time, end_time, date, doctor_id, patient_id) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_appointments, "Appointment.csv")

create_appointment_table()    

# room table
def create_room_table():
    table_name = "Room"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Room(room_no INT,
                                                type VARCHAR(50),
                                                status VARCHAR(50),
                                                cost_per_month INT,
                                                patient_id INT,
                                                PRIMARY KEY (room_no),
                                                FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)                              
                                                )""")
    
        
        insert_rooms = (
            "INSERT INTO Room(room_no , type, status, cost_per_month, patient_id) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "Room.csv")

create_room_table()    

# bill table
def create_bill_table():
    table_name = "Bill"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Bill(bill_amount DECIMAL(10,2),
                                                patient_id INT,
                                                appointment_id INT,
                                                PRIMARY KEY (patient_id, appointment_id),
                                                FOREIGN KEY (patient_id) REFERENCES Patient,
                                                FOREIGN KEY (appointment_id) REFERENCES Appointment
                                                )""")
    
        
        insert_rooms = (
            "INSERT INTO Bill(bill_amount , patient_id, appointment_id) "
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "Bill.csv")

create_bill_table()      

# attends table
def create_attends_table():
    table_name = "Attends"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Attends(doctor_id INT,
                                                    appointmnet_id INT,
                                                    nurse_id INT,
                                                    PRIMARY KEY(doctor_id, appointment_id, nurse_id),
                                                    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),
                                                    FOREIGN KEY (appointment_id) REFERENCES Appointment,
                                                    FOREIGN KEY (nurse_id) REFERENCES Nurse
                                                )""")
    
        
        insert_rooms = (
            "INSERT INTO Attends(doctor_id , appointmnet_id, nurse_id) "
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "Attends.csv")

create_attends_table()  


# scheduled to table
def create_scheduled_to_table():
    table_name = "Scheduled_To"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Scheduled_To(doctor_id INT,
                                                       patient_id INT,
                                                       nurse_id INT,
                                                       PRIMARY KEY(patient_id, doctor_id, nurse_id),
                                                       FOREIGN KEY (patient_id) REFERENCES Patient,
                                                       FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),
                                                       FOREIGN KEY (nurse_id) REFERENCES Nurse,
                                                )""")
    
        insert_rooms = (
            "INSERT INTO Scheduled_To(doctor_id , patient_id, nurse_id) "
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "Scheduled-To.csv")

create_scheduled_to_table()  

# treats table
def create_treats_table():
    table_name = "Treats"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Treats(medicine_id INT,
                                                 medicine_timing CHAR(20),
                                                 medicine_amount INT,
                                                 doctor_id INT,
                                                 patient_id INT,
                                                 PRIMARY KEY(medicine_id, patient_id, doctor_id),
                                                 FOREIGN KEY (patient_id) REFERENCES Patient,
                                                 FOREIGN KEY (doctor_id ) REFERENCES Doctor
                                                )""")
    
        insert_rooms = (
            "INSERT INTO Treats(medicine_id , medicine_timing, medicine_amount, doctor_id, patient_id) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "Treats.csv")

create_treats_table()  

# address table
def create_address_table():
    table_name = "Address"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Address(patient_id INT,
                                                  address CHAR(50),
                                                  PRIMARY KEY(patient_id, address),
                                                  FOREIGN KEY (patient_id) REFERENCES Patient
                                                )""")
    
        insert_rooms = (
            "INSERT INTO Address(patient_id , address) "
            "VALUES (%s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "Address.csv")

create_address_table()  

# disease table
def create_disease_table():
    table_name = "Disease"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Disease(patient_id INT,
                                                  disease CHAR(50),
                                                  PRIMARY KEY(patient_id, disease),
                                                  FOREIGN KEY (patient_id) REFERENCES Patient
                                                 )""")
    
        insert_rooms = (
            "INSERT INTO Disease(patient_id , disease) "
            "VALUES (%s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "Disease.csv")

create_disease_table()  

# record table
def create_record_table():
    table_name = "Record"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Record(record_id INT,
                                                 appointment_id INT,
                                                 patient_id INT,
                                                 doctor_id INT,
                                                 PRIMARY KEY (record_id),
                                                 FOREIGN KEY (appointment_id) REFERENCES Appointment(appointment_id),
                                                 FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
                                                 FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id))""")
    
        insert_records = (
            "INSERT INTO Record(record_id , appointment_id, patient_id, doctor_id) "
            "VALUES (%s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_records, "Record.csv")

create_record_table()  

########################## QUERIES ##########################

# doctors list query
db_cursor.execute("""SELECT *
                    FROM Doctor""")
doctors_list = db_cursor.fetchall()


# administrators list query
db_cursor.execute("""SELECT *
                    FROM Administrator""")
administrators_list = db_cursor.fetchall()



@app.route('/')
def hello_world():  # put application's code here
    return "Hello World"

# Routes
@app.route('/api/doctors')
def show_doctors():
    #return render_template('index.html', doctors_list=doctors_list)
    # http://127.0.0.1:5000/doctors-list
    global doctors_list  # Assuming doctors_list is available globally
    return jsonify(doctors_list)
@app.route('/administrators-list')
def show_administrators():
    return render_template('index.html', administrators_list=administrators_list)
    # http://127.0.0.1:5000/administrators-list
if __name__ == '__main__':
    app.run()
