import { Component } from '@angular/core';
import {DepartmentsService} from "./departments.service";

@Component({
  selector: 'app-departments-list',
  templateUrl: './departments-list.component.html',
  styleUrls: ['./departments-list.component.css']
})
export class DepartmentsListComponent {
  departments: any[] = [];
  filters: any = {}; // Define filters here

  constructor(private departmentsService: DepartmentsService) {}

  ngOnInit() {
    this.filters = {}; // Initialize filters
    this.fetchDepartments();
  }

  fetchDepartments() {
    this.departmentsService.getDepartments(this.filters)
      .subscribe((data: any[]) => {
        this.departments = data;
      });
  }

  applyFilters() {

    this.fetchDepartments();
    console.log(this.filters.department_administrator_name)
  }

  clearFilters() {
    this.filters = {}; // Reset filters
    this.fetchDepartments();
  }
}
