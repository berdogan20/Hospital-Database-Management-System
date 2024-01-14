import { TestBed } from '@angular/core/testing';

import { AddNurseService } from './add-nurse.service';

describe('AddNurseService', () => {
  let service: AddNurseService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AddNurseService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
