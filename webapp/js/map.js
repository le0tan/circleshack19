var geocoder;
function initMap() {
	var map = new google.maps.Map(document.getElementById('map'), {
	  center: {lat: 1.35, lng: 103.8198},
	  zoom: 11.2
	});
	geocoder = new google.maps.Geocoder();
	var marker;
	map.addListener('click', function(event){
		if(marker!=null) marker.setMap(null);
		marker = createMarker(map, event.latLng);
	})
}

function createMarker(map, latLng) {
	var marker = new google.maps.Marker(
		{
			position: latLng,
			map: map
		});
	createInfoWindow(map, marker);
	return marker;
}

function createInfoWindow(map, marker) {
	geocoder.geocode( { 'location': marker.position}, function(results, status) {
      if (status == 'OK') {
        contentString = results[0].formatted_address;
        var infoWindow = new google.maps.InfoWindow({
    		content: contentString
  		});
  		infoWindow.open(map, marker);
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    });
}