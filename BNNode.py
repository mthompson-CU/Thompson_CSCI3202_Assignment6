# Author: Matthew Thompson
# Date: 10/25/15
# Implements a node for use in a Bayesian Network

class BNNode():
	def __init__(self, distribution={}, children=[], parents=[]):
		self.distribution = distribution
		self.children = children
		self.parents = parents
		