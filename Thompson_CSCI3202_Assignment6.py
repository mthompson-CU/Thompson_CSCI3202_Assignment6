# Author: Matthew Thompson
# 10/25/15
# Assignment 6: Bayesian Networks

import sys
import getopt
import BN

def buildBayesNet():
	distributions = {'P': {'true': 0.9, 'false': 0.1}, 'S': {'true': 0.3, 'false': 0.7}, 'C': {'tt': 0.03, 'tf': 0.001, 'ft': 0.05, 'ff': 0.02}, 'X': {'true': 0.9, 'false': 0.2}, 'D': {'true': 0.65, 'false': 0.30}}
		
	bayesNet = BN.BN(distributions)

	bayesNet.addDirectedEdge('P', 'C')
	bayesNet.addDirectedEdge('S', 'C')
	bayesNet.addDirectedEdge('C', 'X')
	bayesNet.addDirectedEdge('C', 'D')

	return bayesNet

def getOptions(argv, bayesNet):
	# Inspired by Prof. Hoenigman's getoptExample.py
	try:
		opts, args = getopt.getopt(argv[1:], "m:g:j:p:")
	except getopt.GetoptError as err:
		# print help information and exit:
		print str(err) # will print something like "option -a not recognized"
		sys.exit(2)
	for option, arguments in opts:
		if option in ("-p"):
			bayesNet.setPriorValue(arguments[0], float(arguments[1:]))
		elif option in ("-m"):
			print "flag", option
			print "args", arguments
			bayesNet.calculateMarginalProbability(arguments)
		elif option in ("-g"):
			print "flag", option
			print "args", arguments
			p = arguments.find("|")
			bayesNet.calculateConditionalProbability(arguments[:p], arguments[p+1:])
		elif option in ("-j"):
			print "flag", option
			print "args", arguments
			bayesNet.calculateJointProbability(arguments)
		else:
			assert False, "unhandled option"
		
	# ...

def main(argv):
	# Build Bayes Net
	bayesNet = buildBayesNet()

	# Get input
	getOptions(argv, bayesNet)

	return

if __name__ == '__main__':
	main(sys.argv)