import { Component, OnInit,AfterViewInit } from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/map';
import { Point } from './point';
import { PointService } from './point.service';
import { MapsManagerService } from 'angular-cesium';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit,AfterViewInit  {
 
    points: Point[];
    cesiumViewer;
    
    constructor(private _http:Http,
                private pointService: PointService,
                private mapsManagerService: MapsManagerService) {
        //const viewer = mapsManagerService.getMap().getCesiumViewer();
        
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
        //this.c1.name = "eli";
    }
   
    ngOnInit() {
        
    }
   
    ngAfterViewInit(){
        //this.getPoints();
        const cesiumViewer = this.mapsManagerService.getMap().getCesiumViewer()
        var glowingLine = cesiumViewer.entities.add({
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
