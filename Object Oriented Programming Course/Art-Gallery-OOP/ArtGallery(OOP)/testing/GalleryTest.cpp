#include "GalleryTest.h"

void GalleryTest::runAllTests()
{
	test_constructors();
	test_gettersAndSetters();
	test_arrayOperations();
	test_fileOperations();
	test_equalityOperators();
}

void GalleryTest::test_constructors()
{
	Gallery g;
	assert(g.getName() == "Art Gallery" && g.size() == 0);
	Gallery g1("Example");
	assert(g1.getName() == "Example" && g1.size() == 0);
}

void GalleryTest::test_gettersAndSetters()
{
	Gallery g;
	g.setName("Example");
	assert(g.getName() == "Example");
}

void GalleryTest::test_arrayOperations()
{
	Gallery g;
	Painting p1("1", "name", "author", 100, 50, 60);
	Painting p2("2", "name2", "author2", 101, 51, 61);
	Painting p3("3", "name3", "author3", 102, 52, 62);
	//append
	g.append(p1);
	assert(g.get(0) == p1 && g.size() == 1);
	try
	{
		g.append(p1);
		assert(false);
	}
	catch (int x)
	{
		if (x == -2)
			assert(true);
	}
	//popBack
	assert(g.popBack() == p1);
	assert(g.size() == 0);
	try
	{
		g.popBack();
		assert(false);
	}
	catch (int x)
	{
		if (x == -5)
			assert(true);
	}
	//remove at index
	g.append(p1);
	g.append(p2);
	try
	{
		g.remove_at_index(-1);
		assert(false);
	}
	catch (int x)
	{
		if (x == -1)
			assert(true);
	}
	try
	{
		g.remove_at_index(2);
		assert(false);
	}
	catch (int x)
	{
		if (x == -1)
			assert(true);
	}
	assert(g.remove_at_index(1) == p2);
	assert(g.size() == 1);
	//remove by value
	g.append(p2);
	assert(g.remove(p3) == false);
	assert(g.size() == 2);
	assert(g.remove(p2) == true);
	assert(g.size() == 1);
	//get at index
	g.append(p2);
	try
	{
		g.get(-1);
		assert(false);
	}
	catch (int x)
	{
		if (x == -1)
			assert(true);
	}
	try
	{
		g.get(2);
		assert(false);
	}
	catch (int x)
	{
		if (x == -1)
			assert(true);
	}
	assert(g.get(0) == p1 && g.get(1) == p2);
	//search
	assert(g.search(p1) == true && g.search(p3) == false);
	//edit at index
	try
	{
		g.edit_at_index(p1, 1);
		assert(false);
	}
	catch (int x)
	{
		if (x == -2)
			assert(true);
	}
	try
	{
		g.edit_at_index(p3, -1);
		assert(false);
	}
	catch (int x)
	{
		if (x == -1)
			assert(true);
	}
	try
	{
		g.edit_at_index(p3, 2);
		assert(false);
	}
	catch (int x)
	{
		if (x == -1)
			assert(true);
	}
	g.edit_at_index(p3, 1);
	assert(g.get(1) == p3);
}

void GalleryTest::test_fileOperations()
{
	string path = "generated_files/generated_testing_fileOperations.csv";
	Gallery g1, g2;
	Painting p1("1", "name", "author", 100, 50, 60);
	Painting p2("2", "name2", "author2", 101, 51, 61);
	Painting p3("3", "name3", "author3", 102, 52, 62);
	g1.append(p1);
	g1.append(p2);
	g1.append(p3);
	g1.save_into_file(path);
	g2.load_from_file(path);
	assert(g1 == g2);
}

void GalleryTest::test_equalityOperators()
{
	Gallery g1, g2;
	Gallery g3("name");
	Painting p1("1", "name", "author", 100, 50, 60);
	Painting p2("2", "name2", "author2", 101, 51, 61);
	Painting p3("3", "name3", "author3", 102, 52, 62);
	assert(g1 == g2);
	assert(!(g1 != g2));
	assert(!(g1 == g3));
	assert(g1 != g3);
	g1.append(p1);
	g2.append(p1);
	assert(g1 == g2);
	assert(!(g1 != g2));
	g1.append(p2);
	g2.append(p3);
	assert(g1 != g2);
	assert(!(g1 == g2));
	g2.append(p2);
	assert(g1 != g2);
	assert(!(g1 == g2));
}
