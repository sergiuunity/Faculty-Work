import datetime
with_age = True
from utils.general_functions import is_cnp_valid
taken_cnps = []


class Patient:
    def __init__(self, fn, ln, d, c):
        self.__first_name = fn
        self.__last_name = ln
        self.__disease = d
        if is_cnp_valid(int(c)) and int(c) not in taken_cnps:
            taken_cnps.append(int(c))
            self.__cnp = int(c)
        else:
            raise ValueError("The given CNP is not valid or it is not unique. Try a new command.")

    def __str__(self):
        """
        Converts a Patient type object into a string
        """
        generated_str = f'{self.__first_name} {self.__last_name} with CNP ({self.__cnp}) suffering of {self.__disease}'
        if with_age:
            generated_str += f', age: {self.get_age()}'
        return generated_str

    def __eq__(self, other):
        """
        Returns True if two Patients are equal and False otherwise.
        """
        return self.__first_name == other.__first_name and self.__last_name == other.__last_name and self.__disease == other.__disease and self.__cnp == other.__cnp

    def get_first_name(self):
        """
        Getter method - returns the first_name of a patient.
        """
        return self.__first_name

    def get_last_name(self):
        """
        Getter method - returns the last_name of a patient.
        """
        return self.__last_name

    def get_disease(self):
        """
        Getter method - returns the disease of a patient.
        """
        return self.__disease

    def get_cnp(self):
        """
        Getter method - returns the personal numerical code of a patient.
        """
        return self.__cnp

    def get_age(self):
        """
        Returns the age of the patient in years based on his/her CNP.
        """
        today_year = datetime.datetime.today().year
        today_month = datetime.datetime.today().month
        today_day = datetime.datetime.today().day
        age = (today_year - (self.__cnp // 10 ** 10) % 100) % 100
        if (self.__cnp // 10 ** 8) % 100 > today_month or (
                (self.__cnp // 10 ** 8) % 100 == today_month and (self.__cnp // 10 ** 6) % 100 > today_day):
            age -= 1
        return age

    def set_first_name(self, fn):
        """
        Setter method - sets the first_name of a patient.
        """
        self.__first_name = fn

    def set_last_name(self, ln):
        """
        Setter method - sets the last_name of a patient.
        """
        self.__last_name = ln

    def set_disease(self, d):
        """
        Setter method - sets the disease of a patient.
        """
        self.__disease = d

    def set_cnp(self, c):
        """
        Setter method - sets the personal numerical code of a patient.
        """
        if is_cnp_valid(int(c)) and int(c) not in taken_cnps:
            taken_cnps.remove(self.get_cnp())
            taken_cnps.append(int(c))
            self.__cnp = int(c)
        else:
            raise ValueError("The given CNP is not valid or it is not unique. Try a new command.")
