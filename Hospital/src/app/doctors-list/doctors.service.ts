import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

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

  deleteDoctor(doctorId: string): Observable<any> {
    console.log("service : ", doctorId) // S031
    const deleteUrl = `${this.apiUrl}/${doctorId}`;
    console.log(deleteUrl) // http://127.0.0.1:5000/api/doctors/S031
    return this.http.delete<any>(deleteUrl);
  }

}
