#pragma once
#include "Exhibit.h"

class Action
{
public:
	//contructors
	Action();
	Action(int type, Painting parameter);

	//getters and setters
	int getType() const;
	Painting getParameter() const;

	void setType(int type);
	void setParameter(Painting parameter);


private:
	int type;//-1 - remove, +1 - add
	Painting parameter;
};