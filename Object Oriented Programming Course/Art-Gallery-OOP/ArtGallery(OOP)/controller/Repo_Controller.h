#pragma once
#include <string>
#include <stack>
#include "../repository/Gallery.h"

using std::string;

class GalleryController
{
public:
	//constructors
	GalleryController();
	GalleryController(Gallery managed_gallery);

	//gallery related
	string getName();
	void setName(string name);

	//dynamic array operations
	int size();
	void append(string id, string name, string author, int estimated_price, int width, int height);
	void remove_at_index(int index);
	void edit_at_index(string id, string name, string author, int estimated_price, int width, int height, int index);
	Painting& get(int index);
	
	//loading and saving from a file
	void load_from_file(string path);
	void save_into_file(string path);

	//undo-redo
	void undo();
	void redo();

	//operators
	friend ostream& operator<<(ostream& out, const GalleryController& controlla);
	bool operator==(const GalleryController& other)const;
	bool operator!=(const GalleryController& other)const;

private:
	Gallery managed_gallery;
	stack<Action> undo_stack;
	stack<Action> redo_stack;
};