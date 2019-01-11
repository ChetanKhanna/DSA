#include "LinkedListOps.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	// testing Linked-Listm
	LinkedList *L;
	L = LinkedList_create();
	printf("%s\n", "LinkedList created.");
	int arr[10];
	int arr2[20];
	arr[0] = arr2[0] = 25;
	arr[1] = 50;
	arr2[1] = 100;
	LinkedList_insert_stack(L, arr);
	LinkedList_insert_stack(L, arr2);
	printf("%s\n", "Assignment done.");
	printf("%d\n", L->num_nodes);
	printf("%d\n", *(L->head->array));
	int *p;
	p = LinkedList_pop_stack(L);
	printf("%d%c%d\n", p[1], ' ', L->num_nodes);
	LinkedList_insert_queue(L, arr2);
	printf("%d\n", *(L->head->next->array +1));
	p = LinkedList_pop_queue(L);
	printf("%d%c%d\n", p[1], ' ', L->num_nodes);	
	// testing some arrays and pointers
	int test_arr[10] = {1,2,3,4,5,};
	int *t = test_arr;
	printf("%d%c%d\n", *t,' ', test_arr[0]);
	printf("%ld%c%ld\n", &test_arr,' ', &t);
	printf("%ld%c%ld\n", (&test_arr +1),' ', (&t +1));
	return 0;
}
