import { Component, OnInit,AfterViewInit } from '@angular/core';
import {Http, Response} from '@angular/http';
import {Observable} from 'rxjs';
import 'rxjs/add/operator/map';
import { Point } from '../utils/services/dataProvider/point.model';
import { PointService } from '../utils/services/dataProvider/point.service';
import { MapsManagerService } from 'angular-cesium';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit,AfterViewInit  {
 
    points: Point[];
    cesiumViewer;
    runPoints;
    ridePoints;
    otherPoints;

    
    constructor(private _http:Http,
                private pointService: PointService,
                /*private mapsManagerService: MapsManagerService*/) {
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
        //this.getPoints();
    }
   
    ngAfterViewInit(){
        //this.getPoints();
       //const cesiumViewer = this.mapsManagerService.getMap().getCesiumViewer()
         /*console.log("got viewer");

        this.runPoints = new Cesium.PointPrimitiveCollection();
        this.ridePoints = new Cesium.PointPrimitiveCollection();
        this.otherPoints = new Cesium.PointPrimitiveCollection();
        console.log("created primitives");
        
        
        
        
        console.log("got points");
        this.addPointCollection();
        console.log("added collections");
        
        
        cesiumViewer.scene.primitives.add(this.runPoints);
        cesiumViewer.scene.primitives.add(this.ridePoints);
        cesiumViewer.scene.primitives.add(this.otherPoints);
        console.log("added primitives");*/
        /*
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
    });*/
        
    }
  
    getPoints(): void {
        this.pointService.getPoints().subscribe(points => this.points = points);
	}
  /*
    addPointCollection(): void{
	
    //var t = js_data;
    //var tmp=JSON.parse(js_data);
	//console.log(this.points.length)
	var x;
    for(x in this.points){
        
        var z=this.points[x];
		var filename = z.filename;
		var type = z.activitytype;
        var lat= z.position.lat; //  * ( 180 / power );
        var lon= z.position.long; //  * ( 180 / power );
		//var alt = z.altitude;
		console.log(filename);
		if(type == 0){
			if( otherFileList.indexOf(filename) < 0){
				otherFileList.push(filename);	
			}
			
			this.otherPoints.add({
				position : new Cesium.Cartesian3.fromDegrees(lon,lat),
				pixelSize : 5,
				color : Cesium.Color.YELLOW
			});
		}
		if(type == 1){
			if( rideFileList.indexOf(filename) < 0){
				rideFileList.push(filename);	
			}
			this.ridePoints.add({
				position : new Cesium.Cartesian3.fromDegrees(lon,lat),
				pixelSize : 5,
				color : Cesium.Color.GREEN
			});
		}
		if(type == 2){
			if( runFileList.indexOf(filename) < 0){
				runFileList.push(filename);	
			}
			this.runPoints.add({
				position : new Cesium.Cartesian3.fromDegrees(lon,lat),
				pixelSize : 5,
				color : Cesium.Color.BLUE
			});
		}
		
    }
  
}*/
}
 
