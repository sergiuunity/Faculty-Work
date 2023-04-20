#include "ExhibitTest.h"
#include <sstream>

void ExhibitTest::runAllTests()
{
	test_constructors();
	test_gettersAndSetters();
	test_equalityOperators();
}

void ExhibitTest::test_constructors()
{
	Exhibit e;
	assert(e.getId() == "" && e.getName() == "Unnamed" && e.getAuthor() == "Unknown" && e.getEstimated_price() == 0);
	Exhibit e1("1", "name", "author", 100);
	assert(e1.getId() == "1" && e1.getName() == "name" && e1.getAuthor() == "author" && e1.getEstimated_price() == 100);
}

void ExhibitTest::test_gettersAndSetters()
{
	Exhibit e;
	e.setId("1");
	e.setName("name");
	e.setAuthor("author");
	e.setEstimated_price(100);
	assert(e.getId() == "1" && e.getName() == "name" && e.getAuthor() == "author" && e.getEstimated_price() == 100);
}

void ExhibitTest::test_equalityOperators()
{
	Exhibit e1("1", "name", "author", 100);
	Exhibit e2("1", "name", "author", 200);
	Exhibit e3("1", "name", "author", 100);
	assert(e1 == e1);
	assert(e1 == e3);
	assert(!(e1 == e2));
	assert(!(e1 != e1));
	assert(!(e1 != e3));
	assert(e1 != e2);
}

void PaintingTest::runAllTests()
{
	test_constructors();
	test_gettersAndSetters();
	test_equalityOperators();
}

void PaintingTest::test_constructors()
{
	Painting p;
	assert(p.getId() == "" && p.getName() == "Unnamed" && p.getAuthor() == "Unknown" && p.getEstimated_price() == 0 && p.getWidth() == 0 && p.getHeight() == 0);
	Painting p1("1", "name", "author", 100, 50, 60);
	assert(p1.getId() == "1" && p1.getName() == "name" && p1.getAuthor() == "author" && p1.getEstimated_price() == 100 && p1.getWidth() == 50 && p1.getHeight() == 60);
}

void PaintingTest::test_gettersAndSetters()
{
	Painting p;
	p.setId("1");
	p.setName("name");
	p.setAuthor("author");
	p.setEstimated_price(100);
	p.setWidth(50);
	p.setHeight(60);
	assert(p.getId() == "1" && p.getName() == "name" && p.getAuthor() == "author" && p.getEstimated_price() == 100 && p.getWidth() == 50 && p.getHeight() == 60);
}

void PaintingTest::test_equalityOperators()
{
	Painting p1("1", "name", "author", 100, 50, 60);
	Painting p2("1", "name", "author", 200, 99, 99);
	Painting p3("1", "name", "author", 100, 50, 60);
	assert(p1 == p1);
	assert(p1 == p3);
	assert(!(p1 == p2));
	assert(!(p1 != p1));
	assert(!(p1 != p3));
	assert(p1 != p2);
}