import pygame
import numpy as np

class Visualizer():
    def __init__(self, frontier):
        #startups
        frontier.shape = np.shape(frontier)
        pygame.init()
        pygame.display.set_caption("Flame2.0: Fire Simulator")
        image = pygame.display.set_mode(frontier.shape, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def vis(self, frontier):
        # publish state of fire, agents,hotspots, and actions?
        print self
        values = (frontier)#what to display
        values[values == 0] = 0xFFFFFFF #background
        image = pygame.Surface(self.frontier.shape)
        pygame.surfarray.blit_array(image, values)

        screen.blit(image, (0,0))
