import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Doctor} from "./Doctor";

@Injectable({
  providedIn: 'root'
})
export class DoctorsService {
  private apiUrl = 'http://127.0.0.1:5000/api/doctors'; // Your Flask API URL

  constructor(private http: HttpClient) { }

  getDoctors(gender?: string, specialization?: string): Observable<Doctor[]> {
    let url = this.apiUrl;

    // Check and construct the URL with query parameters if applicable
    if (gender && specialization) {
      url += `?gender=${gender}&specialization=${specialization}`;
    } else if (gender) {
      url += `?gender=${gender}`;
    } else if (specialization) {
      url += `?specialization=${specialization}`;
    }

    return this.http.get<Doctor[]>(url);
  }
  addDoctor(newDoctor: Doctor): Observable<Doctor> {
    return this.http.post<Doctor>(this.apiUrl, newDoctor);
  }

}
