import point_module
from point_module import MyPoint
from point_repository_module import PointRepository


def print_menu():
    """
    Prints all the options available to the user.
    """
    print("exit - exit the program")
    print("menu - print the menu")
    print("1 - get all points")
    print("2 - add a point to the repository")
    print("3 - get the point at a given index")
    print("4 - get all the points of a given color")
    print("5 - get all points inside a given square")
    print("6 - get the minimum distance between two points")
    print("7 - update a point at a given index")
    print("8 - delete a point by index")
    print("9 - delete all points that are inside a given square")
    print("10 - plot all points in a chart")
    print("13 - get the maximum distance between two points")
    print("16 - shift all points on x axis")
    print("17 - shift all points on y axis")
    print("20 - delete all points within a distance from a point")


def start():
    """
    Starts the program.
    """
    my_repository = PointRepository(
        [MyPoint(2, 3, "blue"), MyPoint(6, 6, "red"), MyPoint(-10, 7, "green"), MyPoint(0, 1, "red"),
         MyPoint(10, -5, "magenta"), MyPoint(0, 2, "yellow"), MyPoint(8, 11, "magenta"), MyPoint(-4, -6, "blue"),
         MyPoint(-32, 100, "yellow"), MyPoint(0, 0, "red")])
    print_menu()
    command = input("--> ")
    while command != "exit" and command != "0" and command != "stop":
        if command == "menu":
            print_menu()
        elif command == "1":
            print(my_repository)
        elif command == "2":
            new_point = []
            try:
                new_point.append(int(input("X coordinate: ")))
                new_point.append(int(input("Y coordinate: ")))
                new_point.append(input("Color of the point: "))
                my_repository.add_point(MyPoint(new_point[0], new_point[1], new_point[2]))
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif command == "3":
            try:
                read_index = int(input("Index: "))
                print(my_repository.get_point_at_index(read_index))
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif command == "4":
            read_color = input("Color: ")
            if read_color in point_module.valid_colors:
                new_points_list = my_repository.get_all_points_of_color(read_color)
                if len(new_points_list.get_points()) != 0:
                    print(new_points_list)
                else:
                    print("No points with given color found.")
            else:
                print("Invalid color. Try a new command.")
        elif command == "5":
            try:
                read_x = int(input("Up-left corner x coordinate: "))
                read_y = int(input("Up-left corner y coordinate: "))
                read_length = int(input("Square length: "))
                up_left_point = MyPoint(read_x, read_y, "red")
                new_points_list = my_repository.get_all_points_in_square(up_left_point, read_length)
                if len(new_points_list.get_points()) != 0:
                    print(new_points_list)
                else:
                    print("No points with given color found.")
            except ValueError as ve:
                print(ve)
        elif command == "6":
            try:
                print("Minimum distance is: ", my_repository.get_min_distance_between_two_points())
            except IndexError as ie:
                print("You need at least 2 points in the repository for this command. Try a new command.")
        elif command == "7":
            new_point = []
            try:
                read_index = int(input("Index: "))
                read_x = int(input("X coordinate: "))
                read_y = int(input("Y coordinate: "))
                read_color = input("Color of the point: ")
                new_point = MyPoint(read_x, read_y, read_color)
                my_repository.update_point_at_index(new_point, read_index)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif command == "8":
            try:
                read_index = int(input("Index: "))
                my_repository.delete_point_by_index(read_index)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif command == "9":
            try:
                read_x = int(input("Up-left corner x coordinate: "))
                read_y = int(input("Up-left corner y coordinate: "))
                read_length = int(input("Square length: "))
                up_left_point = MyPoint(read_x, read_y, "red")
                my_repository.delete_points_inside_square(up_left_point, read_length)
            except ValueError as ve:
                print(ve)
        elif command == "10":
            my_repository.plot_all_points()
        elif command == "13":
            try:
                print("Maximum distance is: ", my_repository.get_max_distance_between_two_points())
            except IndexError as ie:
                print("You need at least 2 points in the repository for this command. Try a new command.")
        elif command == "16":
            try:
                read_distance = int(input("By how much(+ or -): "))
                my_repository.shift_all_points_on_x(read_distance)
            except ValueError as ve:
                print(ve)
        elif command == "17":
            try:
                read_distance = int(input("By how much(+ or -): "))
                my_repository.shift_all_points_on_y(read_distance)
            except ValueError as ve:
                print(ve)
        elif command == "20":
            try:
                read_x = int(input("Point x coordinate: "))
                read_y = int(input("Point y coordinate: "))
                read_length = int(input("Distance: "))
                center = MyPoint(read_x, read_y, "red")
                my_repository.delete_all_points_within_distance(center, read_length)
            except ValueError as ve:
                print(ve)
        else:
            print("Invalid command, try a new one.")
        command = input("--> ")
