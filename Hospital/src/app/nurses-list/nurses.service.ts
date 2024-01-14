import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class NursesService {
  private apiUrl = 'http://127.0.0.1:5000/api/nurses';
  constructor(private http: HttpClient) {}

  getNurses(filters: any): Observable<any[]> {
  // Use HttpClient to make GET request with filters
  return this.http.get<any[]>(this.apiUrl, { params: filters });
  }
}
