import { TestBed } from '@angular/core/testing';

import { CreateAppointmentService } from './create-appointment.service';

describe('CreateAppointmentService', () => {
  let service: CreateAppointmentService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CreateAppointmentService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
