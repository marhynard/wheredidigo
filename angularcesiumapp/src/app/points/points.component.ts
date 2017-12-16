import { Component, OnInit } from '@angular/core';
import { Point } from '../../utils/services/dataProvider/point.model';
import { PointService } from '../../utils/services/dataProvider/point.service';

@Component({
  selector: 'app-points',
  templateUrl: './points.component.html',
  styleUrls: ['./points.component.css']
})
export class PointsComponent implements OnInit {
	
	points: Point[];


  constructor(private pointService: PointService) { }

  ngOnInit() {
  this.getPoints();
  }

  getPoints(): void {
	this.pointService.getPoints().subscribe(points => this.points = points);
	}
  
}
