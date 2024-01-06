import { Component, OnInit } from '@angular/core';
import {DoctorsService} from "./doctors.service";
@Component({
  selector: 'app-doctors-list',
  templateUrl: './doctors-list.component.html',
  styleUrls: ['./doctors-list.component.css']
})
export class DoctorsListComponent implements OnInit {
  doctors: any[];

  constructor(private doctorsService: DoctorsService) {
  }

  ngOnInit(): void {
    this.getDoctors();
  }

  getDoctors(): void {
    this.doctorsService.getDoctors()
      .subscribe((data) => {
        this.doctors = data;
        console.log(this.doctors); // Do something with the data
      });
  }
}
