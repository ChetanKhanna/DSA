#include "StackOps.h"
#include <stdio.h>

int main(int argc, char const *argv[])
{
	SHEAD *f;
	f = createStack();
	pushStack(f, "Hello");
	SNODE *r;
	r = popStack(f);
	printf("%s\n", r->val);
	return 0;
}