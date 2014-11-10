__author__ = 'Caleytown'
__author__ = 'skeel3r' # what is this for?

class FireController():

    def __init__(self,scorer,fireProducer,fireConsumers):
        self.scorer = scorer
        self.frontierProducer = fireProducer
        self.frontierConsumers = frontierConsumers

    def tick(self):
        frontierData = self.frontierProducer.getFireData(tick)
        for x in self.fireConsumers:
            x.consumeFireData(frontierData)

        self.scorer.calcScore(self.frontierConsumers, frontierData)

        for x in self.frontierConsumers:
            x.updateScore(self.scorer)

    def hasData(self):
        return self.frontierProducer.hasData()



