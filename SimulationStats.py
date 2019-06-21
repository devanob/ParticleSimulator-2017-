import pygame

"""[summary]
    Provided User Interface Abstraction Such As Simulator Status And Intructions
"""
class SimulatorUIstate:
    #constructor 
    def __init__(self, screen, font , fontSize, color, x, y):
        pygame.init()
        self.screen = screen
        self.textDict= {}
        self.fontType = pygame.font.Font(font,fontSize)
        self.color = color
        self.fontSize = fontSize
        (self.x, self.y) = (x,y)
        self.hideMeue = False

    #displays U.I message to end user 
    def message_display(self): 
        yPos = self.y
        for property, value in self.textDict.items():
            rendered_text = self.fontType.render("{} : {}".format(property,value), True, (self.color))
            self.screen.blit(rendered_text,(self.x, yPos))
            yPos+=self.fontSize +1 
    #toggles UI
    def toggle(self):
        self.hideMeue = not self.hideMeue
            


        
    #next frame logic
    def nextFrame(self):
        pass
    #draw U.I
    def draw(self):
        if not self.hideMeue:
            self.message_display()
    
