from point_module import MyPoint
import point_module
import general_functions
import matplotlib.pyplot as plt
plt.style.use('seaborn')


class PointRepository:
    def __init__(self, point_list=[]):
        self.__points = point_list.copy()

    def __str__(self):
        """
        Converts a PointRepository object into a string.
        """
        generated_str = f""
        for point in self.__points:
            generated_str += str(point) + "\n"
        return generated_str

    def __eq__(self, other):
        """
        Input: another PointRepository type object.
        Check if other parameter is equal to the current object.
        Returns True if they are equal and False if not.
        """
        if self.get_number_of_points() != other.get_number_of_points():
            return False
        for point_index in range(self.get_number_of_points()):
            if self.__points[point_index] != other.__points[point_index]:
                return False
        return True

    def get_points(self):
        """
        Getter method - returns the list of points.
        """
        return self.__points

    def get_number_of_points(self):
        """
        Get the number of points in the repository.
        Returns the number of points
        """
        return len(self.__points)

    def add_point(self, input_point):
        """
        Input: a MyPoint type object.
        Adds a new point to the repository.
        """
        self.__points.append(input_point)

    def get_point_at_index(self, input_index):
        """
        Input: an index.
        Returns the point at the given index.
        """
        if -1 < input_index < len(self.__points):
            return self.__points[input_index]
        else:
            raise IndexError("An index error has occurred. Try a new command.")

    def get_all_points_of_color(self, input_color):
        """
        Input: a string representing a color.
        Returns a PointRepository type object with all the points that have the given color.
        """
        points_of_color = PointRepository()
        for point in self.__points:
            if point.get_color() == input_color:
                points_of_color.add_point(point)
        return points_of_color

    def get_all_points_in_square(self, input_corner, input_length):
        """
        Input: a MyPoint type object representing the up-left corner of the square and the length of a square
        Returns a PointRepository type object with all the points inside the given square.
        """
        points_in_square = PointRepository()
        for point in self.__points:
            if general_functions.check_if_in_square(point, input_corner, input_length):
                points_in_square.add_point(point)
        return points_in_square

    def get_min_distance_between_two_points(self):
        """
        Gets the minimum distance between two points from all the points in the repository and returns it.
        """
        if len(self.__points) > 1:
            min_distance = general_functions.distance_between_two_points(self.__points[0], self.__points[1])
            for i in range(len(self.__points) - 1):
                for j in range(i + 1, len(self.__points)):
                    current_distance = general_functions.distance_between_two_points(self.__points[i], self.__points[j])
                    if current_distance < min_distance:
                        min_distance = current_distance
            return min_distance
        else:
            raise IndexError

    def get_max_distance_between_two_points(self):
        """
        Gets the maximum distance between two points from all the points in the repository and returns it.
        """
        if len(self.__points) > 1:
            max_distance = general_functions.distance_between_two_points(self.__points[0], self.__points[1])
            for i in range(len(self.__points) - 1):
                for j in range(i + 1, len(self.__points)):
                    current_distance = general_functions.distance_between_two_points(self.__points[i], self.__points[j])
                    if current_distance > max_distance:
                        max_distance = current_distance
            return max_distance
        else:
            raise IndexError

    def update_point_at_index(self, input_point, input_index):
        """
        Input: a MyPoint type object and an index.
        Updates the point at the given index in the repository with the new given point.
        """
        if -1 < input_index < len(self.__points):
            self.__points[input_index].set_x(input_point.get_x())
            self.__points[input_index].set_y(input_point.get_y())
            self.__points[input_index].set_color(input_point.get_color())
        else:
            raise IndexError

    def delete_point_by_index(self, input_index):
        """
        Input: an index.
        Deletes the point at the given index.
        """
        if -1 < input_index < len(self.__points):
            self.__points.pop(input_index)
        else:
            raise IndexError

    def delete_point(self, input_point):
        """
        Input: a point.
        Deletes all the points that are the same as the given point.
        """
        while input_point in self.__points:
            self.__points.remove(input_point)

    def delete_points_inside_square(self, input_corner, input_length):
        """
        Input: a MyPoint type object representing the up-left corner of the square and the length of a square
        Deletes the points inside the given square.
        """
        new_points_list = self.get_all_points_in_square(input_corner, input_length)
        for point in new_points_list.get_points():
            self.delete_point(point)

    def conversion_for_plotting(self):
        """
        Returns the three needed components for plotting the points of the repository - x's, y's and colors.
        """
        x, y, col = [], [], []
        for point in self.__points:
            x.append(point.get_x())
            y.append(point.get_y())
            col.append(point.get_color())
        return x, y, col

    def plot_all_points(self):
        """
        Plots all the points in a chart.
        """
        x, y, col = self.conversion_for_plotting()
        plt.scatter(x, y, c=col)
        plt.show()

    def shift_all_points_on_x(self, x_distance):
        """
        Input: a distance.
        Shifts all the points on x by the given distance.
        """
        for point in self.__points:
            point.set_x(point.get_x() + x_distance)

    def shift_all_points_on_y(self, y_distance):
        """
        Input: a distance.
        Shifts all the points on y by the given distance.
        """
        for point in self.__points:
            point.set_y(point.get_y() + y_distance)

    def get_all_points_inside_circle(self, input_center, input_radius):
        """
        Input: a distance and a point.
        Generates a repository containing all the points inside the circle with given radius and center.
        Returns the generated repository.
        """
        points_in_circle = PointRepository()
        for point in self.__points:
            if general_functions.check_if_in_circle(point, input_center, input_radius):
                points_in_circle.add_point(point)
        return points_in_circle

    def delete_all_points_within_distance(self, input_point, input_distance):
        """
        Input: a distance and a point.
        Deletes all the points within a given distance from a given point.
        """
        new_points_list = self.get_all_points_inside_circle(input_point, input_distance)
        for point in new_points_list.get_points():
            self.delete_point(point)

