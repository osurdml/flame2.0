from FireController import FireController
from TestFireConsumer import TestFireConsumer
from TestFireProducer import TestFireProducer
from TestScorer import TestScorer

FrontierConsumer = TestFrontierConsumer()
FrontierConsumer2 = TestFrontierConsumer()
FrontierProducer = TestFrontierProducer()
scorer = TestScorer()

FrontierController = FrontierController(scorer,FrontierProducer,[FrontierConsumer, FrontierConsumer2])

while(FireController.hasData()):
    FrontierController.tick()
    Visualizer.Vis(FrontierController.frontierData,fireConsumer)

