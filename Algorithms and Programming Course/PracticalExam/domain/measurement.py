class Measurement:
    def __init__(self, hour, minute, rainfall):
        if 0 <= hour < 24:
            self.__hour = hour
        else:
            raise ValueError("The hour should be a number between 0 and 24. Try a new command.")
        if 0 <= minute < 60:
            self.__minute = minute
        else:
            raise ValueError("The minute should be a number between 0 and 60. Try a new command.")
        if rainfall >= 0:
            self.__rainfall = rainfall
        else:
            raise ValueError("The rainfall should be a positive number. Try a new command.")

    def __str__(self):
        """
        Returns the string representation of a measurement type object.
        """
        return f"{self.__hour}:{self.__minute} - {self.__rainfall} mm"

    def get_hour(self):
        """
        Getter method - returns the hour of a measurement.
        """
        return self.__hour

    def get_minute(self):
        """
        Getter method - returns the minute of a measurement.
        """
        return self.__minute

    def get_rainfall(self):
        """
        Getter method - returns the rainfall of a measurement.
        """
        return self.__rainfall

    def set_hour(self, hour):
        """
        Setter method - replaces the hour of a measurement with a given one or raises error if not valid.
        """
        if 0 <= hour < 24:
            self.__hour = hour
        else:
            raise ValueError("The hour should be a number between 0 and 24. Try a new command.")

    def set_minute(self, minute):
        """
        Setter method - replaces the minute of a measurement with a given one or raises error if not valid.
        """
        if 0 <= minute < 60:
            self.__minute = minute
        else:
            raise ValueError("The minute should be a number between 0 and 60. Try a new command.")

    def set_rainfall(self, rainfall):
        """
        Setter method - replaces the rainfall of a measurement with a given one or raises error if not valid.
        """
        if rainfall >= 0:
            self.__rainfall = rainfall
        else:
            raise ValueError("The rainfall should be a positive number. Try a new command.")
