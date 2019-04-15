from random import shuffle
import time
from itertools import permutations

# Defining vetex class of graph
class Vertex:
	
	def __init__(self, key):
		self.id = key
		self.connection = {}

	def __str__(self):
		return str(self.id) + ' connected to: ' + str([x for x in self.connection])

# defining Graph for the problme
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

def goalTest(assignment, graph):
	if len(assignment) == len(graph.getVertices()): ## Checking if all variables are assigned
		## Writting constraints implicitly
		if assignment['WA'] == assignment['NT']:
			return False
		if assignment['WA'] == assignment['SA']:
			return False
		if assignment['SA'] == assignment['NT']:
			return False
		if assignment['SA'] == assignment['Q']:
			return False
		if assignment['SA'] == assignment['NSW']:
			return False
		if assignment['SA'] == assignment['V']:
			return False
		if assignment['Q'] == assignment['NT']:
			return False
		if assignment['Q'] == assignment['NSW']:
			return False
		if assignment['NSW'] == assignment['V']:
			return False
		return True
	return False

def nextUnassignedVar(assignment, graph):
	for n in graph.getVertices() - assignment.keys():	## This gives a list of unassigned vertices
														## by overloading '-' operator
		return n

def checkAssignmentConsistency(var, val, assignment, graph):
	for c in graph.getVertex(var).connection: ## graph.getVertex(var).connection returns list of 
											  ## child nodes of 'Vertex' var. Check graph and vertex classes
		if c in assignment: 				  ## if c not in dict assignment, assignment[c] will raise Error
			if assignment[c] == val:
				return False
	return True

def forwardCheckFiletr(var, assignment, graph):
	'''
	remove the val assinged to var from domain of all 
	neighbours of var 
	'''
	for c in graph.getVertex(var).connection:
		if assignment[var] in graph.domain[c]:
			graph.domain[c].remove(assignment[var])

def filterPass(assignment, graph):
	'''
	if any of the unassigned var has an empty domain (after forwardCheckFilter)
	then the assignment to var is faulty and needs to be backtracked -- return False
	'''
	for n in graph.getVertices() - assignment.keys():
		if not graph.domain[n]:
			return False
	return True

def arcConsistencyFilter(assignment, graph):
	'''
	Check for arc consistency on all arcs in the graph. 
	
	An arc is a pair of nodes having a connection. It is non-reflexive
	in nature and hence (a,b) differs from (b,a).

	if (head, tail) is the arc under consideration then first remove all 
	conflicting values from tail and re-add all pairs of (x, tail) back in the 
	arc list where x is a neighbour of tail. Re-adding is neccessary for consistency.

	A val in tail is considered conflicting if corresponding to it there is no
	val in domain of head.

	arcConsistenctFilter can be called either before assignment as a preprocessor
	or after assignment to detect early backtrack.
	'''

	# make list of all connected pairs in graph
	arcs = list(permutations(graph.domain, 2))
	while arcs:
		head, tail = arcs.pop(0)
		if removeInconsistent(head, tail, graph):
			for x in graph.getVertex(tail).connection:
				arcs.append((x, tail))

def removeInconsistent(head, tail, graph):
	'''
	The only possiblity where corresponding to a val in tail
	there exist no available val in head is when the domain of 
	head comprises only [val] where val is val of tail under considertaion.
	'''
	removed = False
	if head in graph.getVertex(tail).connection:
		for val in graph.domain[tail]:
			if graph.domain[head] == [val]:
				graph.domain[tail].remove(val)
				removed = True
	return removed

def restoreDomain(var, val, graph):
	for c in graph.getVertex(var).connection:
		graph.domain[c].append(val)  ## re-add removed color to domain of neighbours

def BacktrackSearch(graph):  
	return RecursiveBackTrack(dict(), graph)

def RecursiveBackTrack(assignment, graph):

	var = nextUnassignedVar(assignment, graph)

	if goalTest(assignment, graph):
		return assignment

	for val in graph.domain[var]:
		# arcConsistencyFilter(assignment, graph)
		if checkAssignmentConsistency(var, val, assignment, graph):
			arcConsistencyFilter(assignment, graph)
			assignment[var] = val
			forwardCheckFiletr(var, assignment, graph)  ## Filetring added: Forward Check
			
			if not filterPass(assignment, graph):
				## If forward check filters makes domain of an unassigned vertex empty, Fail  
				restoreDomain(var, val, graph)  ## restore affected vertices before deletion
				del assignment[var]
				continue  ## continue to explore remaining colors in current vertex domain; don't return to prev vertex

			saved_domain = graph.domain

			# arcConsistencyFilter(assignment, graph)

			if not filterPass(assignment, graph):  
			## if first forwardCheck passes and this fails
			## then mistake made in forwardCheckFilter assigment, therefore
			## restore domain of graph and then call restoreDomain function
			## to restore domain to the state before assignment
				graph.domain = saved_domain
				restoreDomain(var, val, graph)
				del assignment[var]
				continue

			result = RecursiveBackTrack(assignment, graph)
			if result:
				return result
			restoreDomain(var, assignment[var], graph)  ## restore affected vertices before deletion
			del assignment[var] ## Remove wrongly assigned variable and prepare to Backtrack
	return False

###################################################################################################################

COLORS = ['RED', 'GREEN', 'BLUE'] ## Possible options for coloring map
## Making graph for Australia
G = Graph()
G.addEdge('WA', 'NT', twoWay = True) ## turning twoWay on to ensure no two
G.addEdge('WA', 'SA', twoWay = True) ## adjacent vertices are missed.
G.addEdge('SA', 'NT', twoWay = True)
G.addEdge('SA', 'Q', twoWay = True)
G.addEdge('SA', 'NSW', twoWay = True)
G.addEdge('SA', 'V', twoWay = True)
G.addEdge('Q', 'NT', twoWay = True)
G.addEdge('Q', 'NSW', twoWay = True)
G.addEdge('NSW', 'V', twoWay = True)
# G.addVertex('T')

shuffle(COLORS)
for v in G.getVertices():
	G.domain[v] = []
	for c in COLORS:
		G.domain[v].append(c)



start = time.clock()
MAP = BacktrackSearch(G)
print(MAP)
print(time.clock() - start)