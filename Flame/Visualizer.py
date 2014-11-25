import pygame
import numpy as np
import osgeo.gdal

class Visualizer():
    def __init__(self):
        #startups
        toa_file = "ash1_raster.toa"
        self.frontier1 = np.array(osgeo.gdal.Open(toa_file).ReadAsArray())
        pygame.init()
        pygame.display.set_caption("Flame2.0: Fire Simulator")
        self.screen = pygame.display.set_mode(self.frontier1.shape, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def vis(self, frontier, agentLocations):
        # publish state of fire, agents,hotspots, and actions?
        values = (self.frontier1).astype(np.uint32)  #what to display
        values[values == 0] = 0xFFFFFF #background

        # Clear the screen
        self.screen.fill((0,0,0))

        # Blit the fire
        pygame.surfarray.blit_array(self.screen, values)

        # Draw the agents
        for x in agentLocations:
            pygame.draw.circle(self.screen, (0,125,0), (x[0], x[1]), 4)

        pygame.display.flip()
