class FrontierController():

    def __init__(self, Scorer, FrontierProducer, FilterConsumers, Filters):
        self.scorer = Scorer
        self.frontierProducer = FrontierProducer
        self.filterConsumers = FilterConsumers
        self.filters = Filters # how to feed back hotspots and/or fov
        self.agentLocations = []
        self.step = 0

    def tick(self,workingNN):
        self.frontierData = self.frontierProducer.getFrontierData(self.step)
        #apply data filter to find hotspots or any other non agent specific info
        self.filters[0].filterData(self.frontierData)
        for x in self.filterConsumers:
            self.agentLocations.append(x.getLocation())
            #print self.agentLocations
        for x in self.filterConsumers:
            #apply agent specific filter
            self.filters[1].filterData(self.frontierData, self.filters[0].getData(), x.getLocation(), self.agentLocations)
            x.setTime(self.step)
            x.consumeFilterData(self.filters[1].getData()) #give agent specific data

        self.scorer.calcScore(self.filterConsumers, self.filters[0].getData(),workingNN)

        for x in self.filterConsumers:
            x.updateScore(self.scorer.getScore())

        self.step += .01

    def hasData(self):
        return self.frontierProducer.hasData()

    def getAgentLocations(self):
        return self.agentLocations
