import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AddDoctorService {
  private apiUrl = 'http://127.0.0.1:5000/api/doctors';

  constructor(private http: HttpClient) { }

  addDoctor(doctorData: any): Observable<any> {
    return this.http.post(this.apiUrl, doctorData);
  }
}
