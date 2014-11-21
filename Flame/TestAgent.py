from Agent import Agent
from abc import ABCMeta, abstractmethod
import numpy as np
import random
class TestAgent(Agent):

    def __init__(self):
        someNumber = 0
        self.x = random.randint(45, 50)
        self.y = random.randint(45, 50)
        self.time = 0

    def updateScore(self, score):
        return "updatedScore"

    def consumeFilterData(self, data):
        self.action = (random.randint(-1,1), random.randint(-1,1))


    def getLocation(self):
        self.x = int(self.x)
        self.y = int(self.y)
        return (self.x, self.y)

    def takeAction(self):
        self.x = self.x + self.action[0]
        self.y = self.y + self.action[1]

    def setTime(self, time):
        self.time = time
