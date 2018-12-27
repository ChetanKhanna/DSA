#include "StackOps.h"
#include <stdbool.h>
#include <stdlib.h>

SHEAD * createStack()
{
	SHEAD *head;
	head = (SHEAD *)malloc(sizeof(SHEAD));
	head->num_nodes = 0;
	head->next = NULL;
	return head;
}

SNODE * popStack(SHEAD *head)
{
	SNODE *node;
	node = head->next;
	head->num_nodes = head->num_nodes-1;
	head->next = head->next->next;
	return node;
}

void pushStack(SHEAD *head, int val)
{
	SNODE *new_node;
	new_node->val = val;
	new_node->next = head->next;
	head->next = new_node;
	head->num_nodes = head->num_nodes+1;
}

_Bool isEmptyStack(SHEAD *head)
{
	return (head->num_nodes == 0);
}