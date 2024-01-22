import { Component, OnInit } from '@angular/core';
import {DoctorsService} from "./doctors.service";
import {specializations} from "./specializations";

@Component({
  selector: 'app-doctors-list',
  templateUrl: './doctors-list.component.html',
  styleUrls: ['./doctors-list.component.css']
})
export class DoctorsListComponent implements OnInit {
  doctors: any[] = [];
  departments: string[] = specializations;
  filters: any = {}; // Define filters here

  constructor(private doctorsService: DoctorsService) {}
  ngOnInit() {
    this.filters = {}; // Initialize filters
    this.fetchDoctors();
  }
  fetchDoctors() {
    this.doctorsService.getDoctors(this.filters)
      .subscribe((data: any[]) => {
        this.doctors = data;
      });
  }
  applyFilters() {
    // Call fetchAppointments to apply updated filters
    this.fetchDoctors();
  }

  clearFilters() {
    this.filters = {}; // Reset filters
    this.fetchDoctors(); // Fetch doctors without filters
  }

  onDeleteDoctor(doctorId: string) {
    this.doctorsService.deleteDoctor(doctorId).subscribe(() => {
      // Refresh the list after deletion
      console.log("doctor_id: ", doctorId)
      this.fetchDoctors();
    });
  }

}
