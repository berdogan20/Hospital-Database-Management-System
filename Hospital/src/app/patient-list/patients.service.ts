import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from "@angular/common/http";
import { Observable } from "rxjs";
import { Patient } from "./Patient";

@Injectable({
  providedIn: 'root'
})
export class PatientsService {
  private apiUrl = 'http://127.0.0.1:5000/api/patients';

  constructor(private http: HttpClient) {}

  getPatients(filters: any): Observable<any[]> {
  // Use HttpClient to make GET request with filters
  return this.http.get<any[]>(this.apiUrl, { params: filters });
  }
}

