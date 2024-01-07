import {Component, OnInit} from '@angular/core';
import {Doctor} from "../doctors-list/Doctor";
import {DoctorsService} from "../doctors-list/doctors.service";
import {Patient} from "./Patient";
import {PatientsService} from "./patients.service";

@Component({
  selector: 'app-patient-list',
  templateUrl: './patient-list.component.html',
  styleUrls: ['./patient-list.component.css']
})
export class PatientListComponent implements OnInit{
  patients: Patient[];

  constructor(private patientsService: PatientsService) {
  }

  ngOnInit(): void {
  this.patientsService.getPatients()
    .subscribe((data: any[]) => {
      this.patients = data.map(patientData => {
        return new Patient(
          patientData[0],
          patientData[1],
          patientData[2],
          patientData[3],
          patientData[4],
          patientData[5],
          patientData[6],
          patientData[7],
          patientData[8]
        );
      });
      console.log(this.patients); // Ensure Doctor instances are created
    });
  }
}
