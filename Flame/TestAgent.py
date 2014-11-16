from Agent import Agent
from abc import ABCMeta, abstractmethod

class TestAgent(Agent):

    def __init__(self):
        someNumber = 0
        self.location = (50, 50)

    def updateScore(self):
        return "updatedScore"

    def consumeFrontierData(self):
        print self.location
        action = (0, 1)
        self.location = self.location + action
        return self.location
