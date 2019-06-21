import pygame
import math
import random

"""
Paricle Object Represet An Abstraction Of One Particle Object In The Simulation
"""
class Particle:
    #constructor
    def __init__(self, screen, size,x_pos, y_pos, red, blue, green, containerWidth, containerHeight):
        self.x = x_pos
        self.y = y_pos
        self.size = size
        self.colour = (red, blue, green)
        self.screen = screen
        self.speed = random.uniform(2.5, 10)
        self.angle = random.uniform(-math.pi*2, math.pi*2)
        self.width = containerWidth
        self.height = containerHeight
        self.degreeOfFreedom = (math.pi / 180) * 5
        self.mass = 0.34 * size;
    # check if particle hit container or all reflect at opposite angle with a degree of random amount 
    def containerReflection(self):
        if self.x > self.width - self.size:
            self.x = 2.0 * (self.width - self.size) - self.x
            self.angle = - self.angle + random.uniform(-self.degreeOfFreedom , self.degreeOfFreedom)
        elif self.x < self.size:
            self.x = 2.0 * self.size - self.x
            self.angle = - self.angle +random.uniform(-self.degreeOfFreedom , self.degreeOfFreedom)
        if self.y > self.height - self.size:
            self.y = 2.0 * (self.height - self.size) - self.y
            self.angle = - self.angle + random.uniform(-self.degreeOfFreedom , self.degreeOfFreedom) +  math.pi
        elif self.y < self.size:
            self.y = 2.0 * self.size - self.y
            self.angle = math.pi - self.angle + random.uniform(-self.degreeOfFreedom ,self.degreeOfFreedom)
    def gravityFactor(self):
        pass
    #draw next frame
    def nextFrame(self):
        self.x += (math.sin(self.angle) * self.speed)
        self.y += (math.cos(self.angle) * self.speed)
        ##bounce of container 
        self.containerReflection()
    #draw particle
    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.size, 0)

if __name__ == "__main__":
    pass