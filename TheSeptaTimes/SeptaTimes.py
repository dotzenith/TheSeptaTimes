import json
import requests
from fuzzywuzzy import process
from datetime import datetime
from colorama import Fore, Style


class TheSeptaTimes():
    def __init__(self):
        self.base_link = "https://www3.septa.org/hackathon/"
        self.stations = [
            '9th St', '30th Street Station', '49th St', 'Airport Terminal A', 'Airport Terminal B',
            'Airport Terminal C-D', 'Airport Terminal E-F', 'Allegheny', 'Allen Lane', 'Ambler',
            'Angora', 'Ardmore', 'Ardsley', 'Bala', 'Berwyn',
            'Bethayres', 'Bridesburg', 'Bristol', 'Bryn Mawr', 'Carpenter',
            'Chalfont', 'Chelten Avenue', 'Cheltenham', 'Chester TC', 'Chestnut Hill East',
            'Chestnut Hill West', 'Churchmans Crossing', 'Claymont', 'Clifton-Aldan', 'Colmar',
            'Conshohocken', 'Cornwells Heights', 'Crestmont', 'Croydon', 'Crum Lynne',
            'Curtis Park', 'Cynwyd', 'Darby', 'Daylesford', 'Delaware Valley College',
            'Devon', 'Downingtown', 'Doylestown', 'East Falls', 'Eastwick Station',
            'Eddington', 'Eddystone', 'Elkins Park', 'Elm St', 'Elwyn Station',
            'Exton', 'Fern Rock TC', 'Fernwood', 'Folcroft', 'Forest Hills',
            'Ft Washington', 'Fortuna', 'Fox Chase', 'Germantown', 'Gladstone',
            'Glenside', 'Gravers', 'Gwynedd Valley', 'Hatboro', 'Haverford',
            'Highland', 'Highland Ave', 'Holmesburg Jct', 'Ivy Ridge', 'Market East',
            'Jenkintown-Wyncote', 'Langhorne', 'Lansdale', 'Lansdowne', 'Lawndale',
            'Levittown', 'Link Belt', 'Main St', 'Malvern', 'Manayunk',
            'Marcus Hook', 'Meadowbrook', 'Media', 'Melrose Park', 'Merion',
            'Miquon', 'Morton', 'Mt Airy', 'Moylan-Rose Valley', 'Narberth',
            'Neshaminy Falls', 'New Britain', 'Newark', 'Noble', 'Norristown TC',
            'North Broad St', 'North Hills', 'North Philadelphia', 'North Wales', 'Norwood',
            'Olney', 'Oreland', 'Overbrook', 'Paoli', 'Penllyn'
            'Pennbrook', 'Penn Medicine Station', 'Philmont', 'Primos',
            'Prospect Park', 'Queen Lane', 'Radnor', 'Ridley Park', 'Rosemont',
            'Roslyn', 'Rydal', 'Ryers', 'Secane', 'Sedgwick',
            'Sharon Hill', 'Somerton', 'Spring Mill', 'St. Davids', 'St. Martins',
            'Stenton', 'Strafford', 'Suburban Station', 'Swarthmore', 'Swarthmore',
            'Tacony', 'Temple U', 'Thorndale', 'Torresdale', 'Trenton',
            'Trevose', 'Tulpehocken', 'Upsal', 'Villanova', 'Wallingford',
            'Warminster', 'Washington Lane', 'Wayne', 'Wayne Jct', 'West Trenton',
            'Whitford', 'Willow Grove', 'Wilmington', 'Wissahickon', 'Wister',
            'Woodbourne', 'Wyndmoor', 'Wynnefield Avenue', 'Wynnewood', 'Yardley',
        ]

    def json_to_py(self, link):
        '''
        json_to_py(link) -> dictionary or list

        Makes a request to the given link and returns an object

        :param link -- link to a json response
        '''
        response = requests.get(link)
        py_object = json.loads(response.content)

        return py_object

    def get_next_to_arrive(self, origin, destination, num=2):
        '''
        get_next_to_arrive(origin, destination, num) -> list of dictionaries

        builds a url to return trains running from the origin to the destination

        :param origin -- starting train station
        :param destination -- ending train station
        :param num -- number of trains going from origin to train.
                      (the default is 2 since that seems to be upper limit for most
                       train stations but results vary depending on the origin and destination)
        '''
        next_to_arrive_link = f'{self.base_link}NextToArrive/{origin}/{destination}/{num}'
        next_trains = self.json_to_py(next_to_arrive_link)

        return next_trains

    def get_station_arrivals(self, station, num=5):
        '''
        get_station_arrivals(station, num) -> list of dictionaries

        builds a url to return a specified number of trains arriving at a given station

        :param station -- name of the station to check for arrivals
        :param num -- the number of trains to return
                      (the default is set to 5, which is in line with the septa default.
                       the max is 200 according to septa)
        '''
        station_arrivals_link = f'{self.base_link}/Arrivals/{station}/{num}'
        obj = self.json_to_py(station_arrivals_link)
        key_to_obj_dict = list(obj.keys())[0]
        trains = (obj[key_to_obj_dict])

        return trains

    def get_train_schedule(self, train):
        '''
        get_train_schedule(train) -> list of dictionaries

        builds a url to return the schedule of a specific train based on the train number

        :param train -- the ID of any given train
        '''
        train_schedule_link = f'{self.base_link}/RRSchedules/{train}'
        train_schedule = self.json_to_py(train_schedule_link)

        return train_schedule

    def search_station(self, guess_name):
        '''
        search_station(guess_name) -> string

        searches the list of train stations to find one that matches the guessed name

        The official names for train stations vs the api names for train stations differs
        here and there. this functions is to help search for the api name of a certain train
        station and also to confirm if the train station you're searching for exists or not

        :param guess_name - the station you want to search for
        '''
        station = process.extractOne(guess_name, self.stations)[0]

        return station

    def get_stations_list(self):
        '''
        get_station_list() -> list

        returns the list of all train stations in the septa api at the time of writing
        '''
        return self.stations

    def convert_station_time(self, time):
        '''
        conver_staion_time(time) -> string

        converts the time returned by the station arrivals api to a human-readable format

        :param time -- time in the format given by the station arrivals api
        '''
        new_time = time.split(' ')[1]
        twenty_four_hour_time = ":".join(new_time.split(":", 2)[:-1])
        normal_time = datetime.strptime(
            twenty_four_hour_time, "%H:%M").strftime("%I:%M %p")

        return normal_time

    '''
    These Next Three functions are meant to process the results of get_next_to_arrive(),
    get_station_arrivals(), and get_train_schedule() respectively.

    Having these function here makes my life easier in the main script. As such, I've moved them
    out of the way to make sure they don't get in the way of someone who does not want to parse through
    the data the same way I did.
    '''

    def parse_next_to_arrive(self, next_trains):
        '''
        parse_next_to_arrive(next_trains) -> list of strings

        parses the data given by the get_next_to_arrive() function and
        returns it in a nice and colorful format

        :param next_trains -- the list of dictionaries from get_next_to_arrive()
        '''
        next_trains_list = [f"{train['orig_train']:<11}"
                            f"{train['orig_departure_time']:<13}"
                            f"{train['orig_arrival_time']:<11}"
                            f"{train['orig_delay']:<9}"
                            f"{train['orig_line']}" for train in next_trains]

        # making the header string and adding it to the beginning of the list
        header_string = f"{Fore.MAGENTA}{'Train #':<11}{Style.RESET_ALL}" \
                        f"{Fore.GREEN}{'Departure':<13}{Style.RESET_ALL}" \
                        f"{Fore.CYAN}{'Arrival':<11}{Style.RESET_ALL}" \
                        f"{Fore.RED}{'Delay':<9}{Style.RESET_ALL}" \
                        f"{Fore.YELLOW}{'Line'}{Style.RESET_ALL}"
      
        next_trains_list.insert(0, header_string)

        return next_trains_list

    def parse_station_arrivals(self, trains):
        '''
        parse_station_arrivals(trains) -> list of strings

        parses the data given by get_station_arrivals() and returns it in a  nice and
        colorful format

        :param trains -- the list of dictionaries returned by get_station_arrivals()
        '''
        try:
            north = trains[0]['Northbound']
            north_trains_list = [f"{'North':<13}"
                                 f"{train['train_id']:<11}"
                                 f"{str(train['next_station']):<27}"
                                 f"{self.convert_station_time(train['sched_time']):<12}"
                                 f"{train['status']:<10}"
                                 f"{train['destination']}" for train in north]
        except TypeError:
            north_trains_list = ['No Northbound trains at the time']

        try:
            south = trains[1]['Southbound']
            south_trains_list = [f"{'South':<13}"
                                 f"{train['train_id']:<11}"
                                 f"{str(train['next_station']):<27}"
                                 f"{self.convert_station_time(train['sched_time']):<12}"
                                 f"{train['status']:<10}"
                                 f"{train['destination']}" for train in south]
        except TypeError:
            south_trains_list = ['No Southbound trains at the time']

        # making the header string and adding it to the beginning of the list
        header_string = f"{Fore.BLUE}{'Direction':<13}{Style.RESET_ALL}" \
                        f"{Fore.CYAN}{'Train #':<11}{Style.RESET_ALL}" \
                        f"{Fore.GREEN}{'Next Station':<27}{Style.RESET_ALL}" \
                        f"{Fore.MAGENTA}{'Time':<12}{Style.RESET_ALL}" \
                        f"{Fore.RED}{'Status':<10}{Style.RESET_ALL}" \
                        f"{Fore.YELLOW}{'Destination'}{Style.RESET_ALL}"
       
        final_list = (north_trains_list + south_trains_list)
        final_list.insert(0, header_string)

        return final_list

    def parse_train_schedule(self, train_schedule):
        '''
        parse_train_schedule(train_schedule) -> list of strings

        parses the data given by get_train_schedule() and returns it in a nice and colorful format

        :param train_schedule -- the list of dictionaries returned by get_train_schedule()
        '''

        train_schedule_list = [f"{stop['station']:<27}"
                               f"{stop['sched_tm']:<18}"
                               f"{stop['act_tm']}" for stop in train_schedule]

        # making the header string and adding it to the beginning of the list
        header_string = f"{Fore.YELLOW}{'Station':<27}{Style.RESET_ALL}" \
                        f"{Fore.CYAN}{'Scheduled Time':<18}{Style.RESET_ALL}" \
                        f"{Fore.GREEN}{'Actual Time'}{Style.RESET_ALL}"
       
        train_schedule_list.insert(0, header_string)
        return train_schedule_list
