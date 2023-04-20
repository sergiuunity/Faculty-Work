#include "FilteringTest.h"
#include <cassert>

void FilteringTest::runAllTests()
{
	test_getPrice();
	test_getType();
	test_setPrice();
	test_setType();
	test_filterPrice();
	test_filterType();
	test_filterDeparture();
	test_filterDestination();
	test_filteringCriteriaAnd();
	test_filteringCriteriaOr();
}

void FilteringTest::test_getPrice()
{
	FilteringCriteriaPrice my_filter(3);
	assert(my_filter.getPrice() == 3);
	FilteringCriteriaPrice my_filter2;
	assert(my_filter2.getPrice() == 0);

}

void FilteringTest::test_getType()
{
	FilteringCriteriaType my_filter(3);
	assert(my_filter.getType() == OfferType(3));
	FilteringCriteriaType my_filter2;
	assert(my_filter2.getType() == OfferType(0));
}

void FilteringTest::test_setPrice()
{
	FilteringCriteriaPrice my_filter;
	my_filter.setPrice(77);
	assert(my_filter.getPrice() == 77);
}

void FilteringTest::test_setType()
{
	FilteringCriteriaType my_filter;
	my_filter.setType(1);
	assert(my_filter.getType() == OfferType(1));

}


void FilteringTest::test_filterPrice()
{	
	DynamicArray<Offer> allOffers;
	DynamicArray<Offer> o;
	FilteringCriteriaPrice my_filter(100);
	FilteringCriteriaPrice my_filter2(1000);
	assert(my_filter.filter(o) == DynamicArray<Offer>());

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

	DynamicArray<Offer> wantedResult;
	wantedResult.append(e1);
	wantedResult.append(e2);
	wantedResult.append(e6);
	assert(my_filter2.filter(allOffers) == wantedResult);

}

void FilteringTest::test_filterType()
{
	DynamicArray<Offer> allOffers;
	DynamicArray<Offer> o;
	FilteringCriteriaType my_filter(4);
	FilteringCriteriaType my_filter2(2);
	FilteringCriteriaType my_filter3;
	assert(my_filter.filter(o) == DynamicArray<Offer>());

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

	DynamicArray<Offer> wantedResult;
	wantedResult.append(e1);
	wantedResult.append(e2);

	assert(my_filter2.filter(allOffers) == wantedResult);
	assert(my_filter3.filter(allOffers) == DynamicArray<Offer>());
}

void FilteringTest::test_filterDeparture()
{
	FilteringCriteriaDeparture my_filter;
	assert(my_filter.getDeparture() == "");
	my_filter = FilteringCriteriaDeparture("Bucharest");
	assert(my_filter.getDeparture() == "Bucharest");
	my_filter.setDeparture("Here");
	assert(my_filter.getDeparture() == "Here");

	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 4);
	Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);
	
	DynamicArray<Offer> allOffers;
	DynamicArray<Offer> WANTED;
	allOffers.append(e1);
	allOffers.append(e2);
	allOffers.append(e3);
	allOffers.append(e4);
	allOffers.append(e5);
	allOffers.append(e6);
	WANTED.append(e1);
	WANTED.append(e6);
	my_filter = FilteringCriteriaDeparture("Cluj-Napoca");
	assert(my_filter.filter(allOffers) == WANTED);

}

void FilteringTest::test_filterDestination()
{
	FilteringCriteriaDestination my_filter;
	assert(my_filter.getDestination() == "");
	my_filter = FilteringCriteriaDestination("Bucharest");
	assert(my_filter.getDestination() == "Bucharest");
	my_filter.setDestination("Here");
	assert(my_filter.getDestination() == "Here");

	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("3", 1297, "Bucharest", "Rome", "13.06.2022", "20.06.2022", 2);
	Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);

	DynamicArray<Offer> allOffers;
	DynamicArray<Offer> WANTED;
	allOffers.append(e1);
	allOffers.append(e2);
	allOffers.append(e3);
	allOffers.append(e4);
	allOffers.append(e5);
	allOffers.append(e6);
	WANTED.append(e1);
	WANTED.append(e3);
	my_filter = FilteringCriteriaDestination("Rome");
	assert(my_filter.filter(allOffers) == WANTED);

}

