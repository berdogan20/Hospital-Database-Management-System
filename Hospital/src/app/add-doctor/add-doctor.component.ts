import { Component } from '@angular/core';
import {specializations} from "../doctors-list/specializations";
import {Doctor} from "../doctors-list/Doctor";
import {DoctorsService} from "../doctors-list/doctors.service";

@Component({
  selector: 'app-add-doctor',
  templateUrl: './add-doctor.component.html',
  styleUrls: ['./add-doctor.component.css']
})
export class AddDoctorComponent {

  departments: string[] = specializations;
  newDoctor: Doctor = {
      doctor_id: '',
      fname: '',
      lname: '',
      gender: '',
      specialization: '',
      phone_number: '',
      department_id: '',
      email: ''
    };

  constructor(private doctorsService: DoctorsService) {}

  onSubmitNewDoctor() {
    this.doctorsService.addDoctor(this.newDoctor).subscribe(
      (response) => {
        console.log('New doctor added:', response);
        // Optionally, perform any actions upon successful addition
      },
      (error) => {
        console.error('Error adding doctor:', error);
        // Handle error scenarios appropriately
      }
    );
  }
}
