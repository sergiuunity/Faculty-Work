#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>

#include "complex_test.h"
#include "complex_number.h"

using namespace std;

int main(int argc, char** argv) {

#if ENABLE_TESTS > 0
	run_complex_tests(true);
#endif
	Complex c1(10, 20);
	Complex* c2 = (Complex*)malloc(2*sizeof(float));
	c2->setReal(2);
	c2->setImag(3);
	printf("c2.real = %f\nc2.imag = %f\n", c2->getReal(), c2->getImag());
	cout << "conjugate = " << c1.conjugate() << endl;
	Complex sum = c1 + c1;
	cout << "sum = " << sum << endl;
	Complex diff = c1 - c1;
	cout << "diff = " << diff << endl;
	Complex prod = c1 * c1;
	cout << "prod = " << prod << endl;
	float s = 3;
	c1.multiply(s);
	cout << "scal_prod = " << c1 << endl;
	Complex toCompare(30, 60);
	if (c1.equals(toCompare) == true)
		printf("Works\n");
	else
		printf("Error\n");
	printf("magnitude = %f\n", c2->magnitude());
	printf("phase = %f\n", c2->phase());
	float r, theta;
	c2->toPolar(&r, &theta);
	printf("r = %f; theta = %f\n", r, theta);
	cout << "c1.toString = " << c1.toString() << endl;
	sum = c1.add(*c2);
	cout << "sum = " << sum << endl;
	diff = c1.subtract(*c2);
	cout << "diff = " << diff << endl;
	prod = c1.multiply(*c2);
	cout << "prod = " << prod << endl;
	Complex x(1, 2);
	Complex y(1, 2);
	if (x == y)
		printf("Works\n");
	else
		printf("Error\n");
	if (x != c1)
		printf("Works\n");
	else
		printf("Error\n");
	free(c2);
	istringstream sstr("-9+99i");
	Complex read;
	sstr >> read;
	cout << read;
	return 0;
}