__author__ = 'Caleytown'

fireConsumer = testFireConsumer()
fireConsumer2 = testFireConsumer()
fireProducer = testFireProducer()
scorer = testScorer()

fireController = FireController(scorer,fireProducer,[fireConsumer, fireConsumer2])

while(fireController.hasdata()):
    fireController.tick()

