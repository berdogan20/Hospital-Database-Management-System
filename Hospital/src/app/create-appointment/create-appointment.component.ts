import {Component, OnInit} from '@angular/core';
import {DoctorsService} from "../doctors-list/doctors.service";
import {ActivatedRoute} from "@angular/router";
import {specializations} from "../doctors-list/specializations";
import {AddDoctorService} from "../add-doctor/add-doctor.service";
import {CreateAppointmentService} from "./create-appointment.service";

@Component({
  selector: 'app-create-appointment',
  templateUrl: './create-appointment.component.html',
  styleUrls: ['./create-appointment.component.css']
})
export class CreateAppointmentComponent implements OnInit{
  patient_id: string = "not loaded yet"
  doctors: any[] = []
  filters: any = {}; // Define filters here

  constructor(private route: ActivatedRoute,
              private doctorsService: DoctorsService,
              private createAppointmentService: CreateAppointmentService) {}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.patient_id = params.get('patient_id');
      this.filters = {}; // Update filters assignment
    });
   this.fetchDoctors()
  }

  fetchDoctors() {
    this.doctorsService.getDoctors(this.filters)
      .subscribe((data: any[]) => {
        this.doctors = data;
      });
    console.log(this.doctors)
  }


  appointmentData: any = {};
  submitting = false;
  responseMessage: string | null = null;


  submitForm() {
    console.log(this.appointmentData)
    this.submitting = true;
    this.responseMessage = null;

    this.appointmentData.patient_id = this.patient_id
    this.createAppointmentService.addAppointment(this.appointmentData).subscribe(
      response => {
        console.log('Appointment added successfully:', response);
        this.responseMessage = 'Appointment added successfully';
      },
      error => {
        console.error('Error adding Appointment:', error);
        this.responseMessage = 'Error adding Appointment';
      }
    ).add(() => {
      this.submitting = false;
    });
  }
}
