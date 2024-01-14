import { Component } from '@angular/core';
import {specializations} from "../doctors-list/specializations";
import {AddNurseService} from "./add-nurse.service";

@Component({
  selector: 'app-add-nurse',
  templateUrl: './add-nurse.component.html',
  styleUrls: ['./add-nurse.component.css']
})
export class AddNurseComponent {

    protected readonly departments = specializations;
    data: any = {};
    submitting = false;
    responseMessage: string | null = null;

    constructor(private addNurseService: AddNurseService) {}

    submitForm() {
      console.log(this.data)
      this.submitting = true;
      this.responseMessage = null;

      this.addNurseService.addData(this.data).subscribe(
        response => {
          console.log('Nurse added successfully:', response);
          this.responseMessage = 'Nurse added successfully';
        },
        error => {
          console.error('Error adding Nurse:', error);
          this.responseMessage = 'Error adding Nurse';
        }
      ).add(() => {
        this.submitting = false;
      });
    }
}
