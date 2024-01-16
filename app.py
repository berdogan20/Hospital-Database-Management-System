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


def create_patient_table():
    table_name = "Patient"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Patient(
                                patient_id CHAR(10) NOT NULL,
                                fname CHAR(15) NOT NULL,
                                lname CHAR(15) NOT NULL,
                                email CHAR(30) NOT NULL,
                                phone_number CHAR(10) NOT NULL,
                                gender CHAR(1) NOT NULL,
                                bdate DATE,
                                address CHAR(120),
                                PRIMARY KEY (patient_id)
                            )""")
        insert_patients = (
            "INSERT INTO Patient(patient_id, fname, lname, email, phone_number, gender, bdate, address)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_patients, "InitialData/Patient.csv")

def create_staff_table():
    table_name = "Staff"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Staff(
                                id CHAR(10) NOT NULL,
                                fname CHAR(15) NOT NULL,
                                lname CHAR(15) NOT NULL,
                                email CHAR(30) NOT NULL,
                                phone_number CHAR(11) NOT NULL,
                                gender CHAR(1) NOT NULL,
                                PRIMARY KEY (id)
                            )""")
        insert_staff = (
            "INSERT INTO Staff(id, fname, lname, email, phone_number, gender)"
            "VALUES (%s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_staff, "InitialData/Staff.csv")

def create_administrator_table():
    table_name = "Administrator"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Administrator(
                                id CHAR(10) NOT NULL,
                                PRIMARY KEY (id),
                                FOREIGN KEY (id) REFERENCES Staff(id) ON DELETE CASCADE
                            )""")
        insert_administrators = (
            "INSERT INTO Administrator(id)"
            "VALUES (%s)"
        )
        populate_table(db_connection, db_cursor, insert_administrators, "InitialData/Administrator.csv")


def create_doctor_table():
    table_name = "Doctor"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Doctor(
                                id CHAR(10) NOT NULL,
                                title CHAR(30),
                                department_id CHAR(10) NOT NULL,
                                PRIMARY KEY (id),
                                FOREIGN KEY (id) REFERENCES Staff(id) ON DELETE CASCADE,
                                FOREIGN KEY (department_id) REFERENCES Department(department_id)
                            )""")

        insert_doctors = (
            "INSERT INTO Doctor(id, title, department_id)"
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_doctors, "InitialData/Doctor.csv")


def create_nurse_table():
    table_name = "Nurse"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Nurse(
                                id CHAR(10) NOT NULL,
                                specialization CHAR(30),
                                department_id CHAR(10) NOT NULL,
                                PRIMARY KEY (id),
                                FOREIGN KEY (id) REFERENCES Staff(id) ON DELETE CASCADE,
                                FOREIGN KEY (department_id) REFERENCES Department(department_id)
                            )""")

        insert_nurses = (
            "INSERT INTO Nurse(id, specialization, department_id)"
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_nurses, "InitialData/Nurse.csv")


def create_department_table():
    table_name = "Department"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Department(
                                department_id CHAR(10) NOT NULL,
                                department_name CHAR(30) NOT NULL,
                                administrator_id CHAR(10) NOT NULL,
                                PRIMARY KEY (department_id),
                                FOREIGN KEY (administrator_id) REFERENCES Administrator(id)
                            )""")
        insert_departments = (
            "INSERT INTO Department(department_id, department_name, administrator_id)"
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_departments, "InitialData/Department.csv")

