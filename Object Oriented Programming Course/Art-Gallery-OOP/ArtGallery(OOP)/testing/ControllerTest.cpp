#include "ControllerTest.h"

void ControllerTest::runAllTests()
{
	test_gettersAndSetters();
	test_fileOperations();
	test_undo_redo();
	test_equalityOperators();
}

void ControllerTest::test_gettersAndSetters()
{
	GalleryController gc;
	assert(gc.getName() == "Art Gallery");
	gc.setName("Example");
	assert(gc.getName() == "Example");
}

void ControllerTest::test_fileOperations()
{
	string path = "generated_files/generated_testing_fileOperations.csv";
	Gallery g1, g2;
	GalleryController gc1(g1);
	GalleryController gc2(g2);
	gc1.append("1", "name", "author", 100, 50, 60);
	gc1.append("2", "name2", "author2", 101, 51, 61);
	gc1.append("3", "name3", "author3", 102, 52, 62);
	gc1.save_into_file(path);
	gc2.load_from_file(path);
	assert(gc1 == gc2);

}


void ControllerTest::test_undo_redo()
{
	GalleryController gc;
	Painting p1("1", "name", "author", 100, 50, 60);
	Painting p2("2", "name2", "author2", 101, 51, 61);
	Painting p3("3", "name3", "author3", 102, 52, 62);
	try 
	{
		gc.undo();
		assert(false);
	}
	catch (int x)
	{
		if (x == -3)
			assert(true);
	}
	gc.append("1", "name", "author", 100, 50, 60);
	gc.append("2", "name2", "author2", 101, 51, 61);
	gc.append("3", "name3", "author3", 102, 52, 62);
	gc.undo();
	assert(gc.size() == 2);
	gc.redo();
	assert(gc.size() == 3);
	try
	{
		gc.redo();
		assert(false);
	}
	catch (int x)
	{
		if (x == -3)
			assert(true);
	}
	gc.remove_at_index(2);
	gc.undo();
	assert(gc.size() == 3);
	gc.redo();
	assert(gc.size() == 2);
}

void ControllerTest::test_equalityOperators()
{
	Gallery g1, g2;
	Gallery g3("name");
	GalleryController gc1(g1);
	GalleryController gc2(g2);
	GalleryController gc3(g3);
	assert(gc1 == gc2);
	assert(!(gc1 != gc2));
	assert(!(gc1 == gc3));
	assert(gc1 != gc3);
	gc1.append("1", "name", "author", 100, 50, 60);
	gc2.append("1", "name", "author", 100, 50, 60);
	assert(gc1 == gc2);
	assert(!(gc1 != gc2));
	gc1.append("2", "name2", "author2", 101, 51, 61);
	gc2.append("3", "name3", "author3", 102, 52, 62);
	assert(gc1 != gc2);
	assert(!(gc1 == gc2));
	gc2.append("2", "name2", "author2", 101, 51, 61);
	assert(gc1 != gc2);
	assert(!(gc1 == gc2));
}

