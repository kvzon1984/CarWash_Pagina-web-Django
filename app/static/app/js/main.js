//map
function iniciarMap() {
	var coord = { lat: -33.5983822, lng: -70.5785959 }
	var map = new google.maps.Map(document.getElementById("map"), {
		zoom: 10,
		center: coord,
	})
	var marker = new google.maps.Marker({
		position: coord,
		map: map,
	})
}
