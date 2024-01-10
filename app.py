from flask import Flask, request
from flask_mysqldb import MySQL
import mysql.connector
import csv
from flask import jsonify
from flask_cors import CORS
from datetime import timedelta


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="bbmsh899",
  auth_plugin='mysql_native_password'
)

mysql = MySQL(app)

# creating database_cursor to perform SQL operation to run queries
db_cursor = db_connection.cursor(buffered=True)
#db_cursor.execute("DROP DATABASE hospital")


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

# doctor table
def create_doctor_table():
    table_name = "Doctor"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Doctor(doctor_id CHAR(6) NOT NULL, 
                                                   fname VARCHAR(50),
                                                   lname VARCHAR(50),  
                                                   gender CHAR(1), 
                                                   specialization VARCHAR(50), 
                                                   phone_number CHAR(11), 
                                                   department_id CHAR(6), 
                                                   email VARCHAR(50), 
                                                   PRIMARY KEY (doctor_id),
                                                   FOREIGN KEY (department_id) REFERENCES Department (department_id))""")
        insert_doctors = (
            "INSERT INTO Doctor(doctor_id, fname, lname, gender, specialization, phone_number, department_id, email) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_doctors, "InitialData/Doctors.csv")

create_doctor_table()


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



# doctors table


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





####### STAFF AND NURSE CAN BE ADDED ############ SHOULD BE ADDED, DO NOT FORGET TO CHANGE ER MODEL



























########################## QUERIES ##########################




############################## METHODS #######################
@app.route('/')
def hello_world():  # put application's code here
    return "Hello World"

# Routes
@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    global db_cursor

    # Fetch query parameters for filtering
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    gender = request.args.get('gender')
    department = request.args.get('department')

    # Construct the base query
    query = "SELECT * FROM Doctor WHERE 1"

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if fname:
        query += " AND fname LIKE %s"
        params.append(f"{fname}%")  # Add '%' for partial match
    if lname:
        query += " AND lname LIKE %s"
        params.append(f"{lname}%")  # Add '%' for partial match
    if gender:
        query += " AND gender = %s"
        params.append(gender)
    if department:
        query += " AND department_id IN (SELECT department_id FROM Department WHERE department_name = %s)"
        params.append(department)

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    doctors = db_cursor.fetchall()

    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return obj

    doctors = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in
                    doctors]

    # Now jsonify your updated appointments list
    response = jsonify(doctors)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/doctors', methods=['POST'])
def add_doctor():
    # Get the doctor data from the request
    doctor_data = request.json  # Assuming data is sent as JSON

    # Process the doctor data (e.g., store in database)
    # Your logic to add a doctor to the database goes here

    # Return a response (you can echo back the added data or a success message)
    return jsonify({'message': 'Doctor added successfully', 'data': doctor_data}), 200



@app.route('/api/patients', methods=['GET'])
def get_patients():
    global db_cursor

    # Fetch query parameters for filtering
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    sex = request.args.get('sex')
    age = request.args.get('age')
    insurance_details = request.args.get('insurance_details')

    # Construct the base query
    query = "SELECT * FROM Patient WHERE 1"

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if fname:
        query += " AND fname LIKE %s"
        params.append(f"{fname}%")  # Add '%' for partial match
    if lname:
        query += " AND lname LIKE %s"
        params.append(f"{lname}%")  # Add '%' for partial match
    if insurance_details:
        query += " AND insurance_details LIKE %s"
        params.append(f"{insurance_details}%")  # Add '%' for partial match
    if sex:
        query += " AND sex = %s"
        params.append(sex)
    if age:
        query += " AND age = %s"
        params.append(age)

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    patients = db_cursor.fetchall()

    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return obj

    patients = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in patients]

    # Now jsonify your updated patients list
    response = jsonify(patients)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    global db_cursor

    # Fetch query parameters for filtering
    date = request.args.get('date')
    doctor_fname = request.args.get('doctor_fname')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    # Construct the base query
    query = "SELECT * FROM Appointment WHERE 1"

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if date:
        query += " AND date = %s"
        params.append(date)
    if doctor_fname:
        query += " AND doctor_id IN (SELECT doctor_id FROM Doctor WHERE fname = %s)"
        params.append(doctor_fname)
    if start_time:
        query += " AND start_time >= %s"
        params.append(start_time)
    if end_time:
        query += " AND end_time <= %s"
        params.append(end_time)

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    appointments = db_cursor.fetchall()

    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)  # Convert timedelta to string before serialization
        return obj  # Return the object unchanged if it's not a timedelta

    # Assuming appointments is a list of tuples fetched from the database
    # Convert timedelta objects in appointments tuples
    appointments = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in
                    appointments]

    # Now jsonify your updated appointments list
    response = jsonify(appointments)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == '__main__':
    app.run()