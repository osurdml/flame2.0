from FrontierProducer import frontierProducer

class FireController():

    def __init__(self,scorer,fireProducer,fireConsumers):
        self.scorer = scorer
        self.frontierProducer = frontierProducer
        self.frontierConsumers = frontierConsumers

    def tick(self):
        self.frontierData = self.frontierProducer.getFrontierData(step)
        for x in self.fireConsumers:
            x.consumeFireData(frontierData)

        self.scorer.calcScore(self.frontierConsumers, frontierData)

        for x in self.frontierConsumers:
            x.updateScore(self.scorer)

        visualizer.vis()
        step += 1
    def hasData(self):
        return self.frontierProducer.hasData()



