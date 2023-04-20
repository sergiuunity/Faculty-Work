#include "complex_number.h"
#include <sstream>
#include <iomanip>
#include <string>
using namespace std;

Complex::Complex()
{
	this->real = 0;
	imag = 0;
}
Complex::Complex(float real, float imag)
{
	this->real = real;
	this->imag = imag;
}
void Complex::setReal(float real)
{
	this->real = real;
}
void Complex::setImag(float imag)
{
	this->imag = imag;
}
float Complex::getReal()const
{
	return real;
}
float Complex::getImag()const
{
	return imag;
}

bool Complex::operator==(const Complex& b)const
{
	if (this->real == b.real && this->imag == b.imag)
		return true;
	else
		return false;
}

bool Complex::operator!=(const Complex& b)const
{
	if (this->real == b.real && this->imag == b.imag)
		return false;
	else
		return true;
}

Complex Complex::operator+(const Complex& b)const
{
	Complex sum(this->real + b.real, this->imag + b.imag);
	return sum;
}

Complex Complex::operator-(const Complex& b)const
{
	Complex sum(this->real - b.real, this->imag - b.imag);
	return sum;
}

Complex Complex::operator*(const Complex& b)const
{
	Complex sum(this->real * b.real - this->imag * b.imag, this->real * b.imag + this->imag * b.real);
	return sum;
}

Complex Complex::conjugate()const
{
	Complex result(this->real, (this->imag) * (-1));
	return result;
}
Complex Complex::add(Complex c)const
{
	return (*this) + c;
}

Complex Complex::subtract(Complex c)const
{
	return (*this) - c;
}

Complex Complex::multiply(Complex c)const
{
	return (*this) * c;
}

void Complex::multiply(float s)
{
	this->real = (this->real) * s;
	this->imag = (this->imag) * s;;
	
}

bool Complex::equals(Complex other)const
{
	if (this->real == other.real && this->imag == other.imag)
		return true;
	else
		return false;
}

float Complex::magnitude()
{
	return sqrt(this->real * this->real + this->imag * this->imag);
}

float Complex::phase()
{
	return (atan2(this->imag, this->real));
}

void Complex::toPolar(float* r, float* theta)
{
	(*r) = (*this).magnitude();
	(*theta) = (*this).phase();
}

std::string Complex::toString() const{
	ostringstream out;
	if (this->real == 0)
		if (this->imag == 0)
			out << this->real;
		else
			if (this->imag == 1)
				out << "i";
			else
				if (this->imag == -1)
					out << "-" << "i";
				else
					out << this->imag << "i";
	else
		if (this->imag == 0)
			out << this->real;
		else
			if (this->imag == 1)
			{
				out << std::setprecision(2) << std::fixed;
				out << this->real << "+" << "i";
			}
			else
				if (this->imag == -1)
				{
					out << std::setprecision(2) << std::fixed;
					out << this->real << "-" << "i";
				}
				else
					if (this->imag > 0)
					{
						out << std::setprecision(2) << std::fixed;
						out << this->real << "+" << this->imag << "i";
					}
					else
					{
						out << std::setprecision(2) << std::fixed;
						out << this->real << this->imag << "i";
					}

	string result = out.str();
	return result;
}

std::ostream& operator<<(std::ostream& out, const Complex& c)
{
	out << c.toString();
	return out;
}

std::istream& operator>>(std::istream& in, Complex& c)
{
	in >> c.real >> c.imag;
	return in;
}