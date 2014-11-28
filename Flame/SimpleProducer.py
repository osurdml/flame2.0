from FrontierProducer import FrontierProducer
import numpy as np
from abc import ABCMeta, abstractmethod

class SimpleProducer(FrontierProducer):
    def __init__(self):
        self.hotSpots = []
        self.hotSpots.append([23,100])
      #  self.hotSpots.append([66,80])
      #  self.hotSpots.append([99,50])
      #  self.hotSpots.append([56,10])
      #  self.hotSpots.append([110,50])
      #  self.hotSpots.append([50,130])
      #  self.hotSpots.append([63,90])
        
    def getFrontierData(self, step):
        return self.hotSpots
    
    
    
    def hasData(self): pass