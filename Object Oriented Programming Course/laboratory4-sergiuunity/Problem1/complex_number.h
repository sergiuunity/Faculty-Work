#pragma once
#include <string>
#include <fstream>

class Complex {
public:
	Complex();

	Complex(float, float);

	void setReal(float);

	void setImag(float);

	float getReal()const;

	float getImag()const;

	Complex conjugate()const;

	Complex add(Complex)const;

	Complex subtract(Complex)const;

	Complex multiply(Complex)const;

	void multiply(float);

	bool equals(Complex)const;

	float magnitude();

	float phase();

	void toPolar(float* r, float* theta);

	std::string toString()const;

	Complex operator-(const Complex& c)const;

	Complex operator*(const Complex& c)const;

	bool operator==(const Complex& c)const;

	bool operator!=(const Complex& c)const;

	Complex operator+(const Complex& c)const;

	friend std::istream& operator>>(std::istream& in, Complex& c);

	friend std::ostream& operator<<(std::ostream& out, const Complex& c);

private:
	float real, imag;

};


