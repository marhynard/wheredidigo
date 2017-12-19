import { Component, OnInit, ViewChild } from '@angular/core';
import { Observable } from 'rxjs';
import { AcNotification } from '../../../node_modules/angular-cesium/src/angular-cesium/models/ac-notification';
import { AcLayerComponent } from '../../../node_modules/angular-cesium/src/angular-cesium/components/ac-layer/ac-layer.component';
import { TracksDataProvider } from '../../utils/services/dataProvider/tracksDataProvider.service';

@Component({
	selector: 'point-layer',
	templateUrl: 'point-layer.component.html',
	styleUrls: ['./point-layer.component.css'],
	providers: [TracksDataProvider]
})
export class PointLayerComponent implements OnInit {
	@ViewChild(AcLayerComponent) layer: AcLayerComponent;

	points$: Observable<AcNotification>;
	Cesium = Cesium;
	show = true;

	constructor(private tracksDataProvider: TracksDataProvider) {
	}

	ngOnInit() {
        console.log("point-layer");
		this.points$ = this.tracksDataProvider.get();
        console.log("got points");
	}

	removeAll() {
		this.layer.removeAll();
	}

	setShow($event: boolean) {
		this.show = $event
	}

}