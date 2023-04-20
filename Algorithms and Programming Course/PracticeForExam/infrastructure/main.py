from infrastructure.song_repository import SongRepository
from domain.song import Song
from tests.tests import run_all_tests

my_repository = SongRepository([Song("pop", "Artist1", 100), Song("pop", "Artist2", 50), Song("pop", "Artist3", 250),
                                Song("pop", "Artist4", 1240), Song("pop", "Artist5", 400),
                                Song("rock", "Artist6", 210), Song("rock", "Artist7", 21), Song("rock", "Artist8", 750),
                                Song("rock", "Artist9", 890), Song("rock", "Artist10", 300)
                                ])


def menu():
    """
    Prints the menu.
    """
    print("0 - end the program")
    print("1 - print the repository")
    print("2 - update a song at index")
    print("3 - identify the most listened pop and rock songs")
    print("4 - print the name of the artist for the song with the least listeners for both pop and rock songs")


def start():
    """
    Initializes the app.
    """
    menu()
    run_all_tests()
    command = input("-->")
    while command != "0":
        if command == "1":
            print(my_repository)
        elif command == "2":
            try:
                index = int(input("Index:"))
                category = input("Category:")
                name = input("Name of artist:")
                number = int(input("Number of listeners"))
                my_repository.update_song_at_index(index, category, name, number)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
            print(my_repository)
        elif command == "3":
            print(my_repository.most_listened_songs())
        elif command == "4":
            try:
                print(my_repository.name_of_artist_with_least_listened_to_song())
            except IndexError as ie:
                print(ie)
        else:
            print("Unknown command. Try a new one.")
        command = input("-->")


start()
