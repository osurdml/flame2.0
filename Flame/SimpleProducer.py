from FrontierProducer import FrontierProducer
import numpy as np
from abc import ABCMeta, abstractmethod

class SimpleProducer(FrontierProducer):
    def __init__(self):
        self.hotSpots = []
        self.hotSpots.append([5,5])
        self.hotSpots.append([30,5])
        
    def getFrontierData(self, step):
        return self.hotSpots
    
    
    
    def hasData(self): pass