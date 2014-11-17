from FrontierController import FrontierController
from TestFrontierConsumer import TestFrontierConsumer
from FarsiteProducer import FarsiteProducer
from TestScorer import TestScorer
from NeuroSim import NeuroSim
#from Visualizer import Visualizer
import time
import numpy as np
import neurolab as nl

neuroSim = NeuroSim()

populationSize = 100
NNetList = []
for k in range(0,populationSize):
    NNetList.append(nl.net.newff([[1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10], [1, 10]], [5, 5, 1]))
    neuroSim.calcScore(NNetList[k])

