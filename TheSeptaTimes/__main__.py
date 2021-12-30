import sys
from TheSeptaTimes.SeptaTimes import TheSeptaTimes
import argparse


def main():
    septa = TheSeptaTimes()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", help="Determines whether you want to `search` or `list`")
    parser.add_argument(
        "-o", "--origin", help="the starting train station")
    parser.add_argument(
        "-d", "--destination", help="the ending station")
    parser.add_argument(
        "-s", "--station", help="any given station")
    parser.add_argument(
        "-t", "--trainID", help="the ID of any given train")
    parser.add_argument(
        "-n", "--numResults", help="the number of results"
    )

    args = parser.parse_args()

    if args.action == "search":
        if args.station is not None:
            search_result = f"Station matching your guess: {septa.search_station(args.station)}"
            print(search_result)
        else:
            print("Please enter a valid train station")

    elif args.action == "list":
        if (args.origin is not None and args.destination is not None):
            if args.numResults is not None:
                next_trains = septa.get_next_to_arrive(
                    septa.search_station(args.origin), septa.search_station(args.destination), args.numResults)
                hr_next_trains = septa.parse_next_to_arrive(next_trains)
                for train in hr_next_trains:
                    print(train)
            else:
                next_trains = septa.get_next_to_arrive(
                    septa.search_station(args.origin), septa.search_station(args.destination))
                hr_next_trains = septa.parse_next_to_arrive(next_trains)
                for train in hr_next_trains:
                    print(train)
        elif (args.station is not None):
            if args.numResults is not None:
                trains = septa.get_station_arrivals(
                    septa.search_station(args.station), args.numResults)
                hr_schedule = septa.parse_station_arrivals(trains)
                for train in hr_schedule:
                    print(train)
            else:
                trains = septa.get_station_arrivals(
                    septa.search_station(args.station))
                hr_schedule = septa.parse_station_arrivals(trains)
                for train in hr_schedule:
                    print(train)
        elif (args.trainID is not None):
            train_schedule = septa.get_train_schedule(args.trainID)
            if "error" in train_schedule:
                print("No train found with that number")
            else:
                hr_train_schedule = septa.parse_train_schedule(train_schedule)
                for stop in hr_train_schedule:
                    print(stop)


if __name__ == "__main__":
    main()
