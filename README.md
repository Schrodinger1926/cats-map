[![Build Status](https://travis-ci.org/Schrodinger1926/cats-map.svg?branch=master)](https://travis-ci.org/Schrodinger1926/cats-map) ![Heroku](https://heroku-badge.herokuapp.com/?app=cats-map)

NOTE: 
   Don't worry about failing build
   Some issue with local db connection at travis. Looking into that!
   Local tests are passing.

 


# Welcome to revamped Schrodinger's Map

## Overview

Randomly click any location on google map,

click on a real address location and you will be rewarded with an amazing marker. else an alert will be 

issued. If bored you can reset all the data and start again.


## Functionality in a nutshell

1. *(MAP TRIGGER)* Map click will generate geocoordinate

2. *(MAP LISTENER)* A maps listener will reverse geocode and validate data

3. *(PUSH)* The valid address you clicked will be pushed to firebase realtime database and a sqlite3 database on flask backend.
4. *(DELETE)* Reset will clear data on both the databases separately 

5. *(DECOUPLED)* Firebase and sqlite are NOT synced (Tried that!, wouldn't that be cool?)

6. *(FIREBASE LISTENER)* Any data pushed into firebase will trigger firebase listener, receives wholedataset and lay markers accordingly.







![Alt text](/assets/maps.png?raw=true)


## How to setup

### LOCAL DEVELOPMENT ENVIORNMENT

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

#### HEROKU DEPLOYMENT

* Deployments are done directly from this git repository. 

* Procfile
   ```
   web: flask run --host 0.0.0.0 --port ${PORT}
   init: flask db init
   migrate: flask db migrate
   upgrade: flask db upgrade
   ```
* runtime.txt
   `python-2.7.10`

* added env Config Vars key,val pairs on app setting. (could be done from CLI as well)
   ```
   FLASK_APP run.py
   FLASK_CONFIG development
   ```

* Using heroku-postgresql as production database

* Manual deployement trigger,


# Documentation

## FRONT END


#### config.js
```javascript
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
![Alt text](/assets/firebase_database.png?raw=true)


#### main.js

PART-1: VALIDATE AND PUSH ADDRESS TO DATABASES

```javascript
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


```javascript
// Arguments: ..
// Returns: Entire firebase database,  Type: array of JSON objects
ref.on(.. , func{

	...

	// Triggered on changes on firebase database


	// Reset marker


	});
```


PART-3: HELPING FUNCTION


```javascript
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

![Alt text](/assets/backend.png?raw=true)

#### MODEL

A simple three data attribute model

* Location.id

    Returns a unique (integer) id assigned to model object during session transaction

* Location.lat

    Returns (float) latitude of the Location instance geocoordinate 

* Location.lng

    Return (float) longitude of the Location instance geocoordinate

* Location.address

    Returns (string) precise address of the Location instance geocoordinate



#### VIEWS

* /

   method : GET
   returns `index.html`, the home page of application


   method: POST
   Stores incomming data to sqlite storage. Expects geoocordinate as JSON.


* /fetch

   method: GET
   returns a table of sqlite database.

* /clear
	 
   method: GET
   clears all the backend sqlite data


## FOOTNOTES

* Spent a hell lot time with concepts, bugs and architecture.
* From almost no experience in javascript, maps, ajax, ORM, Flask, firebase, tests and more to an intermediate level in 4 days. 
* I struggled a lot witht the architecture, bascially the whole flask app now looks like kind of Django. Why Django is needed? I think I understood it the hard and a permament way.

* Won't say a J learning curve, it wasn't an exponential in the later stage. It was a vertical.

* I feel front test were also to be done. Will try!