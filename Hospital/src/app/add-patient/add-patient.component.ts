import { Component } from '@angular/core';
import {specializations} from "../doctors-list/specializations";
import {AddDoctorService} from "../add-doctor/add-doctor.service";
import {AddPatientService} from "./add-patient.service";

@Component({
  selector: 'app-add-patient',
  templateUrl: './add-patient.component.html',
  styleUrls: ['./add-patient.component.css']
})
export class AddPatientComponent {
  data: any = {};
  submitting = false;
  responseMessage: string | null = null;

  constructor(private addPatientService: AddPatientService) {}

  submitForm() {
    console.log(this.data)
    this.submitting = true;
    this.responseMessage = null;

    this.addPatientService.addData(this.data).subscribe(
      response => {
        console.log('Patient added successfully:', response);
        this.responseMessage = 'Patient added successfully';
      },
      error => {
        console.error('Error adding Patient:', error);
        this.responseMessage = 'Error adding Patient';
      }
    ).add(() => {
      this.submitting = false;
    });
  }
}
