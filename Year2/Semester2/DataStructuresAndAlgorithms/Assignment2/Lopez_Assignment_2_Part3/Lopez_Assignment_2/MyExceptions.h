#ifndef MYEXCEPTIONS_H
#define MYEXCEPTIONS_H
#include"stdafx.h"
#include<string>
using namespace std;
// implement exceptions
/*this code is taken from QueueProject sln provided on slate
so as to save time, because of this some of it may not be used*/
class RuntimeException {
private:
	string errorMsg;
public:
	RuntimeException(const string& err) {
		errorMsg = err;
	}
	string getMessage() const { return errorMsg; }
};
class StackException : public RuntimeException {
public:
	StackException(const string& err) : RuntimeException(err) {}
};
class QueueException : public RuntimeException {
public:
	QueueException(const string& err) : RuntimeException(err) {}
};
#endif
