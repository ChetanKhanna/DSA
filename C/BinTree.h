// header file for binary tree data structure

// I planned on using variable Data Type first,
// but that would hinder the purpose of this project
// which is to learn DSA.
// Leaving them for future reference.

/*typedef union{
	int i;
	float f;
	char str[100];
}DATA;*/

struct Binary_Tree{
	/*DATA val;*/
	int val;
	struct Binary_Tree *left;
	struct Binary_Tree *right;
};
typedef struct Binary_Tree NODE;

typedef struct
{
	int count;
	NODE *root;
}ROOT;