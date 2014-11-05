from abc import ABCMeta, abstractmethod
from FireConsumer import FireConsumer


class TestFireConsumer(FireConsumer):

    def __init__(self):
        someNumber = 0

    def updateScore(self):
        return "updatedScore"

    def consumeFireData(self):
        return "fireData"

