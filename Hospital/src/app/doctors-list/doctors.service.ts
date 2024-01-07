import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Doctor} from "./Doctor";

@Injectable({
  providedIn: 'root'
})
export class DoctorsService {
  private doctorsUrl = 'http://127.0.0.1:5000/api/doctors'; // Your Flask API URL

  constructor(private http: HttpClient) { }

  getDoctors(): Observable<Doctor[]> {
    return this.http.get<Doctor[]>(this.doctorsUrl);
  }
}
