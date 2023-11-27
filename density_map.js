// initialize Leaflet
var map = L.map('map').setView({lon: -98.230850, lat: 38.938048}, 4.5);


// add the OpenStreetMap tiles
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '&copy; <a href="https://openstreetmap.org/copyright">OpenStreetMap contributors</a>'
}).addTo(map);

// show the scale bar on the lower left corner
L.control.scale({imperial: true, metric: true}).addTo(map);

// show a marker on the map
//L.marker({lon: 0, lat: 0}).bindPopup('The center of the world').addTo(map);

/*
L.control.textbox = function(opts) { return new L.Control.textbox(opts);}
L.control.textbox({ position: 'bottomleft' }).addTo(map);
*/
var legend = L.control({position: 'bottomright'});

legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'legendbox'),
    grades = [0, 10, 20, 50, 100, 200, 500, 1000],
    labels = [];

    div.innerHTML = "Legend<br>"

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
    return div;
};

function getColor(d) {
    return d > 1000 ? '#800026' :
           d > 500  ? '#BD0026' :
           d > 200  ? '#E31A1C' :
           d > 100  ? '#FC4E2A' :
           d > 50   ? '#FD8D3C' :
           d > 20   ? '#FEB24C' :
           d > 10   ? '#FED976' :
                      '#FFEDA0';
}  

legend.addTo(map);

// adding ZCTA layer onto the map

import ZCTA_population_json from 'ZCTA_population_data.json'; //with path
var json_parsed = $.parseJSON(ZCTA_population_json);
var ZCTA_population_items = json_parsed.Items;

function get_ZCTA_population(zcta_number) {
    for (var i = 1; i < ZCTA_population_items.length; ++i) {
        if (Number(ZCTA_population_items[i][3]) == Number(zcta_number)){
            return ZCTA_population_items[i][0];
        }
    }
}

console.log(get_ZCTA_population("08109"));
/*
var ZCTA_map = L.geoJson(us_ZCTA,{
    onEachFeature: function( _feature, layer){
        layer.bindPopup('<p> Zipcode: '+layer.feature.properties.ZCTA5CE20+'</p><br><p>Population: '+ get_ZCTA_population(layer.feature.properties.ZCTA5CE20)+'</p>');
        layer.on('mouseover', function (e){
            this.openPopup();
        });
    }
}).addTo(map);
*/

// hue based on population of each ZCTA area 

/*
L.geoJSON(us_ZCTA, {
    style: function(feature) {
        switch (features.properties.ZCTA5CE20) {
            case 'Republican': return {color: "#ff0000"};
            case 'Democrat':   return {color: "#0000ff"};
        }
    }
}).addTo(map);

*/
