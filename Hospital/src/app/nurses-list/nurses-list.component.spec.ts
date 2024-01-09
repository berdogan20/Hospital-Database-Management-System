import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NursesListComponent } from './nurses-list.component';

describe('NursesListComponent', () => {
  let component: NursesListComponent;
  let fixture: ComponentFixture<NursesListComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [NursesListComponent]
    });
    fixture = TestBed.createComponent(NursesListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
