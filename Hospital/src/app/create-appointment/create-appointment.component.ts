import {Component, OnInit} from '@angular/core';
import {DoctorsService} from "../doctors-list/doctors.service";
import {PatientsService} from "../patient-list/patients.service";
import {forkJoin} from "rxjs";
import {DoctorsListComponent} from "../doctors-list/doctors-list.component";

@Component({
  selector: 'app-create-appointment',
  templateUrl: './create-appointment.component.html',
  styleUrls: ['./create-appointment.component.css']
})
export class CreateAppointmentComponent implements OnInit{
  doctors: any[] = []
  patients: any[] = []
  filters: any = {}; // Define filters here


  ngOnInit() {
    this.filters = {}; // Initialize filters

  }


}
