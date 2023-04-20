#pragma once
#include "filteringCriteria.h"

class FilteringTest
{
public:
	static void runAllTests();
	static void test_getPrice();
	static void test_getType();
	static void test_setPrice();
	static void test_setType();
	static void test_filter();
	static void test_filterPrice();
	static void test_filterType();
	static void test_filterTypeAndPrice();

};

