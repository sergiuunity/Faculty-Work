from infrastructure.song_repository import SongRepository
from domain.song import Song


def run_all_tests():
    """
    Runs all the tests.
    """
    test_name_of_artist_with_least_listened_to_song()
    print("All tests passed!")


def test_name_of_artist_with_least_listened_to_song():
    """
    Tests the function name_of_artist_with_least_listened_to_song.
    """
    test_repository = SongRepository(
        [Song("pop", "Artist1", 100), Song("pop", "Artist2", 50), Song("pop", "Artist3", 250),
         Song("pop", "Artist4", 1240), Song("pop", "Artist5", 400),
         Song("rock", "Artist6", 210), Song("rock", "Artist7", 21), Song("rock", "Artist8", 750),
         Song("rock", "Artist9", 890), Song("rock", "Artist10", 5)
         ])
    assert test_repository.name_of_artist_with_least_listened_to_song() == ("Artist2", "Artist10")
    test_repository = SongRepository()
    try:
        test_repository.name_of_artist_with_least_listened_to_song()
        assert False
    except UnboundLocalError:
        assert True
    test_repository = SongRepository(
        [Song("pop", "Artist1", 0), Song("rock", "Artist10", 0)
         ])
    assert test_repository.name_of_artist_with_least_listened_to_song() == ("Artist1", "Artist10")
