import pygame
import numpy as np
import osgeo.gdal

class Visualizer():
    def __init__(self):
        #startups
        toa_file = "ash1_raster.toa"
        frontier = np.array(osgeo.gdal.Open(toa_file).ReadAsArray())
        pygame.init()
        pygame.display.set_caption("Flame2.0: Fire Simulator")
        self.screen = pygame.display.set_mode(frontier.shape, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def vis(self, frontier):
        # publish state of fire, agents,hotspots, and actions?
        values = (frontier).astype(np.uint32)  #what to display
        values[values == 0] = 0xFFFFFF #background
        image = pygame.Surface(frontier.shape)
        pygame.surfarray.blit_array(image, values)
        
        self.screen.blit(image, (0,0))
        pygame.display.flip()
