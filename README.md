[![Build Status](https://travis-ci.org/Schrodinger1926/cats-map.svg?branch=master)](https://travis-ci.org/Schrodinger1926/cats-map)


# Welcome to revamped Schrodinger's Map

![Alt text](/assets/maps.png?raw=true)


## How to setup

### DEVELOPMENT ENVIORNMENT

Ensure you are on Python 2.7.10

#### setup virtual env
```
$ virtualenv dev
$ source dev/bin/activate

```

#### clone project
```
$ git clone https://github.com/Schrodinger1926/cats-map
$ cd cats-map
```

#### install dependencies and set paths
```
$ pip install -r requirements.txt
$ export PYTHONPATH=$(pwd)
$ export FLASK_APP=run.py
$ export FLASK_CONFIG=development
```


#### Run test cases

`$ nose2`


#### Launch on test server (If you want to start with fresh sqlite)
```
$ flask db init
$ flask db migrate
$ flask db upgrade

```

<!-- #### HEROKU CLI DEPLOYMENT

In progres -->


## FRONT END


#### config.js
```
var config = {
    apiKey: "...",
    authDomain: "...",
    databaseURL: "...",
    projectId: "...",
    storageBucket: "...",
    messagingSenderId: "..."
  };
  firebase.initializeApp(config);   // establish connection

// 
//  Your firbase realtime database configuration
//  
//  Go to firabse console to get credentials
```

Looks somewhat like this, JSON data storage
![Alt text](/assets/firabase_database.png?raw=true)


#### main.js

PART-1: VALIDATE AND PUSH ADDRESS TO DATABASES

```
var ref = firebase.database().ref('...');

// gets reference to the node


function myMap(){
	...

	// Callback function to google maps api

	var mapOptions = {

		...

		// sets maps fields like center, zoom, mapTypeID
	}

	map = new google.maps.Map( dumpelement , mapOptions);

	var geocoder = new google.maps.Geocoder();

	// Arguments: map                   ,  Type: google.maps.Map instance 
	// Returns: Entire firebase database,  Type: array of JSON objects
	google.maps.event.addListener(map, 'click', function(event) {

		...

		
		// On click listener, returns geocode


		// Arguments: Geo-coordinates, callback
		// Returns: Precise real address
		geocoder.geocode({

				latitude/longitude

				// coordinates

			}, func(){

				//1. Validates data

				google.maps.GeocoderStatus.OK && results[0] && location_type == 'ROOFTOP'


				//2. Set markers


				//3. Push data to firabse database
				ref.push(..)

				//4. Push data to sqlite flask backend
				$.ajax({
					..
					})

				});

				...

	}


}

```


PART-2: RETERIVE DATA

```
// Arguments: ..
// Returns: Entire firebase database,  Type: array of JSON objects
ref.on(.. , func{

	...

	// Triggered on changes on firebase database


	// Reset marker


	});
```


PART-3: HELPING FUNCTION

```
// Arguments: None
// Returns: None
function clearMarker(){
	...

	// clears gloabal marker array
}


// Arguments: None
// Return: None
function resetData(){
	..

	//1.  Delete firebase database
	ref.remove();

	//2. Delete sqlite backend database
	$.ajax({
			...

			// sends get request on clear handler
		});


}
```


## BACK END


#### MODEL

A simple three data attribute model

model.id
	Returns a unique (integer) id assigned to model object during session transaction

model.lat
	Returns (float) latitude of the Location instance geocoordinate 

model.lng
	Return (float) longitude of the Location instance geocoordinate

model.address
	Returns (string) precise address of the Location instance geocoordinate














