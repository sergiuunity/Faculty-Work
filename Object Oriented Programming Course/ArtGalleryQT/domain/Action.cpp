#include "Action.h"

Action::Action()
{
	this->type = 0;
	this->parameter = Painting();
}

Action::Action(int type, Painting parameter)
{
	this->type = type;
	this->parameter = parameter;
}

int Action::getType() const
{
	return type;
}

Painting Action::getParameter() const
{
	return parameter;
}

void Action::setType(int type)
{
	this->type = type;
}

void Action::setParameter(Painting parameter)
{
	this->parameter = parameter;
}
