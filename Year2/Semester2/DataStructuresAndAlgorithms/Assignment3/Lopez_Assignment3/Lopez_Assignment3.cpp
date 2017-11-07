/*Requirements:
Write a c++ Program that reads 100 ints from file into array.
then copy array into binary search tree.
program then outputs:
-number of comprisons made to search for given int in bst
-number of comparisons to search for given int in array*/
#include "stdafx.h"
#include<iostream>
#include<fstream>
#include <string>
#define MaxWordSize 4
using namespace std;
string vals[100];

//define btree node data, taken from BSTExample code
typedef struct {
	char word[MaxWordSize + 1];
	int freq;
}NodeData;

// define the tree node
typedef struct treeNode {
	NodeData data;
	struct treeNode *left, *right;
}TreeNode, *TreeNodePtr;

// declare the binary tree
typedef struct {
	TreeNodePtr root;
}BinarySearchTree;

NodeData newNodeData(char str[], int n) {
	NodeData temp;
	strcpy_s(temp.word, str);
	temp.freq = n;
	return temp;
}

TreeNodePtr newTreeNode(NodeData d) {
	TreeNodePtr p = new TreeNode;
	p->data = d;
	p->left = p->right = NULL;
	return p;
}

TreeNodePtr findOrInsert(BinarySearchTree bt, NodeData d) {
	TreeNodePtr newTreeNode(NodeData);
	if (bt.root == NULL) return newTreeNode(d);
	TreeNodePtr curr = bt.root;
	int comparisons = 0;
	int cmp;
	while ((cmp = strcmp(d.word, curr->data.word)) != 0) {
		comparisons += 1;
		if (cmp<0) { // if left
			if (curr->left == NULL) return curr->left = newTreeNode(d);
			curr = curr->left;
		}
		else { // try right
			if (curr->right == NULL) return curr->right = newTreeNode(d);
			curr = curr->right;
		}	
	}
	
	return curr;
}

void loadFileToArray() {
	//load the file and shove values into array
	ifstream myfile("integers.txt");
	if (myfile.is_open()) {
		for (int i = 0; i <100; i++) {
			myfile >> vals[i];
			//cout << vals[i]<<"\n";
		}
		cout << "Files loaded successfully\n";
	}
}

void loadArrayToBST(BinarySearchTree bst) {
	/*go through array, insert word into tree*/
	for (int i = 0; i < 100; i++) {
		string tmp = vals[i];
		char word[5];
		strcpy_s(word, tmp.c_str());
		if (bst.root == NULL) {
			bst.root = newTreeNode(newNodeData(word, 1));
		}
		else {
			TreeNodePtr node = findOrInsert(bst, newNodeData(word, 0));
		}
	}
}

int searchArray(string v[],string s) {
	int cmp = 0;
	for (int i = 0; i < 100; i++) {
		int temp = 0;
		if (v[i] == s) {
			cmp += 1;
			break;
		}
		else { cmp += 1; }
	}
	return cmp;
}

int main()
{
	TreeNodePtr newTreeNode(NodeData);
	NodeData newNodeData(char[],int);
	TreeNodePtr findOrInsert(BinarySearchTree, NodeData);
	int findVal = 0;

	//declare binary tree
	BinarySearchTree bst;
	bst.root = NULL;

	/*three guesses as to what this method does*/
	loadFileToArray();

	loadArrayToBST(bst);

	string testVals[10] = { "90","49","100","30","75","79","25","5","15","55" };
	
	/*search by array*/
	cout << "searching test values through array:\n";
	for (int i = 0; i < 10; i++) {
		cout << searchArray(vals, testVals[i])<<" comparisons for "<<testVals[i]<<"\n";
	}
	/*
	returns pointer. I have no idea where to put the code to return
	comparisons made*/
	/*
	cout << "searching test values through bst:\n";
	for (int i = 0; i < 100; i++) {
		string tmp = vals[i];
		char word[5];
		strcpy_s(word, tmp.c_str());
		cout<<findOrInsert(bst, newNodeData(word,1));
	}
	*/
	system("pause");
}

