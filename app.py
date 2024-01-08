from flask import Flask, request
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
  passwd="123678zulal",
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


# administrator table
def create_administrator_table():
    table_name = "Administrator"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Administrator(admin_id CHAR(6) NOT NULL, 
                                                         fname CHAR(50), 
                                                         lname CHAR(50), 
                                                         phone_number CHAR(11), 
                                                         email CHAR(50), 
                                                         PRIMARY KEY (admin_id))""")
        insert_administrators = (
            "INSERT INTO Administrator(admin_id, fname, lname, phone_number, email) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_administrators, "InitialData/Administrator.csv")

create_administrator_table()

#department table
def create_department_table():
    table_name = "Department"
    if not table_exists(table_name):
        #Create Table
        db_cursor.execute("""CREATE TABLE Department(department_id CHAR(6) NOT NULL,  
                                                      department_name VARCHAR(50) NOT NULL, 
                                                      PRIMARY KEY (department_id))""")
        insert_departments = (
            "INSERT INTO Department(department_id, department_name)"
            "VALUES (%s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_departments, "InitialData/Department.csv")

create_department_table()


# doctors table
def create_doctor_table():
    table_name = "Doctor"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Doctor(doctor_id CHAR(6) NOT NULL, 
                                                   gender CHAR(1),                                                    
                                                   lname VARCHAR(50), 
                                                   specialization VARCHAR(50), 
                                                   fname VARCHAR(50), 
                                                   department_id CHAR(6), 
                                                   phone_number CHAR(11), 
                                                   email VARCHAR(50), 
                                                   PRIMARY KEY (doctor_id),
                                                   FOREIGN KEY (department_id) REFERENCES Department (department_id))""")
        insert_doctors = (
            "INSERT INTO Doctor(doctor_id, gender, lname, specialization, fname, department_id, phone_number, email) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_doctors, "InitialData/Doctors.csv")

create_doctor_table()


# patient table
def create_patient_table():
    table_name = "Patient"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Patient(patient_id CHAR(6) NOT NULL,
                                                  fname VARCHAR(50),
                                                  lname VARCHAR(50),
                                                  email VARCHAR(50),
                                                  phone_number CHAR(11), 
                                                  birth_date DATE,
                                                  age INT,
                                                  sex CHAR(1),
                                                  address VARCHAR(50),
                                                  insurance_details VARCHAR(255),
                                                  PRIMARY KEY (patient_id)  
                                                )""")
        insert_patients = (
            "INSERT INTO Patient(patient_id , fname, lname, email, phone_number, birth_date, age, sex, address, insurance_details) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_patients, "InitialData/Patient.csv")


create_patient_table()


# appointment table
def create_appointment_table():
    table_name = "Appointment"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Appointment(appointment_id CHAR(6) NOT NULL,
                                                        start_time TIME,
                                                        end_time TIME,
                                                        date DATE,
                                                        doctor_id CHAR(6) NOT NULL,
                                                        patient_id CHAR(6) NOT NULL,                                                     
                                                        PRIMARY KEY (appointment_id),
                                                        FOREIGN KEY (doctor_id) REFERENCES Doctor (doctor_id),
                                                        FOREIGN KEY (patient_id) REFERENCES Patient (patient_id)
                                                    )""")

        insert_appointments = (
            "INSERT INTO Appointment(appointment_id , start_time, end_time, date, doctor_id, patient_id) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_appointments, "InitialData/Appointment.csv")

create_appointment_table()  

# record table
def create_record_table():
    table_name = "Record"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Record(doctor_id CHAR(6) NOT NULL,
                                                 patient_id CHAR(6) NOT NULL,
                                                 appointment_id CHAR(6) NOT NULL,
                                                 medicine_id CHAR(6) NOT NULL,
                                                 medicine_timing VARCHAR(50),
                                                 medicine_amount VARCHAR(50),
                                                 disease VARCHAR(50),
                                                 PRIMARY KEY(doctor_id, patient_id, appointment_id, medicine_id),
                                                 FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
                                                 FOREIGN KEY (doctor_id) REFERENCES Doctor (doctor_id),
                                                 FOREIGN KEY (appointment_id) REFERENCES Appointment (appointment_id)
                                                )""")

        insert_rooms = (
            "INSERT INTO Record(doctor_id , patient_id, appointment_id, medicine_id, medicine_timing, medicine_amount, disease) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Record.csv")

create_record_table();

####### STAFF AND NURSE CAN BE ADDED ############
########################## QUERIES ##########################

# doctors list query
db_cursor.execute("""SELECT *
                    FROM Doctor""")
doctors_list = db_cursor.fetchall()


# administrators list query
db_cursor.execute("""SELECT *
                    FROM Administrator""")
administrators_list = db_cursor.fetchall()


############################## METHODS #######################
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


@app.route('/api/administrators')
def show_administrators():
    #return render_template('index.html', administrators_list=administrators_list)
    # http://127.0.0.1:5000/administrators-list
    global administrators_list  # Assuming doctors_list is available globally
    return jsonify(administrators_list)

@app.route('/api/patients', methods=['GET'])
def get_some_patients():
    # Execute SQL query to fetch patients from the database
    db_cursor.execute("SELECT * FROM Patient")
    patients_list = db_cursor.fetchall()
    print(patients_list)


    # Default limit if not provided in the query parameter
    limit = int(request.args.get('limit', 5))

    # Get the requested number of patients based on the limit
    paginated_patients = patients_list[:limit]

    return jsonify(paginated_patients)


if __name__ == '__main__':
    app.run()
