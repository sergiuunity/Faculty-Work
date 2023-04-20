#include "SMMIterator.h"
#include "SortedMultiMap.h"

SMMIterator::SMMIterator(const SortedMultiMap& d) : map(d){
	currentElement = d.head;
}

void SMMIterator::first(){
	currentElement = map.head;
}

void SMMIterator::last() {
	currentElement = map.tail;
}

void SMMIterator::next(){
	if (currentElement == nullptr) throw exception();
	currentElement = currentElement->next;
}

void SMMIterator::prev() {
	if (currentElement == nullptr) throw exception();
	currentElement = currentElement->prev;
}

bool SMMIterator::valid() const{
	return currentElement != nullptr;
}

TElem SMMIterator::getCurrent() const{
	if (currentElement == nullptr) throw exception();
	return currentElement->data;
}


