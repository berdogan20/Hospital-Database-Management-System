import { Component } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {PatientDetailService} from "./patient-detail.service";

@Component({
  selector: 'app-patient-profile',
  templateUrl: './patient-profile.component.html',
  styleUrls: ['./patient-profile.component.css']
})
export class PatientProfileComponent {
  patient_id: string = "not loaded yet"
  patientDetail: any = {};
  filters: any = {}; // Define filters as an array

  constructor(private route: ActivatedRoute, private patientDetailService: PatientDetailService) {}

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.patient_id = params.get('patient_id');
      this.filters = {patient_id: this.patient_id}; // Update filters assignment
      console.log(this.filters)
      this.fetchPatientDetail();
    });
  }

  fetchPatientDetail() {
    this.patientDetailService.getPatientDetail(this.filters)
      .subscribe((data: any[]) => {
        this.patientDetail = data;
        console.log(this.patientDetail); // Move inside subscribe block
      });
  }
}
