# department table
def create_department_table():
    table_name = "Department"
    if not table_exists(table_name):
        # Create Table
        db_cursor.execute("""CREATE TABLE Department( department_id CHAR(10) NOT NULL,  
                                                      department_name VARCHAR(100) NOT NULL, 
                                                      admin_id CHAR(15),
                                                      PRIMARY KEY (department_id),
                                                      FOREIGN KEY (admin_id) REFERENCES Administrator(admin_id))
                                                       """)
        insert_departments = (
            "INSERT INTO Department(department_id, department_name, admin_id) "
            "VALUES (%s, %s, %s)"
        )
        populate_table(db_connection, db_cursor, insert_departments, "InitialData/Department.csv")


create_department_table()


# staff table
def create_staff_table():
    table_name = "Staff"
    if not table_exists(table_name):
        # Create Table
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
        populate_table(db_connection, db_cursor, insert_staff, "InitialData/Staff.csv")


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
        populate_table(db_connection, db_cursor, insert_nurses, "InitialData/Nurse.csv")


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
        populate_table(db_connection, db_cursor, insert_patients, "InitialData/Patient.csv")


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
        populate_table(db_connection, db_cursor, insert_appointments, "InitialData/Appointment.csv")


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
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Room.csv")


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
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Bill.csv")


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
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Attends.csv")


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
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Scheduled-To.csv")


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
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Treats.csv")


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
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Address.csv")


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
        populate_table(db_connection, db_cursor, insert_rooms, "InitialData/Disease.csv")


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
        populate_table(db_connection, db_cursor, insert_records, "InitialData/Record.csv")


create_record_table()