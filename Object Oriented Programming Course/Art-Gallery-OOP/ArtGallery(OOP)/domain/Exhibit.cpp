#include <iostream>
#include <sstream>
#include <string>
#include "Exhibit.h"
using namespace std;

Exhibit::Exhibit()
{
	//initializes an exhibit with default values.
	this->id = "";
	this->name = "Unnamed";
	this->author = "Unknown";
	this->estimated_price = 0;
}

Exhibit::Exhibit(string id, string name, string author, int estimated_price)
{
	//initializes an exhibit with given values.
	this->id = id;
	this->name = name;
	this->author = author;
	this->estimated_price = estimated_price;
}

string Exhibit::getId() const
{
	return id;
}

string Exhibit::getName() const
{
	return name;
}

string Exhibit::getAuthor() const
{
	return author;
}

int Exhibit::getEstimated_price() const
{
	return estimated_price;
}

void Exhibit::setId(string id)
{
	this->id = id;
}

void Exhibit::setName(string name)
{
	this->name = name;
}

void Exhibit::setAuthor(string author)
{
	this->author = author;
}

void Exhibit::setEstimated_price(int estimated_price)
{
	this->estimated_price = estimated_price;
}

bool Exhibit::operator==(const Exhibit& x) const
{
	//compares two Exhibit type objects.
	return id == x.getId() && name == x.getName() && author == x.getAuthor() && estimated_price == x.getEstimated_price();
}

bool Exhibit::operator!=(const Exhibit& x) const
{
	//compares two Exhibit type objects.
	return !(*this == x);
}

std::ostream& operator<<(std::ostream& out, const Exhibit& x)
{	
	out << x.name << "[" << x.id << "] by " << x.author << " estimated at " << x.estimated_price << "$.";
	return out;
}

Painting::Painting() : Exhibit()
{
	//initializes a painting with default values.
	this->width = 0;
	this->height = 0;
}

Painting::Painting(string id, string name, string author, int estimated_price, int width, int height) : Exhibit(id, name, author, estimated_price)
{
	//initializes a painting with the given values.
	this->width = width;
	this->height = height;
}

int Painting::getWidth() const
{
	return width;
}

int Painting::getHeight() const
{
	return height;
}

void Painting::setWidth(int width)
{
	this->width = width;
}

void Painting::setHeight(int height)
{
	this->height = height;
}

bool Painting::operator==(const Painting& x) const
{
	//compares two Painting type objects.
	return id == x.getId() && name == x.getName() && author == x.getAuthor() && estimated_price == x.getEstimated_price() && width == x.getWidth() && height == x.getHeight();
}

bool Painting::operator!=(const Painting& x) const
{
	//compares two Painting type objects.
	return !(*this == x);
}


std::ostream& operator<<(std::ostream& out, const Painting& x)
{
	out << x.name << "[" << x.id << "](" << x.width << "x" << x.height << "cm) by " << x.author << " estimated at " << x.estimated_price << "$.";
	return out;
}

