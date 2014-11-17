from Scorer import Scorer
from abc import ABCMeta, abstractmethod

class TestScorer(Scorer):

    def __init__(self):
        someNumber = 0


    def calcScore(self,frontierConsumer, frontierData):
        return "calcScore"
