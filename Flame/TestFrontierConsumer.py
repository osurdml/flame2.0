from abc import ABCMeta, abstractmethod
from FrontierConsumer import FrontierConsumer


class TestFrontierConsumer(FrontierConsumer):

    def __init__(self):
        someNumber = 0

    def updateScore(self, scorer):
        return "updatedScore"

    def consumeFrontierData(self, frontierData):

        return "frontierData"

