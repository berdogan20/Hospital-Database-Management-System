import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule
import { RouterModule } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PatientListComponent } from './patient-list/patient-list.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { DoctorsListComponent } from './doctors-list/doctors-list.component';
import { DoctorProfileComponent } from './doctor-profile/doctor-profile.component';
import { CreateAppointmentComponent } from './create-appointment/create-appointment.component';
import { AddDoctorComponent } from './add-doctor/add-doctor.component';
import { WelcomeComponent } from './welcome/welcome.component';
import {FormsModule} from "@angular/forms";
import {MenuComponent} from "./menu/menu.component";
import {AppointmentsListComponent} from "./appointments-list/appointments-list.component";
import {NursesListComponent} from "./nurses-list/nurses-list.component";
import {DepartmentsListComponent} from "./departments-list/departments-list.component";
import { AddPatientComponent } from './add-patient/add-patient.component';
import { AddNurseComponent } from './add-nurse/add-nurse.component';
import { PatientProfileComponent } from './patient-profile/patient-profile.component';

@NgModule({
  declarations: [
    AppComponent,
    PatientListComponent,
    NotFoundComponent,
    DoctorsListComponent,
    DoctorProfileComponent,
    CreateAppointmentComponent,
    AddDoctorComponent,
    WelcomeComponent,
    MenuComponent,
    DepartmentsListComponent,
    NursesListComponent,
    AppointmentsListComponent,
    AddPatientComponent,
    AddNurseComponent,
    PatientProfileComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([
      { path: '', component: WelcomeComponent, pathMatch: 'full' },
      { path: 'welcome', component: WelcomeComponent },
      { path: 'menu', component: MenuComponent},
      { path: 'doctors', component: DoctorsListComponent },
      { path: 'patients', component: PatientListComponent},
      { path: 'appointments', component: AppointmentsListComponent },
      { path: 'nurses', component: NursesListComponent },
      { path: 'departments', component: DepartmentsListComponent },
      { path: 'add-doctor', component: AddDoctorComponent },
      { path: 'add-patient', component: AddPatientComponent },
      { path: 'add-nurse', component: AddNurseComponent },
      { path: 'add-appointment/:patient_id', component: CreateAppointmentComponent },
      { path: 'doctor-profile/:doctor_id', component: DoctorProfileComponent},
      { path: 'patient-profile/:patient_id', component: PatientProfileComponent},
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
