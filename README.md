<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   
   <img src="https://img.shields.io/github/stars/dotzenith/TheSeptaTimes?color=F8BD96&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/forks/dotzenith/TheSeptaTimes?color=DDB6F2&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/repo-size/dotzenith/TheSeptaTimes?color=ABE9B3&labelColor=302D41&style=for-the-badge">
   
   <img src="https://img.shields.io/github/commit-activity/y/dotzenith/TheSeptaTimes?color=96CDFB&labelColor=302D41&style=for-the-badge&label=COMMITS"/>
   <br>
</div>

<p/>

---

### ❖ TheSeptaTimes

TheSeptaTimes is a python package designed to make accessing info about Septa's regional rail network easier. I made this because I commute to college every day via septa, and checking the time for the next train via the app or the website simply takes too much time. I wanted something I could access from my terminal, and thus, TheSeptaTimes was born. 

  <img src="https://github.com/dotzenith/dotzenith/blob/main/assets/TheSeptaTimes/septa.gif" alt="septa gif">

---

### ❖ Installation

> Install from pip

```sh
pip3 install TheSeptaTimes
```

> Install from source
- First, install [poetry](https://python-poetry.org/)

```sh
git clone https://github.com/dotzenith/TheSeptaTimes.git
cd TheSeptaTimes
poetry build
pip3 install ./dist/theseptatimes-0.2.1.tar.gz
```

---

### ❖ Usage

```sh
Usage: tst [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  arrivals  Find the next arrivals at a given train station
  next      Search for the next train going from an origin to a destination
  search    Search for a given station
  train     Track a given train using it's number
```

> Fuzzy search for a train station
```sh
tst search admr
```

> Get times for the next two trains that go from a given train station to another
```sh
tst next '30th Street Station' 'North Philadelphia'
```

> List the next 6 arrivals at a given train station
```sh
tst arrivals '30th Street Station' 6
```

> Take a look at any given train's schedule using the train number
```sh
tst train 9374
```

---

### ❖ What's New? 
0.2.0 - Minor structural changes

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>

