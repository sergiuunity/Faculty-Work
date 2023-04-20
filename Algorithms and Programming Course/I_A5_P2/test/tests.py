import unittest
from domain.department_class import Department
from domain.patient_class import Patient
from infrastructure.department_repository import DepartmentRepository
from application.department_repository_controller import DepartmentRepositoryController
from utils import general_functions
from utils import backtracking
from domain import patient_class


class TestPatient(unittest.TestCase):
    def test_get_age(self):
        """
        Tests the function get_age.
        """
        patient = Patient("George", "Manson", "allergy", "1980430130846")
        self.assertEqual(patient.get_age(), 23)
        patient = Patient("Mark", "Shelton", "anemia", "5210612453170")
        self.assertEqual(patient.get_age(), 0)
        patient = Patient("John", "Bird", "headache", "6030312407383")
        self.assertEqual(patient.get_age(), 18)


class TestDepartmentRepositoryController(unittest.TestCase):
    def setUp(self):
        self.empty_controller = DepartmentRepositoryController(DepartmentRepository())
        self.example_patient = Patient("George", "Manson", "allergy", "1980430130846")
        patient_class.taken_cnps = []
        example = DepartmentRepository(
            [Department("Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                           Patient("Hannah", "Redd", "stroke", 2910830317287),
                                           Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
             Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2890125259914),
                                          Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                          Patient("Wilt", "Norris", "headache", 1890903333287),
                                          Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                          Patient("Judith", "Park", "headache", 2900919387383)]),
             Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                    Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
             Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
             Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                            Patient("Tiffany", "Sam", "arthritis", 2560306012395)])])
        self.example_controller = DepartmentRepositoryController(example)

    def test_get_number_of_departments(self):
        """
        Tests the function get_number_of_departments.
        """
        self.assertEqual(self.example_controller.get_number_of_departments(), 5)
        self.assertEqual(self.empty_controller.get_number_of_departments(), 0)
        test_controller = DepartmentRepository(
            [Department("Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 1900627067576)])])
        self.assertEqual(test_controller.get_number_of_departments(), 1)

    def test_add_department(self):
        """
        Tests the function get_number_of_departments.
        """
        self.empty_controller.add_department(Department("Radiology", 20, []))
        self.assertEqual(self.empty_controller, DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, [])])))
        self.empty_controller.add_department(Department("Virology", 70, []))
        self.assertEqual(self.empty_controller, DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, []),
                                  Department("Virology", 70, [])])))
        self.empty_controller.add_department(Department("Orthopedics", 10, []))
        self.assertEqual(self.empty_controller, DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, []),
                                  Department("Virology", 70, []),
                                  Department("Orthopedics", 10, [])])))

    def test_delete_department_by_id(self):
        """
        Tests the function delete_department_by_id.
        """
        test_controller = DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, []),
                                  Department("Virology", 70, []),
                                  Department("Orthopedics", 10, [])]))
        test_controller.delete_department_by_id(test_controller.get_department_repository().get_departments()[0]
                                                .get_id())
        self.assertEqual(test_controller, DepartmentRepositoryController(
            DepartmentRepository([
                Department("Virology", 70, []),
                Department("Orthopedics", 10, [])])))
        self.assertRaises(ValueError, test_controller.delete_department_by_id, -3)
        test_controller.delete_department_by_id(test_controller.
                                                get_department_repository().get_departments()[1].get_id())
        self.assertEqual(test_controller, DepartmentRepositoryController(
            DepartmentRepository([Department("Virology", 70, [])])))

    def test_update_by_id(self):
        """
        Tests the function update_by_id.
        """
        test_controller = DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, []),
                                  Department("Virology", 70, []),
                                  Department("Orthopedics", 10, [])]))
        test_controller.update_by_id(test_controller.get_department_repository().get_departments()[0].get_id(),
                                     "Neurology", 10)
        self.assertEqual(test_controller, DepartmentRepositoryController(
            DepartmentRepository([Department("Neurology", 10, []),
                                  Department("Virology", 70, []),
                                  Department("Orthopedics", 10, [])])))
        test_controller.update_by_id(test_controller.get_department_repository().get_departments()[2].get_id(),
                                     "Cardiology", 40)
        self.assertEqual(test_controller, DepartmentRepositoryController(
            DepartmentRepository([Department("Neurology", 10, []),
                                  Department("Virology", 70, []),
                                  Department("Cardiology", 40, [])])))
        self.assertRaises(ValueError, test_controller.update_by_id, -32, "Random", 10)

    def test_add_patient_by_id(self):
        """
        Tests the function add_patient_by_id.
        """
        test_controller = DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, []),
                                  Department("Virology", 70, []),
                                  Department("Orthopedics", 10, [])]))
        test_controller.add_patient_by_id(test_controller.get_department_repository().get_departments()[2].get_id(),
                                          self.example_patient)
        self.assertEqual(test_controller, DepartmentRepositoryController(DepartmentRepository([
            Department("Radiology", 20, []),
            Department("Virology", 70, []),
            Department("Orthopedics", 10, [self.example_patient])])))
        self.assertRaises(ValueError, self.empty_controller.add_patient_by_id, -4, self.example_patient)
        test_controller.add_patient_by_id(test_controller.get_department_repository().get_departments()[2].get_id(),
                                          Patient("Carl", "Harrison", "sprain", 1920627385666))

    def test_delete_patient_at_index_from_department_with_id(self):
        """
        Tests the function delete_patient_at_index_from_department_with_id.
        """
        test_controller = DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, [Patient("Marry", "Kennedy", "anemia", 6001020026930)]),
                                  Department("Virology", 70, []),
                                  Department("Orthopedics", 10, [])]))
        test_controller.delete_patient_at_index_from_department_with_id(
            test_controller.get_department_repository().get_departments()[0].get_id(), 0)
        self.assertEqual(test_controller, DepartmentRepositoryController(DepartmentRepository([
            Department("Radiology", 20, []),
            Department("Virology", 70, []),
            Department("Orthopedics", 10, [])])))
        self.assertRaises(ValueError, self.empty_controller.delete_patient_at_index_from_department_with_id, -4, 2)
        self.assertRaises(ValueError, self.empty_controller.delete_patient_at_index_from_department_with_id,
                          9323232, 20)

    def test_modify_patient_at_index_from_department_with_id(self):
        """
        Tests the function modify_patient_at_index_from_department_with_id.
        """
        test_controller = DepartmentRepositoryController(
            DepartmentRepository([Department("Radiology", 20, [Patient("Marry", "Kennedy", "anemia", 6001020026930)]),
                                  Department("Virology", 70, []),
                                  Department("Orthopedics", 10, [])]))
        self.assertRaises(IndexError, test_controller.modify_patient_at_index_from_department_with_id,
                          test_controller.get_department_repository().get_departments()[2].get_id(), -3, "Bob", "White",
                          1881204037434, "tbc")
        test_controller.modify_patient_at_index_from_department_with_id(
            test_controller.get_department_repository().get_departments()[0].get_id(), 0,
            "Bob", "White", 1881204037434, "tbc")
        patient_class.taken_cnps = []
        self.assertEqual(test_controller, DepartmentRepositoryController(DepartmentRepository([
            Department("Radiology", 20, [Patient("Bob", "White", "tbc", 1881204037434)]),
            Department("Virology", 70, []),
            Department("Orthopedics", 10, [])])))

    def test_identify_patients_with_string_in_name(self):
        """
        Tests the function identify_patients_with_string_in_name.
        """
        self.assertRaises(ValueError, self.example_controller.identify_patients_with_string_in_name, "str", -4)
        patient_class.taken_cnps = []
        self.assertEqual(self.
                         example_controller.
                         identify_patients_with_string_in_name
                         ("th", self.example_controller.
                          get_department_repository().get_departments()[1].get_id()),
                         [Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                          Patient("Judith", "Park", "headache", 2900919387383)])
        self.assertEqual(self.
                         example_controller.
                         identify_patients_with_string_in_name
                         ("xyz", self.example_controller.
                          get_department_repository().get_departments()[0].get_id()),
                         [])

    def test_sort_departments_by_number_of_patients(self):
        """
        Tests the function sort_departments_by_number_of_patients.
        """
        patient_class.taken_cnps = []
        self.empty_controller.sort_departments_by_number_of_patients("increasing")
        self.assertEqual(self.empty_controller, DepartmentRepositoryController(DepartmentRepository()))
        self.example_controller.sort_departments_by_number_of_patients("increasing")
        self.assertEqual(self.example_controller, DepartmentRepositoryController(DepartmentRepository([
            Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
            Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                   Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
            Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                           Patient("Tiffany", "Sam", "arthritis", 2560306012395)]),
            Department(
                "Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                   Patient("Hannah", "Redd", "stroke", 2910830317287),
                                   Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
            Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2890125259914),
                                         Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                         Patient("Wilt", "Norris", "headache", 1890903333287),
                                         Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                         Patient("Judith", "Park", "headache", 2900919387383)])
        ])))
        patient_class.taken_cnps = []
        self.example_controller.sort_departments_by_number_of_patients("decreasing")
        self.assertEqual(self.example_controller, DepartmentRepositoryController(DepartmentRepository([
            Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2890125259914),
                                         Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                         Patient("Wilt", "Norris", "headache", 1890903333287),
                                         Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                         Patient("Judith", "Park", "headache", 2900919387383)]),
            Department(
                "Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                   Patient("Hannah", "Redd", "stroke", 2910830317287),
                                   Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
            Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                   Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
            Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                           Patient("Tiffany", "Sam", "arthritis", 2560306012395)]),
            Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)])
        ])))

    def test_sort_patients_by_cnp_in_department_with_id(self):
        """
        Tests the function sort_patients_by_cnp_in_department_with_id.
        """
        patient_class.taken_cnps = []
        self.assertRaises(ValueError, self.example_controller.sort_patients_by_cnp_in_department_with_id, "random",
                          self.example_controller.get_department_repository().get_departments()[0].get_id())
        patient_class.taken_cnps = []
        self.example_controller.sort_patients_by_cnp_in_department_with_id(
            "increasing", self.example_controller.get_department_repository().get_departments()[1].get_id())
        self.assertEqual(self.example_controller, DepartmentRepositoryController(DepartmentRepository(
            [Department("Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                           Patient("Hannah", "Redd", "stroke", 2910830317287),
                                           Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
             Department("Neurology", 30, [Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                          Patient("Wilt", "Norris", "headache", 1890903333287),
                                          Patient("Amy", "Scott", "headache", 2890125259914),
                                          Patient("Judith", "Park", "headache", 2900919387383),
                                          Patient("Bertha", "Kim", "epilepsy", 2981231519852)
                                          ]),
             Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                    Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
             Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
             Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                            Patient("Tiffany", "Sam", "arthritis", 2560306012395)])])))
        patient_class.taken_cnps = []
        self.example_controller.\
            sort_patients_by_cnp_in_department_with_id("decreasing", self.example_controller.
                                                       get_department_repository().get_departments()[0].get_id())
        self.assertEqual(self.example_controller, DepartmentRepositoryController(DepartmentRepository(
            [Department("Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                           Patient("Hannah", "Redd", "stroke", 2910830317287),
                                           Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
             Department("Neurology", 30, [Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                          Patient("Wilt", "Norris", "headache", 1890903333287),
                                          Patient("Amy", "Scott", "headache", 2890125259914),
                                          Patient("Judith", "Park", "headache", 2900919387383),
                                          Patient("Bertha", "Kim", "epilepsy", 2981231519852)
                                          ]),
             Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                    Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
             Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
             Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                            Patient("Tiffany", "Sam", "arthritis", 2560306012395)])])))

    def test_get_departments_with_patients_with_first_name(self):
        """
        Tests the function get_departments_with_patients_with_first_name.
        """
        patient_class.taken_cnps = []
        self.assertEqual(self.example_controller.get_departments_with_patients_with_first_name("Johny"),
                         DepartmentRepository(
                             [Department("Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                                            Patient("Hannah", "Redd", "stroke", 2910830317287),
                                                            Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
                              Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                                             Patient("Tiffany", "Sam", "arthritis", 2560306012395)])]))
        patient_class.taken_cnps = []
        self.assertEqual(self.example_controller.get_departments_with_patients_with_first_name("Redd"),
                         DepartmentRepository([]))
        patient_class.taken_cnps = []
        self.assertEqual(self.example_controller.get_departments_with_patients_with_first_name("Kelly"),
                         DepartmentRepository([Department("Renal Unit", 40, [
                             Patient("Kelly", "Gib", "kidney stones", 6000205248718)])]))

    def test_get_departments_with_patients_under_given_age(self):
        """
        Tests the function get_departments_with_patients_under_given_age.
        """
        patient_class.taken_cnps = []
        self.assertEqual(self.example_controller.get_departments_with_patients_under_given_age(10),
                         DepartmentRepository([]))
        patient_class.taken_cnps = []
        self.assertRaises(TypeError, self.example_controller.get_departments_with_patients_under_given_age, "text")
        self.assertEqual(self.example_controller.get_departments_with_patients_under_given_age(100),
                         DepartmentRepository(
                             [Department("Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                                            Patient("Hannah", "Redd", "stroke", 2910830317287),
                                                            Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
                              Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2890125259914),
                                                           Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                                           Patient("Wilt", "Norris", "headache", 1890903333287),
                                                           Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                                           Patient("Judith", "Park", "headache", 2900919387383)]),
                              Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                                     Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
                              Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
                              Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                                             Patient("Tiffany", "Sam", "arthritis", 2560306012395)])]))

    def test_sort_patients_alphabetically_in_each_department(self):
        """
        Tests the function sort_patients_alphabetically_in_each_department.
        """
        patient_class.taken_cnps = []
        self.assertRaises(ValueError, self.example_controller.sort_patients_alphabetically_in_each_department, "random")
        patient_class.taken_cnps = []
        self.example_controller.sort_patients_alphabetically_in_each_department("increasing")
        self.assertEqual(self.example_controller,
                         DepartmentRepositoryController(DepartmentRepository(
                             [Department("Cardiology", 50,
                                         [Patient("Hannah", "Redd", "stroke", 2910830317287),
                                          Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                          Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
                              Department("Neurology", 30, [
                                  Patient("Amy", "Scott", "headache", 2890125259914),
                                  Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                  Patient("Judith", "Park", "headache", 2900919387383),
                                  Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                  Patient("Wilt", "Norris", "headache", 1890903333287)]),
                              Department("ENT", 60, [
                                  Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                  Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
                              Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
                              Department("Orthopedics", 60, [
                                  Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                  Patient("Tiffany", "Sam", "arthritis", 2560306012395)])])))
        patient_class.taken_cnps = []
        self.example_controller.sort_patients_alphabetically_in_each_department("decreasing")
        self.assertEqual(self.example_controller,
                         DepartmentRepositoryController(DepartmentRepository(
                             [Department("Cardiology", 50,
                                         [Patient("Timothy", "Reynold", "stroke", 1931101414047),
                                          Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                          Patient("Hannah", "Redd", "stroke", 2910830317287),
                                          ]),
                              Department("Neurology", 30, [
                                  Patient("Wilt", "Norris", "headache", 1890903333287),
                                  Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                  Patient("Judith", "Park", "headache", 2900919387383),
                                  Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                  Patient("Amy", "Scott", "headache", 2890125259914)
                              ]),
                              Department("ENT", 60, [
                                  Patient("Penny", "Tanya", "sinusitis", 2910627383279),
                                  Patient("Daniel", "Williams", "tinnitus", 1960130120454)
                              ]),
                              Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
                              Department("Orthopedics", 60, [
                                  Patient("Tiffany", "Sam", "arthritis", 2560306012395),
                                  Patient("Johny", "Kemp", "scoliosis", 1860210393595)
                                  ])])))

    def test_sort_departments_by_number_of_patients_with_age_above_given_age(self):
        """
        Tests the function sort_departments_by_number_of_patients_with_age_above_given_age.
        """
        patient_class.taken_cnps = []
        self.assertRaises(ValueError, self.empty_controller.
                          sort_departments_by_number_of_patients_with_age_above_given_age, 70, "text")
        patient_class.taken_cnps = []
        self.example_controller.sort_departments_by_number_of_patients_with_age_above_given_age(90, "increasing")
        self.assertEqual(self.example_controller,
                         DepartmentRepositoryController(
                             DepartmentRepository(
                                 [Department("Cardiology", 50,
                                             [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                              Patient("Hannah", "Redd", "stroke", 2910830317287),
                                              Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
                                  Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2890125259914),
                                                               Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                                               Patient("Wilt", "Norris", "headache", 1890903333287),
                                                               Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                                               Patient("Judith", "Park", "headache", 2900919387383)]),
                                  Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                                         Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
                                  Department("Renal Unit", 40,
                                             [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
                                  Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                                                 Patient("Tiffany", "Sam", "arthritis",
                                                                         2560306012395)])])
                         ))
        patient_class.taken_cnps = []
        self.example_controller.sort_departments_by_number_of_patients_with_age_above_given_age(20, "decreasing")
        self.assertEqual(self.example_controller,
                         DepartmentRepositoryController(
                             DepartmentRepository(
                                 [Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2890125259914),
                                                               Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                                               Patient("Wilt", "Norris", "headache", 1890903333287),
                                                               Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                                               Patient("Judith", "Park", "headache", 2900919387383)]),
                                  Department("Cardiology", 50,
                                             [Patient("Johny", "Specter", "hearth attack", 5010616032007),
                                              Patient("Hannah", "Redd", "stroke", 2910830317287),
                                              Patient("Timothy", "Reynold", "stroke", 1931101414047)]),
                                  Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1960130120454),
                                                         Patient("Penny", "Tanya", "sinusitis", 2910627383279)]),
                                  Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                                                 Patient("Tiffany", "Sam", "arthritis",
                                                                         2560306012395)]),
                                  Department("Renal Unit", 40,
                                             [Patient("Kelly", "Gib", "kidney stones", 6000205248718)])
                                  ])
                         ))

    def test_is_cnp_valid(self):
        """
        Tests the function is_cnp_valid.
        """
        self.assertEqual(general_functions.is_cnp_valid(1900518437307), True)
        self.assertEqual(general_functions.is_cnp_valid(2900518437307), True)
        self.assertEqual(general_functions.is_cnp_valid(1900518837307), False)

    def test_has_at_most_p_patients_suffering_of_same_disease(self):
        patient_class.taken_cnps = []
        example_department = Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2890125259914),
                                                          Patient("Bertha", "Kim", "epilepsy", 2981231519852),
                                                          Patient("Wilt", "Norris", "headache", 1890903333287),
                                                          Patient("Mike", "Jackson", "brain tumor", 1880530329470),
                                                          Patient("Judith", "Park", "headache", 2900919387383)])
        self.assertEqual(example_department.has_at_most_p_patients_suffering_of_same_disease(3), True)
        self.assertEqual(example_department.has_at_most_p_patients_suffering_of_same_disease(2), False)
        self.assertEqual(example_department.has_at_most_p_patients_suffering_of_same_disease(-20), False)
