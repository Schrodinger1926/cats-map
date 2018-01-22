[![Build Status](https://travis-ci.org/Schrodinger1926/cats-map.svg?branch=master)](https://travis-ci.org/Schrodinger1926/cats-map)


# Welcome to revamped Schrodinger's Map

![Alt text](/assets/map.png?raw=true)


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

#### Launch on test server
`$ flask run`




