#pragma once
#include "../controller/Repo_Controller.h"
#include <cassert>

class ControllerTest
{
public:
	static void runAllTests();
	static void test_gettersAndSetters();
	static void test_fileOperations();
	static void test_undo_redo();
	static void test_equalityOperators();
};