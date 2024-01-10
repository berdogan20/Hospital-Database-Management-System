import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Doctor} from "./Doctor";

@Injectable({
  providedIn: 'root'
})
export class DoctorsService {
   private apiUrl = 'http://127.0.0.1:5000/api/doctors';
  constructor(private http: HttpClient) {}

  getDoctors(filters: any): Observable<any[]> {
  // Use HttpClient to make GET request with filters
  return this.http.get<any[]>(this.apiUrl, { params: filters });
  }


  addDoctor(newDoctor: Doctor): Observable<Doctor> {
    return this.http.post<Doctor>(this.apiUrl, newDoctor);
  }
}
