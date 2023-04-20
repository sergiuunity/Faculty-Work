#pragma once
#include "../domain/Exhibit.h"
#include <cassert>

class ExhibitTest
{
public:
	static void runAllTests();
	static void test_constructors();
	static void test_gettersAndSetters();
	static void test_equalityOperators();
};

class PaintingTest
{
public:
	static void runAllTests();
	static void test_constructors();
	static void test_gettersAndSetters();
	static void test_equalityOperators();
};