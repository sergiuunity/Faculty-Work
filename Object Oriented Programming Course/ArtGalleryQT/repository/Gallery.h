#pragma once
#include <string>
#include <ostream>
#include <vector>
#include "../domain/Exhibit.h"
#include "../domain/Action.h"

using namespace std;

class Gallery
{
public:
	//constructors
	Gallery();
	Gallery(string name);

	//getters and setters
	string getName() const;

	void setName(string name);

	//dynamic array operations
	int size() const;
	void append(Painting p);
	Painting popBack();
	Painting remove_at_index(int index);
	bool remove(Painting p);
	Painting& get(int index);
	bool search(const Painting p) const;
	void edit_at_index(Painting p,int index);

	//loading and saving from a file
	void load_from_file(string path);
	void save_into_file(string path) const;

	//operators
	friend ostream& operator<<(ostream& out, const Gallery& arr);
	bool operator==(const Gallery& other)const;
	bool operator!=(const Gallery& other)const;

private:
	string name;
	vector<Painting> gallery;
};

