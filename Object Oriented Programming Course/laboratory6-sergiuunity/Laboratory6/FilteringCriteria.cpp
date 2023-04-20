#include "FilteringCriteria.h"

DynamicArray FilteringCriteria::filter(DynamicArray& data)
{
	return data;
}

float FilteringPrice::getPrice() const
{
	return this->price;
}

void FilteringPrice::setPrice(float price)
{
	this->price = price;
}

FilteringPrice::FilteringPrice()
{
	this->price = 0;
}

FilteringPrice::FilteringPrice(float price)
{
	this->price = price;
}

DynamicArray FilteringPrice::filter(DynamicArray& data)
{
	DynamicArray output_array;
	for (int i = 0; i < data.getLength(); i++)
	{
		if (data.get(i).getPrice() < this->price)
		{
			output_array.append(data.get(i));
		}
	}
	return output_array;
}

OfferType FilteringType::getType() const
{
	return this->type;
}

void FilteringType::setType(int type)
{
	this->type = (OfferType)(type);
}

FilteringType::FilteringType()
{
	this->type = (OfferType)(0);
}

FilteringType::FilteringType(int type)
{
	this->type = (OfferType)(type);
}

DynamicArray FilteringType::filter(DynamicArray& data)
{
	DynamicArray output_array;
	for (int i = 0; i < data.getLength(); i++)
	{
		if (data.get(i).getType() == this->type)
		{
			output_array.append(data.get(i));
		}
	}
	return output_array;
}

OfferType FilteringCriteriaTypeAndPrice::getType() const
{
	return this->type;
}

float FilteringCriteriaTypeAndPrice::getPrice() const
{
	return this->price;
}

void FilteringCriteriaTypeAndPrice::setType(int type)
{
	this->type = (OfferType)(type);
}

void FilteringCriteriaTypeAndPrice::setPrice(float price)
{
	this->price = price;
}

FilteringCriteriaTypeAndPrice::FilteringCriteriaTypeAndPrice()
{
	this->type = (OfferType)(0);
	this->price = 0;
}

FilteringCriteriaTypeAndPrice::FilteringCriteriaTypeAndPrice(int type, float price)
{
	this->type = (OfferType)(type);
	this->price = price;
}

DynamicArray FilteringCriteriaTypeAndPrice::filter(DynamicArray& data)
{
	DynamicArray output_array;
	FilteringType first_filter(int(this->type));
	FilteringPrice second_filter(this->price);
	output_array = first_filter.filter(data);
	output_array = second_filter.filter(output_array);
	return output_array;

}
