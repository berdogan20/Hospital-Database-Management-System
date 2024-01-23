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
  order_by: string = 'department_rating'; // Default order by department rating
  order_direction: string = 'asc'; // Default order direction is ascending

  constructor(private departmentsService: DepartmentsService) {}

  ngOnInit() {
    this.filters = {}; // Initialize filters
    this.fetchDepartments();
  }

  fetchDepartments() {
    const params = {
      ...this.filters,
      order_by: this.order_by,
      order_direction: this.order_direction
    };

    this.departmentsService.getDepartments(params)
      .subscribe((data: any[]) => {
        this.departments = data;
      });
  }

  applyOrder() {
    this.fetchDepartments();
  }

  applyFilters() {

    this.fetchDepartments();
    console.log(this.filters.department_administrator_name)
  }

  clearFilters() {
    this.filters = {}; // Reset filters
    this.fetchDepartments();
  }

  protected readonly parseInt = parseInt;
}
