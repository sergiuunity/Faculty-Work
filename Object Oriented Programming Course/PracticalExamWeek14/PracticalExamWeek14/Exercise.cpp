#include "Exercise.h"
#include <sstream>
#include <iostream>

Exercise::Exercise()
{
	this->name = "";
	this->body = (BodyPart)(0);
	this->intensity = 0.0f;
}

Exercise::Exercise(string name, int body, float intensity)
{
	this->name = name;
	this->body = (BodyPart)(body);
	this->intensity = intensity;
}

std::string Exercise::to_string(string name, int bodyPart, float intensity) const
{
	std::ostringstream out;
	string type_str;

	out << name << " " << bodyPart << " " << intensity << "";

	string result = out.str();
	return result;
}

string Exercise::getName() const
{
	return name;
}

BodyPart Exercise::getBody() const
{
	return body;
}

float Exercise::getIntensity() const
{
	return intensity;
}

void Exercise::setName(string name)
{
	this->name = name;
}

void Exercise::setBody(int body)
{
	this->body = (BodyPart)(body);
}

void Exercise::setIntensity(float intensity)
{
	this->intensity = intensity;
}

std::istream& operator>>(std::istream& in, Exercise& e)
{
	int body;
	in >> e.name >> body >> e.intensity;
	e.setBody(body);
	return in;
}

std::ostream& operator<<(std::ostream& out, const Exercise& e)
{
	out << e.to_string(e.name, (int)(e.body), e.intensity);
	return out;
}
