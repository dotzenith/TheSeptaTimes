# RegionalSeptaTimes

RegionalSeptaTimes is a python package designed to make accessing info about Septa's regional rail network easier. I made this because I commute to college every day via septa, and checking the time for the next train via the app or the website simply takes too much time. I wanted something I could access from my terminal, and thus, RegionalSeptaTimes was born. 

# Installation

Install from pip

```bash
pip install RegionalSeptaTimes
```
or install from source
```bash
git clone https://github.com/ZenithDS/RegionalSeptaTimes.git
```

```bash
cd RegionalSeptaTimes
```

```bash
pip install .
```

# Usage

## As CLI App
```
usage: rst [-h] [-o ORIGIN] [-d DESTINATION] [-s STATION] [-t TRAINID] [-n NUMRESULTS] action

positional arguments:
  action                Determines whether you want to `search` or `list`

optional arguments:
  -h, --help            show this help message and exit
  -o ORIGIN, --origin ORIGIN
                        the starting train station
  -d DESTINATION, --destination DESTINATION
                        the ending station
  -s STATION, --station STATION
                        any given station
  -t TRAINID, --trainID TRAINID
                        the ID of any given train
  -n NUMRESULTS, --numResults NUMRESULTS
                        the number of results
```

Search for a train station
```
$ rst search -s admr
  
  Station matching your guess: Ardmore
 ```

Get times for the next two trains that go from a given train station to another
```
$ rst list -o '30th Street Station' -d 'North Philadelphia'
```

List the next 6 arrivals at a given train station
```
$ rst list -s '30th Street Station' -n 6
```

Take a look at any given train's schedule using the train number
```
$ rst list -t 9374
```

## As python Library/Package

print the next train going from a given train station to another
```python
from RegionalSeptaTimes.SeptaTimes import RegionalSeptaTimes

septa = RegionalSeptaTimes()

next_trains = septa.get_next_to_arrive('30th Street Station', 'North Philadelphia', 1)
readable_next_trains = septa.parse_next_to_arrive(next_trains)

for train in readable_next_trains:
    print(train)
```

print the next 6 arrivals at a given train station
```python
from RegionalSeptaTimes.SeptaTimes import RegionalSeptaTimes

septa = RegionalSeptaTimes()

trains = septa.get_station_arrivals('30th Street Station', 5)
readable_trains = septa.parse_station_arrivals(trains)

for train in readable_trains:
    print(trains)
```

print any given train's schedule using the train number
```python
from RegionalSeptaTimes.SeptaTimes import RegionalSeptaTimes

septa = RegionalSeptaTimes()

train_schedule = septa.get_train_schedule(9374)
readable_train_schedule = septa.parse_train_schedule(train_schedule)

for stop in readable_train_schedule:
    print(stop)
    
 ```

