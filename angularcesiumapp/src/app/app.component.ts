import { Component, OnInit } from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/map';
import { Point } from './point';
import { PointService } from './point.service';
import { MapsManagerService } from '../../node_modules/angular-cesium/src/angular-cesium/services/maps-manager/maps-manager.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit  {
 
    points: Point[];
  
    constructor(mapsManagerService: MapsManagerService,private _http:Http,private pointService: PointService) {
        const viewer = mapsManagerService.getMap().getCesiumViewer();
        
        /*var glowingLine = viewer.entities.add({
    name : 'Glowing blue line on the surface',
    polyline : {
    positions : Cesium.Cartesian3.fromDegreesArray([-75, 37,-95, 36,-125, 37]),
    //positions : Cesium.Cartesian3.fromDegreesArray(pointslist),
    width : 10,
    material : new Cesium.PolylineGlowMaterialProperty({
                                                        glowPower : 0.2,
                                                        color : Cesium.Color.ORANGE
            })
        }
    });
        */
        this.c1.name = "eli";
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
