#include "BigInteger.h"

#include <cctype> // for isdigit
#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;





BigInteger::BigInteger()
{
	//std::cout << "default" << "\n";
	digits = new int[100]();
	this->sign = 0;
	this->num_digits = 100;
	//for (int i = 0; i < num_digits; i++)
	//	printf("%i - %d\n", i, digits[i]);

}

BigInteger::BigInteger(std::string str)
{
	//std::cout << "parametrized" << "\n";
	this->num_digits = str.size();
	int start;
	bool is_zero = true;
	for (int i = 0; i < str.size(); i++)
		if (str[i] != '0' && str[i] != '+' && str[i] != '-')
			is_zero = false;

	if (str[0] == '-' || str[0] == '+')
	{
		start = 1; this->num_digits--;
	}
	else start = 0;

	if (str[0] == '-' && is_zero == false)
	{
		(this->sign) = -1;
	}
	else {
		if (is_zero == true)(this->sign) = 0;
		else (this->sign) = 1;
	}

	digits = new int[num_digits + 1];
	for (int i = start; i <= str.size(); i++)
	{
		digits[i - start] = int(str[i]) - 48;
	}

}
//
//BigInteger::BigInteger(int size)
//{
//	digits = new int[size]();
//	this->sign = 0;
//	this->num_digits = size;
//	//for (int i = 0; i < num_digits; i++)
//	//	printf("%i - %d\n", i, digits[i]);
//
//}



BigInteger::~BigInteger()
{
	//std::cout << "destructor" << "\n";
	delete[] digits;
}



BigInteger& BigInteger::operator = (const BigInteger& x)
{
	//std::cout << "assignment operator" << "\n";
	if (this != &x)
	{
		delete[] digits;
		sign = x.sign;
		num_digits = x.num_digits;
		digits = new int[num_digits + 1];
		for (int i = 0; i < num_digits; i++)
			digits[i] = x.digits[i];
	}
	return *this;
}

BigInteger::BigInteger(const BigInteger& orig)
{
	//std::cout << "copy constructor" << "\n";
	if (this != &orig)
	{
		sign = orig.sign;
		num_digits = orig.num_digits;
		digits = new int[num_digits + 1];
		for (int i = 0; i < num_digits; i++)
			digits[i] = orig.digits[i];
		//memcpy(digits, orig.digits, num_digits + 1);
	}
}

int BigInteger::sgn()const
{
	return this->sign;
}


void BigInteger::negate()
{
	this->sign *= -1;
}

void BigInteger::change_sign(int sgn)
{
	this->sign = sgn;
}

int BigInteger::compare(const BigInteger& n)const
{
	if (this->sign == n.sign)
	{
		if (this->sign == 0) return 0;
		else
		{
			int i = 0, j = 0;
			while (digits[i] == 0)i++;
			while (n.digits[j] == 0)j++;

			if (this->sign == 1)
			{
				if (num_digits - i < n.num_digits - j) return -1;
				else
					if (num_digits - i > n.num_digits - j) return 1;
					else
					{
						while (i < num_digits && j < n.num_digits)
						{
							if (digits[i] < n.digits[j]) return -1;
							else if (digits[i] > n.digits[j]) return 1;
							i++; j++;
						}
						return 0;
					}
			}
			else
			{
				if (num_digits - i < n.num_digits - j) return 1;
				else
					if (num_digits - i > n.num_digits - j) return -1;
					else
					{
						while (i < num_digits && j < n.num_digits)
						{
							if (digits[i] < n.digits[j]) return 1;
							else if (digits[i] > n.digits[j]) return -1;
							i++; j++;
						}
						return 0;
					}
			}
		}

	}
	else
	{
		if (this->sign < n.sign)
			return -1;
		else
			return 1;
	}
}


bool BigInteger::operator==(const BigInteger& n)const
{
	if ((*this).compare(n) == 0)
		return true;
	else
		return false;
}

