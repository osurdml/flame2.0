__author__ = 'Caleytown'
from Agent import Agent
from abc import ABCMeta, abstractmethod

class TestAgent(Agent):

    def __init__(self):
        someNumber = 0

    def updateScore(self):
        return "updatedScore"

    def consumeFireData(self):
        return "consumedFireData"
