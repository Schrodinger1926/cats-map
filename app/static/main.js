var markersArray=[];
var recentlyClicked;

// Get reference to firebase realtime database
var ref = firebase.database().ref('datapoints');

function myMap(){
  // console.log("setting options")
  var mapOptions = {
    // Put Berlin @ Center 52.52, 13.4
    // -5.50, 122.59  bau bau, indonesia
    // JAPAN: 35.68, 139.69
    center: new google.maps.LatLng(35.68, 139.69),
    zoom: 17,
    mapTypeId: google.maps.MapTypeId.HYBRID
  }

  // Dump map
  map = new google.maps.Map(document.getElementById("map"), mapOptions);

  // reverse Geocoder
  var geocoder = new google.maps.Geocoder();

  // Onclick listener map
  google.maps.event.addListener(map, 'click', function(event) {
    
    recentlyClicked = event.latLng;
    
    geocoder.geocode({
      
      'latLng': event.latLng

    }, function(results, status) {
          if (status == google.maps.GeocoderStatus.OK) {
            
            console.log(results[0].geometry.location_type);
            
            // validates down to street precise locations only
            if (results[0] && results[0].geometry.location_type == 'ROOFTOP') {

              // payload for firebase and sqlite calls
              var data={      
                  lat: results[0].geometry.location.lat(),
                  lng: results[0].geometry.location.lng(),
                  address: results[0].formatted_address
                }

                // To add the marker to the map, call setMap();
                var marker = new google.maps.Marker({
                   position: recentlyClicked,
                   animation: google.maps.Animation.DROP,
                   title: results[0].formatted_address
                  });

                // Add marker to global array
                markersArray.push(marker);

                // Place marker
                marker.setMap(map);

                // Push data to firebase realtime database
                ref.push(data);

                // Push data to sqlite backend
                $.ajax({
                    url: '/',
                    method: 'POST',
                    data: JSON.stringify(data),
                    contentType: 'application/json; charset=UTF-8',

                  }).done(function(response){
                    if (response.status == "FAILED") {
                      alert("Data din't got pushed to sqlite");
                    }
                
                  });

            }


            else{
              // accurate address not available
              alert("Precise address not indexed by maps")
            }
                
          }

          // Status not Ok, probably you clicked on ocean or something
          else{
            alert("Invalid address!");
          }
      });
    });
  }


var htmlTableHeaders = "<tr>" +
                          "<th>   INDEX   </td>" +
                          "<th> LATITUTDE </td>" +
                          "<th> LONGITUDE </td>" +
                          "<th>  ADDRESS  </td>" +
                       "</tr>";


// Trigger when data changes in firebase database, returns whole database
ref.on("value",function(snapshot){
  // clear firebase address list
  document.getElementById("firebaseList").innerHTML = htmlTableHeaders;
  
  // clear markers
  clearMarkers();
  
  var htmlcontent = htmlTableHeaders;

  // For some reason js loop index is not responding
  var counter = 1;
  
  // Iterate through each point
  snapshot.forEach(function(v){

   // set all markers again
   var marker = new google.maps.Marker({
      position: { lat: v.val().lat,
                  lng: v.val().lng
                },
      animation: google.maps.Animation.DROP,
      title: v.val().address
   });

   // create markers array
   markersArray.push(marker);

   // set marker
   marker.setMap(map);

   // create html table
   htmlcontent += "<tr>" +
                    "<td>" + counter + "</td>" + 
                    "<td>" + v.val().lat + "</td>" +
                    "<td>" + v.val().lng + "</td>" +
                    "<td>" + v.val().address + "</td>" +
                  "</tr>";
    
    // increment counter
    counter += 1;

 });

  document.getElementById("firebaseList").innerHTML = htmlcontent;

});


function clearMarkers(){
  for (var i = 0; i < markersArray.length; i++) {
    markersArray[i].setMap(null);
  }
  markersArray.length = 0;
}

// Triggers on reset click
function resetData(){
  clearMarkers();
  // clear firebase database
  ref.remove();

  // clear backend sqlite database
  $.ajax({
    url: '/clear',
    method:'GET',
  }).done(function (response) {
    if (response.status == "FAILED") {
      alert("Sqlite reset failed");
    }
    else{
      alert(response.deleted_rows_count + " rows successfully deleted from sqlite backend as well");
    }
  });

}