from pythonds import PriorityQueue
from math import inf

class Vertex:
	
	def __init__(self, key):
		self.id = key
		self.distance = 0
		self.connection = {}
		self.parent = None

	def __str__(self):
		return str(self.id) + ' connected to: ' + str([x for x in self.connection])

	def setDistance(self, distance):
		self.distance = distance

	def getDistance(self):
		return self.distance

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertex = 0

	def __contains__(self, item):
		return item in self.vertList

	def __iter__(self):
		return iter(self.vertList.keys())

	def __setitem__(self, key, value):
		self.addVertex(key)

	def __getitem__(self, key):
		return self.getVertex(key).connection.keys()
		## returning dict.keys() is mandatory for the '-' operation used below
		## since (dict.keys() - set) is valid but (dict - set) is not

	def addVertex(self, vert):
		if vert not in self.vertList:
			newVert = Vertex(vert)
			self.vertList[vert] = newVert
			self.numVertex = self.numVertex + 1

	def addEdge(self, fromVert, toVert, weight = 0, twoWay = False):
		if fromVert not in self.vertList:
			self.addVertex(fromVert)
		if toVert not in self.vertList:
			self.addVertex(toVert)

		self.vertList[fromVert].connection[toVert] = weight

		if twoWay:
			self.vertList[toVert].connection[fromVert] = weight

	def getVertex(self, vertKey):
		if vertKey in self.vertList:
			return self.vertList[vertKey]
		else:
			return None

	def getVertices(self):
	 return self.vertList.keys()

def MinSpaningTree(graph, start_vertex):
	## We will push the entire graph in a Priority Queue
	fringe = PriorityQueue()
	## set distances of each vertex except starting vertex to Inf
	for v in graph.getVertices():
		vert = graph.getVertex(v)
		vert.setDistance(inf)
		vert.setParent(None)
	graph.getVertex(start_vertex).setDistance(0)
	fringe.buildHeap([(graph.getVertex(v).getDistance(), v) 
		for v in graph.getVertices()]) 
	while not fringe.isEmpty():
		node = fringe.delMin()
		## update value of all connected vertices of node
		for x in graph.getVertex(node).connection:
			vert = graph.getVertex(x)
			new_cost = graph.getVertex(node).connection[x]
			if x in fringe and new_cost < vert.getDistance():
				vert.setDistance(new_cost)
				vert.setParent(node)
				fringe.decreaseKey(x, new_cost)

#######################################################
G = Graph()
G.addEdge('A', 'B', weight=2, twoWay=True)
G.addEdge('A', 'C', weight=3, twoWay=True)
G.addEdge('B', 'C', weight=1, twoWay=True)
G.addEdge('B', 'D', weight=1, twoWay=True)
G.addEdge('B', 'E', weight=4, twoWay=True)
G.addEdge('C', 'F', weight=5, twoWay=True)
G.addEdge('D', 'E', weight=1, twoWay=True)
G.addEdge('E', 'F', weight=1, twoWay=True)
G.addEdge('F', 'G', weight=1, twoWay=True)

MinSpaningTree(G, 'A')
for v in G.getVertices():
	print(v, ': ', G.getVertex(v).getParent())
