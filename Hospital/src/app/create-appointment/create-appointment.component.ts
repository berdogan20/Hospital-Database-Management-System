import {Component, OnInit} from '@angular/core';
import {DoctorsService} from "../doctors-list/doctors.service";
import {PatientsService} from "../patient-list/patients.service";

@Component({
  selector: 'app-create-appointment',
  templateUrl: './create-appointment.component.html',
  styleUrls: ['./create-appointment.component.css']
})
export class CreateAppointmentComponent implements OnInit{
  doctors: any[] = []
  patients: any[] = []
  filters: any = {}; // Define filters here

  constructor(private doctorsService: DoctorsService,
              private patientsService: PatientsService) {
  }

  ngOnInit()
  {
    this.filters = {}; // Initialize filters
    this.fetchDoctors();
    this.fetchPatients();
  }

  fetchDoctors() {
    this.doctorsService.getDoctors(this.filters)
      .subscribe((data: any[]) => {
        this.doctors = data;
      });
    console.log(this.doctors)
  }


  fetchPatients() {
    this.patientsService.getPatients(this.filters)
      .subscribe((data: any[]) => {
        this.patients = data;
      });
    console.log(this.patients)
  }

}
