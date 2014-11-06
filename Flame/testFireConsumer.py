from abc import ABCMeta, abstractmethod
from FireConsumer import FireConsumer


class TestFireConsumer(FireConsumer):

    def __init__(self):
        someNumber = 0

    def updateScore(self, scorer):
        return "updatedScore"

    def consumeFireData(self, fireData):
        #take an action
        return "fireData"

