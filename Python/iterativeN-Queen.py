from random import randint
import time

class Vertex:
	
	def __init__(self, key):
		self.id = key
		self.connection = {}

	def __str__(self):
		return str(self.id) + ' connected to: ' + str([x for x in self.connection])


class Graph:

	def __init__(self):
		self.vertList = {}
		self.numVertex = 0
		self.domain = {}

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

#############################################################################################################

#### The Idea: since there are N queens and in the NxN board, each queen must be in a different row. The nodes
#### of the graph formed below represents queen in row[i], for eg. node[3] = 6 shows that queen in 3rd row is
#### in the 6th column. Since this is iterative CSP, there is no 'domain'. We randomly assign each var a value
#### and then improve its value based on the heuristic functions defined below.
 
def goalTest(assignment, graph):
	## If all assignments have heuristic value 0, goal is reached
	for var in assignment:
		if minConflictValHeuristic(var, assignment, graph) > 0:
			return False
	return True

def nextConflictedVar(assignment, graph):
	## accessing vertices and returning the first vertex which has conflicted assignment
	for n in graph.getVertices():
		if minConflictValHeuristic(n, assignment, graph) > 0:
			return n

def minConflictValHeuristic(var, assignment, graph):
	## The heuristic value = the number of queens which are in the same column as queen 'var'
	## If no queen is in same row as queen 'var', then assignment is un-conflicted
	H = 0
	for q in graph.getVertices():
		if q!=var and assignment[var] == assignment[q]:
			H += 1
	return H

def minConflictValHeuristicVal(var, assignment, graph):
	## pos contains all possible positions possible for queen 'var', which is in face all columns
	## in NxN board. To get N, we count number of vertices in the graph
	pos = [(i, list(assignment.values()).count(i)) for i in range(len(graph.getVertices()))]
	## We now sort the pos list with second element as key
	## The second element of tuple gives the count of queens located in that column -- an indirect
	## way to compute minConflictHeuristic. We then sort it, and place the queen in the col with min
	## number of queens.
	pos.sort(key = lambda x: x[1])
	## since list is sorted in ascending order, return first element
	return pos[0][0]

def iterativeSearch(assignment, graph):
	while not goalTest(assignment, graph):
		var = nextConflictedVar(assignment, graph)
		print('var selected:', var)
		val = minConflictValHeuristicVal(var, assignment, graph)
		print('val assigned:', val)
		assignment[var] = val
	return assignment

#############################################################################################################

G = Graph()
N = 1000
for i in range(N):
	G.addVertex(i)

assignment = {}
for n in G.getVertices():
	assignment[n] = randint(0,999)
print('initial assignment:', assignment)

startTime = time.clock()
newAssignment = iterativeSearch(assignment, G)
endTime = time.clock()
print('final assignment:', newAssignment)
print('Time taken to assign', N, 'queens:', endTime - startTime)