#include <iostream>
#include <string>
#pragma once

using std::string;


typedef enum {
	NO_TYPE = 0,
	CIRCUIT = 1,
	CITY_BREAK = 2,
	CRUISE = 3,
	ALL_INCLUSIVE = 4
}OfferType;


class Offer
{
public:
	//constructor
	Offer();
	Offer(std::string, float, std::string, std::string, std::string, std::string, int);
	

	//displaying
	std::string to_string()const;

	friend std::ostream& operator<<(std::ostream& out, const Offer& o);

	//getters and setters
	string getId()const;
	float getPrice()const;
	string getDeparture()const;
	string getDestination()const;
	string getStartDate()const;
	string getEndDate()const;
	OfferType getType()const;

	void setId(string);
	void setPrice(float);
	void setDeparture(string);
	void setDestination(string);
	void setStartDate(string);
	void setEndDate(string);
	void setType(int);

	//operators
	bool operator==(const Offer& other)const;

	bool operator!=(const Offer& other)const;



private:
	std::string id;
	float price;
	std::string departure, destination;
	std::string start_date, end_date;
	OfferType type;
};