from utils import general_functions, backtracking
from domain import patient_class


class DepartmentRepository:
    def __init__(self, department_list=[]):
        self.__departments = department_list.copy()

    def __str__(self):
        """
        Converts a DepartmentRepository type object into a string.
        """
        generated_str = ""
        for department in self.__departments:
            generated_str += "*" + str(department) + "\n"
        return generated_str

    def __eq__(self, other):
        """
        Returns True if two DepartmentRepositories are equal and False otherwise.
        """
        if self.get_number_of_departments() == other.get_number_of_departments():
            for index in range(self.get_number_of_departments()):
                if self.__departments[index] != other.__departments[index]:
                    return False
        return self.get_number_of_departments() == other.get_number_of_departments()

    def get_departments(self):
        """
        Getter method - returns the list of departments.
        """
        return self.__departments

    def set_departments(self, department_list):
        """
        Setter method - sets the department_list.
        """
        self.__departments = department_list

    def get_number_of_departments(self):
        """
        Get the number of departments in the repository.
        Returns the number of departments.
        """
        return len(self.__departments)

    def add_department(self, input_department):
        """
        Adds the given department to the repository.
        """
        self.__departments.append(input_department)

    def delete_department_by_id(self, input_id):
        """
        Deletes the department with the given ID from the repository.
        """
        for patient in self.__departments[self.get_index_by_id(input_id)].get_patients():
            patient_class.taken_cnps.remove(patient.get_cnp())
        self.__departments.pop(self.get_index_by_id(input_id))

    def get_index_by_id(self, input_id):
        """
        Returns the index of the department with the given ID if it exists, or raises an error if
        such ID does not exist.
        """
        for index in range(self.get_number_of_departments()):
            if self.__departments[index].get_id() == input_id:
                return index
        raise ValueError("No such ID was found. Try a new command")

    def update_by_id(self, input_id, input_name, input_number_of_beds):
        """
        Updates the name and the number of beds of the department with the given id by the given values.
        """
        index = self.get_index_by_id(input_id)
        self.__departments[index].set_name(input_name)
        self.__departments[index].set_number_of_beds(input_number_of_beds)

    def add_patient_by_id(self, input_id, input_patient):
        """
        Adds a given patient to the department with the given ID.
        """
        self.__departments[self.get_index_by_id(input_id)].add_patient(input_patient)

    def delete_patient_at_index_from_department_with_id(self, input_id, input_index):
        """
        Deletes the patient at the given index from the department with the given ID from the repository.
        """
        self.__departments[self.get_index_by_id(input_id)].delete_patient_at_index(input_index)

    def modify_patient_at_index_from_department_with_id(self, input_id, input_index, input_fn, input_ln, input_cnp,
                                                        input_disease):
        """
        Modifies the patient at the given index from the department with the given ID from
        the repository with the given values.
        """
        self.__departments[self.get_index_by_id(input_id)].modify_patient_at_index(input_index, input_fn,
                                                                                   input_ln, input_cnp,
                                                                                   input_disease)

    def identify_patients_with_string_in_name_in_department_with_id(self, input_string, input_id):
        """
        Creates and returns a list containing the patients from the department with the given id
        having the given string in the first or in the last name.
        """
        return self.__departments[self.get_index_by_id(input_id)].identify_patients_with_string_in_name(input_string)

    def sort_patients_by_cnp_in_department_with_id(self, increasing, input_id):
        """
        Sorts the patients by CNP in the department with the given ID, increasingly or decreasingly.
        """
        self.__departments[self.get_index_by_id(input_id)].sort_patients_by_cnp(increasing)

    def sort_departments_by_number_of_patients(self, increasing):
        """
        Sorts the departments in the repository by the number of patients, increasingly or decreasingly.
        """
        if increasing == "increasing":
            return general_functions.general_sort(self.__departments,
                                                  lambda d1, d2: d1.get_number_of_patients() <= d2.
                                                  get_number_of_patients())
        elif increasing == "decreasing":
            return general_functions.general_sort(self.__departments,
                                                  lambda d1, d2: d1.get_number_of_patients() >= d2.
                                                  get_number_of_patients())
        else:
            raise ValueError("The given input should be increasing or decreasing. Try a new command.")

    def get_departments_with_patients_with_first_name(self, input_fn):
        """
        Returns a repository with all the departments which have patients with the given first name.
        """
        return DepartmentRepository(general_functions.list_filter
                                    (self.__departments,
                                     lambda department: len(
                                         department.identify_patients_with_given_first_name(input_fn)) > 0))

    def get_departments_with_patients_under_given_age(self, input_age):
        """
        Returns a repository with all the departments which have patients with age under given age.
        """
        return DepartmentRepository(general_functions.list_filter
                                    (self.__departments,
                                     lambda department: len(
                                         department.identify_patients_under_given_age(input_age)) > 0))

    def sort_patients_alphabetically_in_each_department(self, increasing):
        """
        Sorts the patients in every department alphabetically.
        """
        for department in self.__departments:
            department.sort_patients_alphabetically(increasing)

    def sort_departments_by_number_of_patients_with_age_above_given_age(self, input_age, increasing):
        """
        Sorts the departments by the number of patients with age above a given age.
        """
        if increasing == "increasing":
            return general_functions.general_sort(self.__departments, lambda d1, d2: len(d1.identify_patients_above_given_age(input_age)) <= len(d2.identify_patients_above_given_age(input_age)))
        elif increasing == "decreasing":
            return general_functions.general_sort(self.__departments, lambda d1, d2: len(d1.identify_patients_above_given_age(input_age)) >= len(d2.identify_patients_above_given_age(input_age)))
        else:
            raise ValueError("The given input should be increasing or decreasing. Try a new command.")

    def groups_of_k_departments_having_at_most_p_patients_with_same_disease(self, k, p):
        """
        Generates the groups of k departments having at most p patients with same disease.
        """
        return backtracking.groups_of_k_departments_having_at_most_p_patients_with_same_disease\
            (self.get_number_of_departments(), k, p, self.get_departments())

    def group_of_k_patients_same_department_and_disease(self, n, k):
        """
            Generates the groups of k patients from same department suffering from the same disease.
        """
        #for department in self.get_departments():



