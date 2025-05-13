
var map = L.map('map').setView([53.4218, -2.9496], 14);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
maxZoom: 19,
attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

var busMarkerLayer = L.layerGroup().addTo(map);

// Setup socket
var socket = io();

// Get user input and send to backend
const busForm = document.getElementById('form');
busForm.addEventListener('submit', function (e) {
    e.preventDefault(); // Stop page from refreshing when form is submitted
    const textField = document.getElementById('text');
    socket.emit('line', {line: textField.value})
    textField.value = '';

})

// Listen out for data
socket.on('bus locations', function(locationData){
    console.log(locationData) // Handling the retrieved data

    busMarkerLayer.clearLayers();

    locationData.forEach(bus => {
        var lat = bus.lat;
        var long = bus.long;
        var busMarker = L.marker([lat, long]).addTo(busMarkerLayer);
    });
});
