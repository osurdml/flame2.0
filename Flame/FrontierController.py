class FrontierController():

    def __init__(self, scorer, FrontierProducer, FrontierConsumers):
        self.scorer = scorer
        self.frontierProducer = FrontierProducer
        self.frontierConsumers = FrontierConsumers
        self.step = 0

    def tick(self):
        self.frontierData = self.frontierProducer.GetFrontierData(self.step)
        for x in self.frontierConsumers:
            x.consumeFrontierData(self.frontierData)

        self.scorer.calcScore(self.frontierConsumers, self.frontierData)

        for x in self.frontierConsumers:
            x.updateScore(self.scorer)

        self.step += .01

    def hasData(self):
        return self.frontierProducer.hasData()



