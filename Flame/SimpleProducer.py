from FrontierProducer import FrontierProducer
import numpy as np
from abc import ABCMeta, abstractmethod
from random import randint

class SimpleProducer(FrontierProducer):
    def __init__(self):
        self.hotSpots = []
        #self.hotSpots.append([23,100])
        #self.hotSpots.append([50,50])
        #self.hotSpots.append([66,80])
        #self.hotSpots.append([99,50])
        #self.hotSpots.append([56,10])
        #self.hotSpots.append([78,50])
        self.hotSpots.append([50,130])
        self.hotSpots.append([63,90])
        self.hotSpots.append([87,5])
        #self.hotSpots.append([111,98])
        
    def getFrontierData(self, step):
        #for x in self.hotSpots:
            #rand = randint(1,4)
            #if(rand == 1):
            #    x[0] += 1
            #elif(rand == 2):
            #    x[0] -= 1
            #elif(rand == 3):
            #    x[1] += 1
            #elif(rand == 4):
            #    x[1] -= 1
            #randNumb = randint(1,40)
            #if(randNumb == 1):
            #    x[0] == randint(1,100)
            #    x[1] == randint(1,100)


        return self.hotSpots
    
    
    
    def hasData(self): pass