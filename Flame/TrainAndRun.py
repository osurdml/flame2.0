from FrontierController import FrontierController
from FarsiteProducer import FarsiteProducer
from TestScorer import TestScorer
from NeuroSim import NeuroSim
#from Visualizer import Visualizer
import time
import numpy as np
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.optimization import GA
#from Visualizer import Visualizer


def evaluator(x):
    nN._setParameters(x)
    neuroSim = NeuroSim(nN,0)
    print "."
    return neuroSim.calcScore()

populationSize = 100
NNetList = []
nN = FeedForwardNetwork()

inLayer = LinearLayer(18)
hiddenLayer1 = SigmoidLayer(5)
hiddenLayer2 = SigmoidLayer(5)
outLayer = LinearLayer(4)

nN.addInputModule(inLayer)
nN.addModule(hiddenLayer1)
nN.addModule(hiddenLayer2)
nN.addOutputModule(outLayer)

in_to_hidden1 = FullConnection(inLayer,hiddenLayer1)
hidden1_to_hidden2 = FullConnection(hiddenLayer1,hiddenLayer2)
hidden_to_out = FullConnection(hiddenLayer2,outLayer)

nN.addConnection(in_to_hidden1)
nN.addConnection(hidden1_to_hidden2)
nN.addConnection(hidden_to_out)

nN.sortModules()
print nN.params

ga = GA(evaluator,nN.params,maxEvaluations = 10)
result = ga.learn()
what = ga.select()
print "..."
print result
print "..."

neuroSim = NeuroSim(nN,1)
neuroSim.calcScore()