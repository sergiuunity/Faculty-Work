#include <math.h>
#include <stdio.h>

#include "complex_number.h"

Complex complex_create(float r, float i)
{
	Complex c;
	c.real = r;
	c.imag = i;
	return c;
}

void set_real(Complex* c, float r)
{
	c->real = r;
}

void set_imag(Complex* c, float i)
{
	c->imag =i;
}

float get_real(Complex c)
{
	return c.real;
}

float get_imag(Complex c)
{
	return c.imag;
}

Complex complex_conjugate(Complex c)
{
	Complex result;
	result.real = c.real;
	result.imag = (c.imag) * (-1);
	return result;
}

Complex complex_add(Complex c1, Complex c2)
{
	Complex result;
	result.real = c1.real + c2.real;
	result.imag = c1.imag + c2.imag;
	return result;
}

Complex complex_subtract(Complex c1, Complex c2)
{
	Complex result;
	result.real = c1.real - c2.real;
	result.imag = c1.imag - c2.imag;
	return result;
}

Complex complex_multiply(Complex c1, Complex c2)
{
	Complex result;
	result.real = c1.real * c2.real - c1.imag * c2.imag;
	result.imag = c1.real * c2.imag + c2.real * c1.imag;
	return result;
}

void complex_scalar_mult(Complex* c, float s)
{
	c->real = (c->real) * s;
	c->imag = (c->imag) * s;
}

bool complex_equals(Complex c1, Complex c2)
{
	if (c1.real == c2.real && c1.imag == c2.imag)
		return true;
	else
		return false;
}

float complex_mag(Complex c)
{
	return sqrt(c.real * c.real + c.imag * c.imag);
}

float complex_phase(Complex c)
{
	return (atan2(c.imag, c.real));
}

void complex_to_polar(Complex c, float* r, float* theta)
{
	(*r) = complex_mag(c);
	(*theta) = complex_phase(c);
}

void complex_display(Complex c)
{
	printf("%f + %f*i\n", c.real, c.imag);
}
