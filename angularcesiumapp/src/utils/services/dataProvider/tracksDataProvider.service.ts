import { Injectable } from '@angular/core';
//import { Observable } from 'rxjs/Observable';
import { Observable } from 'rxjs/Rx';
import { ActionType } from '../../../../node_modules/angular-cesium/src/angular-cesium/models/action-type.enum';
import { convertToCesiumObj } from '../dataCovertor/convertToCesiumObject';
import { WebSocketSupplier } from '../webSocketSupplier/webSocketSupplier';
import { Subscriber } from 'rxjs/Subscriber';
import { Point } from './point.model';
import { PointService } from './point.service';

@Injectable()
export class TracksDataProvider {
	//private _socket: SocketIO.Socket;
	points: Point[];

	constructor(private pointService: PointService /*webSocketSupplier: WebSocketSupplier*/) {
		//this._socket = webSocketSupplier.get();
		//this.pointService.getPoints().subscribe(points => this.points = points);
        console.log("inside constructor for tracksDataProvider");
	}

	get() {
        console.log("inside get for tracksDataProvider");
        //this just doesn't seem to be right.  Need to figure out how to create the obsevable stuff
		return Observable.create((observer: Subscriber<any>) => {
			this.pointService.getPoints().subscribe(
            
			points => {
				//this.points = points
				points.forEach(
                    
					(acNotification: any) => {
						let action;
						if (acNotification.action === 'ADD_OR_UPDATE') {
							action = ActionType.ADD_UPDATE;
						}
						else if (acNotification.action === 'DELETE') {
							action = ActionType.DELETE;
						}
                        console.log(action);
						acNotification.actionType = action;
                        console.log(acNotification.entity);
						acNotification.entity = convertToCesiumObj(acNotification.entity);
						observer.next(acNotification);
					}
				);
			},
			err => {
                console.log(err);
			
			});
		});
		/*return Observable.create((observer: Subscriber<any>) => {
			this.pointService.getPoints().subscribe(points => this.points = points);
			this._socket.on('birds', (data: any) => {
				data.forEach(
					(acNotification: any) => {
						let action;
						if (acNotification.action === 'ADD_OR_UPDATE') {
							action = ActionType.ADD_UPDATE;
						}
						else if (acNotification.action === 'DELETE') {
							action = ActionType.DELETE;
						}
						acNotification.actionType = action;
						acNotification.entity = convertToCesiumObj(acNotification.entity);
						observer.next(acNotification);
					});
			});
		});*/
	}
}
