#include "OfferTest.h"
#include <iostream>
#include <cassert>
#include <string>
#include <sstream>
#include "Offer.h"

using namespace std;

void OfferTest::runAllTests()
{
	test_constructors();
	test_to_string();
	test_insertionOperator();
	test_getId();
	test_getPrice();
	test_getDeparture();
	test_getDestination();
	test_getStartDate();
	test_getEndDate();
	test_getType();
	test_setId();
	test_setPrice();
	test_setDeparture();
	test_setDestination();
	test_setStartDate();
	test_setEndDate();
	test_setType();
	test_equality();
	test_inequality();

}

void OfferTest::test_constructors()
{
	Offer o("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 7);
	assert(o.getType() == OfferType(0));
	Offer o2("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", -1);
	assert(o2.getType() == OfferType(0));

}

void OfferTest::test_to_string()
{
	Offer o;
	assert(o.to_string() == "Offer(ID:)");
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.to_string() == "Offer(ID:1)");

}

void OfferTest::test_insertionOperator()
{
	Offer o;
	ostringstream out, out2;
	out << o;
	string to_test = out.str();
	assert(to_test == "Offer(ID:)");
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	out2 << o;
	to_test = out2.str();
	assert(to_test == "Offer(ID:1)");

}

void OfferTest::test_getId()
{
	Offer o;
	assert(o.getId() == "");
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.getId() == "1");
}

void OfferTest::test_getPrice()
{
	Offer o;
	assert(o.getPrice() == 0);
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.getPrice() == 397);
}

void OfferTest::test_getDeparture()
{
	Offer o;
	assert(o.getDeparture() == "");
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.getDeparture() == "Cluj-Napoca");
}

void OfferTest::test_getDestination()
{
	Offer o;
	assert(o.getDestination() == "");
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.getDestination() == "Rome");
}

void OfferTest::test_getStartDate()
{
	Offer o;
	assert(o.getStartDate() == "");
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.getStartDate() == "10.07.2022");
}

void OfferTest::test_getEndDate()
{
	Offer o;
	assert(o.getEndDate() == "");
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.getEndDate() == "14.07.2022");
}

void OfferTest::test_getType()
{
	Offer o;
	assert(o.getType() == OfferType(0));
	o = Offer("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	assert(o.getType() == OfferType(2));
}

void OfferTest::test_setId()
{
	Offer o;
	assert(o.getId() == "");
	o.setId("1");
	assert(o.getId() == "1");
}

void OfferTest::test_setPrice()
{
	Offer o;
	assert(o.getPrice() == 0);
	o.setPrice(397);
	assert(o.getPrice() == 397);
}

void OfferTest::test_setDeparture()
{
	Offer o;
	assert(o.getDeparture() == "");
	o.setDeparture("Cluj-Napoca");
	assert(o.getDeparture() == "Cluj-Napoca");
}

void OfferTest::test_setDestination()
{
	Offer o;
	assert(o.getDestination() == "");
	o.setDestination("Rome");
	assert(o.getDestination() == "Rome");
}

void OfferTest::test_setStartDate()
{
	Offer o;
	assert(o.getStartDate() == "");
	o.setStartDate("10.07.2022");
	assert(o.getStartDate() == "10.07.2022");
}

void OfferTest::test_setEndDate()
{
	Offer o;
	assert(o.getEndDate() == "");
	o.setEndDate("14.07.2022");
	assert(o.getEndDate() == "14.07.2022");
}

void OfferTest::test_setType()
{
	Offer o;
	assert(o.getType() == OfferType(0));
	o.setType(2);
	assert(o.getType() == OfferType(2));
}

void OfferTest::test_equality()
{
	Offer o,p;
	assert(o == p);
	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("1", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);

	assert(o == p);
	assert(e1 == e2);
	assert(!(e1 == e3));
}

void OfferTest::test_inequality()
{
	Offer o, p;
	assert(o == p);
	Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	Offer e2("1", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	Offer e3("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);

	assert(!(o != p));
	assert(!(e1 != e2));
	assert(e1 != e3);

}
