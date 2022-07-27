import typer
from theseptatimes import TheSeptaTimes

app = typer.Typer(add_completion=False)
septa = TheSeptaTimes()

@app.command()
def search(
    station: str
):
    """
    Search for a given station
    """
    print(f"Closest matching station to your guess: {septa.search_station(station)}")

@app.command()
def train(
    train_num: str
):
    """
    Track a given train using it's number
    """
    
    train_schedule = septa.get_train_schedule(train_num)
    if "error" in train_schedule:
        print("No train found with that number")
    else:
        hr_train_schedule = septa.parse_train_schedule(train_schedule)
        for stop in hr_train_schedule:
            print(stop)

@app.command()
def next(
    origin: str,
    destination: str,
    num: str = typer.Argument(2, show_default=False)
):
    """
    Search for the next train going from an origin to a destination
    """
    next_trains = septa.get_next_to_arrive(
        septa.search_station(origin), septa.search_station(destination), num)
    hr_next_trains = septa.parse_next_to_arrive(next_trains)
    for train in hr_next_trains:
        print(train)

@app.command()
def arrivals(
    station: str,
    num: str = typer.Argument(5, show_default=False)
):
    """
    Find the next arrivals at a given train station 
    """
    trains = septa.get_station_arrivals(septa.search_station(station), num)
    hr_schedule = septa.parse_station_arrivals(trains)
    for train in hr_schedule:
        print(train)

def main():
    app()