def create_appointment_record_table():
    table_name = "Appointment_Record"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Appointment_Record(
                                appointment_id CHAR(10) NOT NULL,
                                record_id CHAR(10),
                                date DATE NOT NULL,
                                start_time CHAR(10) NOT NULL,
                                end_time CHAR(10) NOT NULL,
                                insurance_details CHAR(150),
                                patient_id CHAR(10) NOT NULL,
                                doctor_id CHAR(10) NOT NULL,
                                PRIMARY KEY (appointment_id),
                                FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
                                FOREIGN KEY (doctor_id) REFERENCES Doctor(id)
                            )""")
        insert_appointments = (
            "INSERT INTO Appointment_Record(appointment_id, record_id, date, start_time, end_time, insurance_details, patient_id, doctor_id)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_appointments, "InitialData/Appointment_Record.csv")


def create_secretary_table():
    table_name = "Secretary"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Secretary (
                             id CHAR(10) NOT NULL,
                             doctor_id CHAR(10) NOT NULL,
                             PRIMARY KEY (id),
                             FOREIGN KEY (id) REFERENCES Staff(id)
                             ON DELETE CASCADE,
                             FOREIGN KEY (doctor_id) REFERENCES Doctor(id))
                             """)
        insert_secretaries = (
            "INSERT INTO Secretary(id, doctor_id)"
            "VALUES (%s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_secretaries, "InitialData/Secretary.csv")

def create_secretary_language_table():
    table_name = "Secretary_Language"
    if not table_exists(table_name):
        db_cursor.execute("""CREATE TABLE Secretary_Language(
                                secretary_id CHAR(10) NOT NULL,
                                language CHAR(30) NOT NULL,
                                PRIMARY KEY (secretary_id, language),
                                FOREIGN KEY (secretary_id) REFERENCES Secretary(id)
                            )""")
        insert_secretary_languages = (
            "INSERT INTO Secretary_Language(secretary_id, language)"
            "VALUES (%s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_secretary_languages, "InitialData/Secretary_Language.csv")





# Call the functions to create the tables
create_patient_table()
create_staff_table()

create_administrator_table()
create_department_table()
create_doctor_table()
create_nurse_table()
create_secretary_table()

create_appointment_record_table()
create_secretary_language_table()






















########################## QUERIES ##########################




############################## GET METHODS #######################
@app.route('/')
def hello_world():  # put application's code here
    return "Hello World"

@app.route('/api/departments', methods=['GET'])
def get_departments():
    global db_cursor

    # Fetch query parameters for filtering
    department_name = request.args.get('department_name')
    department_administrator_name = request.args.get('department_administrator_name')

    # Construct the base query
    query = ("SELECT * , Staff.fname, Staff.lname "
             "FROM Department "
             "JOIN Staff ON Department.administrator_id = Staff.id "
             "WHERE 1 ")

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if department_name:
        query += " AND department_name LIKE %s"
        params.append(f"{department_name}%")  # Add '%' for partial match
    if department_administrator_name:
        query += " AND administrator_id IN (SELECT id FROM Staff WHERE Staff.fname LIKE %s)"
        params.append(f"{department_administrator_name}%")  # Add '%' for partial match

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    departments = db_cursor.fetchall()

    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)  # Convert timedelta to string before serialization
        return obj  # Return the object unchanged if it's not a timedelta

    departments = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in
               departments]

    # Now jsonify your departments list
    response = jsonify(departments)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/staff', methods=['GET'])
def get_staff():
    global db_cursor
    db_cursor.execute("SELECT * FROM Staff")
    staffs = db_cursor.fetchall()
    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return obj

    staffs = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in
                    staffs]

    print(staffs)
    # Now jsonify your updated doctors list
    response = jsonify(staffs)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    global db_cursor

    # Fetch query parameters for filtering
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    gender = request.args.get('gender')
    department = request.args.get('department')

    # Construct the base query
    query = ("SELECT Staff.*, Doctor.title, Department.department_name "
             "FROM Staff JOIN Doctor ON Staff.id = Doctor.id "
             "JOIN Department ON Doctor.department_id = Department.department_id WHERE 1")

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if fname:
        query += " AND Staff.fname LIKE %s"
        params.append(f"{fname}%")  # Add '%' for partial match
    if lname:
        query += " AND Staff.lname LIKE %s"
        params.append(f"{lname}%")  # Add '%' for partial match
    if gender:
        query += " AND Staff.gender = %s"
        params.append(gender)
    if department:
        query += " AND Department.department_name = %s"
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


    # Now jsonify your updated doctors list
    response = jsonify(doctors)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/api/doctor-detail', methods=['GET'])
