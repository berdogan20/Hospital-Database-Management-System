import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorCommentComponent } from './doctor-comment.component';

describe('DoctorCommentComponent', () => {
  let component: DoctorCommentComponent;
  let fixture: ComponentFixture<DoctorCommentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DoctorCommentComponent]
    });
    fixture = TestBed.createComponent(DoctorCommentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
