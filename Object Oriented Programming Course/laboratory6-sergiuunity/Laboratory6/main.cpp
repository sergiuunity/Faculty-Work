#include "OfferTest.h"
#include "FilteringTest.h"
#include "DynamicArrayTest.h"
#include "FilteringCriteria.h"

#include <iostream>
#include <string>
using namespace std;

#include "DynamicArray.h"

void displayMenu() {
	cout << "M|m     Display the menu" << endl;
	cout << "I|i     Show available types" << endl;
	cout << "A|a     Add an offer" << endl;
	cout << "S|s     Show all offers" << endl;
	cout << "P|p     Filters offers by price" << endl;
	cout << "T|t     Filters offers by type" << endl;
	cout << "B|b     Filter offer by type and price" << endl;
	cout << "Q|q     Quit" << endl << endl;
}


int main() {

	OfferTest::runAllTests();
	FilteringTest::runAllTests();
	DynamicArrayTest::runAllTests();

	DynamicArray allOffers;


	////EXAMPLES
	//Offer e1("1", 397, "Cluj-Napoca", "Rome", "10.07.2022", "14.07.2022", 2);
	//Offer e2("2", 997, "Bucharest", "New York", "05.09.2022", "10.09.2022", 2);
	//Offer e3("3", 1297, "Bucharest", "Maldives", "13.06.2022", "20.06.2022", 4);
	//Offer e4("4", 1097, "Bucharest", "Seychelles", "14.07.2022", "21.07.2022", 4);
	//Offer e5("5", 1150, "Budapest", "Port of Spain", "20.07.2022", "27.07.2022", 3);
	//Offer e6("6", 850, "Cluj-Napoca", "Alexandria-Cairo-Luxor", "10.06.2022", "15.06.2022", 1);
	//
	//allOffers.append(e1);
	//allOffers.append(e2);
	//allOffers.append(e3);
	//allOffers.append(e4);
	//allOffers.append(e5);
	//allOffers.append(e6);

	string command;
	displayMenu();
	cout << "Give command...";
	cin >> command;
	while (command != "Q" && command != "q")
	{
		if (command == "M" || command == "m")
		{
			displayMenu();
		}
		else if (command == "I" || command == "i")
		{
			cout << "0 = NO_TYPE" << endl;
			cout << "1 = CIRCUIT" << endl;
			cout << "2 = CITY_BREAK" << endl;
			cout << "3 = CRUISE" << endl;
			cout << "4 = ALL_INCLUSIVE" << endl << endl;
		}
		else if (command == "A" || command == "a")
		{
			try
			{
				string given_id, given_departure, given_destination, given_start_date, given_end_date;
				float given_price;
				int given_type;
				cout << "ID: ";
				cin >> given_id;
				cout << "Departure: ";
				cin >> given_departure;
				cout << "Destination: ";
				cin >> given_destination;
				cout << "Start Date: ";
				cin >> given_start_date;
				cout << "End Date: ";
				cin >> given_end_date;
				cout << "Price($): ";
				cin >> given_price;
				cout << "Type: ";
				cin >> given_type;
				Offer temp_offer(given_id, given_price, given_departure, given_destination, given_start_date, given_end_date, given_type);
				allOffers.append(temp_offer);
			}
			catch (int x)
			{
				cout << "Element with such ID already exists in the array." << endl;
			}
		}
		else if (command == "S" || command == "s")
		{
			cout << allOffers << endl;
		}
		else if (command == "P" || command == "p")
		{
			float given_price;
			cout << "Prices under($): ";
			cin >> given_price;
			FilteringPrice my_filter(given_price);
			cout << my_filter.filter(allOffers) << endl;
		}
		else if (command == "T" || command == "t")
		{
			int given_type;
			cout << "Searched type: ";
			cin >> given_type;
			FilteringType my_filter(given_type);
			cout << my_filter.filter(allOffers) << endl;

		}
		else if (command == "B" || command == "b")
		{
			float given_price;
			int given_type;
			cout << "Searched type: ";
			cin >> given_type;
			cout << "Prices under($): ";
			cin >> given_price;
			FilteringCriteriaTypeAndPrice my_filter(given_type, given_price);
			cout << my_filter.filter(allOffers) << endl;
		}
		else
		{
			cout << "Unknown command. Try a new one." << endl;
		}
		cout << "Give command...";
		cin >> command;
	}
	cout << "The application will now close." << endl;

	return 0;
}