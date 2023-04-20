from infrastructure.department_repository import DepartmentRepository


class DepartmentRepositoryController:
    def __init__(self, department_repository: DepartmentRepository = DepartmentRepository()):
        self.__department_repository = department_repository

    def __str__(self):
        """
        Returns the string representation of the controller.
        """
        return str(self.__department_repository)

    def __eq__(self, other):
        """
        Returns True if two DepartmentRepositoryController type object are equal and False otherwise.
        """
        return self.__department_repository == other.__department_repository

    def get_department_repository(self):
        """
        Getter method - return the department_repository.
        """
        return self.__department_repository

    def set_department_repository(self, department_repository):
        """
        Setter method - sets the department_list.
        """
        self.__department_repository = department_repository

    def get_number_of_departments(self):
        """
        Get the number of departments in the repository.
        Returns the number of departments.
        """
        return self.__department_repository.get_number_of_departments()

    def add_department(self, input_department):
        """
        Adds the given department to the repository.
        """
        self.__department_repository.add_department(input_department)

    def delete_department_by_id(self, input_id):
        """
        Deletes the department with the given ID from the repository.
        """
        self.__department_repository.delete_department_by_id(input_id)

    def update_by_id(self, input_id, input_name, input_number_of_beds):
        """
        Updates the name and the number of beds of the department with the given id by the given values.
        """
        self.__department_repository.update_by_id(input_id, input_name, input_number_of_beds)

    def add_patient_by_id(self, input_id, input_patient):
        """
        Adds a given patient to the department with the given ID.
        """
        self.__department_repository.add_patient_by_id(input_id, input_patient)

    def delete_patient_at_index_from_department_with_id(self, input_id, input_index):
        """
        Deletes the patient at the given index from the department with the given ID from the repository.
        """
        self.__department_repository.delete_patient_at_index_from_department_with_id(input_id, input_index)

    def modify_patient_at_index_from_department_with_id(self, input_id, input_index, input_fn, input_ln, input_cnp,
                                                        input_disease):
        """
        Modifies the patient at the given index from the department with the given ID from
        the repository with the given values.
        """
        self.__department_repository.modify_patient_at_index_from_department_with_id(input_id, input_index, input_fn,
                                                                                     input_ln, input_cnp, input_disease)

    def identify_patients_with_string_in_name(self, input_string, input_id):
        """
        Creates and returns a list containing the patients from the department with the given id
        having the given string in the first or in the last name.
        """
        return self.__department_repository.identify_patients_with_string_in_name_in_department_with_id(input_string, input_id)

    def sort_departments_by_number_of_patients(self, increasing):
        """
        Sorts the departments in the repository by the number of patients, increasingly or decreasingly.
        """
        return self.__department_repository.sort_departments_by_number_of_patients(increasing)

    def sort_patients_by_cnp_in_department_with_id(self, increasing, input_id):
        """
        Sorts the patients by CNP in the department with the given ID, increasingly or decreasingly.
        """
        self.__department_repository.sort_patients_by_cnp_in_department_with_id(increasing, input_id)

    def get_departments_with_patients_with_first_name(self, input_fn):
        """
        Returns a repository with all the departments which have patients with the given first name.
        """
        return self.__department_repository.get_departments_with_patients_with_first_name(input_fn)

    def get_departments_with_patients_under_given_age(self, input_age):
        """
        Returns a repository with all the departments which have patients with age under given age.
        """
        return self.__department_repository.get_departments_with_patients_under_given_age(input_age)

    def sort_patients_alphabetically_in_each_department(self, increasing):
        """
        Sorts the patients in every department alphabetically.
        """
        self.__department_repository.sort_patients_alphabetically_in_each_department(increasing)

    def sort_departments_by_number_of_patients_with_age_above_given_age(self, input_age, increasing):
        """
        Sorts the departments by the number of patients with age above a given age.
        """
        self.__department_repository.sort_departments_by_number_of_patients_with_age_above_given_age(
            input_age, increasing)

    def groups_of_k_departments_having_at_most_p_patients_with_same_disease(self, k, p):
        """
        Generates the groups of k departments having at most p patients with same disease.
        """
        return self.__department_repository.\
            groups_of_k_departments_having_at_most_p_patients_with_same_disease(k, p)
