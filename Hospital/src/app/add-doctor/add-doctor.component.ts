import { Component } from '@angular/core';
import {specializations} from "../doctors-list/specializations";
import {DoctorsService} from "../doctors-list/doctors.service";
import {AddDoctorService} from "./add-doctor.service";

@Component({
  selector: 'app-add-doctor',
  templateUrl: './add-doctor.component.html',
  styleUrls: ['./add-doctor.component.css']
})
export class AddDoctorComponent {
  departments: string[] = specializations
  doctorData: any = {};
  submitting = false;
  responseMessage: string | null = null;

  constructor(private addDoctorService: AddDoctorService) {}

  submitForm() {
    console.log(this.doctorData)
    this.submitting = true;
    this.responseMessage = null;

    this.addDoctorService.addDoctor(this.doctorData).subscribe(
      response => {
        console.log('Doctor added successfully:', response);
        this.responseMessage = 'Doctor added successfully';
      },
      error => {
        console.error('Error adding doctor:', error);
        this.responseMessage = 'Error adding doctor';
      }
    ).add(() => {
      this.submitting = false;
    });
  }
}
