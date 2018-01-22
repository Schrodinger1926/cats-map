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


### FRONT END


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
```
var ref = firebase.database().ref('...');

// gets reference to the node


function myMap(){
	...

	var mapOptions = {

		...

		// sets maps fields like center, zoom, mapTypeID
	}

	map = new google.maps.Map( dumpelement , mapOptions);

	var geocoder = new google.maps.Geocoder();

	// for reverse geocoding, 
	// returns address content 

	google.maps.event.addListener(map, 'click', function(event) {

		...

		// On click listener

		
	}


}

// Callback function to google maps api



```











