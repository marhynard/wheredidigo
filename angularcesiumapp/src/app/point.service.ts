import { Injectable } from '@angular/core';
import {Http, Response} from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
// Import RxJs required methods
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

import { Point } from './point';
//import { POINTS } from './mock-points';

@Injectable()
export class PointService {

  constructor(private http:Http) { }
  
  getPoints(): Observable<Point[]> {
    return this.http.get("./getpoints")
                        .map((res:Response) => res.json())
                        .catch((error:any) => Observable.throw(error.json().error || 'Server error'));

    }

}
