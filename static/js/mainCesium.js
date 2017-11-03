



var viewer = new Cesium.Viewer('cesiumContainer',{
    animation : false,
    timeline : false
});



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
