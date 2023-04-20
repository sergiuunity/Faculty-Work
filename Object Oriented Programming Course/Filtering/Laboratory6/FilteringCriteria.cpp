#include "FilteringCriteria.h"
using std::string;


FilteringCriteriaAnd::FilteringCriteriaAnd(FilteringCriteria* input_filter1, FilteringCriteria* input_filter2)
{
	f1 = input_filter1;
	f2 = input_filter2;
}

DynamicArray<Offer> FilteringCriteriaAnd::filter(DynamicArray<Offer>& data)
{
	DynamicArray<Offer> first, second, result;
	first = (*f1).filter(data);
	second = (*f2).filter(data);
	
	//intersection

	result = first.intersection_of_two_arrays(second);

	return result;
}




FilteringCriteriaOr::FilteringCriteriaOr(FilteringCriteria* input_filter1, FilteringCriteria* input_filter2)
{
	f1 = input_filter1;
	f2 = input_filter2;
}

DynamicArray<Offer> FilteringCriteriaOr::filter(DynamicArray<Offer>& data)
{
	DynamicArray<Offer> first, second, result;
	first = (*f1).filter(data);
	second = (*f2).filter(data);

	//intersection

	result = first.union_of_two_arrays(second);

	return result;
}





float FilteringCriteriaPrice::getPrice() const
{
	return this->price;
}

void FilteringCriteriaPrice::setPrice(float price)
{
	this->price = price;
}

FilteringCriteriaPrice::FilteringCriteriaPrice()
{
	this->price = 0;
}

FilteringCriteriaPrice::FilteringCriteriaPrice(float price)
{
	this->price = price;
}

DynamicArray<Offer> FilteringCriteriaPrice::filter(DynamicArray<Offer>& data)
{
	DynamicArray<Offer> output_array;
	for (unsigned int i = 0; i < data.getLength(); i++)
	{
		if (data.get(i).getPrice() < this->price)
		{
			output_array.append(data.get(i));
		}
	}
	return output_array;
}

OfferType FilteringCriteriaType::getType() const
{
	return this->type;
}

void FilteringCriteriaType::setType(int type)
{
	this->type = (OfferType)(type);
}

FilteringCriteriaType::FilteringCriteriaType()
{
	this->type = (OfferType)(0);
}

FilteringCriteriaType::FilteringCriteriaType(int type)
{
	this->type = (OfferType)(type);
}

DynamicArray<Offer> FilteringCriteriaType::filter(DynamicArray<Offer>& data)
{
	DynamicArray<Offer> output_array;
	for (unsigned int i = 0; i < data.getLength(); i++)
	{
		if (data.get(i).getType() == this->type)
		{
			output_array.append(data.get(i));
		}
	}
	return output_array;
}


string FilteringCriteriaDeparture::getDeparture() const
{
	return this->departure;
}

void FilteringCriteriaDeparture::setDeparture(string departure)
{
	this->departure = departure;
}

FilteringCriteriaDeparture::FilteringCriteriaDeparture()
{
	this->departure = "";
}


FilteringCriteriaDeparture::FilteringCriteriaDeparture(string departure)
{
	this->departure = departure;
}

DynamicArray<Offer> FilteringCriteriaDeparture::filter(DynamicArray<Offer>& data)
{
	DynamicArray<Offer> output_array;
	for (unsigned int i = 0; i < data.getLength(); i++)
	{
		if (data.get(i).getDeparture() == this->departure)
		{
			output_array.append(data.get(i));
		}
	}
	return output_array;


}

string FilteringCriteriaDestination::getDestination() const
{
	return this->destination;
}

void FilteringCriteriaDestination::setDestination(string destination)
{
	this->destination = destination;
}

FilteringCriteriaDestination::FilteringCriteriaDestination()
{
	this->destination = "";
}


FilteringCriteriaDestination::FilteringCriteriaDestination(string destination)
{
	this->destination = destination;
}

DynamicArray<Offer> FilteringCriteriaDestination::filter(DynamicArray<Offer>& data)
{
	DynamicArray<Offer> output_array;
	for (unsigned int i = 0; i < data.getLength(); i++)
	{
		if (data.get(i).getDestination() == this->destination)
		{
			output_array.append(data.get(i));
		}
	}
	return output_array;


}
