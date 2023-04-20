from application.department_repository_controller import DepartmentRepositoryController
from domain.department_class import Department
from domain.patient_class import Patient


def print_menu():
    """
    Prints all the options available to the user.
    """
    print("exit - exit the program")
    print("menu - print the menu")
    print("print - get all departments")
    print("1.1 - add a department to the repository")
    print("1.2 - delete department by ID")
    print("1.3 - update department by ID")
    print("1.4 - add patient to a department")
    print("1.5. - delete patient from a department")
    print("1.6 - update a patient from a department")
    print("3 - sort the patients in a department by CNP")
    print("4 - sort departments by number of patients")
    print("5 - sort departments by the number of patients having the age above a given limit")
    print("6 - sort departments by the number of patients and the patients in a department alphabetically")
    print("7 - identify departments where there are patients under a given age")
    print("8 - identify patients from a given department for which the first name or last name contain a given string")
    print("9 - identify department/departments where there are patients with a given first name ")
    print("10 - form groups of k patients from the same department and the same disease")
    print("11 - form groups of k departments having at most p patients suffering from the same disease")


def start(controller: DepartmentRepositoryController):
    """
    Starts the program.
    """
    print_menu()
    command = input("--> ")
    while command != "exit" and command != "0" and command != "stop":
        if command == "menu":
            print_menu()
        elif command == "print" or command == "1":
            print(controller)
        elif command == "1.1":
            try:
                read_name = input("Name of department:")
                read_number_of_beds = int(input("Number of beds:"))
                controller.add_department(Department(read_name, read_number_of_beds, []))
            except ValueError as ve:
                print(ve)
        elif command == "1.2":
            try:
                read_id = int(input("ID of the department:"))
                controller.delete_department_by_id(read_id)
            except ValueError as ve:
                print(ve)
        elif command == "1.3":
            try:
                read_id = int(input("ID of the department:"))
                read_name = input("Name of department:")
                read_number_of_beds = int(input("Number of beds:"))
                controller.update_by_id(read_id, read_name, read_number_of_beds)
            except ValueError as ve:
                print(ve)
        elif command == "1.4":
            try:
                read_id = int(input("ID of the department:"))
                read_fn = input("First Name of the patient:")
                read_ln = input("Last Name:")
                read_cnp = int(input("CNP:"))
                read_disease = input("Disease:")
                controller.add_patient_by_id(read_id, Patient(read_fn, read_ln, read_disease, read_cnp))
            except ValueError as ve:
                print(ve)
        elif command == "1.5":
            try:
                read_id = int(input("ID of the department:"))
                read_index = int(input("Index of the patient in that department:"))
                controller.delete_patient_at_index_from_department_with_id(read_id, read_index)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif command == "1.6":
            try:
                read_id = int(input("ID of the department:"))
                read_index = int(input("Index of the patient in that department:"))
                read_fn = input("First Name of the patient:")
                read_ln = input("Last Name:")
                read_cnp = int(input("CNP:"))
                read_disease = input("Disease:")
                controller.modify_patient_at_index_from_department_with_id(read_id, read_index, read_fn, read_ln,
                                                                           read_cnp, read_disease)
            except ValueError as ve:
                print(ve)
            except IndexError as ie:
                print(ie)
        elif command == "3":
            try:
                read_id = int(input("ID of the department:"))
                increasing = input("-increasing or decreasing?")
                controller.sort_patients_by_cnp_in_department_with_id(increasing, read_id)
            except ValueError as ve:
                print(ve)
        elif command == "4":
            try:
                increasing = input("-increasing or decreasing?")
                controller.sort_departments_by_number_of_patients(increasing)
            except ValueError as ve:
                print(ve)
        elif command == "5":
            try:
                read_age = int(input("Age limit:"))
                increasing = input("Sort departments - increasing or decreasing?")
                controller.sort_departments_by_number_of_patients_with_age_above_given_age(read_age, increasing)
            except ValueError as ve:
                print(ve)

        elif command == "6":
            try:
                increasing = input("Sort departments - increasing or decreasing?")
                controller.sort_departments_by_number_of_patients(increasing)
                increasing = input("Sort patients - increasing or decreasing?")
                controller.sort_patients_alphabetically_in_each_department(increasing)
            except ValueError as ve:
                print(ve)
        elif command == "7":
            try:
                read_age = int(input("Age limit:"))
                print(controller.get_departments_with_patients_under_given_age(read_age))
            except ValueError as ve:
                print(ve)
        elif command == "8":
            try:
                read_id = int(input("ID of the department:"))
                read_string = input("String:")
                new_list = controller.identify_patients_with_string_in_name(read_string, read_id)
                for element in new_list:
                    print("-", element)
            except ValueError as ve:
                print(ve)
        elif command == "9":
            try:
                read_fn = input("First name to be searched:")
                print(controller.get_departments_with_patients_with_first_name(read_fn))
            except ValueError as ve:
                print(ve)
        elif command == "10":
            try:
                read_k = int(input("K:"))
            except ValueError as ve:
                print(ve)
        elif command == "11":
            try:
                read_k = int(input("K:"))
                read_p = int(input("P:"))
                for group in controller.groups_of_k_departments_having_at_most_p_patients_with_same_disease(read_k, read_p):
                    print(str(group))
                    print('\n')
            except ValueError as ve:
                print(ve)
        else:
            print("Invalid command, try a new one.")
        command = input("--> ")
