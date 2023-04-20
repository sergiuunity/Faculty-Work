#define _CRT_SECURE_NO_WARNINGS
#define _CRTDBG_MAP_ALLOC

#include <crtdbg.h>
#include <stdio.h>
#include <stdlib.h>

#include "complex_test.h"

int compare_real(const void* n1, const void* n2)
{
	Complex* c1 = (Complex*)n1;
	Complex* c2 = (Complex*)n2;
	if (c1->real < c2->real) return -1;
	if (c1->real > c2->real) return 1;
	return 0;
}

int compare_imag(const void* n1, const void* n2)
{
	Complex* c1 = (Complex*)n1;
	Complex* c2 = (Complex*)n2;
	if (c1->imag < c2->imag) return -1;
	if (c1->imag > c2->imag) return 1;
	return 0;
}

int compare_mag(const void* n1, const void* n2)
{
	Complex* c1 = (Complex*)n1;
	Complex* c2 = (Complex*)n2;
	if (complex_mag(*c1) < complex_mag(*c2)) return -1;
	if (complex_mag(*c1) > complex_mag(*c2)) return 1;
	return 0;
}




bool isSorted(Complex* v, int n, int(*compar)(const void*, const void*))
{
	for (int i = 0; i < n - 1; i++)
	{
		if (compar(v + i, v + i + 1) == 1)
			return false;
	}
	return true;
}

int main(int argc, char** argv) {

	run_complex_tests(true);
	
	//1.a.
	//
	//printf("1.a. starts:\n");
	//Complex x;
	//float real, imag, r, theta, scalar, z;
	//printf("Give real and imaginary part:\n");
	//scanf("%f %f", &real, &imag);
	//x.real = real;
	//x.imag = imag;
	//printf("Magnitude: %f\n", complex_mag(x));
	//printf("Phase: %f\n", complex_phase(x));
	//complex_to_polar(x, &r, &theta);
	//printf("Polar form - r: %f; and theta: %f\n", r, theta);
	//printf("Complex conjugate: ");
	//complex_display(complex_conjugate(x));
	//printf("Give scalar:\n");
	//scanf("%f", &scalar);
	//complex_scalar_mult(&x, scalar);
	//printf("Result of scalar multiplication by %f: ", scalar);
	//complex_display(x);

	////1.b.
	//
	//printf("1.a. starts:\n");
	//Complex* y = (Complex*)malloc(sizeof(Complex));
	//printf("Give real and imaginary part:\n");
	//scanf("%f %f", &real, &imag);
	//y->real = real;
	//y->imag = imag;
	//printf("Magnitude: %f\n", complex_mag(*y));
	//complex_to_polar(*y, &r, &theta);
	//printf("Polar form - r: %f; and theta: %f\n", r, theta);
	//printf("Complex conjugate: ");
	//complex_display(complex_conjugate(*y));
	//printf("Give scalar:\n");
	//scanf("%f", &scalar);
	//complex_scalar_mult(y, scalar);
	//printf("Result of scalar multiplication by %f: ", scalar);
	//complex_display(*y);
	//printf("Multiplication result is:");
	//complex_display(complex_multiply(x, *y));
	//free(y);
	
    //2.

	char file_name[8] = "in1.txt";
	int n;
	float real_value, imag_value;
	FILE* my_file = fopen(file_name, "r");
	if (my_file == NULL) exit(-1);
	fscanf(my_file, "%d", &n);
	Complex* all_numbers = (Complex*)malloc(sizeof(Complex) * n);
	for (int i = 0; i < n; i++)
	{
		fscanf(my_file, "%f%f", &real_value, &imag_value);
		all_numbers[i] = complex_create(real_value, imag_value);
	}
	
	printf("Is the array sorted by the real part? - ");
	if (isSorted(all_numbers, n, compare_real) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the imag part? - ");
	if (isSorted(all_numbers, n, compare_imag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the magnitude? - ");
	if (isSorted(all_numbers, n, compare_mag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");


	qsort(all_numbers, n, sizeof(Complex), compare_real);
	printf("The numbers sorted by the real part:\n\n");
	for (int i = 0; i < n; i++)
	{
		complex_display(all_numbers[i]);
	}
	printf("Is the array sorted by the real part? - ");
	if (isSorted(all_numbers, n, compare_real) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the imag part? - ");
	if (isSorted(all_numbers, n, compare_imag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the magnitude? - ");
	if (isSorted(all_numbers, n, compare_mag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("\n");
	qsort(all_numbers, n, sizeof(Complex), compare_imag);
	printf("The numbers sorted by the imaginary part:\n\n");
	for (int i = 0; i < n; i++)
	{
		complex_display(all_numbers[i]);
	}
	printf("Is the array sorted by the real part? - ");
	if (isSorted(all_numbers, n, compare_real) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the imag part? - ");
	if (isSorted(all_numbers, n, compare_imag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the magnitude? - ");
	if (isSorted(all_numbers, n, compare_mag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("\n");
	qsort(all_numbers, n, sizeof(Complex), compare_mag);
	printf("The numbers sorted by the magnitude:\n\n");
	for (int i = 0; i < n; i++)
	{
		complex_display(all_numbers[i]);
	}
	printf("Is the array sorted by the real part? - ");
	if (isSorted(all_numbers, n, compare_real) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the imag part? - ");
	if (isSorted(all_numbers, n, compare_imag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("Is the array sorted by the magnitude? - ");
	if (isSorted(all_numbers, n, compare_mag) == true)
		printf("Yes.\n");
	else
		printf("No.\n");
	printf("\n");


	free(all_numbers);

	return 0;



}