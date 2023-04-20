#pragma once
#include<string>
#include<iostream>


class BigInteger{

public:
	//constructors
	BigInteger();

	BigInteger(std::string);

	//destructor
    ~BigInteger();


	//copy constructor
	BigInteger(const BigInteger& orig);


	//assignment constructor
	BigInteger& operator = (const BigInteger& x);


	//general functions / needed multiple times
	int sgn()const;

	void negate();

	void change_sign(int sgn);

	//comparasion operators
	bool operator==(const BigInteger& n)const;

	bool operator!=(const BigInteger& n)const;

	bool operator<(const BigInteger& n)const;

	bool operator<=(const BigInteger& n)const;

	bool operator>(const BigInteger& n)const;

	bool operator>=(const BigInteger& n)const;

	
	//display
	friend std::ostream& operator<<(std::ostream& out, const BigInteger& n);


	//operators
	BigInteger operator+(const BigInteger& n)const;

	BigInteger operator-(const BigInteger& n)const;

	friend BigInteger& operator+=(BigInteger& A, const BigInteger& B);

	friend BigInteger& operator-=(BigInteger& A, const BigInteger& B);

	BigInteger& operator++();
	BigInteger operator++(int t);

	BigInteger& operator--();
	BigInteger operator--(int t);


private:
	int* digits;
	int sign;
	int num_digits;

	int compare(const BigInteger& n)const;

	BigInteger add(const BigInteger& n)const;
	BigInteger sub(const BigInteger& n)const;


	std::string to_string()const;



};


