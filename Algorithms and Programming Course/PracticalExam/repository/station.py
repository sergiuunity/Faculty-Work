from domain.measurement import Measurement


class Station:
    def __init__(self, repo=[]):
        self.__station = repo

    def __str__(self):
        """
        Returns the string representation of a Station.
        """
        generated_str = f"Measurements:\n"
        for measurement in self.__station:
            generated_str += f"{measurement}\n"
        return generated_str

    def get_station(self):
        """
        Getter method - returns the station.
        """
        return self.__station

    def set_hour(self, station):
        """
        Setter method - replaces the station with a given one or raises error if not valid.
        """
        self.__station = station

    def add_measurement(self, measurement):
        """
        Adds the given measurement to the repository.
        """
        self.__station.append(measurement)

    def sort_measurements(self):
        n = len(self.__station)
        for i in range(n - 1):
            i_min = i
            for j in range(i + 1, n):
                if self.__station[j].get_rainfall() > self.__station[i_min].get_rainfall():
                    i_min = j
            if i_min != i:
                copy = self.__station[i_min]
                self.__station[i_min] = self.__station[i]
                self.__station[i] = copy

