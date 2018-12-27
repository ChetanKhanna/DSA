#include "QueueOps.h"
#include <stdbool.h>
#include <stdlib.h>

QHEAD * createQueue()
{
	QHEAD *head;
	head = (QHEAD *)malloc(sizeof(QHEAD));
	head->num_nodes = 0;
	head->next = NULL;
	return head;
}

QNODE * popQueue(QHEAD *head)
{
	if (head->num_nodes == 0)
		return NULL;
	else if (head->next->next == NULL)
	{
		QNODE *temp_node = head->next;
		head->next = NULL;
		head->num_nodes = 0;
		return temp_node;
	}
	else
	{
		QNODE *temp_node_1, *temp_node_2;
		temp_node_1 = head->next;
		while (temp_node_1->next->next != NULL)
			temp_node_1 = temp_node_1->next;
		temp_node_2 = temp_node_1->next;
		temp_node_1->next = NULL;
		head->num_nodes = head->num_nodes-1;
		return temp_node_2;
	} 
}

void pushQueue(QHEAD *head, int val)
{
	QNODE *new_node;
	new_node->val = val;
	new_node->next = head->next;
	head->next = new_node;
	head->num_nodes = head->num_nodes+1;
}