#include "LinkedListOps.h" // calling the header function which also inherits the structure header
#include <stdlib.h>
#include <stdio.h>

LinkedList * LinkedList_create()
{
	LinkedList *L;
	L = (LinkedList *)malloc(sizeof(LinkedList));
	L->head = NULL;
	L->num_nodes = 0;
	printf("%s%d\n", "Initial val: ", L->num_nodes );
	return L;
}

int LinkedList_insert_stack(LinkedList *L, int *new_array)
{
	// insert at head
	LinkedListNode *node;
	node = (LinkedListNode *)malloc(sizeof(LinkedListNode));
	node->array = new_array;
	node->next = L->head;
	L->head = node;
	L->num_nodes = L->num_nodes + 1;
	return 1;
}

int * LinkedList_pop_stack(LinkedList *L)
{
	// pop head
	LinkedListNode *node;
	node = (LinkedListNode *)malloc(sizeof(LinkedListNode));
	node = L->head;
	L->head = L->head->next;
	L->num_nodes -= 1;
	int *arr = node->array;
	free(node);
	return arr;
}

int LinkedList_insert_queue(LinkedList *L, int *new_array)
{
	// insert at tail
	LinkedListNode *temp, *node;
	node = (LinkedListNode *)malloc(sizeof(LinkedListNode)); // not needed for temp
															 // as it's only used for traversal
	node->array = new_array;
	node->next = NULL; // The incoming element will be the last one in queue
	temp = L->head;
	if (temp == NULL)
		L->head = node;
	else
	{
		while (temp->next != NULL)
			temp = temp->next;
		temp->next = node;
	}
	L->num_nodes += 1;
}

int * LinkedList_pop_queue(LinkedList *L)
{
	// pop head
	return LinkedList_pop_stack(L); // same function as stack	
}
