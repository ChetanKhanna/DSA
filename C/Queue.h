struct queue_list
{
	int val;
	struct queue_list *next;
};
typedef struct queue_list QNODE;

typedef struct
{
	int num_nodes;
	QNODE *next;
}QHEAD;