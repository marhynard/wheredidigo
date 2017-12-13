import { Component, OnInit } from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/map';
import { PointService } from 'point.service';
//import { MapsManagerService } from 'angular-cesium/src/angular-cesium/services/maps-manager/maps-manager.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit  {
 
  points: Point[];
  
  constructor(private _http:Http,private pointService: PointService) {
    this.c1.name = "eli"

   }
   
     ngOnInit() {
  this.getPoints();
  }
   
  title = 'app';
  c1:Cust = new Cust();
  click1(){
    this.getAllBooks().subscribe(b => this.c1 = b)
  }
 
  getAllBooks()
  {
    return this._http
          .get("./getcust")
          .map(r => <Cust>r.json())
  }
  
  getPoints(): void {
	this.pointService.getPoints().subscribe(points => this.points = points);
	}
  
  
}
 
export class Cust{
    name:string;
    age:number;
    city:string;
}
