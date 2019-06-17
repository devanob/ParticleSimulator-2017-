import pygame
from ParticleObject import Particle
import math
import random
import numpy as np


class ParticleSystem:

    def __init__(self,screen,window_width,window_height, particleCount):
        self.window_height = window_height;
        self.window_width = window_width;
        self.screen = screen
        #number of paricles 
        self.particleCount = particleCount
        #empty particle set 
        self.probabSplit = 5
        self.particlesSet = []
        self.ToBeRemoved =[]
        self.ToBeAdded =[]
        for particle in range(self.particleCount):
            size = random.randint(5, 15)
            coords = (random.randint(size, self.window_width ),random.randint(size, self.window_height))
            color = (255,255,255)
            if particle == 5 :
                self.particlesSet.append(Particle(self.screen,size,*coords,*(255,0,0),self.window_width, self.window_height))
            else:
                self.particlesSet.append(Particle(self.screen,size,*coords,*color,self.window_width, self.window_height))
                
                
            
    def nextFrame(self):
        for i in range(self.particleCount):
            self.particlesSet[i].nextFrame()
            for particle in self.particlesSet[i+1:]:
                self.collisionDetection(self.particlesSet[i], particle)
        if len(self.ToBeRemoved) > 0:
             for particle in self.ToBeRemoved:
                 try:
                    self.particlesSet.remove(particle)
                    self.particleCount = self.particleCount -1
                 except:
                     pass
             self.ToBeRemoved = []
        if len(self.ToBeAdded) > 0:
            for particle in self.ToBeAdded:
                self.particlesSet.append(particle)
                self.particleCount = self.particleCount + 1
            self.ToBeAdded = []

        
    def draw(self):
        for particle in self.particlesSet:
            particle.draw()
    def calculateInelasticMomentuem(self,particle1, particle2):
        #Calculate The Velocity Componet Of Each Vector
        part1IntialVel = particle1.speed*np.array([math.cos(particle1.angle), math.sin(particle1.angle)])
        part2IntialVel  = particle2.speed*np.array([math.cos(particle2.angle), math.sin(particle2.angle)])
        #Calculate Find Velocity Of Each Particle 
        massTotal = particle1.mass + particle2.mass
        part1FinalVel = ((particle1.mass - particle2.mass) / massTotal)* part1IntialVel + (2.0 * particle2.mass /(massTotal))*part2IntialVel
        part2FinalVel = ((particle2.mass - particle1.mass) / massTotal)* part2IntialVel + (2.0 * particle1.mass /(massTotal))*part1IntialVel

        (particle1.angle, particle1.speed )= (math.pi / 2.0 - math.atan2(part1FinalVel[0], part1FinalVel[1]),math.hypot(part1FinalVel[0], part1FinalVel[1]))
        (particle2.angle, particle2.speed )= (math.pi / 2.0 - math.atan2(part2FinalVel[0], part2FinalVel[1]),math.hypot(part2FinalVel[0], part2FinalVel[1]))
    
    def calculateElasticMomentuem(self,particle1, particle2,deltaX, deltaY):
        part1IntialVel = particle1.speed*np.array([math.cos(particle1.angle), math.sin(particle1.angle)])
        part2IntialVel  = particle2.speed*np.array([math.cos(particle2.angle), math.sin(particle2.angle)])
        pFinal = (particle1.mass * part1IntialVel + particle2.mass* part2IntialVel) / (particle1.mass + particle2.mass)
        particle = Particle(self.screen, (particle1.size + particle2.size)*0.2, ((particle1.x + particle2.x) / 2.0 ),((particle1.y + particle2.y) / 2.0 ),*(255,255,255),self.window_width,self.window_height)
        (particle1.angle, particle1.speed )= (    math.pi / 2.0 - math.atan2(pFinal[0], pFinal[1]),math.hypot(pFinal[0], pFinal[1]) )
        (particle2.angle, particle2.speed )= (    math.pi / 2.0 - math.atan2(pFinal[0], pFinal[1]),math.hypot(pFinal[0], pFinal[1]) )
        overlap = (particle1.size + particle2.size - math.hypot(deltaX, deltaY)) / 2.0 
        angle = math.atan2(deltaY, deltaX) +  math.pi / 2.0
        particle1.x += math.sin(angle) * overlap
        particle2.y -= math.cos(angle) * overlap
        particle2.x -= math.sin(angle) * overlap
        particle2.y += math.cos(angle) * overlap
        
        

        



    def calculateMomentuem(self, particle1, particle2, deltaX, deltaY):
         angle = math.atan2(deltaY, deltaX) +  math.pi / 2.0
        #  #Particle 1-After Collision
        #  particleOne = vectorAddition(particle1.angle, particle1.speed*(particle1.mass-particle2.mass)/(particle1.mass + particle2.mass),\
        #      angle, 2.0*particle2.speed*particle2.mass/(particle1.mass + particle2.mass))
        #  particleTwo = vectorAddition(particle2.angle, particle2.speed*(particle2.mass-particle1.mass)/(particle1.mass + particle2.mass), \
        #      angle + math.pi, 2.0*particle1.speed*particle1.mass/(particle1.mass + particle2.mass))

        #  (particle1.angle, particle1.speed) = particleOne
        #  (particle2.angle, particle2.speed) = particleTwo
        
         self.calculateInelasticMomentuem(particle1, particle2)
         overlap = (particle1.size + particle2.size - math.hypot(deltaX, deltaY)) / 2.0 
         particle1.x += math.sin(angle) * overlap
         particle2.y -= math.cos(angle) * overlap
         particle2.x -= math.sin(angle) * overlap
         particle2.y += math.cos(angle) * overlap
        

        

    def collisionDetection(self, particle1, particle2):
        deltaX = particle1.x - particle2.x
        deltaY = particle1.y - particle2.y
        delta = math.hypot(deltaX, deltaY)
        if delta < particle1.size + particle2.size:
             angle = math.atan2(deltaX, deltaY) +   math.pi/ 2.0
             if random.uniform(0.0, 100) < self.probabSplit:
                 self.calculateElasticMomentuem(particle1, particle2,deltaX, deltaY)
             else:
                 self.calculateMomentuem(particle1,particle2, deltaX, deltaY)
        else:
            # particle1.colour = (255,255,255)
            # particle2.colour = (255,255,255)
            False
