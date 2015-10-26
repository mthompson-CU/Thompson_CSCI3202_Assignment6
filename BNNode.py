# Author: Matthew Thompson
# Date: 10/25/15
# Implements a node for use in a Bayesian Network

class BNNode():
	def __init__(self, name, distribution={}):
		self.name = name
		self.distribution = distribution