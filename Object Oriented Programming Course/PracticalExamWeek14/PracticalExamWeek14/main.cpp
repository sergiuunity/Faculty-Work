#include <iostream>
#include "Exercise.h"
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using std::ifstream;

int main()
{
	//citire din fisier
	std::vector<Exercise> v;
	ifstream my_file("exercises.txt");
	while (!(my_file.eof()))
	{
		string new_string;
		int new_body;
		float new_intensity;
		my_file >> new_string >> new_body >> new_intensity;
		Exercise current_exercise = Exercise(new_string, new_body, new_intensity);
		v.push_back(current_exercise);
	}

	my_file.close();


	//displaying the vector
	for (auto it = v.begin(); it != v.end(); it++)
	{
		std::cout << *it << std::endl;
	}

}