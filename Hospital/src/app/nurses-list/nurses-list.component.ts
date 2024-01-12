import { Component } from '@angular/core';
import {NursesService} from "./nurses.service";
import {specializations} from "../doctors-list/specializations";

@Component({
  selector: 'app-nurses-list',
  templateUrl: './nurses-list.component.html',
  styleUrls: ['./nurses-list.component.css']
})
export class NursesListComponent {
  nurses: any[] = [];
  departments: string[] = specializations
  filters: any = {}; // Define filters here

  constructor(private nursesService: NursesService) {}

  ngOnInit() {
    this.filters = {}; // Initialize filters
    this.fetchNurses();
  }

  fetchNurses() {
    this.nursesService.getNurses(this.filters)
      .subscribe((data: any[]) => {
        this.nurses = data;
      });
  }

  applyFilters() {

    this.fetchNurses();
  }

  clearFilters() {
    this.filters = {}; // Reset filters
    this.fetchNurses();
  }
}
