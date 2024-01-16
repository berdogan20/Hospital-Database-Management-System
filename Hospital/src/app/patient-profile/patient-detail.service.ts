import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class PatientDetailService {
  private apiUrl = 'http://127.0.0.1:5000/api/patient-detail';
  constructor(private http: HttpClient) {}

  getPatientDetail(filters: any): Observable<any[]> {
  // Use HttpClient to make GET request with filters
  return this.http.get<any[]>(this.apiUrl, { params: filters });
  }

}
