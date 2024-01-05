import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorsListItemComponent } from './doctors-list-item.component';

describe('DoctorsListItemComponent', () => {
  let component: DoctorsListItemComponent;
  let fixture: ComponentFixture<DoctorsListItemComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DoctorsListItemComponent]
    });
    fixture = TestBed.createComponent(DoctorsListItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
