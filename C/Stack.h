struct stack_list
{
	int val;
	struct stack_list *next;
};
typedef struct stack_list SNODE;

typedef struct
{
	int num_nodes;
	SNODE *next;
}SHEAD;