bool BigInteger::operator!=(const BigInteger& n)const
{
	if ((*this).compare(n) != 0)
		return true;
	else
		return false;
}

bool BigInteger::operator<(const BigInteger& n)const
{
	if ((*this).compare(n) == -1)
		return true;
	else
		return false;
}

bool BigInteger::operator<=(const BigInteger& n)const
{
	if ((*this).compare(n) != 1)
		return true;
	else
		return false;
}

bool BigInteger::operator>(const BigInteger& n)const
{
	if ((*this).compare(n) == 1)
		return true;
	else
		return false;
}

bool BigInteger::operator>=(const BigInteger& n)const
{
	if ((*this).compare(n) != -1)
		return true;
	else
		return false;
}

void adds(int* result, int* arr1, int* arr2, int arr1_sz, int arr2_sz)
{
	int k = arr1_sz > arr2_sz ? arr1_sz : arr2_sz;

	int i = arr1_sz - 1, j = arr2_sz - 1;
	k--;
	while (i >= 0 && j >= 0)
	{
		result[k] = arr1[i] + arr2[j];
		i--; j--; k--;
	}
	while (i >= 0)
	{
		result[k] = arr1[i];
		i--; k--;
	}
	while (j >= 0)
	{
		result[k] = arr2[j];
		j--; k--;
	}
}

int digitalize(int* result, int arr_sz)
{
	int carry = 0;
	for (int i = arr_sz - 1; i >= 0; i--)
	{
		if (result[i] + carry > 9) {
			result[i] = result[i] - 10 + carry;
			carry = 1;
		}
		else
		{
			result[i] = result[i] + carry;
			carry = 0;
		}
	}

	return carry;
}

void dg(int* result, int arr_sz)
{
	int borrow = 0;
	for (int i = arr_sz - 1; i >= 0; i--)
	{
		if (result[i] - borrow < 0) {
			result[i] = 10 + result[i] - borrow;
			borrow = 1;
		}
		else
		{
			result[i] = result[i] - borrow;
			borrow = 0;
		}
	}


}


void negate_arr(int* result, int arr_sz)
{
	for (int i = 0; i < arr_sz; i++)
	{
		result[i] *= -1;
	}
}

void remove_zeros(string* str)
{
	int i = 0;
	while ((*str)[i] == '0')
		i++;
	(*str).erase(0, i);
}

BigInteger BigInteger::add(const BigInteger& x)const
{
	if (this->sign == 0) {
		return x;
	}
	else
		if (x.sign == 0)
		{
			return (*this);
		}
	BigInteger copy = x;
	copy.negate();
	if (copy == (*this)) return BigInteger("0");

	if (sign == x.sign)
	{
		int k = this->num_digits > x.num_digits ? this->num_digits : x.num_digits;

		string str(k, '0');

		BigInteger sum(str);

		adds(sum.digits, this->digits, x.digits, this->num_digits, x.num_digits);
 
		int carry = digitalize(sum.digits, k);

		sum = BigInteger(sum.to_string());

		if (carry == 1)
			if (sum.sgn() != 0)
				sum = BigInteger("1" + sum.to_string());
			else {
				string str(sum.num_digits, '0');
				sum = BigInteger("1" + str);
			}

		sum.change_sign(sign);

		return sum;

	}
	else
	{
		BigInteger diff = x;
		diff.negate();
		diff = (*this).sub(diff);

		if (this->sign == -1)
		{
			BigInteger copy = *this;
			copy.negate();
			if (copy > x)diff.change_sign(-1);
			else diff.change_sign(1);
		}
		else
		{
			BigInteger copy = x;
			copy.negate();
			if (copy < (*this))diff.change_sign(1);
			else diff.change_sign(-1);
		}

		return diff;

	}


}


