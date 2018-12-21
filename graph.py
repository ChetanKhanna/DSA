from collections import defaultdict

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

	def __contains__(self, item):
		return item in self.vertList

	def __iter__(self):
		return iter(self.vertList.keys())

	def __setitem__(self, key, value):
		self.addVertex(key)

	def __getitem__(self, key):
		return self.getVertex(key).connection.keys()
		## returning dict.keys() is mandatory for the - operation used blow
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


### Test Cases ###

# g = Graph()
# g.addVertex('Manhattan')
# g.addVertex('London')
# g.addVertex('Paris')
# g.addVertex('New York')	

# for x in g:
# 	print(x)
# 	#print(type(x))

# g.addEdge('Manhattan', 'New York', weight = 5, twoWay = True)
# g.addEdge('Paris', 'London', weight = 10)
# g.addEdge('New York', 'London', weight = 6)

# for x in g:
# 	print(g.vertList[x])

def buildGraph(wordfile):
	d = {}
	g = Graph()
	wfile = open(wordfile, 'r')

	for lines in wfile:
		for word in lines.split():
			for i in range(4):
				bucket = word[:i] + '_' + word[i+1:]
				if bucket in d:
					d[bucket].append(word)
				else:
					d[bucket] = [word]

	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1, word2)

	return g

### TEST CASES ###
# G = buildGraph('wordfile')
# print('FOOL' in G)
# print(G.getVertex("FOOL"))
# print(len(G.getVertices()))

def DFStest(graph, start):
	visited, stack = set(), [start]
	while stack:
		node = stack.pop()
		if node not in visited:
			visited.add(node)
			for c in graph[node] - visited:
				# if c not in visited
				stack.append(c)

	return visited

### TEST CASES ###
# G = Graph()
# G.addEdge('A', 'B')
# G.addEdge('A', 'C')
# G.addEdge('B', 'D')
# G.addEdge('B', 'E')
# G.addEdge('C', 'F')
# G.addEdge('E', 'F')

# V = DFStest(G, 'B')
# print(V)

