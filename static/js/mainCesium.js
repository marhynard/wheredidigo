



var viewer = new Cesium.Viewer('cesiumContainer',{
    animation : false,
    timeline : false
});



function getPointsList(){
    //var n=JSON.parse(data);

    let pointslist = [-75, 37,-95, 36,-125, 37];

    return pointslist;
    
}



    
var glowingLine = viewer.entities.add({
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
    });

viewer.zoomTo(viewer.entities);
