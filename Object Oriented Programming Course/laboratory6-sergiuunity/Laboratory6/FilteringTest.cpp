#include "FilteringTest.h"
#include <cassert>

void FilteringTest::runAllTests()
{
	test_getPrice();
	test_getType();
	test_setPrice();
	test_setType();
	test_filter();
	test_filterPrice();
	test_filterType();
	test_filterTypeAndPrice();
}

void FilteringTest::test_getPrice()
{
	FilteringPrice my_filter(3);
	assert(my_filter.getPrice() == 3);
	FilteringPrice my_filter2;
	assert(my_filter2.getPrice() == 0);
	FilteringCriteriaTypeAndPrice my_filter3(0, 3);
	assert(my_filter3.getPrice() == 3);
	FilteringCriteriaTypeAndPrice my_filter4;
	assert(my_filter4.getPrice() == 0);

}

void FilteringTest::test_getType()
{
	FilteringType my_filter(3);
	assert(my_filter.getType() == OfferType(3));
	FilteringType my_filter2;
	assert(my_filter2.getType() == OfferType(0));
	FilteringCriteriaTypeAndPrice my_filter3(2, 3);
	assert(my_filter3.getType() == OfferType(2));
	FilteringCriteriaTypeAndPrice my_filter4;
	assert(my_filter4.getType() == OfferType(0));

}

void FilteringTest::test_setPrice()
{
	FilteringPrice my_filter;
	my_filter.setPrice(77);
	assert(my_filter.getPrice() == 77);
	FilteringCriteriaTypeAndPrice my_filter2;
	my_filter2.setPrice(99);
	assert(my_filter2.getPrice() == 99);
}

void FilteringTest::test_setType()
{
	FilteringType my_filter;
	my_filter.setType(1);
	assert(my_filter.getType() == OfferType(1));
	FilteringCriteriaTypeAndPrice my_filter2;
	my_filter2.setType(3);
	assert(my_filter2.getType() == OfferType(3));

}

void FilteringTest::test_filter()
{
	DynamicArray DA;
	FilteringCriteria my_filter;
	assert(my_filter.filter(DA) == DA);
	DA.append(Offer("6", 850, "Cluj - Napoca", "Alexandria - Cairo - Luxor", "10.06.2022", "15.06.2022", 1));
	assert(my_filter.filter(DA) == DA);
}

void FilteringTest::test_filterPrice()
{	
	DynamicArray allOffers;
	DynamicArray o;
	FilteringPrice my_filter(100);
	FilteringPrice my_filter2(1000);
	assert(my_filter.filter(o) == DynamicArray());

	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 4);
	Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);

	allOffers.append(e1);
	allOffers.append(e2);
	allOffers.append(e3);
	allOffers.append(e4);
	allOffers.append(e5);
	allOffers.append(e6);

	DynamicArray wantedResult;
	wantedResult.append(e1);
	wantedResult.append(e2);
	wantedResult.append(e6);
	assert(my_filter2.filter(allOffers) == wantedResult);

}

void FilteringTest::test_filterType()
{
	DynamicArray allOffers;
	DynamicArray o;
	FilteringType my_filter(4);
	FilteringType my_filter2(2);
	FilteringType my_filter3;
	assert(my_filter.filter(o) == DynamicArray());

	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 4);
	Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);

	allOffers.append(e1);
	allOffers.append(e2);
	allOffers.append(e3);
	allOffers.append(e4);
	allOffers.append(e5);
	allOffers.append(e6);

	DynamicArray wantedResult;
	wantedResult.append(e1);
	wantedResult.append(e2);

	assert(my_filter2.filter(allOffers) == wantedResult);
	assert(my_filter3.filter(allOffers) == DynamicArray());
}

void FilteringTest::test_filterTypeAndPrice()
{
	DynamicArray allOffers;
	DynamicArray o;
	FilteringCriteriaTypeAndPrice my_filter;
	FilteringCriteriaTypeAndPrice my_filter2(2, 500);
	FilteringCriteriaTypeAndPrice my_filter3(100, 4);
	FilteringCriteriaTypeAndPrice my_filter4(2000, 0);
	FilteringCriteriaTypeAndPrice my_filter5(2, 397);
	assert(my_filter.filter(o) == DynamicArray());

	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 4);
	Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);

	allOffers.append(e1);
	allOffers.append(e2);
	allOffers.append(e3);
	allOffers.append(e4);
	allOffers.append(e5);
	allOffers.append(e6);

	DynamicArray wantedResult;
	wantedResult.append(e1);

	assert(my_filter2.filter(allOffers) == wantedResult);
	assert(my_filter3.filter(allOffers) == DynamicArray());
	assert(my_filter4.filter(allOffers) == DynamicArray());
	assert(my_filter5.filter(allOffers) == DynamicArray());
}