def get_doctor_detail_info():
    global db_cursor

    # Fetch query parameters for filtering
    doctor_id = request.args.get('doctor_id')

    query = ("""
        SELECT 
            Doctor.id AS doctor_id,
            Doctor.title AS doctor_title,
            StaffDoctor.fname AS doctor_fname,
            StaffDoctor.lname AS doctor_lname,
            StaffDoctor.email AS doctor_email,
            StaffDoctor.phone_number AS doctor_phone_number,
            Secretary.id AS secretary_id,
            StaffSecretary.fname AS secretary_fname,
            StaffSecretary.lname AS secretary_lname,
            StaffSecretary.email AS secretary_email,
             StaffSecretary.phone_number AS secretary_phone_number,
            Secretary_Language.language AS secretary_language
        FROM Doctor
        LEFT JOIN Secretary ON Doctor.id = Secretary.doctor_id
        LEFT JOIN Staff AS StaffDoctor ON Doctor.id = StaffDoctor.id
        LEFT JOIN Staff AS StaffSecretary ON Secretary.id = StaffSecretary.id
        LEFT JOIN Secretary_Language ON Secretary.id = Secretary_Language.secretary_id
    """)

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if doctor_id:
        query += " WHERE Doctor.id = %s"
        params.append(doctor_id)

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    result = db_cursor.fetchall()

    doctor_details = {}
    for row in result:
        doctor_id = row[0]  # Access the first element of the tuple
        if doctor_id not in doctor_details:
            doctor_details[doctor_id] = {
                'doctor_title': row[1],
                'doctor_fname': row[2],
                'doctor_lname': row[3],
                'doctor_email': row[4],
                'doctor_phone_number': row[5],
                'secretaries': []
            }

        secretary_id = row[6]
        if secretary_id:
            doctor_details[doctor_id]['secretaries'].append({
                'secretary_id': secretary_id,
                'secretary_fname': row[7],
                'secretary_lname': row[8],
                'secretary_email': row[9],
                'secretary_phone_number': row[10],
                'languages': [row[11]] if row[11] else []
            })


    # Now jsonify your updated result
    response = jsonify(doctor_details)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





@app.route('/api/nurses', methods=['GET'])
def get_nurses():
    global db_cursor

    # Fetch query parameters for filtering
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    specialization = request.args.get('specialization')
    gender = request.args.get('gender')
    department = request.args.get('department')

    # Construct the base query
    query = ("SELECT *, Nurse.specialization, Department.department_name "
             "FROM Staff "
             "NATURAL JOIN Nurse "
             "NATURAL JOIN Department "
             "WHERE 1")

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if fname:
        query += " AND Staff.fname LIKE %s"
        params.append(f"{fname}%")  # Add '%' for partial match
    if lname:
        query += " AND Staff.lname LIKE %s"
        params.append(f"{lname}%")  # Add '%' for partial match
    if gender:
        query += " AND Staff.gender = %s"
        params.append(gender)
    if specialization:
        query += " AND Nurse.specialization LIKE %s"
        params.append(specialization)
    if department:
        query += " AND Department.department_name LIKE %s"
        params.append(department)

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    nurses = db_cursor.fetchall()

    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return obj

    nurses = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in
                    nurses]


    # Now jsonify your updated doctors list
    response = jsonify(nurses)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




