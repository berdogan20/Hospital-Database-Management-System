import {Component, OnDestroy, OnInit} from '@angular/core';
import {Patient} from "./Patient";
import {PatientsService} from "./patients.service";
import {Subscription} from "rxjs";
import {AppointmentsService} from "../appointments-list/appointments.service";
import {specializations} from "../doctors-list/specializations";

@Component({
  selector: 'app-patient-list',
  templateUrl: './patient-list.component.html',
  styleUrls: ['./patient-list.component.css']
})
export class PatientListComponent implements OnInit{
  patients: any[] = [];
  filters: any = {}; // Define filters here

  constructor(private patientsService: PatientsService) {}

  ngOnInit() {
    this.filters = {}; // Initialize filters
    this.fetchPatients();
  }

  fetchPatients() {
    this.patientsService.getPatients(this.filters)
      .subscribe((data: any[]) => {
        this.patients = data;
      });
  }

  applyFilters() {
    this.fetchPatients();
  }

  clearFilters() {
    this.filters = {}; // Reset filters
    this.fetchPatients(); // Fetch appointments without filters
  }

}
