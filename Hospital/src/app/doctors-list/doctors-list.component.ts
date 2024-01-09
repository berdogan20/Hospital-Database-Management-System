import { Component, OnInit } from '@angular/core';
import {DoctorsService} from "./doctors.service";
import {Doctor} from "./Doctor";
import {Observable, Subscription} from "rxjs";
import {specializations} from "./specializations";

@Component({
  selector: 'app-doctors-list',
  templateUrl: './doctors-list.component.html',
  styleUrls: ['./doctors-list.component.css']
})
export class DoctorsListComponent implements OnInit {
  doctors: Doctor[];
  subscription: Subscription;
  specializations: string[] = specializations;
  selectedSpecialization: string = '';
  selectedGender: string = '';
  selectedFname: string = '';
  selectedLname: string = '';
  constructor(private doctorsService: DoctorsService) {
  }

  ngOnInit(): void {
    this.fetchDoctors();
  }
  fetchDoctors(): void {

    var gender = '';
    if (this.selectedGender == 'Female') {
      gender = "F"
    }
    else if (this.selectedGender == 'Male') {
      gender = "M"
    }
    else {
      gender = ''
    }
    var specialization = '';
    if (this.selectedSpecialization == 'All') {
      specialization = ''
    }
    else {
      specialization = this.selectedSpecialization
    }

    this.subscription = this.doctorsService.getDoctors(gender, specialization)
      .subscribe((data: any[]) => {
        this.doctors = data.map(doctorData => {
          return new Doctor(
            doctorData[0], // doctor_id
            doctorData[1], // gender
            doctorData[2], // lname
            doctorData[3], // specialization
            doctorData[4], // fname
            doctorData[5], // department_id
            doctorData[6], // email
            doctorData[7]  // phone_number
          );
        });
        console.log(this.doctors); // Ensure Doctor instances are created
      });
  }

onFilterChange(): void {
  this.fetchDoctors();
}

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  onFnameChange(value: string): void {
    this.selectedFname = value;

  }

  onLnameChange(value: string): void {
    this.selectedLname = value;
  }




}
