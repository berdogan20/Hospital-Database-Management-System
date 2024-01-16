import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { specializations } from "../doctors-list/specializations";
import { DoctorsService } from "../doctors-list/doctors.service";
import { DoctorDetailService } from "./doctor-detail.service";

@Component({
  selector: 'app-doctor-profile',
  templateUrl: './doctor-profile.component.html',
  styleUrls: ['./doctor-profile.component.css']
})
export class DoctorProfileComponent implements OnInit {
  doctor_id: string = "Not Loaded";
  doctorDetail: any[] = [];
  filters: any = {}; // Define filters as an array

  constructor(private route: ActivatedRoute, private doctorDetailService: DoctorDetailService) {}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.doctor_id = params.get('doctor_id');
      this.filters = {doctor_id: this.doctor_id}; // Update filters assignment
      console.log(this.filters)
      this.fetchDoctorDetail();
    });
  }

  fetchDoctorDetail() {
    this.doctorDetailService.getDoctorDetail(this.filters)
      .subscribe((data: any[]) => {
        this.doctorDetail = data;
        console.log(this.doctorDetail); // Move inside subscribe block
      });
  }
}
