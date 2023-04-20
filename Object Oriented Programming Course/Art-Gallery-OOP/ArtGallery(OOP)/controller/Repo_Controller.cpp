#include <iostream>
#include <sstream>
#include <string>
#include "Repo_Controller.h"

using namespace std;

GalleryController::GalleryController()
{
	//initializes a controller with default data.
	this->managed_gallery = Gallery();
}

GalleryController::GalleryController(Gallery managed_gallery)
{
	//initializes a controller with the given data.
	this->managed_gallery = managed_gallery;
}

string GalleryController::getName()
{
	return managed_gallery.getName();
}

void GalleryController::setName(string name)
{
	//changes the name of the managed gallery.
	managed_gallery.setName(name);
}

int GalleryController::size()
{
	return managed_gallery.size();
}

void GalleryController::append(string id, string name, string author, int estimated_price, int width, int height)
{
	//adds an element with the given data to the gallery.
	managed_gallery.append(Painting(id, name, author, estimated_price, width, height));
	undo_stack.push(Action(1, Painting(id, name, author, estimated_price, width, height)));
}

void GalleryController::remove_at_index(int index)
{
	//removes the element at the given index from the gallery.
	Painting temp = managed_gallery.remove_at_index(index);
	undo_stack.push(Action(-1, temp));
}

void GalleryController::edit_at_index(string id, string name, string author, int estimated_price, int width, int height, int index)
{
	//replaces the values of the element at the given index with the given ones.
	managed_gallery.edit_at_index(Painting(id, name, author, estimated_price, width, height), index);
}

Painting& GalleryController::get(int index)
{
	return (managed_gallery.get(index));
}

void GalleryController::load_from_file(string path)
{	
	//replaces the content of the gallery with the content from the given file.
	managed_gallery.load_from_file(path);
}

void GalleryController::save_into_file(string path)
{
	//saves the content of the gallery in the given file.
	managed_gallery.save_into_file(path);
}

void GalleryController::undo()
{
	//undoes the previous add/remove action applied by the user.
	if (undo_stack.empty() == false)
	{
		Action last_action = undo_stack.top();
		redo_stack.push(last_action);
		if (last_action.getType() == -1)
			managed_gallery.append(last_action.getParameter());
		else if (last_action.getType() == 1)
			managed_gallery.remove(last_action.getParameter());
		undo_stack.pop();
	}
	else
		throw(-3);

}

void GalleryController::redo()
{
	//redoes the previous undoed action applied by the user.
	if (redo_stack.empty() == false)
	{
		Action last_action = redo_stack.top();
		undo_stack.push(last_action);
		if (last_action.getType() == -1)
			managed_gallery.remove(last_action.getParameter());
		else if (last_action.getType() == 1)
			managed_gallery.append(last_action.getParameter());
		redo_stack.pop();
	}
	else
		throw(-3);
}

bool GalleryController::operator==(const GalleryController& other) const
{
	//compares two controllers.
	return this->managed_gallery == other.managed_gallery;
}

bool GalleryController::operator!=(const GalleryController& other) const
{
	//compares two controllers.
	return !((*this) == other);
}

ostream& operator<<(ostream& out, const GalleryController& controlla)
{
	out << controlla.managed_gallery;
	return out;
}
