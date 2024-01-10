
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

create_record_table()