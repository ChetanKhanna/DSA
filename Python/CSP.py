## This program was made after watching video from UCB CS 188 course.
## Thanks for the wonderful content.

import graph
from random import shuffle

def BacktrackSearch(graph):  
	return RecursiveBacktrack(dict(), graph)

def RecursiveBacktrack(assignment, graph):
	if goalTest(assignment, graph):
		return assignment

	var = nextUnassignedVar(assignment, graph)
	if not var: ## In case no variable left to assign value
		return assignment
	shuffle(COLORS) ## Increasing variety of colors used to fill map.
	for val in COLORS: ## Picking colors from possible colors
		if checkConsistent(var, val, assignment, graph):
			assignment[var] = val ## Checking consistency before assigning if an
								  ## integral part of CSP
			result = RecursiveBacktrack(assignment, graph)
			if result:
				return result
			del assignment[var] ## Remove wrongly assigned variable and prepare to Backtrack
	return False

def goalTest(assignment, graph):
	if len(assignment) == len(graph.getVertices()): ## Checking if all variables are assigned
		## Writting constraints explicitly
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
	for n in graph.getVertices() - assignment.keys():
		return n

def checkConsistent(var, val, assignment, graph):
	for c in graph.getVertex(var).connection: ## graph.getVertex(var).connection returns list of 
											  ## child nodes of 'Vertex' var. Check graph and vertex classes
		if c in assignment: ## if c not in dict assignment, assignment[c] will raise Error
			if assignment[c] == val:
				return False
	return True


COLORS = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'GREY', 'WHITE'] ## Possible options for coloring map
## Making graph for Australia
G = graph.Graph()
G.addEdge('WA', 'NT', twoWay = True) ## turning twoWay on to ensure no two
G.addEdge('WA', 'SA', twoWay = True) ## adjacent vertices are missed.
G.addEdge('SA', 'NT', twoWay = True)
G.addEdge('SA', 'Q', twoWay = True)
G.addEdge('SA', 'NSW', twoWay = True)
G.addEdge('SA', 'V', twoWay = True)
G.addEdge('Q', 'NT', twoWay = True)
G.addEdge('Q', 'NSW', twoWay = True)
G.addEdge('NSW', 'V', twoWay = True)
G.addVertex('T')

MAP = BacktrackSearch(G)
print(MAP)