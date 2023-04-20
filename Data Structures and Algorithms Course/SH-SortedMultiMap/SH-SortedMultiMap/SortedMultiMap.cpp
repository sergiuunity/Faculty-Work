#include "SMMIterator.h"
#include "SortedMultiMap.h"
#include <iostream>
#include <vector>
#include <exception>
using namespace std;


SortedMultiMap::SortedMultiMap(Relation r) {
	length = 0;
	relation = r;
	head = nullptr;
	tail = nullptr;
}
//complexity: O(1)

void SortedMultiMap::add(TKey c, TValue v) {
	PNode new_node = new Node(TElem(c, v), nullptr, nullptr);
	if (head == nullptr)//add at the beginning
	{
		head = new_node;
		tail = new_node;
	}
	else
		if (relation(c, head->data.first) == true)//new node becomes head
		{
			new_node->next = head;
			head = new_node;
			head->next->prev = head;
		}
		else //we must go through the dll
		{
			PNode current_node = head;
			while (current_node->next != nullptr && relation(c, current_node->next->data.first) == false)
			{
				current_node = current_node->next;
			}
			if (current_node->next != nullptr)	//add in middle
			{
				new_node->next = current_node->next;
				current_node->next->prev = new_node;
				current_node->next = new_node;
				new_node->prev = current_node;
			}
			else//add at the end
			{
				new_node->prev = tail;
				tail->next = new_node;
				tail = new_node;
			}
		}

	length++;
}
/*
complexity: Total: O(length)
Best Case:When the new element must come first, becoming the head - O(1)
Worst Case: When the new element must come last, becoming the tail - O(length)
*/

vector<TValue> SortedMultiMap::search(TKey c) const {
	vector <TValue> output_vector;

	PNode current_node = head;
	while (current_node != nullptr && current_node->data.first != c)
	{ 
		current_node = current_node->next;
	}
	while (current_node != nullptr && current_node->data.first == c)
	{
		output_vector.push_back(current_node->data.second);
		current_node = current_node->next;
	}
	return output_vector;
}
/*
complexity: Total: O(length)
Best Case:When the tail is the only found element - O(1)
Worst Case: When the tail is a searched element - O(length)
*/

bool SortedMultiMap::remove(TKey c, TValue v) {
	PNode current_node = head;
	TElem new_element = TElem(c, v);
	if (this->isEmpty() == false) {
		while (current_node != nullptr && current_node->data!=new_element)
		{
			current_node = current_node->next;
		}
		if (current_node != nullptr)
		{
			if (current_node->prev == nullptr)//remove head
			{
				if (current_node->next == nullptr)//when it's the only element
				{
					head = nullptr;
					tail = nullptr;
					length--;
					return true;
				}
				else//more elements, remove head
				{
					PNode copy_node = head;
					head = head->next;
					head->prev = nullptr;
					delete copy_node;
					length--;
					return true;
				}
			}
			else if (current_node->next == nullptr)//remove tail
			{
				PNode copy_node = tail;
				tail = tail->prev;
				tail->next = nullptr;
				delete copy_node;
				length--;
				return true;
			}
			else if (current_node->prev != nullptr && current_node->next != nullptr)
			{
				current_node->next->prev = current_node->prev;
				current_node->prev->next = current_node->next;
				current_node->prev = nullptr;
				current_node->next = nullptr;
				delete current_node;
				length--;
				return true;
			}
		}
	}
    return false;
}
/*
complexity: Total: O(length)
Best Case:When the element is the head - O(1)
Worst Case: When the element is the tail - O(length)
*/


int SortedMultiMap::size() const {
	return length;
}
//complexity: O(1)

bool SortedMultiMap::isEmpty() const {
	return length == 0;
}
//complexity: O(1)

SMMIterator SortedMultiMap::iterator() const {
	return SMMIterator(*this);
}
//complexity: O(1)

SortedMultiMap::~SortedMultiMap() {
	while (head != nullptr) {
		PNode p = head;
		head = head->next;
		delete p;
	}
}
//complexity: O(length)


SortedMultiMap::SortedMultiMap(const SortedMultiMap& other)
{
	length = other.length;
	relation = other.relation;
	if (other.head == nullptr)
	{
		head = nullptr;
		tail = nullptr;
	}
	else
	{
		head = new Node(other.head->data, other.head->prev, other.head->next);
		PNode current_node = other.head->next;
		PNode temp = head;
		while (current_node != nullptr)
		{
			temp->next = new Node(current_node->data, nullptr, temp);
			temp = temp->next;
			current_node = current_node->next;
		}
		tail = temp;
	}
}
//complexity: O(length)

SortedMultiMap& SortedMultiMap::operator=(const SortedMultiMap& other)
{
	length = other.length;
	relation = other.relation;
	while (head != nullptr) {
		PNode p = head;
		head = head->next;
		delete p;
	}
	if (other.head == nullptr)
	{
		head = nullptr;
		tail = nullptr;
	}
	else
	{
		head = new Node(other.head->data, other.head->prev, other.head->next);
		PNode current_node = other.head->next;
		PNode temp = head;
		while (current_node != nullptr)
		{
			temp->next = new Node(current_node->data, nullptr, temp);
			temp = temp->next;
			current_node = current_node->next;
		}
		tail = temp;
	}
	return *this;
}
//complexity: O(length)

SortedMultiMap::Node::Node(TElem d, PNode n, PNode p)
{
		data = d;
		next = n;
		prev = p;
}
//complexity: O(1)

