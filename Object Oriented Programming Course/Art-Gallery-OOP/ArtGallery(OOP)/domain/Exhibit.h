#pragma once
#include <string>
using std::string;

class Exhibit
{
public:
	//constructors
	Exhibit();
	Exhibit(string id, string name, string author, int estimated_price);

	//getters and setters
	string getId() const;
	string getName() const;
	string getAuthor() const;
	int getEstimated_price() const;
	
	void setId(string id);
	void setName(string name);
	void setAuthor(string author);
	void setEstimated_price(int estimated_price);

	//operators
	friend std::ostream& operator<<(std::ostream& out, const Exhibit& x);
	bool operator==(const Exhibit& x) const;
	bool operator!=(const Exhibit& x) const;

protected:
	string id;
	string name;
	string author;
	int estimated_price;

private:
};


class Painting : public Exhibit
{
public:
	//constructors
	Painting();
	Painting(string id, string name, string author, int estimated_price, int width, int height);

	//getters and setters
	int getWidth() const;
	int getHeight() const;

	void setWidth(int width);
	void setHeight(int height);

	//operators
	friend std::ostream& operator<<(std::ostream& out, const Painting& x);
	bool operator==(const Painting& x) const;
	bool operator!=(const Painting& x) const;

protected:

private:
	int width;
	int height;
};

