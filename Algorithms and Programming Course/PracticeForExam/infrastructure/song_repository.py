from domain.song import Song
from utils.functions import general_identify

class SongRepository:
    def __init__(self, sl=[]):
        self.__songs = sl

    def __str__(self):
        """
        Returns the string representation of a SongRepository type object.
        """
        generated_str = ""
        for song in self.__songs:
            generated_str += f'{song}' + "\n"
        return generated_str

    def get_songs(self):
        """
        Getter method - returns the songs list.
        """
        return self.__songs

    def set_songs(self, new_sl):
        """
        Setter method - replaces the current songs list with the given one.
        """
        self.__songs = new_sl

    def update_song_at_index(self, index, category, artist, listeners):
        """
        Updates the song at the given index in the repository with the given values.
        """
        self.__songs[index].set_category(category)
        self.__songs[index].set_nameOfArtist(artist)
        self.__songs[index].set_numberOfListeners(listeners)

    def name_of_artist_with_least_listened_to_song(self):
        """
        Returns the name of the artist which has the song with the least listeners.
        """
        least_number_p = 8000000000
        least_number_r = 8000000000
        for song in self.__songs:
            if song.get_numberOfListeners() < least_number_p and song.get_category() == "pop":
                least_number_p = song.get_numberOfListeners()
                least_artist_p = song.get_nameOfArtist()
            elif song.get_numberOfListeners() < least_number_r and song.get_category() == "rock":
                least_number_r = song.get_numberOfListeners()
                least_artist_r = song.get_nameOfArtist()
        return least_artist_p, least_artist_r

    def is_most_listened(self, given_song):
        """
        Returns True if a given song is the most listened one in the Repository and False otherwise.
        """
        for song in self.__songs:
            if song.get_numberOfListeners > given_song.get_numberOfListeners:
                return False
        return given_song in self.__songs

    def most_listened_songs(self):
        """
        Returns the most listened pop song and the most listened rock song in the repository.
        """
        return general_identify(self.__songs, lambda s: self.is_most_listened(s) and s.get_category() == "pop"), general_identify(self.__songs, lambda s: self.is_most_listened(s) and s.get_category() == "rock")