@app.route('/api/patients', methods=['GET'])
def get_patients():
    global db_cursor

    # Fetch query parameters for filtering
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    gender = request.args.get('gender')
    age = request.args.get('age')

    # Construct the base query
    query = ("SELECT * "
             "FROM Patient"
             " WHERE 1")

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
    if age:
        query += " AND YEAR(CURDATE()) - YEAR(bdate) = %s"
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
    # Fetch query parameters for filtering
    date = request.args.get('date')
    doctor_fname = request.args.get('doctor_fname')
    patient_fname = request.args.get('patient_fname')
    patient_id = request.args.get('patient_id')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    # Construct the base query
    query = ("SELECT Appointment_Record.*, Staff.fname as doctor_fname, Staff.lname as doctor_lname, Patient.fname as patient_fname, Patient.lname as patient_lname "
             "FROM Appointment_Record "
             "JOIN Staff ON Appointment_Record.doctor_id = Staff.id "
             "JOIN Patient ON Appointment_Record.patient_id = Patient.patient_id "
             "WHERE 1")

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if date:
        query += " AND date = %s"
        params.append(date)
    if doctor_fname:
        query += " AND doctor_id IN (SELECT id FROM Staff WHERE fname LIKE %s)"
        params.append(f"{doctor_fname}%")
    if patient_fname:
        query += " AND patient_id IN (SELECT patient_id FROM Patient WHERE fname LIKE %s)"
        params.append(f"{patient_fname}%")
    if patient_id:
        query += " AND patient_id = %s"
        params.append(patient_id)
    if start_time:
        query += " AND start_time >= %s"
        params.append(start_time)
    if end_time:
        query += " AND end_time <= %s"
        params.append(end_time)

    # Execute the query with filters (if any)
    with db_connection.cursor() as db_cursor:
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



@app.route('/api/secretaries', methods=['GET'])
def get_secretaries():
    global db_cursor

    # Fetch query parameters for filtering
    doctor_id = request.args.get('doctor_id')

    # Prepare parameters for the query
    params = []

    # Construct the base query
    query = ("SELECT Staff.* "
             "FROM Secretary, Staff "
             "WHERE Secretary.id = Staff.id ")

    # Check and add filters to the query
    if doctor_id:
        query += " AND doctor_id IN (SELECT id FROM Doctor WHERE id = %s)"
        params.append(doctor_id)

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    secretaries = db_cursor.fetchall()

    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return obj

    secretaries = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in
                    secretaries]


    # Now jsonify your updated doctors list
    response = jsonify(secretaries)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/api/secretary_languages', methods=['GET'])
