import {Component, Input, OnInit} from '@angular/core';
import {Doctor} from "../doctors-list/Doctor";

@Component({
  selector: 'app-doctors-list-item',
  templateUrl: './doctors-list-item.component.html',
  styleUrls: ['./doctors-list-item.component.css']
})
export class DoctorsListItemComponent implements OnInit{
  @Input() doctor: Doctor;

  ngOnInit(): void {
    console.log(this.doctor); // Log doctor in ngOnInit
    // You can perform other initialization or operations involving this.doctor here
  }
}
