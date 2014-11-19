from abc import ABCMeta, abstractmethod
from FilterConsumer import FilterConsumer


class TestFilterConsumer(FilterConsumer):

    def __init__(self):
        someNumber = 0

    def updateScore(self, scorer):
        return "updatedScore"

    def consumeFilterData(self, filterData):

        return "frontierData"

