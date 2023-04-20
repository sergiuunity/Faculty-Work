#include "ActionTest.h"

void ActionTest::runAllTests()
{
	test_allFunctionalities();
}

void ActionTest::test_allFunctionalities()
{
	Action a1;
	assert(a1.getType() == 0 && a1.getParameter() == Painting());
	Painting p1("1", "name", "author", 100, 50, 50);
	a1.setType(1);
	a1.setParameter(p1);
	assert(a1.getType() == 1 && a1.getParameter() == p1);
	Action a2(-1, p1);
	assert(a2.getType() == -1 && a2.getParameter() == p1);
}
