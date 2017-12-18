//This file contains the "model" for what a point contains.

export interface Point {
  filename : string | null;
  activitytype : number | null;
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
  position: Position | null;
 
}

export interface Position {
  lat: number | null;
  long: number | null;
  alt: number | null;
}