def get_secretary_languages():
    global db_cursor

    # Fetch query parameters for filtering
    secretary_id = request.args.get('secretary_id')

    # Construct the base query
    query = ("SELECT * FROM Secretary_Language")

    # Prepare parameters for the query
    params = []

    # Check and add filters to the query
    if secretary_id:
        query += " AND secretary_id IN (SELECT id FROM Secretary WHERE id = %s)"
        params.append(secretary_id)

    # Execute the query with filters (if any)
    if params:
        db_cursor.execute(query, tuple(params))
    else:
        db_cursor.execute(query)

    languages = db_cursor.fetchall()

    def serialize_timedelta(obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return obj

    languages = [dict(zip(db_cursor.column_names, (serialize_timedelta(field) for field in row))) for row in
                    languages]


    # Now jsonify your updated doctors list
    response = jsonify(languages)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response










################################# POST METHODS #################################
import uuid
from flask import abort

def generate_unique_id():
    return str(uuid.uuid4())[:10]

@app.route('/api/doctors', methods=['POST'])
def add_doctor():
    global db_connection, db_cursor
    data = request.json  # Assuming the data is sent as JSON in the request body

    # Validate and extract data from the JSON
    fname = data.get('fname')
    lname = data.get('lname')
    email = data.get('email')
    phone_number = data.get('phone_number')
    gender = data.get('gender')
    title = data.get('title')
    department_name = data.get('department_name')

    # Perform validation
    if not all([fname, lname, email, phone_number, gender, title, department_name]):
        return jsonify({"error": "All fields are required"}), 400

    # Fetch the department ID based on the department name
    get_department_id_query = "SELECT department_id FROM Department WHERE department_name = %s"

    try:
        with db_connection.cursor() as cursor:
            cursor.execute(get_department_id_query, (department_name,))
            department_id = cursor.fetchone()
            if department_id:
                id = generate_unique_id()

                # Insert the new staff into the database
                insert_staff_query = (
                    "INSERT INTO Staff(id, fname, lname, email, phone_number, gender)"
                    "VALUES (%s, %s, %s, %s, %s, %s)"
                )

                # Insert the new doctor into the database
                insert_doctor_query = (
                    "INSERT INTO Doctor(id, title, department_id)"
                    "VALUES (%s, %s, %s)"
                )
                cursor.execute(insert_staff_query, (id, fname, lname, email, phone_number, gender))
                cursor.execute(insert_doctor_query, (id, title, department_id[0]))
                db_connection.commit()

                return jsonify({"message": "Doctor added successfully"}), 201
            else:
                return jsonify({"error": "Department not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/nurses', methods=['POST'])
def add_nurses():
    global db_connection, db_cursor
    data = request.json  # Assuming the data is sent as JSON in the request body

    # Validate and extract data from the JSON
    fname = data.get('fname')
    lname = data.get('lname')
    email = data.get('email')
    phone_number = data.get('phone_number')
    gender = data.get('gender')
    specialization = data.get('specialization')
    department_name = data.get('department_name')

    # Perform validation
    if not all([fname, lname, email, phone_number, gender, specialization, department_name]):
        return jsonify({"error": "All fields are required"}), 400

    # Fetch the department ID based on the department name
    get_department_id_query = "SELECT department_id FROM Department WHERE department_name = %s"

    try:
        with db_connection.cursor() as cursor:
            cursor.execute(get_department_id_query, (department_name,))
            department_id = cursor.fetchone()
            if department_id:
                id = generate_unique_id()

                # Insert the new staff into the database
                insert_staff_query = (
                    "INSERT INTO Staff(id, fname, lname, email, phone_number, gender)"
                    "VALUES (%s, %s, %s, %s, %s, %s)"
                )

                # Insert the new nurse into the database
                insert_nurse_query = (
                    "INSERT INTO Nurse(id, specialization, department_id)"
                    "VALUES (%s, %s, %s)"
                )
                cursor.execute(insert_staff_query, (id, fname, lname, email, phone_number, gender))
                cursor.execute(insert_nurse_query, (id, specialization, department_id[0]))
                db_connection.commit()

                return jsonify({"message": "Nurse added successfully"}), 201
            else:
                return jsonify({"error": "Department not found"}), 404

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500



@app.route('/api/patients', methods=['POST'])
def add_patient():
    global db_connection, db_cursor
    data = request.json  # Assuming the data is sent as JSON in the request body

    # Validate and extract data from the JSON
    fname = data.get('fname')
    lname = data.get('lname')
    email = data.get('email')
    phone_number = data.get('phone_number')
    gender = data.get('gender')
    bdate = data.get('bdate')
    address = data.get('address')

    # Perform validation
    if not all([fname, lname, email, phone_number, gender, bdate, address]):
        return jsonify({"error": "All fields are required"}), 400

    try:
        with db_connection.cursor() as cursor:
            patient_id = generate_unique_id()

            # Insert the new staff into the database
            insert_patient_query = (
                "INSERT INTO Patient(patient_id, fname, lname, email, phone_number, gender, bdate, address)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            )

            cursor.execute(insert_patient_query, (patient_id, fname, lname, email, phone_number, gender, bdate, address))
            db_connection.commit()

            return jsonify({"message": "Patient added successfully"}), 201

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500



@app.route('/api/administrator', methods=['POST'])
def add_administrator():
    global db_connection, db_cursor
    data = request.json  # Assuming the data is sent as JSON in the request body

    # Validate and extract data from the JSON
    fname = data.get('fname')
    lname = data.get('lname')
    email = data.get('email')
    phone_number = data.get('phone_number')
    gender = data.get('gender')

    # Perform validation
    if not all([fname, lname, email, phone_number, gender]):
        return jsonify({"error": "All fields are required"}), 400

    try:
        with db_connection.cursor() as cursor:
            id = generate_unique_id()

            # Insert the new staff into the database
            insert_staff_query = (
                "INSERT INTO Staff(id, fname, lname, email, phone_number, gender)"
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )

            # Insert the new administrator into the database
            insert_administrator_query = (
                "INSERT INTO Administrator(id)"
                "VALUES (%s)"
            )
            cursor.execute(insert_staff_query, (id, fname, lname, email, phone_number, gender))
            cursor.execute(insert_administrator_query, (id))
            db_connection.commit()

            return jsonify({"message": "Administrator added successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500









if __name__ == '__main__':
    app.run()