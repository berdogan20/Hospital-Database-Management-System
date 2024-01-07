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
# db_cursor.execute("DROP DATABASE hospital")

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
        populate_table(db_connection, db_cursor, insert_doctors, "InitialData/Doctors.csv")

create_doctor_table()

# administrator table
def create_administrator_table():
    table_name = "Administrator"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Administrator( department_id CHAR(10) NOT NULL,  
                                                         admin_id CHAR(15) NOT NULL, 
                                                         phone_number CHAR(15), 
                                                         fname CHAR(50), 
                                                         lname CHAR(50), 
                                                         email CHAR(50), 
                                                         PRIMARY KEY (admin_id))""")
        insert_administrators = (
            "INSERT INTO Administrator(department_id, admin_id, phone_number, fname, lname, email) "
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_administrators, "InitialData/Administrator.csv")

create_administrator_table()

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
        populate_table(db_connection, db_cursor, insert_patients, "InitialData/Patient.csv")


create_patient_table()
































########################## QUERIES ##########################

# doctors list query
db_cursor.execute("""SELECT *
                    FROM Doctor""")
doctors_list = db_cursor.fetchall()


# administrators list query
db_cursor.execute("""SELECT *
                    FROM Administrator""")
administrators_list = db_cursor.fetchall()

# patients list query
db_cursor.execute("""SELECT *
                    FROM Patient""")
patients_list = db_cursor.fetchall()









##############################
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

@app.route('/api/patients')
def show_patients():
    global patients_list  # Assuming doctors_list is available globally
    return jsonify(patients_list)

if __name__ == '__main__':
    app.run()
