    class BinaryTree():
    def __init__(self, root, left = None, right = None):
        self.root = root
        self.left = left
        self.right = right
        
    def AddLeft(self, val):
        if self.left == None:
            self.left = val
        else:
            new_node = BinaryTree(val)
            new_node.left = self.left
            self.left = new_node
            
    def AddRight(self, val):
        if self.right == None:
            self.right = val
        else:
            new_node = BinaryTree(val)
            new_node.right = self.right
            self.right = new_node
            
    def GetLeftNode(self):
        return self.left
        
    def GetRightNode(self):
        return self.right
    
    def GetRoot(self):
        return self.root
    
    def SetRoot(self, val):
        self.root = val
   
## Depth First Traversal (Recursion) ##
def PreOrder(tree):
    if tree:
        print(tree.root)
        PreOrder(tree.left)
        PreOrder(tree.right)

def PostOrder(tree):
    if tree:
        PostOrder(tree.left)
        PostOrder(tree.right)
        print(tree.GetRoot())
            
def InOrder(tree):
    if tree:
        InOrder(tree.left)
        print(tree.GetRoot())
        InOrder(tree.right)
            
## Breadth First Traversal (Without Recursion)
def BreadthFirstTraveral(tree):
    queue = [tree]
    while len(queue) > 0:
        print(queue[0].GetRoot())
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
def PreOrderStack(tree):
    stack = [tree]
    while len(stack) > 0:
        node = stack.pop()
        print(node.root)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def InOrderStack(tree):
    current = tree
    stack = []
    done = False
    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                print(current.root)
                current = current.right
            else:
                done = True

def PostOrderStack(tree):
    s1 = [tree]
    s2 = []
    while len(s1) > 0:
        node = s1.pop()
        s2.append(node)
        if node.right:
            s1.append(node.right)
        if node.left:
            s1.append(node.left)
    while len(s2) > 0:
        node = s2.pop()
        print(node.root)
   
  
#### TEST CASES ####        
# BT = BinaryTree
# bt = BT(2, BT(6, BT(2), BT(5)), BT(4, None, BT(3)))
# bt.GetRightNode().AddLeft(BT(22))
# print("DFT::PreOrder")
# PreOrder(bt)
# print("\nDFT::PostOrder")
# PostOrder(bt)
# print("\nDFT::InOrder")
# InOrder(bt)
# print("\nBFT")
# BreadthFirstTraveral(bt)
# print("\nPreOrderStack::")
# PreOrderStack(bt)
# print("\nInOrderStack::")
# InOrderStack(bt)
# print("\nPostOrderStack::")
# PostOrderStack(bt)
