import heapq
from pythonds.trees.binheap import BinHeap
from queue import PriorityQueue

""" What is a Prioruty Queue and Why to use it:
    http://btechsmartclass.com/DS/U3_T6.html
"""
""" Inspirations:
	https://dbader.org/blog/priority-queues-in-python
	http://interactivepython.org/courselib/static/pythonds/Trees/BinaryHeapOperations.html
"""

## Using usual Lists to implement a Priority Queue ##
## This method is slowest as it takes O(n) for insertion
## and O(n*logn) for sorting

class MaxPQ:
    def __init__(self):
        self.pq = []
        
    def insert(self, val):
        self.pq.append(val)
        
    def _FindMax(self):
        s = sorted(self.pq, reverse = True)
        return s[0]
        
    def remove(self):
        m = self._FindMax()
        self.pq.remove(m)
        return m
        
    def __repr__(self):
        return repr(self.pq)
        
    def __str__(self):
        return "MaxPQ: {}".format(str(self.pq))
## Test Case for MaxPQ ##         
# p = MaxPQ()
# p.insert(3)
# p.insert(4)
# p.insert(1)
# p.insert(10)
# p.insert(2)
# print(p.remove())
# print(p.remove())
# print(p)

## Using PriorityQueue ##
#pq = PriorityQueue({1: "a", 2: "b", 3: "c"})
pq = PriorityQueue()
pq.put((2, 'code'))
pq.put((1, 'sleep'))
pq.put((3, 'eat'))
while not pq.empty():
	print(pq.get())

## Using Binary Heap to implement Priority queue ##
p1 = [(2, "code"), (1, "eat"), (3, "sleep")]
heapq.heapify(p1)
p2 = []
heapq.heappush(p2, (1, "code"))
heapq.heappush(p2, (2, "eat"))
print("p1", p1)
while p1:
	print(heapq.heappop(p1))
print("p2", p2)
while p2:
	print(heapq.heappop(p2))

## Using pythonds module ##
p3 = BinHeap()
p3.insert(1)
p3.insert(2)
p3.insert(4)
print("p3", p3)
print(p3.delMin())
