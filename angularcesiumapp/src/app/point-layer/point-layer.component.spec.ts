import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PointLayerComponent } from './point-layer.component';

describe('PointLayerComponent', () => {
  let component: PointLayerComponent;
  let fixture: ComponentFixture<PointLayerComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PointLayerComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PointLayerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
