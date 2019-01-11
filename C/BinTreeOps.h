#include "BinTree.h"

// I planned on using variable Data Type first,
// but that would hinder the purpose of this project
// which is to learn DSA.
// Leaving them for future reference.

/*extern ROOT * createBinTree();
extern void setRoot(ROOT *, DATA);
extern DATA getRoot(ROOT *);
extern void setVal(NODE *, DATA);
extern DATA getVal(NODE *);
extern void setLeft(NODE *, DATA);
extern DATA getLeft(NODE *);
extern void setRight(NODE *, DATA);
extern DATA getRight(NODE *);*/

extern ROOT * createBinTree();
extern void setRootVal(ROOT *, int);
extern int getRootVal(ROOT *);
extern void setNodeVal(ROOT *, NODE *, int);
extern int getNodeVal(ROOT *, NODE *);
extern void setLeftNode(ROOT *, NODE *, int);
extern NODE * getLeftNode(ROOT *, NODE *);
extern void setRightNode(ROOT *, NODE *, int);
extern NODE * getRightNode(ROOT *, NODE *);

extern int DFS(ROOT *, NODE *);
extern int BFS(ROOT *, NODE *);
