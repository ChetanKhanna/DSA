struct Node // This will represent a single node in linked list
{
	int *array; // pointer to an interger array
	struct Node *next; // pointer to next node in linked list
};
typedef struct Node LinkedListNode; 

typedef struct // Defining head of Linked List seperately for easy access 
{
	LinkedListNode *head; // the head of linked list is also a node
	int num_nodes;	// storing number of nodes in linked list for reference
}LinkedList; 