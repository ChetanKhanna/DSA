#include "LinkedList.h" // importing Linked List Structure defined in other header file

// Create new LinkedList
LinkedList * LinkedList_create();
// Functions for using linked list as stack
int LinkedList_insert_stack(LinkedList *, int *);
int * LinkedList_pop_stack(LinkedList *);
// Functions for using linked list as queue
int LinkedList_insert_queue(LinkedList *, int *);
int * LinkedList_pop_queue(LinkedList *);
