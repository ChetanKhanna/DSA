#include "BinTreeOps.h"
#include <stdlib.h>
#include <stdio.h>
#include "StackOps.h"
#include "QueueOps.h"

ROOT * createBinTree()
{
	ROOT * r;
	r = (ROOT *)malloc(sizeof(ROOT));
	r->count = 1;
	r->root = NULL;

	return r;
}

void setRootVal(ROOT *r, int d)
{
	r->root->val = d;
}

int getRootVal(ROOT *r)
{
	return r->root->val;
}

void setNodeVal(ROOT *r, NODE *n, int val)
{
	n->val = val;
}

int getNodeVal(ROOT *r, NODE *n)
{
	return n->val;
}

void setLeftNode(ROOT *r, NODE *n, int val)	// old value will be re-written
{
	if (n->left == NULL)
	{
		NODE *temp;
		temp->val = val;
		temp->right = NULL;
		temp->left = NULL;
		n->left = temp;
		r->count += 1;
	}
	else
	{
		n->left->val = val;
	}
}

NODE * getLeftNode(ROOT *r, NODE *n)
{
	return n->left;
}

void setRightNode(ROOT *r, NODE *n, int val)	// old value will be re-written
{
	if (n->left == NULL)
	{
		NODE *temp;
		temp->val = val;
		temp->right = NULL;
		temp->left = NULL;
		n->right = temp;
		r->count += 1;
	}
	else
		n->right->val = val;
}

NODE * getRightNode(ROOT *r, NODE *n)
{
	return n->right;
}
