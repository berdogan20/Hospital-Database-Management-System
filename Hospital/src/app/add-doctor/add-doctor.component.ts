import { Component } from '@angular/core';
import {specializations} from "../doctors-list/specializations";
import {DoctorsService} from "../doctors-list/doctors.service";

@Component({
  selector: 'app-add-doctor',
  templateUrl: './add-doctor.component.html',
  styleUrls: ['./add-doctor.component.css']
})
export class AddDoctorComponent {

  departments: string[] = specializations

}
