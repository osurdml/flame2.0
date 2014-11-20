from Agent import Agent
from abc import ABCMeta, abstractmethod
import numpy as np
import random
class TestAgent(Agent):

    def __init__(self):
        someNumber = 0
        self.x = random.randint(45, 50)
        self.y = random.randint(45, 50)

    def updateScore(self):
        return "updatedScore"

    def consumeFilterData(self, data):
        action = (random.randint(-1,1), random.randint(-1,1))
        self.x = self.x + action[0]
        self.y = self.y + action[1]

    def getLocation(self):
        self.x = int(self.x)
        self.y = int(self.y)
        return (self.x, self.y)
