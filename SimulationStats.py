import pygame

class SimulatorUIstate:

    def __init__(self, screen, font , fontSize, color, x, y):
        pygame.init()
        self.screen = screen
        self.textDict= {}
        self.fontType = pygame.font.Font(font,fontSize)
        self.color = color
        self.fontSize = fontSize
        (self.x, self.y) = (x,y)


    def message_display(self): 
        yPos = self.y
        for property, value in self.textDict.items():
            rendered_text = self.fontType.render("{} : {}".format(property,value), True, (self.color))
            self.screen.blit(rendered_text,(self.x, yPos))
            yPos+=self.fontSize +1 
            


        
        
    def nextFrame(self):
        pass
    def draw(self):
        self.message_display()
    
