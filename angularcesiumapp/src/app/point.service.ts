import { Injectable } from '@angular/core';
import {Http, Response} from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';

import { Point } from './point';
import { POINTS } from './mock-points';

@Injectable()
export class PointService {

  constructor(private _http:Http) { }
  
  getPoints(): Observable<Point[]> {
  
  
  
  return of(POINTS);
}

  getAllPoints()
  {
    return this._http
          .get("./getpoints")
          .map(r => <Point>r.json())
  }


}
