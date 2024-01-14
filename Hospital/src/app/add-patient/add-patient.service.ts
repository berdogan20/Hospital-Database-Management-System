import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AddPatientService {
  private apiUrl = 'http://127.0.0.1:5000/api/patients';

  constructor(private http: HttpClient) { }

  addData(data: any): Observable<any> {
    return this.http.post(this.apiUrl, data);
  }
}
