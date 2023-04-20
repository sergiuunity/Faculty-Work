#include <iostream>
#include <fstream>
#include "Gallery.h"

Gallery::Gallery()
{
	this->name = "Art Gallery";
}

Gallery::Gallery(string name)
{
	this->name = name;
}

string Gallery::getName() const
{
	return this->name;
}

void Gallery::setName(string name)
{
	this->name = name;
}

int Gallery::size() const
{
	return gallery.size();
}

void Gallery::append(Painting p)
{
	//add an element at the end of the repository. ignoreStacks asks if we should add the current action to the undo stack or not.
	//throws error if the element is already in the repository.
	if (this->search(p) == false)
	{
		gallery.push_back(p);
	}
	else
	{
		throw(-2);
	}
}

Painting Gallery::popBack()
{
	//removes last element and returns it.
	if (this->size() != 0)
	{
		Painting temp = this->get(this->size() - 1);
		this->remove_at_index(this->size() - 1);
		return temp;
	}
	else
	{
		throw(-5);
	}
}

Painting Gallery::remove_at_index(int index)
{
	//removes the element at the given index or throws an error if the index is out of range. ignoreStacks asks if we should add the current action to the undo stack or not.
	//returns the removed element.
	if (index >= 0 && index < this->size())
	{
		Painting temp = this->get(index);
		gallery.erase(gallery.begin() + index);
		return temp;
	}
	else
	{
		throw(-1);
	}
}

bool Gallery::remove(Painting p)
{
	//removes the given element.
	//returns true if the element is in the repository and false if not.
	if (this->search(p) == true)
	{
		gallery.erase(std::remove(gallery.begin(), gallery.end(), p), gallery.end());
		return true;
	}
	return false;
}

Painting& Gallery::get(int index)
{
	//returns a pointer to the element having the given index. If the index is out of range it throws an error.
	if (index >= 0 && index < this->size())
	{
		return gallery.at(index);
	}
	else
	{
		throw(-1);
	}
}

bool Gallery::search(const Painting v) const
{
	//returns true if the given element is in the repo and false otherwise.
	for (auto it = gallery.begin(); it != gallery.end(); ++it)
		if (*it == v)
			return true;
	return false;
}

void Gallery::edit_at_index(Painting p, int index)
{	
	//switches the value of the element at the given index with the given new value. It throws an error if the new value is already in the repository or if the index is out of range.
	if (this->search(p) == false)
	{
		if (index >= 0 && index < this->size())
		{
			gallery[index] = p;
		}
		else
		{
			throw(-1);
		}
	}
	else
	{
		throw(-2);
	}
}

void Gallery::load_from_file(string path)
{
	//switches the repository content with the one from the given file.
	ifstream input_file;
	input_file.open(path);
	string id, name, author, estimated_price, width, height;
	getline(input_file, name, '\n');
	this->name = name;

	//empty the current gallery repository
	while (gallery.size() != 0)
		gallery.pop_back();

	while (input_file.good())
	{
		getline(input_file, id, ',');
		getline(input_file, name, ',');
		getline(input_file, author, ',');
		getline(input_file, estimated_price, ',');
		getline(input_file, width, ',');
		getline(input_file, height, '\n');
		this->append(Painting(id, name, author, stoi(estimated_price), stoi(width), stoi(height)));
	}
	input_file.close();
}

void Gallery::save_into_file(string path) const
{
	//loads the given file with the repository data.
	ofstream output_file;
	output_file.open(path);
	output_file << name;
	for (auto it = gallery.begin(); it != gallery.end(); ++it)
	{
		output_file << endl << (*it).getId() << "," << (*it).getName() << "," << (*it).getAuthor() << "," << (*it).getEstimated_price() << "," << (*it).getWidth() << "," << (*it).getHeight();
		//if (it != gallery.end() - 1)
		//	output_file << endl;
	}
	output_file.close();
}


ostream& operator<<(ostream& out, const Gallery& arr)
{
	out << " " << arr.name << ":" << endl;
	if (arr.size() == 0)
	{
		out << "Currently Empty." << endl;
	}
	else
	{
		for (auto it = arr.gallery.begin(); it != arr.gallery.end(); ++it)
			out << *it << endl;
	}
	return out;
}

bool Gallery::operator==(const Gallery& other) const
{
	//compares two galleriess.
	return name == other.name && this->gallery == other.gallery;
}

bool Gallery::operator!=(const Gallery& other) const
{
	//compares two galleriess.
	return !(*this == other);
}
