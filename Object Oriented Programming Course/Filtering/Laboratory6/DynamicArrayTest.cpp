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
	test_set_operations();
}

void DynamicArrayTest::test_getLenght()
{
	DynamicArray<Offer> DA;
	assert(DA.getLength() == 0);
	for (int i = 0; i < 10; i++)
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
	assert(DA.getLength() == 10);

}

void DynamicArrayTest::test_getCapacity()
{
	DynamicArray<Offer> DA;
	assert(DA.getCapacity() == 100);
	DynamicArray<Offer> DA2(5);
	assert(DA2.getCapacity() == 5);
	for (int i = 0; i < 6; i++)
		DA2.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
	assert(DA2.getCapacity() == 10);
}

void DynamicArrayTest::test_append()
{
	DynamicArray<Offer> DA;
	for (int i = 0; i < 5; i++)
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
	for (int i = 0; i < 5; i++)
		assert(DA.get(i).getId() == std::to_string(i));
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
	catch (int)
	{
		assert(true);
	}

}

void DynamicArrayTest::test_popBack()
{
	DynamicArray<Offer> DA;
	try
	{
		DA.popBack();
		assert(false);
	}
	catch (int)
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
	DynamicArray<Offer> DA;
	for (int i = 0; i < 5; i++)
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
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
	catch (int)
	{
		assert(true);
	}
	try
	{
		DA.remove(-1);
		assert(false);
	}
	catch (int)
	{
		assert(true);
	}
}


void DynamicArrayTest::test_get()
{
	DynamicArray<Offer> DA;
	for (int i = 0; i < 5; i++)
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
	for (int i = 0; i < 5; i++)
		assert(DA.get(i) == Offer(std::to_string(i), 0, "", "", "", "", 0));
	try
	{
		DA.get(10);
		assert(false);
	}
	catch (int)
	{
		assert (true);
	}
}

void DynamicArrayTest::test_insertionOperator()
{
	DynamicArray<Offer> DA;
	std::ostringstream out, out2;
	out << DA;
	string to_test = out.str();
	assert(to_test == "[]");

	for (int i = 0; i < 5; i++)
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));

	out2 << DA;
	to_test = out2.str();
	assert(to_test == "[Offer(ID:0) Offer(ID:1) Offer(ID:2) Offer(ID:3) Offer(ID:4) ]");
}

void DynamicArrayTest::test_isElemIn()
{
	DynamicArray<Offer> DA;
	assert(DA.isElemIn(Offer("0", 0, "", "", "", "", 0)) == false);
	DA.append(Offer("0", 0, "", "", "", "", 0));
	assert(DA.isElemIn(Offer("0", 0, "", "", "", "", 0)) == true);


}

void DynamicArrayTest::test_resize()
{
	DynamicArray<Offer> DA(1);
	assert(DA.getCapacity() == 1);
	DA.append(Offer("0", 0, "", "", "", "", 0));
	assert(DA.getCapacity() == 1);
	DA.append(Offer("1", 0, "", "", "", "", 0));
	assert(DA.getCapacity() == 2);
	int *ptr = NULL;
}

void DynamicArrayTest::test_constructors()
{
	DynamicArray<Offer> DA;
	DynamicArray<Offer> DA_copy(DA);
	assert(DA_copy.getLength() == 0);
	assert(DA_copy.getCapacity() == 100);
	for (int i = 0; i < 5; i++)
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
	DynamicArray<Offer> DA_copy2(DA);
	assert(DA_copy2.getLength() == 5);
	assert(DA_copy2.getCapacity() == 100);
	for (int i = 0; i < 5; i++)
	{
		assert(DA_copy2.get(i) == DA.get(i));
	}


}

void DynamicArrayTest::test_copyConstructor()
{
	DynamicArray<Offer> DA;
	DynamicArray<Offer> DA_copy;
	DA_copy = DA;
	assert(DA_copy.getLength() == 0);
	assert(DA_copy.getCapacity() == 100);
	for (int i = 0; i < 5; i++)
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
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
	DynamicArray<Offer> DA;
	DynamicArray<Offer>	DA2;
	assert(DA == DA2);
	DA2 = DynamicArray<Offer>(3);
	assert(!(DA == DA2));
	DA2 = DynamicArray<Offer>();
	for (int i = 0; i < 5; i++)
	{
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
		DA2.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
	}
	assert(DA == DA2);
	DA2.popBack();
	DA2.append(Offer());
	assert(!(DA == DA2));
	DA2.append(Offer(std::to_string(7), 0, "", "", "", "", 0));
	assert(!(DA == DA2));
}

void DynamicArrayTest::test_inequality()
{
	DynamicArray<Offer> DA, DA2;
	assert(!(DA != DA2));
	DA2 = DynamicArray<Offer>(3);
	assert((DA != DA2));
	DA2 = DynamicArray<Offer>();
	for (int i = 0; i < 5; i++)
	{
		DA.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
		DA2.append(Offer(std::to_string(i), 0, "", "", "", "", 0));
	}
	assert(!(DA != DA2));
	DA2.popBack();
	DA2.append(Offer());
	assert((DA != DA2));
	DA2.append(Offer(std::to_string(7), 0, "", "", "", "", 0));
	assert((DA != DA2));
}

void DynamicArrayTest::test_set_operations()
{
	DynamicArray<Offer> DA1;
	DynamicArray<Offer> DA2;
	DynamicArray<Offer> wanted;
	assert(DA1.intersection_of_two_arrays(DA2) == DA1);
	assert(DA1.union_of_two_arrays(DA2) == DA1);
	Offer e1("1", 999, "", "", "", "", 0);
	Offer e2("2", 999, "", "", "", "", 0);
	Offer e3("3", 999, "", "", "", "", 0);
	Offer e4("4", 999, "", "", "", "", 0);
	DA1.append(e1);
	DA2.append(e4);
	assert(DA1.intersection_of_two_arrays(DA2) == wanted);
	wanted.append(e1);
	wanted.append(e4);
	assert(DA1.union_of_two_arrays(DA2) == wanted);
	DA1.append(e2);
	DA1.append(e3);
	DA2.append(e2);
	DA2.append(e3);
	wanted = DynamicArray<Offer>();
	wanted.append(e2);
	wanted.append(e3);
	assert(DA1.intersection_of_two_arrays(DA2) == wanted);
	wanted = DynamicArray<Offer>();
	wanted.append(e1);
	wanted.append(e2);
	wanted.append(e3);
	wanted.append(e4);
	assert(DA1.union_of_two_arrays(DA2) == wanted);
	



}
