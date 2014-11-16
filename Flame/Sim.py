#Frontier simulator 
from FrontierController import FrontierController
from TestAgent import TestAgent
from FarsiteProducer import FarsiteProducer
from TestScorer import TestScorer
from Visualizer import Visualizer
import time

agent1 = TestAgent()
agent2 = TestAgent()
frontierProducer = FarsiteProducer()
scorer = TestScorer()
i = 0
frontierController = FrontierController(scorer,frontierProducer,[agent1, agent2])
visualizer = Visualizer()

while(i < 10000): #frontierController.hasData()):
    frontierController.tick()
    visualizer.vis(frontierController.frontierData)
    i = i +1
