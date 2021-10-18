import json
import requests
from ..src.SeptaTimes import RegionalSeptaTimes
from fuzzywuzzy import process
from datetime import datetime

station_list = []

septa = SeptaTimes()

train_schedule = septa.get_train_schedule(9374)
hr_schedule = septa.parse_train_schedules(train_schedule)

for i in hr_schedule:
    print(i)

'''
trains = septa.get_station_arrivals('30th Street Station', 5)
hr_schedule = septa.parse_station_arrivals(trains)

for stop in hr_schedule:
    print(stop)
'''
'''
train = septa.get_train_schedule(432)
for i in train:
    station = i['station']
    print(station)
'''


'''
trains = septa.get_station_arrivals('30th Street Station', 10)
print(septa.parse_station_arrivals(trains))
'''

'''
train_schedule = septa.get_train_schedule(9374)
hr_schedule = septa.parse_train_schedule(train_schedule)

for i in hr_schedule:
    print(i)
'''

'''
next_trains = septa.get_next_to_arrive(
    '30th Street Station', 'Cornwells Heights', 1)

hr_next_trains = septa.parse_next_to_arrive(next_trains)

for train in hr_next_trains:
    print(train)
'''
