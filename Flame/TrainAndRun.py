from FrontierController import FrontierController
from FarsiteProducer import FarsiteProducer
from TestScorer import TestScorer
from NeuroSim import NeuroSim
#from Visualizer import Visualizer
import time
import numpy as np
from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection
from pybrain.optimization import GA
import pickle
#from Visualizer import Visualizer
score_plot = []

def evaluator(x):
    nN._setParameters(x)
    neuroSim = NeuroSim(nN,0)
    score = neuroSim.calcScore()
    score_plot.append(score)
    with open('LearningScore.pkl','wb') as output:
        pickle.dump(score_plot,output,pickle.HIGHEST_PROTOCOL)
    print score
    return score

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

populationSize = 100


with open('pop_data_1Agent.pkl','rb') as input:
   initPopulation = pickle.load(input)
#initialPopulation = initPopulation

ga = GA(evaluator,nN.params,maxEvaluations = 100,initRangeScaling = 2,elitism = False,populationSize = populationSize,initialPopulation = initPopulation)
ga.minimize = True
result = ga.learn()
currentPopulation = ga.currentpop

with open('pop_data_1Agent.pkl','wb') as output:
    pickle.dump(currentPopulation,output,pickle.HIGHEST_PROTOCOL)



print "..."
print result
print "..."
nN._setParameters(result[0])
inp = 'y'
while inp == 'y':
    neuroSim1 = NeuroSim(nN,1)
    print neuroSim1.calcScore()
    inp = raw_input('y?')

