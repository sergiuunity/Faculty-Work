from ui import console
from application.department_repository_controller import DepartmentRepositoryController
from infrastructure.department_repository import DepartmentRepository
from domain.department_class import Department
from domain.patient_class import Patient

if __name__ == "__main__":
    example = my_repository = DepartmentRepository\
        ([Department("Cardiology", 50, [Patient("Johny", "Specter", "hearth attack", 1880627067576),
                                        Patient("Hannah", "Redd", "stroke", 2961122428076),
                                        Patient("Timothy", "Reynold", "stroke", 1880415016633)]),
         Department("Neurology", 30, [Patient("Amy", "Scott", "headache", 2980430158468),
                                      Patient("Bertha", "Kim", "epilepsy", 2861101404381),
                                      Patient("Wilt", "Norris", "headache", 1940519400842),
                                      Patient("Mike", "Jackson", "brain tumor", 1720813065255),
                                      Patient("Judith", "Park", "headache", 2970225513620)]),
         Department("ENT", 60, [Patient("Daniel", "Williams", "tinnitus", 1650905299181),
                                Patient("Penny", "Tanya", "sinusitis", 2910627383279),]),
          Department("Renal Unit", 40, [Patient("Kelly", "Gib", "kidney stones", 6000205248718)]),
          Department("Orthopedics", 60, [Patient("Johny", "Kemp", "scoliosis", 1860210393595),
                                         Patient("Tiffany", "Sam", "arthritis", 2560306012395)])])
    controller = DepartmentRepositoryController(example)
    console.start(controller)

# type
# python -m unittest test.tests
# in the terminal
