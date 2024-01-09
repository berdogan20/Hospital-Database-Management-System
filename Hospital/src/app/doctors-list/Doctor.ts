export class Doctor {
  constructor(
    public doctor_id: string,
    public fname: string,
    public lname: string,
    public gender: string,
    public specialization: string,
    public phone_number: string,
    public department_id: string,
    public email: string
  ) { }
}
