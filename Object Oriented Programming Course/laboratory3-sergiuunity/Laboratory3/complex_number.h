#pragma once
#include <stdbool.h>

typedef struct comp {
    float real;
    float imag;
}Complex;

Complex complex_create(float, float);

void set_real(Complex*, float);

void set_imag(Complex*, float);

float get_real(Complex);

float get_imag(Complex);
    
Complex complex_conjugate(Complex);

Complex complex_add(Complex, Complex);

Complex complex_subtract(Complex, Complex);

Complex complex_multiply(Complex, Complex);

void complex_scalar_mult(Complex*, float);

bool complex_equals(Complex, Complex);

float complex_mag(Complex);

float complex_phase(Complex);

void complex_to_polar(Complex c, float* r, float* theta);

void complex_display(Complex c);
