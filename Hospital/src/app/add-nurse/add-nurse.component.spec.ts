import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddNurseComponent } from './add-nurse.component';

describe('AddNurseComponent', () => {
  let component: AddNurseComponent;
  let fixture: ComponentFixture<AddNurseComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AddNurseComponent]
    });
    fixture = TestBed.createComponent(AddNurseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
