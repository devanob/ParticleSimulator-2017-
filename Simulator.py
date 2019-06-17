import pygame
from ParticleObject import Particle
from ParticleSystem import ParticleSystem
class Simulator: 
    project_name = "Simuator Project"
    #default window height and width
    height = 800
    width = 1440
    #default screen
    screen = None
    ##default to black
    gl_clear_backgorund = (0,0,0)
    #main run loop 
    def setUp(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.project_name)
        self.screen.fill(self.gl_clear_backgorund)
        pygame.display.flip()
        self.partSystem = ParticleSystem(self.screen,self.width,self.height,100)
    def eventloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.nextFrame()
            self.draw()
    def nextFrame(self):
        self.partSystem.nextFrame()
    def draw(self):
        self.screen.fill(self.gl_clear_backgorund)
        self.partSystem.draw()
        pygame.display.flip()
    def run(self):
        # run event loop
        self.setUp();
        self.eventloop()
        




if __name__ == "__main__":
    sim = Simulator()
    sim.run()