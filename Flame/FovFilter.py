from abc import ABCMeta, abstractmethod
from Filters import Filters
import math

class FovFilter(Filters):
        def __init__(self):
            self.state = 0
            pass
        def filterData(self, frontierData, hotspotData, myLoc, agentLocations):
           # theta = # zero to 2pi angles
           # r = AgentLoc.z*math.sin(angle) # placeholding
           # self.fov = np.int([AgentLoc.x + math.sin(r*theta)], [AgentLoc.y + math.cos(r*theta)])
           # np.logical_and(FrontierData
           #self.fov.HotspotData = np.logical_and(fov, FrontierData)

            #self.state = dict([nmhsq1], [numhsq2], [nmhsq3], [nmhsq4])
            # return distance and angle to each state variable and 
            #Create object called State with list of everything we want
            pass
        def calcDist(self, a, b):
            distance = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
            return distance

        def getData(self): 
            return self.state
