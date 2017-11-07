#include"stdafx.h"
#include "vectorQueue.h"
#include"MyExceptions.h"
#include<iostream>

VectorQueue::VectorQueue(): V(), n(0) {}//constructor

int VectorQueue::size() const//number of items in queue
{
	return V.size();
}

bool VectorQueue::empty() const//is the queue empty?
{
	return n == 0;
}

const Elem & VectorQueue::head()
{
	return V.front();
}

const Elem & VectorQueue::tail()
{
	return V.back();
}

void VectorQueue::enqueue(const Elem & e)
{
	V.resize(V.size());
	V.push_back(e);//push new value to end of queue
}

void VectorQueue::dequeue()
{
	int i;
	//go through vector V and push them all back by one
	for (i = 0; i < V.size(); i++) {
		V.erase(V.begin());
	}

	//V.pop_back();//pop back current last value, reducing size
				 //go through vector and replace all values with tmp values
}

void VectorQueue::print()
{
	int i;
	//go through entire vector and output each value
	for (i = 0; i < V.size(); i++) {
		cout << i << ": " << V[i] << "\n";
	}
}
