__author__ = 'Caleytown'

from FireController import FireController
from TestFireConsumer import TestFireConsumer
from TestFireProducer import TestFireProducer
from TestScorer import TestScorer

fireConsumer = TestFireConsumer()
fireConsumer2 = TestFireConsumer()
fireProducer = TestFireProducer()
scorer = TestScorer()
display = Displayer()

fireController = FireController(scorer,fireProducer,[fireConsumer, fireConsumer2])

while(fireController.hasData()):
    fireController.tick()
    display.display(scorer,fireProducer,[fireConsumer, fireConsumer2])

