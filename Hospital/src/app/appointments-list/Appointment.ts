export class Appointment {
  appointment_id: string;
  start_time: string;
  end_time: string;
  date: string;
  doctor_id: string;
  patient_id: string;

  constructor(
    appointment_id: string,
    start_time: string,
    end_time: string,
    date: string,
    doctor_id: string,
    patient_id: string
  ) {
    this.appointment_id = appointment_id;
    this.start_time = start_time;
    this.end_time = end_time;
    this.date = date;
    this.doctor_id = doctor_id;
    this.patient_id = patient_id;
  }
}
