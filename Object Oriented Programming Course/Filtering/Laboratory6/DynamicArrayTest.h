#pragma once
#include "DynamicArray.h"
#include <cassert>
#include <string>

class DynamicArrayTest
{
public:
	static void runAllTests();
	static void test_getLenght();
	static void test_getCapacity();
	static void test_append();
	static void test_popBack();
	static void test_remove();
	static void test_get();
	static void test_insertionOperator();
	static void test_isElemIn();
	static void test_resize();
	static void test_constructors();
	static void test_copyConstructor();
	static void test_equality();
	static void test_inequality();
	static void test_set_operations();

};

