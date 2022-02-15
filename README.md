<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   
   <img src="https://img.shields.io/github/stars/zenithds/TheSeptaTimes?color=F8BD96&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/forks/zenithds/TheSeptaTimes?color=DDB6F2&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/repo-size/zenithds/TheSeptaTimes?color=ABE9B3&labelColor=302D41&style=for-the-badge">
   
   <img src="https://badges.pufler.dev/visits/zenithds/TheSeptaTimes?style=for-the-badge&color=96CDFB&logoColor=white&labelColor=302D41"/>
   <br>
</div>

<p/>

---

### ❖ TheSeptaTimes

TheSeptaTimes is a python package designed to make accessing info about Septa's regional rail network easier. I made this because I commute to college every day via septa, and checking the time for the next train via the app or the website simply takes too much time. I wanted something I could access from my terminal, and thus, TheSeptaTimes was born. 

---

### ❖ Installation

> Install from pip

```sh
$ pip3 install TheSeptaTimes
```

> Install from source
```sh
$ git clone https://github.com/ZenithDS/TheSeptaTimes.git
$ cd TheSeptaTimes
$ pip install .
```

---

### ❖ Usage

<details>
<summary><strong>As CLI App</strong></summary>

```sh
usage: tst [-h] [-o ORIGIN] [-d DESTINATION] [-s STATION] [-t TRAINID] [-n NUMRESULTS] action

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

> Search for a train station
```sh
$ tst search -s admr
  
  Station matching your guess: Ardmore
 ```

> Get times for the next two trains that go from a given train station to another
```sh
$ tst list -o '30th Street Station' -d 'North Philadelphia'
```

> List the next 6 arrivals at a given train station
```sh
$ tst list -s '30th Street Station' -n 6
```

> Take a look at any given train's schedule using the train number
```sh
$ tst list -t 9374
```

</details>

<details>
<summary><strong>As Python Library/Package</strong></summary>

> print the next train going from a given train station to another
```python
from TheSeptaTimes.SeptaTimes import TheSeptaTimes

septa = TheSeptaTimes()

next_trains = septa.get_next_to_arrive('30th Street Station', 'North Philadelphia', 1)
readable_next_trains = septa.parse_next_to_arrive(next_trains)

for train in readable_next_trains:
    print(train)
```

> print the next 6 arrivals at a given train station
```python
from TheSeptaTimes.SeptaTimes import TheSeptaTimes

septa = TheSeptaTimes()

trains = septa.get_station_arrivals('30th Street Station', 5)
readable_trains = septa.parse_station_arrivals(trains)

for train in readable_trains:
    print(trains)
```

> print any given train's schedule using the train number
```python
from TheSeptaTimes.SeptaTimes import TheSeptaTimes

septa = TheSeptaTimes()

train_schedule = septa.get_train_schedule(9374)
readable_train_schedule = septa.parse_train_schedule(train_schedule)

for stop in readable_train_schedule:
    print(stop)
    
 ```

</details>

---

### ❖ What's New? 
0.0.7 - Improved Formatting for all of the CLI commands

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>

