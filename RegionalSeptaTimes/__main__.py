from SeptaTimes import RegionalSeptaTimes


def main():
    septa = RegionalSeptaTimes()

    for train in septa.parse_train_schedule(septa.get_train_schedule(9374)):
        print(train)


if __name__ == "__main__":
    main()
