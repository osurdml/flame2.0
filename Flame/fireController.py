__author__ = 'Caleytown'

class FireController():

    def __init__(self,scorer,fireProducer,fireConsumers):
        self.scorer = scorer
        self.fireProducer = fireProducer
        self.fireConsumers = fireConsumers

    def tick(self):
        fireData = self.fireProducer.getFireData()
        for x in self.fireConsumers:
            x.consumeFireData(fireData)

        self.scorer.calcScore(self.fireConsumers, fireData)