def DFSpathTest(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(node, path) = stack.pop()
		for c in graph[node] - set(path):
			if c == goal:
				yield path + [c]
			else:
				stack.append((c, path + [c]))

### TEST CASES ###
# G = Graph()
# G.addEdge('A', 'B')
# G.addEdge('A', 'C')
# G.addEdge('B', 'D')
# G.addEdge('B', 'E')
# G.addEdge('C', 'F')
# G.addEdge('E', 'F')

# for p in DFSpathTest(G, 'A', 'F'):
# 	print(p)

def BFStest(graph, start):
	visited, queue = list(), [start] ## make visited a set for optimizing
	while  queue:
		node = queue.pop(0)
		if node not in visited:
			visited.append(node)
			for c in graph[node] - visited:
				queue.append(c)

	return visited

### TEST CASES ###
# G = Graph()
# G.addEdge('A', 'B')
# G.addEdge('A', 'C')
# G.addEdge('B', 'D')
# G.addEdge('B', 'E')
# G.addEdge('C', 'F')
# G.addEdge('E', 'F')

# V = BFStest(G, 'B')
# print(V)

def BFSpathTest(graph, start, goal):
	queue = [(start, [start])]
	while queue:
		(node, path) = queue.pop(0)
		for c in graph[node] - set(path):
			if c == goal:
				yield path + [c]
			else:
				queue.append((c, path + [c]))

### TEST CASES ###
# G = Graph()
# G.addEdge('A', 'B')
# G.addEdge('A', 'C')
# G.addEdge('B', 'D')
# G.addEdge('B', 'E')
# G.addEdge('C', 'F')
# G.addEdge('E', 'F')

# for p in BFSpathTest(G, 'A', 'F'):
# 	print(p)

## Shortest path
# print(list(BFS_path_test(G, 'A', 'F'))[0])
##list() unpacks the genrator while [] doesn't unpack it

### TESTING THE WORD LADDER PROBLEM: SHORTEST PATH BETWEEN TWO WORDS ###
# G = buildGraph('wordfile')
# i = 0
# for p in BFSpathTest(G, 'FOIL', 'SAGE'):
# 	print(p)
# 	i += 1
# 	if i >= 1:
# 		break


def uniform_cost_search(graph, start, goal):
	'''
	Originally I thought of implementing the UCS using heapq module
	However, due to some internal working of the heapq where it seems to compare
	data of equal priority, the code gives a run-time error.
	Hoping to find a work around for this in near future; left for reference.
	'''
	pq = [(graph.getVertex(start).connection[x], (start, x)) 
		for x in graph.getVertex(start).connection]
	heapq.heapify(pq)
	
	while pq:
		next_cheapest = heapq.heappop(pq)

		if next_cheapest[1][-1] == goal:
			return next_cheapest
		else:
			heapq.heappush(pq, [(next_cheapest[0] + graph.getVertex(next_cheapest[1][-1]).connection[x],
				(next_cheapest[1] + (x,))) for x in graph.getVertex(next_cheapest[1][-1]).connection])


def uniform_cost_search_2(graph, start, goal):
	pq = PriorityQueue()
	for x in graph.getVertex(start).connection:
		pq.put((graph.getVertex(start).connection[x], (start, x)))
	visited = set()
	while not pq.empty():
		next_cheapest = pq.get()
		if next_cheapest not in visited:
			visited.add(next_cheapest)
		        
			if next_cheapest[1][-1] == goal:
				return next_cheapest
			else:
				for x in graph.getVertex(next_cheapest[1][-1]).connection:
					pq.put((next_cheapest[0]+graph.getVertex(next_cheapest[1][-1]).connection[x],
						(next_cheapest[1]+(x,))))


### TEST-CASES FOR UCS ###	
# g = Graph()
# g.addVertex('Manhattan')
# g.addVertex('London')
# g.addVertex('Paris')
# g.addVertex('New York')	

# g.addEdge('Manhattan', 'New York', weight = 5, twoWay = True)
# g.addEdge('Paris', 'London', weight = 10)
# g.addEdge('London', 'New York', weight = 6)
# g.addEdge('Paris', 'New York', weight = 12)

# p = uniform_cost_search_2(g, 'Paris', 'New York')
# print(p)


def buildChessBoardGraph():
	G = Graph()
	for row in range(1,9):
		for col in range(1,9):
			moves = getPossibleMoves(row, col) 
			vert = posToVertex((row, col))
			nodes = [posToVertex(x) for x in moves]
			for n in nodes:
				G.addEdge(vert, n)

	return G

def getPossibleMoves(row, col):
	moves = set()
	offset = [(row+2, col+1), (row+2, col-1), (row-2, col+1), (row-2, col-1),
				(row+1, col+2), (row+1, col-2), (row-1, col+2), (row-1, col-2)]

	for x in offset:
		if x[0] in range(1,9) and x[1] in range(1,9):
			moves.add(x)

	return moves

def posToVertex(pos):
	return pos[0] + (pos[1]-1)*8
	

### TESTING CHESS-GRAPH ###
# chess_board = buildChessBoardGraph()
# for x in chess_board:
	# print(chess_board.vertList[x])


def DfsChess():
	graph = buildChessBoardGraph()

	tour = DfsChessSolver(graph, [], 1)
	print(tour)
		

def DfsChessSolver(graph, path, start):
	if len(path) + 1 == 64:
		return path + [start]
	if not graph[start] - set(path):
		return False

	for c in graph[start] - set(path):
		tour = DfsChessSolver(graph, path+[start], c)
		if tour:
			return tour
		
### TESTING KNGHT-TOUR SOLVER ###
# DfsChess()  ## The algo doesn't work well for 8x8
			  ## For 5x5 it gave results under 1 min
			  ## But for 8x8, well, I couldn't wait that long ;) 				
	