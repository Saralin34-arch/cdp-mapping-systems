// Create a map and set its view to a specific location and zoom level
var map = L.map("map").setView([40.70491, -73.97144], 13);

// Add a tile layer to the map (this is the base layer that provides the map imagery)
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "© OpenStreetMap contributors",
}).addTo(map);

// Fetch pizza restaurant data from the NYC Open Data API
fetch(
  "https://data.cityofnewyork.us/resource/43nn-pn8j.geojson?cuisine_description=Pizza&$limit=10000"
)
  .then((response) => response.json())
  .then((data) => {
   data.features.forEach((feature) => {
   L.geoJSON(data).addTo(map);
   
       L.geoJSON(data, {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, {
                radius: 8,
                fillColor: "#ff7800",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 0.8
            });
        }
    }).addTo(map);
  feature.geometry = {
    type: "Point",
    coordinates: [
      Number(feature.properties.longitude),
      Number(feature.properties.latitude),
    ],
  };
});
  })
  .catch((error) => console.error("Error fetching data:", error));