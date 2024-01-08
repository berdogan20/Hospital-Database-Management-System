import {Component, OnDestroy, OnInit} from '@angular/core';
import {Patient} from "./Patient";
import {PatientsService} from "./patients.service";
import {Subscription} from "rxjs";

@Component({
  selector: 'app-patient-list',
  templateUrl: './patient-list.component.html',
  styleUrls: ['./patient-list.component.css']
})
export class PatientListComponent implements OnInit, OnDestroy{
  patients: Patient[];
  subscription: Subscription;
  selectedEntries: number = 5;

  constructor(private patientsService: PatientsService) {
  }

  ngOnInit(): void {
    this.fetchPatients();
  }

  fetchPatients() {
    this.subscription = this.patientsService.getPatients(this.selectedEntries)
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

  onEntriesChange(event: any): void {
    this.selectedEntries = parseInt(event.target.value, 10);
    // Fetch data based on selectedEntries when the dropdown value changes
    this.fetchPatients();
  }

  ngOnDestroy(): void {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }
}
