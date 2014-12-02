from abc import ABCMeta, abstractmethod
from Filters import Filters
import math
import copy

class SimpleFovFilter(Filters):
        def __init__(self):
            self.state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.fov = 500
            self.frontierCenter = [80,80]

        def filterData(self, frontierData, hotspotData, myLoc, agentLocationsList):
            agentLocations = copy.deepcopy(agentLocationsList)
            self.state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

            #remove the current agent from all agents list
            numb = 0;
            for x in range(0,len(agentLocations)):
                if (myLoc == agentLocations[x]):
                    numb = x

            agentLocations.pop(numb)

           #return only the closest agent distance
            closestQ1 = 10000
            closestQ2 = 10000
            closestQ3 = 10000
            closestQ4 = 10000

            for x in agentLocations:
                if self.calcDist(myLoc, x) < self.fov:

                    if (myLoc[0] -x[0]) == 0:
                        angle = 0
                    else:
                        angle = math.atan2((myLoc[1] - x[1]), (myLoc[0] - x[0]))
                            #Quad 3
                    if (angle >= 0) and (angle < math.pi/2):
                        self.state[0] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ3):
                            closestQ3 = dist
                            self.state[1] = dist
                            #Quad 4
                    elif (angle >= math.pi/2) and (angle < math.pi):
                        self.state[2] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ4):
                            closestQ4 = dist
                            self.state[3] = dist
                            #quad 1
                    elif (angle > -math.pi) and (angle <= -math.pi/2):
                        self.state[4] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ1):
                            closestQ1 = dist
                            self.state[5] = dist
                    else:
                            #quad 2
                        self.state[6] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ2):
                            closestQ2 = dist
                            self.state[7] = dist


            #return only the closest Hotspot distance
            closestQ1 = 10000
            closestQ2 = 10000
            closestQ3 = 10000
            closestQ4 = 10000

            for x in hotspotData:
                if self.calcDist(myLoc, x) < self.fov:
                    if (myLoc[0] -x[0]) == 0:
                        angle = 0
                    else:
                        angle = math.atan2((myLoc[1] - x[1]), (myLoc[0] - x[0]))
                    #Quad 3
                    if (angle >= 0) and (angle < math.pi/2):
                        self.state[8] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ3):
                            closestQ3 = dist
                            self.state[9] = dist
                    #Quad 4
                    elif (angle > math.pi/2) and (angle < math.pi):
                        self.state[10] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ4):
                            closestQ4 = dist
                            self.state[11] += dist
                    #Quad 1
                    elif (angle > -math.pi) and (angle <= -math.pi/2):
                        self.state[12] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ1):
                            closestQ1 = dist
                            self.state[13] += dist
                    #Quad 2
                    else:
                        self.state[14] += 1
                        dist = self.calcDist(myLoc, x)
                        if (dist < closestQ2):
                            closestQ2 = dist
                            self.state[15] += dist

            self.state[16] = self.calcDist(myLoc, self.frontierCenter)

        def calcDist(self,a, b):
            distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
            return distance

        def getData(self):
            return self.state
