#pragma once

#include "SortedMultiMap.h"


class SMMIterator{
	friend class SortedMultiMap;
private:
	//DO NOT CHANGE THIS PART
	const SortedMultiMap& map;
	SMMIterator(const SortedMultiMap& map);

	SortedMultiMap::PNode currentElement;

public:
	void first();
	void last();
	void next();
	void prev();
	bool valid() const;
   	TElem getCurrent() const;
};

