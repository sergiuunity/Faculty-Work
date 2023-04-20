#include "Workout.h"
#include <sstream>
#include <iostream>

Workout::Workout()
{
	exerciseDuration = 0;
}

Workout::Workout(int ed)
{
	exerciseDuration = ed;
}

void Workout::generate()
{
	this->buildWarmup();
	this->buildWorkout();
	this->buildCooldown();
}

void Workout::print()
{
	for (auto it = exercises.begin(); it != exercises.end(); it++)
	{
		std::cout << *it << std::endl;
	}
}



HIITWorkout::HIITWorkout() : Workout()
{
}

HIITWorkout::HIITWorkout(int ed): Workout(ed)
{
}



void HIITWorkout::buildWarmup()
{
	for (int i = 0; i < 4; i++)
	{
		int x = rand() % exercises.size();
		exercises.push_back(possible_exercises_warmup[i]);
		workoutDuration += exerciseDuration;
	}
}

void HIITWorkout::buildWorkout()
{
	for (int i = 0; i < 10; i++)
	{
		int x = rand() % exercises.size();
		exercises.push_back(possible_exercises_workout[i]);
		workoutDuration += exerciseDuration;
	}
}

void HIITWorkout::buildCooldown()
{
	for (int i = 0; i < 3; i++)
	{
		int x = rand() % exercises.size();
		exercises.push_back(possible_exercises_cooldown[i]);
		workoutDuration += exerciseDuration;
	}
}

StretchingWorkout::StretchingWorkout() : Workout()
{
}

StretchingWorkout::StretchingWorkout(int ed) : Workout(ed)
{
}

void StretchingWorkout::buildWarmup()
{
}

void StretchingWorkout::buildWorkout()
{
}

void StretchingWorkout::buildCooldown()
{
}
