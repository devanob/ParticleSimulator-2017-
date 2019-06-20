import pygame
from ParticleObject import Particle
from ParticleSystem import ParticleSystem
from SimulationStats import SimulatorUIstate

"""[Simulator]
    Controller Class Than Provided Handles And Initiates Chnages To The Simulator
"""
class Simulator:
    def __init__(self, height, width):
        self.project_name = "Simuator ParticleProject"
        #default window height and width
        self.height = height
        self.width = width
        #default screen
        self.screen = None
        ##default to black
        self.gl_clear_backgorund = (0,0,0)
        self.paused = False 
        self.timeStep=False
    #sets the simulator and intiate certain apsect of the simulator
    def setInstructions(self):
        self.status.textDict["Ince/Decr Inelastic Collision"] = "<--Z/z . x/X-->"
        self.status.textDict["Pause Simulation"] = "P/p"
        self.status.textDict["ForwardStep Simulation"] = "(Right Arrow Key)-->"

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.project_name)
        self.screen.fill(self.gl_clear_backgorund)
        pygame.display.flip()
        self.partSystem = ParticleSystem(self.screen,self.width,self.height,10)
        self.status = SimulatorUIstate(self.screen,pygame.font.get_default_font(),16,(255,0,0),0,0)
        #sets the simulator to Running
        self.status.textDict["Game State"] = "Running"
        self.setInstructions()
    # event loop for the simulator 
    #register and execute logic based on user events
    def eventloop(self):
        #set the simulator intial run 
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.eventHandlier(event)
              
                
            self.nextFrame()
            self.draw()
    # changes internel Simulator logic provide the next frame for the simulator
    def nextFrame(self):
        # run the simulator either if the user is forwarding the simulator 
        if not self.paused or self.timeStep:
            self.partSystem.nextFrame()
        if self.partSystem.stateChange:
            #check of the state of the Particle System Has Chaned
            self.updateUi()
    def draw(self):
        #Draw The Previosuly Made Frame
        self.screen.fill(self.gl_clear_backgorund)
        self.partSystem.draw()
        self.status.draw()
        pygame.display.flip()
    #runs the Simulator
    def run(self):
        # run event loop

        self.setUp();
        self.eventloop()
    def updateUi(self):
        self.status.textDict["Particle Count"] = self.partSystem.particleCount
        self.status.textDict["Probability Elastic Collsion"] = self.partSystem.probabMerge
        self.partSystem.stateChange = False
    def eventHandlier(self,event):
          if event.type == pygame.QUIT:
                    self.running = False
          if event.type ==pygame.MOUSEBUTTONUP:
              self.partSystem.addParticle(*event.pos)
          if event.type == pygame.KEYDOWN:
              if (event.key ==pygame.K_p):
                  self.paused = not self.paused
                  if self.paused:
                      self.status.textDict["Game State"] = "Paused"
                  else:
                      self.status.textDict["Game State"] = "Running"
              elif (event.key ==pygame.K_x):
                  self.partSystem.increaseElasticCollision(True)
              elif (event.key ==pygame.K_z):
                  self.partSystem.increaseElasticCollision(False)
              elif (event.key ==pygame.K_s):
                  self.partSystem.increaseKineticEnergy()
              elif(event.key == pygame.K_RIGHT):
                  self.timeStep = True;
          if event.type == pygame.KEYUP:
              if event.key == pygame.K_RIGHT:
                  self.timeStep = False

          


        



import sys
if __name__ == "__main__":
    print(sys.argv)
    WindowHeight = 500
    WindowWidth = 500
    try:
        if len(sys.argv) > 1 :
            width = int(sys.argv[1])
            height = int(sys.argv[2])
        if width > 1:
            WindowWidth = width
        if height > 1:
            WindowHeight = height
    except:
        pass

    sim = Simulator(WindowWidth,WindowHeight)
    sim.run()