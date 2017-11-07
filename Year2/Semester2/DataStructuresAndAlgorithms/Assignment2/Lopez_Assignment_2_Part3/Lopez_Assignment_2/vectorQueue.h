#pragma once
#ifndef VECTORQUEUE_H
#define VECTORQUEUE_H
#include <string>
#include<vector>
using namespace std;


typedef string Elem; // queue element type
class VectorQueue { // queue as a vector
public:
	VectorQueue(); // constructor
	int size() const; // number of items in the queue
	bool empty() const;// is the queue empty? Returns true if it is empty.
	const Elem& head(); // returns the element located at the head
	const Elem& tail(); // returns the element located at
	void enqueue(const Elem& e); // adds an element at the end
	void dequeue(); // removes the element located at the head
	void print();
private:
	vector<Elem> V; // vector of elements
	int n;//number of elements
};
#endif // !VECTORQUEUE_H