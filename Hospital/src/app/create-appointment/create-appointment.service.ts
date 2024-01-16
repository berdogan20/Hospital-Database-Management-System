import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class CreateAppointmentService {
  private apiUrl = 'http://127.0.0.1:5000/api/add-appointment';
  constructor(private http: HttpClient) { }
  addAppointment(appointmentData: any): Observable<any> {
    return this.http.post(this.apiUrl, appointmentData);
  }
}
