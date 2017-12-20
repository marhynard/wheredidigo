//This file contains the "model" for what a point contains.

export class Point {
    constructor(
        public filename : string,
        public activitytype : number,
        //altitude: number;
        //cadence: number;
        //distance: number;
        //enhanced_altitude: number;
        //enhanced_speed: number; 
        //fractional_cadence: number;
        //position_lat: number;
        //position_long: number;
        //speed: number;    
        //timestamp: string;
        public position: Position
    ){}
  
 
}

export class Position {
    constructor(
        public lat: number,
        public long: number,
        public alt: number
    ){}
  
}