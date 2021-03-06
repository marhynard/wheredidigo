
var viewer = new Cesium.Viewer('cesiumContainer',{
    animation : false,
    timeline : false
});
var pointslist = {{test1|tojson}};

var glowingLine = viewer.entities.add({
    name : 'Glowing blue line on the surface',
    polyline : {
    //positions : Cesium.Cartesian3.fromDegreesArray([-75, 37,-95, 36,-125, 37]),
    positions : Cesium.Cartesian3.fromDegreesArray(pointslist),
    width : 10,
    material : new Cesium.PolylineGlowMaterialProperty({
                                                        glowPower : 0.2,
                                                        color : Cesium.Color.ORANGE
            })
        }
    });

viewer.zoomTo(viewer.entities);
