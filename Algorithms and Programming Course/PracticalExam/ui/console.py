from domain.measurement import Measurement
from repository.station import Station
from tests.tests import test_validation


def print_menu():
    """
    Prints the menu.
    """
    print("0 - exit")
    print("1 - print the menu")
    print("2 - print the station")
    print("3 - add measurement")
    print("4 - sort measurements by rainfall")


def start():
    test_validation()
    print("All tests have passed!")
    my_station = Station([Measurement(12, 30, 70), Measurement(13, 30, 20), Measurement(13, 45, 50)])
    print_menu()
    print(my_station)
    command = input("-->")
    while command != "0":
        if command == "1":
            print_menu()
        elif command == "2":
            print(my_station)
        elif command == "3":
            try:
                hour = int(input("Hour:"))
                minute = int(input("Minute:"))
                rainfall = int(input("Rainfall:"))
                my_station.add_measurement(Measurement(hour, minute, rainfall))
            except ValueError as ve:
                print(ve)
        elif command == "4":
            my_station.sort_measurements()
        else:
            print("Given command not valid. Try a new one.")
        command = input("-->")

