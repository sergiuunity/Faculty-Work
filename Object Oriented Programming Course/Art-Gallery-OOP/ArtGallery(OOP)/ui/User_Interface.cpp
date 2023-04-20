#include <iostream>
#include <string>
#include <algorithm>
#include "User_Interface.h"
#include "../testing/ActionTest.h"
#include "../testing/ExhibitTest.h"
#include "../testing/GalleryTest.h"
#include "../testing/ControllerTest.h"

using std::cout;
using std::cin;
using std::endl;


void printMenu()
{
	//prints the option menu.
	cout << "   exit        Quit the application" << endl;
	cout << "   menu        Print the menu" << endl;
	cout << "display        Display the gallery" << endl;
	cout << "   name        Change the gallery's name" << endl;
	cout << "    add        Add a painting" << endl;
	cout << " remove        Remove at index" << endl;
	cout << "   edit        Edit at index" << endl;
	cout << "   load        Load from file" << endl;
	cout << "   save        Save into file" << endl;
	cout << "   undo        Undo the last add/remove action" << endl;
	cout << "   redo        Redo the last add/remove action" << endl;
	cout << endl;
}

void start(GalleryController controller)
{
	//starts the application.

	ActionTest::runAllTests();
	ExhibitTest::runAllTests();
	PaintingTest::runAllTests();
	GalleryTest::runAllTests();
	ControllerTest::runAllTests();

	cout << "All tests have passed." << endl;

	string command;
	printMenu();
	cout << "Give command...";
	cin >> command;
	transform(command.begin(), command.end(), command.begin(), tolower);
	while (command != "exit" && command != "0")
	{
		if (command == "menu")
		{
			printMenu();
		}
		else if (command == "display")
		{
			cout << controller << endl;
		}
		else if (command == "name")
		{
			string given_name;
			cout << "Name: ";
			cin >> given_name;
			controller.setName(given_name);
		}
		else if (command == "add")
		{
			try
			{
				string given_id, given_name, given_author;
				int given_estimated_price, given_width, given_height;
				cout << "ID: ";
				cin >> given_id;
				cout << "Name: ";
				cin >> given_name;
				cout << "Author: ";
				cin >> given_author;
				cout << "Estimated price: ";
				cin >> given_estimated_price;
				cout << "Width: ";
				cin >> given_width;
				cout << "Height: ";
				cin >> given_height;
				controller.append(given_id, given_name, given_author, given_estimated_price, given_width, given_height);
			}
			catch (int x)
			{
				if (x == -2)
					cout << "Such painting already exists in the gallery. Try a new command." << endl;
			}
		}
		else if (command == "remove")
		{
			try
			{
				int given_index;
				cout << "Index to remove: ";
				cin >> given_index;
				controller.remove_at_index(given_index);
			}
			catch (int x)
			{
				if (x == -1)
					cout << "Index out of range. Try a new command." << endl;
			}

		}
		else if (command == "edit")
		{
			try
			{
				string given_id, given_name, given_author;
				int given_estimated_price, given_width, given_height, given_index;
				cout << "Index to edit: ";
				cin >> given_index;
				cout << "ID: ";
				cin >> given_id;
				cout << "Name: ";
				cin >> given_name;
				cout << "Author: ";
				cin >> given_author;
				cout << "Estimated price: ";
				cin >> given_estimated_price;
				cout << "Width: ";
				cin >> given_width;
				cout << "Height: ";
				cin >> given_height;
				controller.edit_at_index(given_id, given_name, given_author, given_estimated_price, given_width, given_height, given_index);
			}
			catch (int x)
			{
				if (x == -1)
					cout << "Index out of range. Try a new command." << endl;
				else if (x == -2)
					cout << "Such painting already exists in the gallery. Try a new command." << endl;
			}
		}
		else if (command == "load")//generated_files/data.csv
		{
			string given_path;
			cout << "Path to file: ";
			cin >> given_path;
			controller.load_from_file(given_path);
		}
		else if (command == "save")//generated_files/data.csv
		{
			string given_path;
			cout << "Path to file: ";
			cin >> given_path;
			controller.save_into_file(given_path);
		}
		else if (command == "undo")
		{
			try
			{
				controller.undo();
			}
			catch (int x)
			{
				cout << "No add/remove operations have been done. Try a new command." << endl;
			}
		}
		else if (command == "redo")
		{
			try
			{
				controller.redo();
			}
			catch (int x)
			{
				cout << "No undo operations have been done. Try a new command." << endl;
			}
		}
		else
		{
			cout << "Unknown command. Try a new one." << endl;
		}
		cout << "Give command...";
		cin >> command;
		transform(command.begin(), command.end(), command.begin(), tolower);
	}
	cout << "The application will now close." << endl;



}

