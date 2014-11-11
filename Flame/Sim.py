#Frontier simulator 
from FrontierController import FrontierController
from TestFrontierConsumer import TestFrontierConsumer
from FarsiteProducer import FarsiteProducer
from TestScorer import TestScorer
from Visualizer import Visualizer

frontierConsumer = TestFrontierConsumer()
frontierConsumer2 = TestFrontierConsumer()
frontierProducer = FarsiteProducer()
scorer = TestScorer()
i = 0
frontierController = FrontierController(scorer,frontierProducer,[frontierConsumer, frontierConsumer2])
visualizer = Visualizer(frontierController.frontierData)

while(i < 10000): #frontierController.hasData()):
    frontierController.tick()
    visualizer.vis(frontierController.frontierData)
    i = i +1
