#pragma once
#include "DynamicArray.h"
#include <iostream>

using std::string;

// you can add all your filtering classes in this module
class FilteringCriteria
{

public:
	virtual DynamicArray<Offer> filter(DynamicArray<Offer>& data) = 0;
};

class FilteringCriteriaAnd :public FilteringCriteria
{
public:
	//constructor
	FilteringCriteriaAnd(FilteringCriteria* input_filter1, FilteringCriteria* input_filter2);

	//filter
	DynamicArray<Offer> filter(DynamicArray<Offer>& data);
	
protected:
	FilteringCriteria* f1;
	FilteringCriteria* f2; 

};

class FilteringCriteriaOr :public FilteringCriteria
{
public:
	//constructor
	FilteringCriteriaOr(FilteringCriteria* input_filter1, FilteringCriteria* input_filter2);

	//filter
	DynamicArray<Offer> filter(DynamicArray<Offer>& data);

protected:
	FilteringCriteria* f1;
	FilteringCriteria* f2;

};






class FilteringCriteriaPrice : public FilteringCriteria
{
public:
	//getters and setters
	float getPrice()const;
	void setPrice(float price);

	//constructors
	FilteringCriteriaPrice();

	FilteringCriteriaPrice(float price);

	//filter
	DynamicArray<Offer> filter(DynamicArray<Offer>& data);



private:
	float price;
};

class FilteringCriteriaType : public FilteringCriteria
{
public:
	//getters and setters
	OfferType getType()const;
	void setType(int type);

	//constructors
	FilteringCriteriaType();

	FilteringCriteriaType(int type);

	//filter
	DynamicArray<Offer> filter(DynamicArray<Offer>& data);



private:
	OfferType type;
};

class FilteringCriteriaDeparture : public FilteringCriteria
{
public:

	//getters and setters
	string getDeparture()const;
	void setDeparture(string departure);

	//constructors
	FilteringCriteriaDeparture();

	FilteringCriteriaDeparture(string departure);

	//filter
	DynamicArray<Offer> filter(DynamicArray<Offer>& data);



private:
	string departure;


};

class FilteringCriteriaDestination : public FilteringCriteria
{
public:

	//getters and setters
	string getDestination()const;
	void setDestination(string Destination);

	//constructors
	FilteringCriteriaDestination();

	FilteringCriteriaDestination(string Destination);

	//filter
	DynamicArray<Offer> filter(DynamicArray<Offer>& data);



private:
	string destination;


};
