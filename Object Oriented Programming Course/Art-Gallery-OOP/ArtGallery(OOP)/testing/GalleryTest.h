#pragma once
#include "../repository/Gallery.h"
#include <cassert>

class GalleryTest
{
public:
	static void runAllTests();
	static void test_constructors();
	static void test_gettersAndSetters();
	static void test_arrayOperations();
	static void test_fileOperations();
	static void test_equalityOperators();
};