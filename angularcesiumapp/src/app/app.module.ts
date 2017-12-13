import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AngularCesiumModule } from 'angular-cesium';
import { HttpModule } from '@angular/http';
import { HttpClientModule  } from '@angular/common/http';


import { AppComponent } from './app.component';
import { PointsComponent } from './points/points.component';
import { PointService } from './point.service';


@NgModule({
  declarations: [
    AppComponent,
    PointsComponent
  ],
  imports: [
    BrowserModule,
	HttpModule,
    HttpClientModule,
	AngularCesiumModule.forRoot()
  ],
  providers: [PointService],
  bootstrap: [AppComponent]
})
export class AppModule { }
