//-----------------------| Карта |----------------------------------------------
// Создание опций карты
var mapOptions = {
    center: [60.8823, 68.9831],
    
    maxZoom: 14,
    minZoom: 4,
    zoom: 4,
}

// Создание объекта карты
var map = new L.map('map', mapOptions);

// Создание объекта слоя
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
map.attributionControl.addAttribution('&copy; OpenStreetMap</a>');

// Добавление слоя на карту
map.addLayer(layer);


//-----------------------| Панель инструментов |----------------------------------------------
// FeatureGroup предназначена для хранения редактируемых объектов
var drawnFeatures = new L.FeatureGroup();
map.addLayer(drawnFeatures);

// Создание опций панели инструментов
var options = {
    position: 'topleft',
    draw: {
        marker: false,
        circle: false,
        polyline: false,
        circlemarker: false,
    },
}

// Создание объекта панели инструментов
var drawControl = new L.Control.Draw(options);
map.addControl(drawControl);

// Создание объекта для хранения полигонов из БД
var polygonGroup = L.layerGroup();
map.addLayer(polygonGroup);

//-----------------------| Функционал панели инструментов |----------------------------------------------
// Создаение объекта QWebChannel и функции передающей данные в main.py 
var backend = null;
function showCoords(coords) {
    new QWebChannel(qt.webChannelTransport, function(channel) {
        backend = channel.objects.backend;
        backend.getCoord(coords);
    });
}


// Вызов функции showCoords при создании объекта и его добавление в FeatureGroup
map.on('draw:created', function (e){
    var layer = e.layer;
    if(drawnFeatures && drawnFeatures.getLayers().length!==0){
        drawnFeatures.clearLayers();
    }
    drawnFeatures.addLayer(layer);
    
    showCoords(layer.getLatLngs())
});


function setNewBounds(coords){
    var layers = drawnFeatures.getLayers();
    layers[0].setLatLngs(coords);
    
}
//-----------------------| Функции |----------------------------------------------
// Отображение полиона из базы данных

function displayGeoList(geoList) {
    L.polygon(geoList).addTo(polygonGroup)
}

function removeGeoList(mycoords) {
    polygonGroup.eachLayer(function (layer) {
        if (layer instanceof L.Polygon) {
            var coords = layer.getLatLngs();
            if (coords.toString() === mycoords) {
                polygonGroup.removeLayer(layer);
            }
        }
    });
}

function removeAllGeoList() {
    polygonGroup.clearLayers(); 
}



