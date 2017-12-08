import { Injectable } from '@angular/core';

import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';

import { Point } from './point';
import { POINTS } from './mock-points';

@Injectable()
export class PointService {

  constructor() { }
  
  getPoints(): Observable<Point[]> {
  return of(POINTS);
}

}
