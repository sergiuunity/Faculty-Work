#include <iostream>
#include <sstream>
#include <string>
#include "Offer.h"
using namespace std;

Offer::Offer()
{
	this->id = "";
	this->price = 0;
	this->departure = "";
	this->destination = "";
	this->start_date = "";
	this->end_date = "";
	this->type = (OfferType)(0);
}

Offer::Offer(std::string id, float price, std::string departure, std::string destination, std::string start_date, std::string end_date, int type)
{
	this->id = id;
	this->price = price;
	this->departure = departure;
	this->destination = destination;
	this->start_date = start_date;
	this->end_date = end_date;
	if (type >= 0 && type < 5)
		this->type = (OfferType)(type);
	else
		this->type = (OfferType)(0);
}

std::string Offer::to_string()const
{
	ostringstream out;
	string type_str;
	
	
	/*if (this->type == 0)type_str = "NO_TYPE";
	else if (this->type == 1)type_str = "CIRCUIT";
	else if (this->type == 2)type_str = "CITY_BREAK";
	else if (this->type == 3)type_str = "CRUISE";
	else if (this->type == 4)type_str = "ALL_INCLUSIVE";
	out << "Offer[ID: " << this->id << "] of type: " << type_str << "; Destination: " << this->destination << " ; Departure: " << this->departure << "; " << this->start_date << " - " << this->end_date << " ; Price: " << this->price << " $.";
	*/
	
	out << "Offer(ID:" << this->id << ")";

	string result = out.str();
	return result;
}

string Offer::getId() const
{
	return this->id;
}

float Offer::getPrice() const
{
	return this->price;
}

string Offer::getDeparture() const
{
	return this->departure;
}

string Offer::getDestination() const
{
	return this->destination;
}

string Offer::getStartDate() const
{
	return this->start_date;
}

string Offer::getEndDate() const
{
	return this->end_date;
}

OfferType Offer::getType() const
{
	return this->type;
}

void Offer::setId(string id)
{
	this->id = id;
}

void Offer::setPrice(float price)
{
	this->price = price;
}

void Offer::setDeparture(string departure)
{
	this->departure = departure;
}

void Offer::setDestination(string destination)
{
	this->destination = destination;
}

void Offer::setStartDate(string start_date)
{
	this->start_date = start_date;
}

void Offer::setEndDate(string end_date)
{
	this->end_date = end_date;
}

void Offer::setType(int type)
{
	this->type = (OfferType)(type);
}

bool Offer::operator==(const Offer& other) const
{
	if (this->id == other.id) return true;
	return false;
}

bool Offer::operator!=(const Offer& other) const
{
	if (this->id != other.id) return true;
	return false;
}

std::ostream& operator<<(std::ostream& out, const Offer& o)
{
	out << o.to_string();
	return out;
}