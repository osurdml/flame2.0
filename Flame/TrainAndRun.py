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
scoreHistory = []

def evaluator(x):
    NNetList[workingNN]._setParameters(x)
    neuroSim = NeuroSim(NNetList,workingNN,0)
    #neuroSim = NeuroSim(NNetList,0)
    score = neuroSim.calcScore()
    globalScore =  neuroSim.getGlobalScore()
    print globalScore
    scoreHistory.append(globalScore)
    return score

NNetListParams = []
NNetList = []
numberOfAgents = 3
workingNN = 0

for k in range(0,numberOfAgents):
    NNetList.append(FeedForwardNetwork())

    inLayer = LinearLayer(10)
    hiddenLayer1 = SigmoidLayer(5)
    #hiddenLayer2 = SigmoidLayer(5)
    outLayer = LinearLayer(4)

    NNetList[k].addInputModule(inLayer)
    NNetList[k].addModule(hiddenLayer1)
    #NNetList[k].addModule(hiddenLayer2)
    NNetList[k].addOutputModule(outLayer)

    in_to_hidden1 = FullConnection(inLayer,hiddenLayer1)
    #hidden1_to_hidden2 = FullConnection(hiddenLayer1,hiddenLayer2)
    #hidden_to_out = FullConnection(hiddenLayer2,outLayer)
    hidden_to_out = FullConnection(hiddenLayer1,outLayer)

    NNetList[k].addConnection(in_to_hidden1)
    #NNetList[k].addConnection(hidden1_to_hidden2)
    NNetList[k].addConnection(hidden_to_out)

    NNetList[k].sortModules()


#print nN.params


populationSize = 20


#ga = GA(evaluator,NNetList[0].params,maxEvaluations = 20,initRangeScaling = 2,elitism = False,populationSize = populationSize,mutationProb = 0.80)
#ga.minimize = True
#result = ga.learn()
#NNetListParams = result[0]
#initPopulation = ga.currentpop

#with open('4_state_data_20pop.pkl','wb') as output:
#    pickle.dump(initPopulation,output,pickle.HIGHEST_PROTOCOL)
#

with open('smaller_state_data_20pop.pkl','rb') as input:
   initPopulation = pickle.load(input)
#initialPopulation = initPopulation

popList = []
for x in range(0,numberOfAgents):
    popList.append(initPopulation)

for x in range(0,numberOfAgents):
    weights = initPopulation[0]
    NNetListParams.append(weights)


i = 0
while (i < 50):
    for x in range(0,len(NNetListParams)):
        for k in range(0,len(NNetListParams)):
            NNetList[k]._setParameters(NNetListParams[k])

        workingNN = x
        ga = GA(evaluator,NNetListParams[x],maxEvaluations = 20,initRangeScaling = 2,elitism = False,populationSize = populationSize,initialPopulation = popList[x],mutationProb = 0.1)
        ga.minimize = True
        result = ga.learn()
        NNetListParams[x] = result[0]
        popList[x] = ga.currentpop


    i += 1
    print i




for x in range(0,len(NNetListParams)):
    for k in range(0,len(NNetListParams)):
        NNetList[k]._setParameters(NNetListParams[k])

#with open('12nodeNN-20pop.pkl','wb') as output:
#   pickle.dump(currentPopulation,output,pickle.HIGHEST_PROTOCOL)

file = open("scoreHistory.txt", "w")
count = 1
total = 0
smallest = 1000000000
for x in scoreHistory:
    if(count%40 == 0):
        file.write("%s\n" % smallest)
        smallest = 100000000
        total = 0
    else:
        if(x < smallest):
            smallest = x
    count += 1

file.close()

print "..."
print result
print "..."
inp = 'y'
while inp == 'y':
    neuroSim1 = NeuroSim(NNetList,0,1)
    print neuroSim1.calcScore()
    for x in neuroSim1.agents:
        print x.getLocation()
    print neuroSim1.frontierProducer.getFrontierData(.2)
    inp = raw_input('y?')

