# Author: Matthew Thompson
# Date: 10/25/15
# Implements a Bayesian Network

import networkx as nx
import matplotlib.pyplot as plt

class BN():
	def __init__(self, distributions={}):
		self.graph = nx.DiGraph()
		for key in distributions:
			self.graph.add_node(str(key), distributions[key])

	def addDirectedEdge(self, source, destination):
		self.graph.add_edge(source, destination)

	def setPriorValue(self, node, priorValue):
		self.graph.node[node]['true'] = priorValue
		self.graph.node[node]['false'] = float(1 - priorValue)

	def calculateConditionalProbability(self, variable, conditions):
		

		return

	def calculateJointProbability(self, variables):
		if ('P' in variables and 'S' in variables and 'C' in variables):
			print 'P(P,S,C): ' + str(self.graph.node['C']['tt'] * self.graph.node['P']['true'] * self.graph.node['S']['true'])
			print 'P(P,~S,C): ' + str(self.graph.node['C']['tf'] * self.graph.node['P']['true'] * self.graph.node['S']['false'])
			print 'P(~P,S,C): ' + str(self.graph.node['C']['ft'] * self.graph.node['P']['false'] * self.graph.node['S']['true'])
			print 'P(~P,~S,C): ' + str(self.graph.node['C']['ff'] * self.graph.node['P']['false'] * self.graph.node['S']['false'])
			print 'P(P,S,~C): ' + str((1 - self.graph.node['C']['tt']) * self.graph.node['P']['true'] * self.graph.node['S']['true'])
			print 'P(P,~S,~C): ' + str((1 - self.graph.node['C']['tf']) * self.graph.node['P']['true'] * self.graph.node['S']['false'])
			print 'P(~P,S,~C): ' + str((1 - self.graph.node['C']['ft']) * self.graph.node['P']['false'] * self.graph.node['S']['true'])
			print 'P(~P,~S,~C): ' + str((1 - self.graph.node['C']['ff']) * self.graph.node['P']['false'] * self.graph.node['S']['false'])
		elif ('p' in variables and 's' in variables and 'c' in variables and not '~' in variables):
			print self.graph.node['C']['tt'] * self.graph.node['P']['true'] * self.graph.node['S']['true']
		elif ('~p' in variables and '~s' in variables and '~c' in variables):
			print (1 - self.graph.node['C']['ff']) * self.graph.node['P']['false'] * self.graph.node['S']['false']

		return

	def calculateMarginalProbability(self, variable):
		if (variable == 'P'):
			print 'P(P=low): ' + str(self.graph.node['P']['true'])
		elif (variable == 'S'):
			print 'P(S=true): ' + str(self.graph.node['S']['true'])
		elif (variable == 'C'):
			print 'P(C=true): ' + str((self.graph.node['C']['tt'] * self.graph.node['P']['true'] * self.graph.node['S']['true']) + (self.graph.node['C']['tf'] * self.graph.node['P']['true'] * self.graph.node['S']['false']) + (self.graph.node['C']['ft'] * self.graph.node['P']['false'] * self.graph.node['S']['true']) + (self.graph.node['C']['ff'] * self.graph.node['P']['false'] * self.graph.node['S']['false']))
		elif (variable == 'X'):
			print 'P(X=true): ' + str('')
		elif (variable == 'D'):
			print 'P(D=true): ' + str('')


		return 


	# # Handle cases where the varaible is a root cause node
	# 	if (len(self.graph.predecessors(variable)) == 0):
	# 		if ('X' in variable or 'D' in variable):
	# 			if ('C' in conditions):
	# 				print 'P(' + str(variable) + '|' + str(conditions[0]) + '): ' + str(float(self.graph.node[variable]['true']))
	# 				return float(self.graph.node[variable]['true'])
	# 			elif ('P' in conditions or 'S' in conditions):
	# 				print 'P(' + str(variable) + '|' + str(conditions[0]) + '): ' + 'NEEDS TO BE COMPLETED'
	# 				return 1.0
	# 		if ('C' in variable):
	# 			if ('X' in conditions or 'D' in conditions):
	# 				print 'P(' + str(variable) + '|' + str(conditions[0]) + '): ' + 'NEEDS TO BE COMPLETED'
	# 				return 1.0
	# 			elif ('P' in conditions or 'S' in conditions):
	# 				print 'P(' + str(variable) + '|' + str(conditions[0]) + '): ' + 'NEEDS TO BE COMPLETED'
	# 				return 1.0
	# 		if ('P' in variable or 'S' in variable):
	# 			if ('C' in conditions):
	# 				print 'P(' + str(variable) + '|' + str(conditions[0]) + '): ' + 'NEEDS TO BE COMPLETED'
	# 				return 1.0
	# 			elif ('X' in conditions or 'D' in conditions):
	# 				print 'P(' + str(variable) + '|' + str(conditions[0]) + '): ' + 'NEEDS TO BE COMPLETED'
	# 				return 1.0

	# 	# Handle first-layer nodes
	# 	elif (len(self.graph.predecessors(variable)) == 1):
	# 		if ('P' in conditions and 'S' in conditions):
	# 			print 'P(' + str(variable) + '|' + str(conditions[0]) + ',' + str(conditions[1]) + '): ' + str(float(self.graph.node[variable]['tt']))
	# 			jointVariables = []
	# 			jointVariables.append(variable)
	# 			for condition in conditions:
	# 				jointVariables.append(condition)
	# 			return float(self.calculateJointProbability(jointVariables) / self.calculateJointProbability(conditions))
	# 		elif ('P' in conditions and '~S' in conditions):
	# 			print 'P(' + str(variable) + '|' + str(conditions[0]) + ',' + str(conditions[1]) + '): ' + str(float(self.graph.node[variable]['tf']))
	# 			return float(self.graph.node[variable]['tf'])

	# 	# Handle second-layer nodes
	# 	elif (len(self.graph.predecessors(variable)) == 2):
	# 		return


	# product = 1.0
		# for variable in variables:
		# 	#print 'Self.calculateConditionalProbability: ' + str(self.calculateConditionalProbability(variable, self.graph.predecessors(variable)))
		# 	product *= self.calculateConditionalProbability(variable, self.graph.predecessors(variable))
		# print 'P(' + str(variables[0]) + ',' + str(variables[1]) + '): ' + str(product)
		# return product


