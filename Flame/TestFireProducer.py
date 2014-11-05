__author__ = 'Caleytown'
from FireProducer import FireProducer
from abc import ABCMeta, abstractmethod

class TestFireProducer(FireProducer):

    def __init__(self):
        someNumber = 0

    def getFireData(self):
        return "fireData"

    def hasData(self):
        return False