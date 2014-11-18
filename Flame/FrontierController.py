class FrontierController():

    def __init__(self, scorer, FrontierProducer, FrontierConsumers):
        self.scorer = scorer
        self.frontierProducer = FrontierProducer
        self.frontierConsumers = FrontierConsumers
        self.step = 0

    def tick(self):
        self.frontierData = self.frontierProducer.GetFrontierData(self.step)
        #apply data filter to find hotspots or any other non agent specific info
        for x in self.frontierConsumers:
            #apply agent specific filter
            x.consumeFrontierData(self.frontierData,self.step) #give agent specific data

        self.scorer.calcScore(self.frontierConsumers, self.frontierData)

        for x in self.frontierConsumers:
            x.updateScore(self.scorer)

        self.step += .01

    def hasData(self):
        return self.frontierProducer.hasData()



