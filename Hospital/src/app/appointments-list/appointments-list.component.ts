import { Component, OnInit } from '@angular/core';
import {AppointmentsService} from "./appointments.service";

@Component({
  selector: 'app-appointments-list',
  templateUrl: './appointments-list.component.html',
  styleUrls: ['./appointments-list.component.css']
})
export class AppointmentsListComponent implements OnInit {
  appointments: any[] = [];
  filters: any = {}; // Define filters here

  constructor(private appointmentsService: AppointmentsService) {}

  ngOnInit() {
    this.filters = {}; // Initialize filters
    this.fetchAppointments();
  }

  fetchAppointments() {
    this.appointmentsService.getAppointments(this.filters)
      .subscribe((data: any[]) => {
        this.appointments = data;
      });
  }

  applyFilters() {
    // Call fetchAppointments to apply updated filters
    this.fetchAppointments();
  }

  clearFilters() {
    this.filters = {}; // Reset filters
    this.fetchAppointments(); // Fetch appointments without filters
  }
}
