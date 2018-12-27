#include "Queue.h"

extern QHEAD * createQueue();
extern QNODE * popQueue(QHEAD *);
extern void pushQueue(QHEAD *, int);
extern _Bool isEmptyQueue(QHEAD *);