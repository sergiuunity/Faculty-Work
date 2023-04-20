#pragma once
#include "Offer.h"

class OfferTest
{
public:
	void static test_constructors();
	void static test_to_string();
	void static test_insertionOperator();
	void static test_getId();
	void static test_getPrice();
	void static test_getDeparture();
	void static test_getDestination();
	void static test_getStartDate();
	void static test_getEndDate();
	void static test_getType();
	void static test_setId();
	void static test_setPrice();
	void static test_setDeparture();
	void static test_setDestination();
	void static test_setStartDate();
	void static test_setEndDate();
	void static test_setType();
	void static test_equality();
	void static test_inequality();

	static void runAllTests();
};

