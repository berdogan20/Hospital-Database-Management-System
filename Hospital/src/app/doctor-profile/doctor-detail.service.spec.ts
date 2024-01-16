import { TestBed } from '@angular/core/testing';

import { DoctorDetailService } from './doctor-detail.service';

describe('DoctorDetailService', () => {
  let service: DoctorDetailService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DoctorDetailService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
