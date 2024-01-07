import { Component, OnInit } from '@angular/core';
import {DoctorsService} from "./doctors.service";
import {Doctor} from "./Doctor";

@Component({
  selector: 'app-doctors-list',
  templateUrl: './doctors-list.component.html',
  styleUrls: ['./doctors-list.component.css']
})
export class DoctorsListComponent implements OnInit {
  doctors: Doctor[];

  constructor(private doctorsService: DoctorsService) {
  }

  ngOnInit(): void {
  this.doctorsService.getDoctors()
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

}
