class Tree():
    def __init__(self, root, children = None):
        self.root = root
        if children:
            self.children = [child for child in children]
        else:
            self.children = []
            
    def AddChild(self, child):
        self.children.append(child)
        
    def GetRoot(self):
        return self.root
        
    def GetChild_index(self, i):
        if i >= len(self.children):
            return None
        else:   
            return self.children[i]
            
def PreOrder(tree):
    if tree:
        print(tree.root)
        for c in tree.children:
            PreOrder(c)

def PostOrder(tree):
    if tree:
        for c in tree.children:
            PostOrder(c)
        print(tree.root)

def BFT(tree):
    queue = [tree]
    while len(queue) > 0:
        print(queue[0].root)
        node = queue.pop(0)
        for c in node.children:
            queue.append(c)
            
def PreOrderStack(tree):
    stack = [tree]
    while len(stack) > 0:
        node = stack.pop()
        print(node.root)
        for c in node.children:
            stack.append(c)  ### or use stack.extend(node.children)
def PostOrderStack(tree):
    stack1 = [tree]
    stack2 = []
    while len(stack1) > 0:
        node = stack1.pop()
        stack2.append(node)
        for c in node.children:
            stack1.append(c)
    while len(stack2) > 0:
        node = stack2.pop()
        print(node.root)

def iterative_DFS(tree):
    from itertools import count
    for depth in range(3):
        p = iterative_DFS_utility(tree, [], depth)
        print(p)


def iterative_DFS_utility(tree, path, depth):
    if depth <= 0:
        path = [tree.root]
    else:
        path = [tree.root]
        for c in tree.children:
            path += iterative_DFS_utility(c, path, depth - 1)
    return path

#### Test Cases ####
# t = Tree(1, [Tree(2, [Tree(5), Tree(6)]), Tree(3, [Tree(7)]), Tree(4, [Tree(8), Tree(9), Tree(10)])])
# print("\nPreOrder::")
# PreOrder(t)
# print("\nPostOrder::")
# PostOrder(t)
# print("\nBFT::")
# BFT(t)
# print("\nPostOrderStack::")
# PostOrderStack(t)
# print("\nPreOrderStack::")
# PreOrderStack(t)
# iterative_DFS(t)
