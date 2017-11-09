
//TODO add a timeline for the viewer
//TODO add the points with time

//TODO create a heatmap based on time selected

//TODO add the ability to toggle tracks


var viewer = new Cesium.Viewer('cesiumContainer',{
    animation : false,
    timeline : false
});
var points = viewer.scene.primitives.add(new Cesium.PointPrimitiveCollection());



//TODO separate the points by tracks(files)
function getPointsList(){
    var t = js_data;
    var tmp=JSON.parse(js_data);

    let power = 2147483648;
    
    let pointslist = [];//[-75, 37,-95, 36,-125, 37];

    for(x in tmp){
    
        var z=tmp[x];
        var lat= z.fields.position_lat; //  * ( 180 / power );
        var lon= z.fields.position_long; //  * ( 180 / power );
        //var alt = z.fields.altitude;
        pointslist.push(lon);
        pointslist.push(lat);
       // pointslist.push(alt);
    }
    return pointslist;
    
}
function addPointCollection(){
	
    var t = js_data;
    var tmp=JSON.parse(js_data);
	
	
    for(x in tmp){
    
        var z=tmp[x];
        var lat= z.fields.position_lat; //  * ( 180 / power );
        var lon= z.fields.position_long; //  * ( 180 / power );
		var alt = z.fields.altitude;
		points.add({
			position : new Cesium.Cartesian3.fromDegrees(lon,lat),
			color : Cesium.Color.YELLOW
		});
    }
    //return points;
    
}

/*
function addPoint() {
    Sandcastle.declare(addPoint);

    viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883),
        point : {
            pixelSize : 10,
            color : Cesium.Color.YELLOW
        }
    });
}

function setPointProperties() {
    Sandcastle.declare(setPointProperties);

    viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883),
        point : {
            show : true, // default
            color : Cesium.Color.SKYBLUE, // default: WHITE
            pixelSize : 10, // default: 1
            outlineColor : Cesium.Color.YELLOW, // default: BLACK
            outlineWidth : 3 // default: 0
        }
    });
}

function changePointProperties() {
    Sandcastle.declare(changePointProperties);

    var entity = viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883, 300000.0),
        point : {
            pixelSize : 2
        }
    });

    var point = entity.point;
    point.pixelSize = 20.0;
    point.color = Cesium.Color.YELLOW.withAlpha(0.33);
}

function addMultiplePoints() {
    Sandcastle.declare(addMultiplePoints);

    viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883),
        point : {
            color : Cesium.Color.RED,
            pixelSize : 8
        }
    });
    viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-80.50, 35.14),
        point : {
            color : Cesium.Color.BLUE,
            pixelSize : 16
        }
    });
    viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-80.12, 25.46),
        point : {
            color : Cesium.Color.LIME,
            pixelSize : 32
        }
    });
}

function scaleByDistance() {
    Sandcastle.declare(scaleByDistance);

    viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883),
        point : {
            // pixelSize will multiply by the scale factor, so in this
            // example the size will range from 20px (near) to 5px (far).
            pixelSize : 10,
            scaleByDistance : new Cesium.NearFarScalar(1.5e2, 2.0, 1.5e7, 0.5)
        }
    });
}

function fadeByDistance() {
    Sandcastle.declare(fadeByDistance);

    viewer.entities.add({
        position : Cesium.Cartesian3.fromDegrees(-75.59777, 40.03883),
        point : {
            pixelSize : 20,
            translucencyByDistance : new Cesium.NearFarScalar(1.5e2, 1.0, 1.5e7, 0.2)
        }
    });
}

Sandcastle.addToolbarMenu([{
    text : 'Add point',
    onselect : function() {
        addPoint();
        Sandcastle.highlight(addPoint);
    }
}, {
    text : 'Set point properties at creation',
    onselect : function() {
        setPointProperties();
        Sandcastle.highlight(setPointProperties);
    }
}, {
    text : 'Change point properties',
    onselect : function() {
        changePointProperties();
        Sandcastle.highlight(changePointProperties);
    }
}, {
    text : 'Add multiple points',
    onselect : function() {
        addMultiplePoints();
        Sandcastle.highlight(addMultiplePoints);
    }
}, {
    text : 'Scale by viewer distance',
    onselect : function() {
        scaleByDistance();
        Sandcastle.highlight(scaleByDistance);
    }
}, {
    text : 'Fade by viewer distance',
    onselect : function() {
        fadeByDistance();
        Sandcastle.highlight(fadeByDistance);
    }
}]);
*/




//TODO add multiple tracks onto the cesium viewer    
/*var glowingLine = viewer.entities.add({
    name : 'Glowing orange line on the surface',
    polyline : {
    //positions : Cesium.Cartesian3.fromDegreesArray([-75, 37,-95, 36,-125, 37]),
    positions : Cesium.Cartesian3.fromDegreesArray(getPointsList()),
    width : 10,
    material : new Cesium.PolylineGlowMaterialProperty({
                                                        glowPower : 0.2,
                                                        color : Cesium.Color.ORANGE
            })
        }
    });*/

addPointCollection();

viewer.zoomTo(viewer.entities);
