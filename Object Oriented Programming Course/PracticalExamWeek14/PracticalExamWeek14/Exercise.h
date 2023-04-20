#pragma once
#include <string>

using std::string;

typedef enum {
	upper_body = 0,
	abss = 1,
	lower_body = 2
}BodyPart;


class Exercise
{
public:
	Exercise();
	Exercise(string name, int body, float intensity);


	//displaying
	std::string to_string(string name, int bodyPart, float intensity)const;


	//operators
	friend std::istream& operator>>(std::istream& in, Exercise& e);

	friend std::ostream& operator<<(std::ostream& out, const Exercise& e);

	//getters and setters
	string getName()const;
	BodyPart getBody()const;
	float getIntensity()const;

	void setName(string name);
	void setBody(int body);
	void setIntensity(float intensity);

private:
	string name;
	BodyPart body;
	float intensity;

};