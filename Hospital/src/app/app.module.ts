import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http'; // Import HttpClientModule
import { RouterModule } from '@angular/router';
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
import { WelcomeComponent } from './welcome/welcome.component';
import {FormsModule} from "@angular/forms";
import { MenuComponent } from './menu/menu.component';
import { DepartmentsListComponent } from './departments-list/departments-list.component';
import { NursesListComponent } from './nurses-list/nurses-list.component';
import { AppointmentsListComponent } from './appointments-list/appointments-list.component';

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
    AddDoctorComponent,
    WelcomeComponent,
    MenuComponent,
    DepartmentsListComponent,
    NursesListComponent,
    AppointmentsListComponent,
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
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