void FilteringTest::test_filteringCriteriaAnd()
{
	DynamicArray<Offer> allOffers;

	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 4);
	Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);
	Offer e7("7", 997, "Here", "New York", "05.09.2022", "10.09.2022", 2);

	allOffers.append(e1);
	allOffers.append(e2);
	allOffers.append(e3);
	allOffers.append(e4);
	allOffers.append(e5);
	allOffers.append(e6);
	allOffers.append(e7);

	FilteringCriteriaDeparture filter1("Bucharest");
	FilteringCriteriaPrice filter2(1100);
	FilteringCriteriaAnd end_filter(&filter1, &filter2);

	DynamicArray<Offer> testOffers;
	testOffers.append(e1);
	testOffers.append(e2);
	testOffers.append(e3);
	testOffers.append(e4);
	testOffers.append(e5);
	testOffers.append(e6);
	testOffers.append(e7);

	FilteringCriteriaDeparture filter5("Cluj-Napoca");
	FilteringCriteriaPrice filter6(800);
	FilteringCriteriaAnd test_filter(&filter5, &filter6);
	
	assert(end_filter.filter(allOffers) == end_filter.filter(allOffers));
	assert(test_filter.filter(testOffers) == test_filter.filter(testOffers));
	assert(end_filter.filter(allOffers) != test_filter.filter(testOffers));

	FilteringCriteriaDeparture filter7("Oradea");
	FilteringCriteriaAnd test_filter2(&filter5, &filter7);
	assert(end_filter.filter(allOffers) != test_filter2.filter(testOffers));

	FilteringCriteriaDeparture filter8("Bucharest");
	FilteringCriteriaAnd test_filter3(&filter5, &filter8);
	assert(end_filter.filter(allOffers) != test_filter3.filter(testOffers));

	FilteringCriteriaDeparture filter9("Budapest");
	FilteringCriteriaAnd test_filter4(&filter2, &filter9);
	assert(end_filter.filter(allOffers) != test_filter4.filter(testOffers));

	FilteringCriteriaPrice filter10(500);
	FilteringCriteriaAnd test_filter5(&filter10, &filter8);
	assert(end_filter.filter(allOffers) != test_filter5.filter(testOffers));
}


void FilteringTest::test_filteringCriteriaOr()
{
	DynamicArray<Offer> allOffers;

	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 4);
	Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);
	Offer e7("7", 997, "Here", "New York", "05.09.2022", "10.09.2022", 2);

	allOffers.append(e1);
	allOffers.append(e2);
	allOffers.append(e3);
	allOffers.append(e4);
	allOffers.append(e5);
	allOffers.append(e6);
	allOffers.append(e7);

	FilteringCriteriaDeparture filter1("Bucharest");
	FilteringCriteriaPrice filter2(1100);
	FilteringCriteriaOr end_filter(&filter1, &filter2);

	DynamicArray<Offer> testOffers;
	testOffers.append(e1);
	testOffers.append(e2);
	testOffers.append(e3);
	testOffers.append(e4);
	testOffers.append(e5);
	testOffers.append(e6);
	testOffers.append(e7);

	FilteringCriteriaDeparture filter5("Cluj-Napoca");
	FilteringCriteriaPrice filter6(800);
	FilteringCriteriaOr test_filter(&filter5, &filter6);

	assert(end_filter.filter(allOffers) == end_filter.filter(allOffers));
	assert(test_filter.filter(testOffers) == test_filter.filter(testOffers));
	assert(end_filter.filter(allOffers) != test_filter.filter(testOffers));

	FilteringCriteriaDeparture filter7("Oradea");
	FilteringCriteriaOr test_filter2(&filter5, &filter7);
	assert(end_filter.filter(allOffers) != test_filter2.filter(testOffers));

	FilteringCriteriaDeparture filter8("Bucharest");
	FilteringCriteriaOr test_filter3(&filter5, &filter8);
	assert(end_filter.filter(allOffers) != test_filter3.filter(testOffers));

	FilteringCriteriaDeparture filter9("Budapest");
	FilteringCriteriaOr test_filter4(&filter2, &filter9);
	assert(end_filter.filter(allOffers) != test_filter4.filter(testOffers));

	FilteringCriteriaPrice filter10(500);
	FilteringCriteriaOr test_filter5(&filter10, &filter8);
	assert(end_filter.filter(allOffers) != test_filter5.filter(testOffers));
}