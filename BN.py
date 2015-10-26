# Author: Matthew Thompson
# Date: 10/25/15
# Implements a Bayesian Network

import networkx

class BN():
	def __init__(self):
		self.graph = {}

	def addNode(self, node):
		if(not node in self.graph):
			self.graph[node] = []
			print 'Added node ' + str(node.name) + ' with distribution ' + str(node.distribution)
		else:
			raise BaseException
		return

	def addDirectedEdge(self, source, destination):
		for i in self.graph:
			for j in self.graph:
				if (i.name == source and j.name == destination):
					self.graph[i].append(j)
					print 'Added edge from ' + str(i.name) + ' to ' + str(j.name)

	def setPriorValue(self, node, priorValue):
		for i in self.graph:
			if (i.name == node):
				i.distribution['true'] = priorValue
				i.distribution['false'] = float(1 - priorValue)
				print 'Setting new prior distribution for ' + str(i.name) + ': ' + str(i.distribution)

	def calculateConditionalProbability(self, variable, conditions):
		
