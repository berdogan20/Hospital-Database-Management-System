import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from "@angular/common/http";
import { Observable } from "rxjs";
import { Patient } from "./Patient";

@Injectable({
  providedIn: 'root'
})
export class PatientsService {
  private apiUrl = 'http://127.0.0.1:5000/api/patients';

  constructor(private http: HttpClient) { }

  getPatients(entriesPerPage: number): Observable<Patient[]> {
    // Create query parameters to pass the 'entriesPerPage' value
    const params = new HttpParams().set('limit', entriesPerPage.toString());

    // Use the query parameters in the HTTP request
    return this.http.get<Patient[]>(this.apiUrl, { params });
  }
}

