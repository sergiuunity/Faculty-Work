#pragma once
#include <string>
#include "Exercise.h"
#include <vector>

using std::vector;

using std::string;

vector<Exercise> possible_exercises_warmup {Exercise("a1",2, 0.2), Exercise("a2", 2, 0.3), Exercise("a3", 1, 0.1), Exercise("a4", 1, 0.2), Exercise("a5", 0, 0.3), Exercise("a6", 0, 0.3)};
vector<Exercise> possible_exercises_workout{ Exercise("b1",2, 0.8), Exercise("b2", 2, 0.7), Exercise("b3", 1, 0.9), Exercise("b4", 1, 0.6), Exercise("b5", 0, 0.5), Exercise("b6", 0, 0.7) };
vector<Exercise> possible_exercises_cooldown{ Exercise("c1",2, 0.4), Exercise("c2", 2, 0.1), Exercise("c3", 1, 0.2), Exercise("c4", 1, 0.4), Exercise("c5", 0, 0.3), Exercise("c6", 0, 0.3) };


class Workout
{
public:
	Workout();
	Workout(int ed);
	void generate();
	void print();

protected:
	virtual void buildWarmup() = 0;
	virtual void buildWorkout() = 0;
	virtual void buildCooldown() = 0;

	int exerciseDuration;
	int workoutDuration;
	vector<Exercise> exercises;

};


class HIITWorkout: public Workout
{
public:
	HIITWorkout();
	HIITWorkout(int ed);
	void buildWarmup();
	void buildWorkout();
	void buildCooldown();
};


class StretchingWorkout : public Workout
{
public:
	StretchingWorkout();
	StretchingWorkout(int ed);
	void buildWarmup();
	void buildWorkout();
	void buildCooldown();
};