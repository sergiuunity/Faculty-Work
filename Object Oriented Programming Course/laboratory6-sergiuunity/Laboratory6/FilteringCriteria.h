#pragma once
#include "DynamicArray.h"
#include <iostream>


// you can add all your filtering classes in this module
class FilteringCriteria
{
public:
	//filter
	DynamicArray filter(DynamicArray& data);

private:
};


class FilteringPrice : public FilteringCriteria
{
public:
	//getters and setters
	float getPrice()const;
	void setPrice(float price);

	//constructors
	FilteringPrice();

	FilteringPrice(float price);

	//filter
	DynamicArray filter(DynamicArray& data);



private:
	float price;
};

class FilteringType : public FilteringCriteria
{
public:
	//getters and setters
	OfferType getType()const;
	void setType(int type);

	//constructors
	FilteringType();

	FilteringType(int type);

	//filter
	DynamicArray filter(DynamicArray& data);



private:
	OfferType type;
};


class FilteringCriteriaTypeAndPrice : public FilteringCriteria
{
public:
	//getters and setters
	OfferType getType()const;
	float getPrice()const;

	void setType(int type);
	void setPrice(float price);

	//constructors
	FilteringCriteriaTypeAndPrice();

	FilteringCriteriaTypeAndPrice(int type, float price);

	//filter
	DynamicArray filter(DynamicArray& data);


private:
	OfferType type;
	float price;
};