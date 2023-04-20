import random
from utils import general_functions
from domain import patient_class

used_ids = [0] * 1000


class Department:
    def __init__(self, n, b, p=[]):
        self.__name = n
        if b > 0:
            self.__number_of_beds = b
        else:
            raise ValueError("There should be at least one bed in each department. Try a new command.")
        if b < len(p):
            raise ValueError("There are not enough beds in this department. Try a new command.")
        else:
            self.__patients = p
        already_used = True
        id_value = 0
        while already_used:
            id_value = random.randint(1, len(used_ids) - 1)
            if used_ids[id_value] == 0:
                used_ids[id_value] = 1
                already_used = False
        self.__id = id_value

    def __str__(self):
        """
        Converts a Department type object into a string
        """
        generated_str = f'Department {self.__name} with ID {self.__id}, number of beds {self.__number_of_beds},'
        if self.get_number_of_patients() > 0:
            generated_str += f' and patients:' + "\n"
            for patient in self.__patients:
                generated_str += " -" + str(patient) + "\n"
        else:
            generated_str += ' with no patients.' + "\n"
        return generated_str

    def __eq__(self, other):
        """
        Checks if two departments are equal, returns True if they are and False if they are not equal.
        """
        same_patients = True
        if len(self.__patients) == len(other.__patients):
            for index in range(len(self.__patients)):
                if self.__patients[index] != other.__patients[index]:
                    same_patients = False
        return len(self.__patients) == len(other.__patients) and same_patients and self.__name == other.__name and self.__number_of_beds == other.__number_of_beds

    def get_name(self):
        """
        Getter method - returns the name of a department.
        """
        return self.__name

    def get_id(self):
        """
        Getter method - returns the id of a department.
        """
        return self.__id

    def get_number_of_beds(self):
        """
        Getter method - returns the number of beds of a department.
        """
        return self.__number_of_beds

    def get_patients(self):
        """
        Getter method - returns the patients of a department.
        """
        return self.__patients

    def set_name(self, n):
        """
        Setter method - sets the name of a department.
        """
        self.__name = n

    def set_id(self, id_value):
        """
        Setter method - sets the id of a department.
        """
        if used_ids[id_value] == 0:
            used_ids[id_value] = 1
            self.__id = id_value
        else:
            raise ValueError("ID already used. Try a new command.")

    def set_number_of_beds(self, b):
        """
        Setter method - sets the number of beds of a department.
        """
        if self.get_number_of_patients() > b:
            raise ValueError("There are more patients than beds in this department. Try a new command.")
        else:
            self.__number_of_beds = b

    def set_patients(self, p):
        """
        Setter method - sets the patients of a department.
        """
        if self.__number_of_beds < len(p):
            raise ValueError("There are more patients than beds in this department. Try a new command.")
        else:
            self.__patients = p

    def get_number_of_patients(self):
        """
        Returns the number of patients in the department.
        """
        return len(self.__patients)

    def add_patient(self, input_patient):
        """
        Adds a given patient to the department.
        """
        if self.get_number_of_patients() >= self.get_number_of_beds():
            raise ValueError("There are not enough beds for the number of patients. "
                             "Try removing some patients first or modify the number of beds.")
        else:
            self.__patients.append(input_patient)

    def delete_patient_at_index(self, input_index):
        """
        Deletes the patient at the given index from the department.
        """
        if 0 <= input_index < self.get_number_of_patients():
            patient_class.taken_cnps.remove(self.__patients[input_index].get_cnp())
            self.__patients.pop(input_index)
        else:
            raise IndexError("Index is out of range. Try a new command.")

    def modify_patient_at_index(self, input_index, input_fn, input_ln, input_cnp, input_disease):
        """
        Modifies the patient at the given index from the department with the given values.
        """
        if 0 <= input_index < self.get_number_of_patients():
            self.__patients[input_index].set_first_name(input_fn)
            self.__patients[input_index].set_last_name(input_ln)
            self.__patients[input_index].set_cnp(input_cnp)
            self.__patients[input_index].set_disease(input_disease)
        else:
            raise IndexError("Index is out of range. Try a new command.")

    def sort_patients_by_cnp(self, increasing):
        """
        Sorts the patients in the department by CNP, increasingly or decreasingly.
        """
        if increasing == "increasing":
            return general_functions.general_sort(self.__patients,
                                                  lambda p1, p2: p1.get_cnp() <= p2.get_cnp())
        elif increasing == "decreasing":
            return general_functions.general_sort(self.__patients,
                                                  lambda p1, p2: p1.get_cnp() >= p2.get_cnp())
        else:
            raise ValueError("The given input should be increasing or decreasing. Try a new command.")

    def identify_patients_with_string_in_name(self, input_string):
        """
        Creates and returns a list containing the patients from the department having the given string in
        the first or last name.
        """
        return general_functions.list_filter(self.__patients, lambda patient: input_string in patient.get_first_name()
                                                                              or input_string in patient.get_last_name())

    def identify_patients_with_given_first_name(self, input_fn):
        """
        Creates and returns a list containing the patients from the department having the given first name.
        """
        return general_functions.list_filter(self.__patients, lambda patient: input_fn == patient.get_first_name())

    def identify_patients_under_given_age(self, input_age):
        """
        Creates and returns a list containing the patients from the department being under the given age.
        """
        return general_functions.list_filter(self.__patients, lambda patient: patient.get_age() < input_age)

    def identify_patients_above_given_age(self, input_age):
        """
        Creates and returns a list containing the patients from the department being under the given age.
        """
        return general_functions.list_filter(self.__patients, lambda patient: patient.get_age() >= input_age)

    def sort_patients_alphabetically(self, increasing):
        """
        Sorts the patients in the department alphabetically.
        """
        if increasing == "increasing":
            return general_functions.general_sort(self.__patients, lambda p1, p2: p1.get_first_name() + p1.get_last_name() < p2.get_first_name() + p2.get_last_name())
        elif increasing == "decreasing":
            return general_functions.general_sort(self.__patients, lambda p1, p2: p1.get_first_name() + p1.get_last_name() > p2.get_first_name() + p2.get_last_name())
        else:
            raise ValueError("The given input should be increasing or decreasing. Try a new command.")

    def get_number_of_patients_with_disease(self, given_disease):
        """
        Computes and returns the number of patients having the given disease in the department.
        """
        number = 0
        for patient in self.__patients:
            if patient.get_disease() == given_disease:
                number += 1
        return number

    def get_maximum_number_of_patients_with_same_disease(self):
        """
        Computes and returns the maximum number of patients in the department with the same disease.
        """
        maximum = 0
        disease_list = self.get_all_diseases_list()
        for disease in disease_list:
            if self.get_number_of_patients_with_disease(disease) > maximum:
                maximum = self.get_number_of_patients_with_disease(disease)
        return maximum

    def has_at_most_p_patients_suffering_of_same_disease(self, input_p):
        """
        Returns True if the department has at most p patients suffering from the same disease and False otherwise.
        """
        return self.get_maximum_number_of_patients_with_same_disease() <= input_p

    def get_all_diseases_list(self):
        """
        Creates and returns a list containing all the diseases the patients in the department have,
        without repeating them.
        """
        disease_list = []
        for patient in self.__patients:
            if patient.get_disease() not in disease_list:
                disease_list.append(patient.get_disease())
        return disease_list
