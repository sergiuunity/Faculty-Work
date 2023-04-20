#include "DynamicArrayTest.h"
#include <stdlib.h>
#include <sstream>

void DynamicArrayTest::runAllTests()
{
	test_getLenght();
	test_getLenght();
	test_getCapacity();
	test_append();
	test_popBack();
	test_remove();
	test_get();
	test_insertionOperator();
	test_isElemIn();
	test_resize();
	test_constructors();
	test_copyConstructor();
	test_equality();
	test_inequality();
}

void DynamicArrayTest::test_getLenght()
{
	DynamicArray DA;
	assert(DA.getLength() == 0);
	for (int i = 0; i < 10; i++)
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
	assert(DA.getLength() == 10);

}

void DynamicArrayTest::test_getCapacity()
{
	DynamicArray DA;
	assert(DA.getCapacity() == 100);
	DynamicArray DA2(5);
	assert(DA2.getCapacity() == 5);
	for (int i = 0; i < 6; i++)
		DA2.append(Offer(to_string(i), 0, "", "", "", "", 0));
	assert(DA2.getCapacity() == 10);
}

void DynamicArrayTest::test_append()
{
	DynamicArray DA;
	for (int i = 0; i < 5; i++)
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
	for (int i = 0; i < 5; i++)
		assert(DA.get(i).getId() == to_string(i));
	assert(DA.getLength() == 5);
	Offer o("10", 0, "", "", "", "", 0);
	DA.append(o);
	assert(DA.getLength() == 6);
	assert(DA.get(5) == o);
	try
	{
		DA.append(o);
		assert(false);
	}
	catch (int x)
	{
		assert(true);
	}

}

void DynamicArrayTest::test_popBack()
{
	DynamicArray DA;
	try
	{
		DA.popBack();
		assert(false);
	}
	catch (int x)
	{
		assert(true);
	}
	DA.append(Offer("1", 0, "", "", "", "", 0));
	assert(DA.getLength() == 1);
	assert(DA.popBack() == Offer("1", 0, "", "", "", "", 0));
	assert(DA.getLength() == 0);

}

void DynamicArrayTest::test_remove()
{
	DynamicArray DA;
	for (int i = 0; i < 5; i++)
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
	DA.remove(0);
	assert(DA.get(0) != Offer("0", 0, "", "", "", "", 0));
	assert(DA.getLength() == 4);
	assert(DA.remove(3) == Offer("4", 0, "", "", "", "", 0));
	assert(DA.getLength() == 3);
	try
	{
		DA.remove(10);
		assert(false);
	}
	catch (int x)
	{
		assert(true);
	}
	try
	{
		DA.remove(-1);
		assert(false);
	}
	catch (int x)
	{
		assert(true);
	}
}


void DynamicArrayTest::test_get()
{
	DynamicArray DA;
	for (int i = 0; i < 5; i++)
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
	for (int i = 0; i < 5; i++)
		assert(DA.get(i) == Offer(to_string(i), 0, "", "", "", "", 0));
	try
	{
		DA.get(10);
		assert(false);
	}
	catch (int x)
	{
		assert (true);
	}
}

void DynamicArrayTest::test_insertionOperator()
{
	DynamicArray DA;
	ostringstream out, out2;
	out << DA;
	string to_test = out.str();
	assert(to_test == "[]");

	for (int i = 0; i < 5; i++)
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));

	out2 << DA;
	to_test = out2.str();
	assert(to_test == "[Offer(ID:0) Offer(ID:1) Offer(ID:2) Offer(ID:3) Offer(ID:4) ]");
}

void DynamicArrayTest::test_isElemIn()
{
	DynamicArray DA;
	assert(DA.isElemIn(Offer("0", 0, "", "", "", "", 0)) == false);
	DA.append(Offer("0", 0, "", "", "", "", 0));
	assert(DA.isElemIn(Offer("0", 0, "", "", "", "", 0)) == true);


}

void DynamicArrayTest::test_resize()
{
	DynamicArray DA(1);
	assert(DA.getCapacity() == 1);
	DA.append(Offer("0", 0, "", "", "", "", 0));
	assert(DA.getCapacity() == 1);
	DA.append(Offer("1", 0, "", "", "", "", 0));
	assert(DA.getCapacity() == 2);
	int *ptr = NULL;
}

void DynamicArrayTest::test_constructors()
{
	DynamicArray DA;
	DynamicArray DA_copy(DA);
	assert(DA_copy.getLength() == 0);
	assert(DA_copy.getCapacity() == 100);
	for (int i = 0; i < 5; i++)
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
	DynamicArray DA_copy2(DA);
	assert(DA_copy2.getLength() == 5);
	assert(DA_copy2.getCapacity() == 100);
	for (int i = 0; i < 5; i++)
	{
		assert(DA_copy2.get(i) == DA.get(i));
	}


}

void DynamicArrayTest::test_copyConstructor()
{
	DynamicArray DA;
	DynamicArray DA_copy;
	DA_copy = DA;
	assert(DA_copy.getLength() == 0);
	assert(DA_copy.getCapacity() == 100);
	for (int i = 0; i < 5; i++)
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
	DA_copy = DA;
	assert(DA_copy.getLength() == 5);
	assert(DA_copy.getCapacity() == 100);
	for (int i = 0; i < 5; i++)
	{
		assert(DA_copy.get(i) == DA.get(i));
	}

}

void DynamicArrayTest::test_equality()
{
	DynamicArray DA, DA2;
	assert(DA == DA2);
	DA2 = DynamicArray(3);
	assert(!(DA == DA2));
	DA2 = DynamicArray();
	for (int i = 0; i < 5; i++)
	{
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
		DA2.append(Offer(to_string(i), 0, "", "", "", "", 0));
	}
	assert(DA == DA2);
	DA2.popBack();
	DA2.append(Offer());
	assert(!(DA == DA2));
	DA2.append(Offer(to_string(7), 0, "", "", "", "", 0));
	assert(!(DA == DA2));
}

void DynamicArrayTest::test_inequality()
{
	DynamicArray DA, DA2;
	assert(!(DA != DA2));
	DA2 = DynamicArray(3);
	assert((DA != DA2));
	DA2 = DynamicArray();
	for (int i = 0; i < 5; i++)
	{
		DA.append(Offer(to_string(i), 0, "", "", "", "", 0));
		DA2.append(Offer(to_string(i), 0, "", "", "", "", 0));
	}
	assert(!(DA != DA2));
	DA2.popBack();
	DA2.append(Offer());
	assert((DA != DA2));
	DA2.append(Offer(to_string(7), 0, "", "", "", "", 0));
	assert((DA != DA2));
}
