import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignInComponent } from './sign-in/sign-in.component';
import { SignUpComponent } from './sign-up/sign-up.component';
import { PatientListComponent } from './patient-list/patient-list.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { DoctorsListComponent } from './doctors-list/doctors-list.component';
import { DoctorsListItemComponent } from './doctors-list-item/doctors-list-item.component';
import { DoctorProfileComponent } from './doctor-profile/doctor-profile.component';
import { DoctorCommentComponent } from './doctor-comment/doctor-comment.component';
import { CreateAppointmentComponent } from './create-appointment/create-appointment.component';
import { AddDoctorComponent } from './add-doctor/add-doctor.component';

@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    SignUpComponent,
    PatientListComponent,
    NotFoundComponent,
    DoctorsListComponent,
    DoctorsListItemComponent,
    DoctorProfileComponent,
    DoctorCommentComponent,
    CreateAppointmentComponent,
    AddDoctorComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
