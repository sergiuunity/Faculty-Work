#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Write a function that takes as an input an array of integer numbers(both positive and negative numbers)  and returns the value of the triplet with the maximum product, as well as the elements that form this triplet.
// Use pass by pointer / address to return the elements that form that triplet.
// In the main function, you will first read the size of the array n, and then n integers representing the elements in the array.

long long find_max_triplet(int v[], int v_size, int* a, int* b, int* c)
{
	int mx1, mx2, mx3, mn1, mn2;
	mx1 = mx2 = mx3 = INT_MIN;
	mn1 = mn2 = INT_MAX;
	long long c1, c2;
	for (int i = 0; i < v_size; i++)
	{
		if (v[i] > mx1) {
			mx3 = mx2;
			mx2 = mx1;
			mx1 = v[i];
		}
		else
			if (v[i] > mx2) {
				mx3 = mx2;
				mx2 = v[i];
			}
			else
				if (v[i] > mx1)
					mx1 = v[i];
		if (v[i] < mn1) {
			mn2 = mn1;
			mn1 = v[i];
		}
		else if (v[i] < mn2)
			mn2 = v[i];
	}
	c1 = mx1 * mx2 * mx3;
	c2 = mx1 * mn1 * mn2;
	if (c1 > c2) {
		*a = mx3;
		*b = mx2;
		*c = mx1;
		return c1;
	}
	else {
		*a = mn2;
		*b = mn1;
		*c = mx1;
		return c2;
	}
}

int main() {
	int sz, t1, t2, t3, x, end_it = 0;
	long long prod;
	int ok = scanf("%d", &sz);
	if (ok == 1)
	{
		int a[sz];
		for (int i = 0; i < sz;i++)
		{
			ok = scanf("%d", &a[i]);
			if (ok == 0) end_it = 1;
		}
		if (sz > 2 && end_it == 0) {
			prod = find_max_triplet(a, sz, &t1, &t2, &t3);
			if (t1 > t2)
			{
				x = t1;
				t1 = t2;
				t2 = x;
			}
			if (t2 > t3)
			{
				x = t2;
				t2 = t3;
				t3 = x;
			}
			printf("The triplet with the maximum product %lld is (%d,%d,%d)", prod, t1, t2, t3);
		}
		else
		{
			printf("Invalid input! Application will now stop");
		}
	}
	else
	{
		printf("Invalid input! Application will now stop");
	}
	return 0;
}