BigInteger BigInteger::sub(const BigInteger& x)const
{
	if (this->sign == 0) {
		BigInteger copy = x;
		copy.negate();
		return copy;
	}
	else
		if (x.sign == 0)
		{
			return (*this);
		}
	if ((*this) == x)
	{
		return BigInteger("0");
	}
	if (this->sign != x.sign)
	{
		BigInteger copy = x;
		copy.negate();
		copy = (*this).add(copy);

		if ((*this) < x)copy.change_sign(-1);
		else copy.change_sign(1);
		return copy;
	}
	else
	{
		if (this->sign == 1)
		{
			if (*(this) > x)
			{
				BigInteger copy = x;

				negate_arr(copy.digits, x.num_digits);

				int k = this->num_digits > x.num_digits ? this->num_digits : x.num_digits;

				string str(k, '0');

				BigInteger diff(str);

				adds(diff.digits, this->digits, copy.digits, this->num_digits, copy.num_digits);

				dg(diff.digits, k);

				str = diff.to_string();

				remove_zeros(&str);

				diff = BigInteger(str);

				diff.change_sign(1);

				return diff;
			}
			else
			{
				BigInteger copy = *this;

				negate_arr(copy.digits, this->num_digits);

				int k = this->num_digits > x.num_digits ? this->num_digits : x.num_digits;

				string str(k, '0');

				BigInteger diff(str);

				adds(diff.digits, copy.digits, x.digits, copy.num_digits, x.num_digits);

				dg(diff.digits, k);

				str = diff.to_string();

				remove_zeros(&str);

				diff = BigInteger(str);

				diff.change_sign(-1);

				return diff;
			}
		}
		else
		{
			if (*(this) < x)
			{
				BigInteger copy = x;

				negate_arr(copy.digits, x.num_digits);

				int k = this->num_digits > x.num_digits ? this->num_digits : x.num_digits;

				string str(k, '0');

				BigInteger diff(str);

				adds(diff.digits, this->digits, copy.digits, this->num_digits, copy.num_digits);

				dg(diff.digits, k);

				str = diff.to_string();

				remove_zeros(&str);

				diff = BigInteger(str);

				diff.change_sign(-1);

				return diff;
			}
			else
			{
				BigInteger copy = *this;

				negate_arr(copy.digits, this->num_digits);

				int k = this->num_digits > x.num_digits ? this->num_digits : x.num_digits;

				string str(k, '0');

				BigInteger diff(str);

				adds(diff.digits, copy.digits, x.digits, copy.num_digits, x.num_digits);

				dg(diff.digits, k);

				str = diff.to_string();

				remove_zeros(&str);

				diff = BigInteger(str);

				diff.change_sign(1);

				return diff;
			}
		}
		


	}
}


std::string BigInteger::to_string() const {
	ostringstream out;
	//if (this->sign == 0)
	//	out << "0";
	//else
	//{
		if ((*this).sign == -1)
			out << "-";
		for (int i = 0; i < this->num_digits; i++)
			out << digits[i];
	//}
	string result = out.str();
	return result;
}

std::ostream& operator<<(std::ostream& out, const BigInteger& n)
{
	out << n.to_string();
	return out;
}


BigInteger BigInteger::operator+(const BigInteger& n)const
{
	return (*this).add(n);
}

BigInteger BigInteger::operator-(const BigInteger& n)const
{
	return (*this).sub(n);
}

BigInteger& operator+=(BigInteger& A, const BigInteger& B)
{
	BigInteger result = A + B;
	A = result;
	return result;
}

BigInteger& operator-=(BigInteger& A, const BigInteger& B)
{
	BigInteger result = A - B;
	A = result;
	return result;
}

BigInteger& BigInteger::operator++()
{
	*this += (BigInteger("1"));
	return *this;
}

BigInteger BigInteger::operator++(int t)
{	
	BigInteger temp = *this;
	++*this;
	return temp;
}

BigInteger& BigInteger::operator--()
{
	*this -= (BigInteger("1"));
	return *this;
}

BigInteger BigInteger::operator--(int t)
{
	BigInteger temp = *this;
	--* this;
	return temp;
}

