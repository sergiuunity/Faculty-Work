from ui.console import Console
import tests
import data_examples


tests.run_all()
print("\n")
data_examples.run_all()
print("\n")

c = Console()
c.start()
