from Scorer import Scorer
from abc import ABCMeta, abstractmethod

class TestScorer(Scorer):

    def __init__(self):
        someNumber = 0


    def calcScore(self,fireConsumer, fireData):
        return "calcScore"