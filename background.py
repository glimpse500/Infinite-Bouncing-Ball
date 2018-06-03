import pygame
from entities import*
from setting import*

class Background(pygame.Surface):
    def __init__(self,size):
        super(Background,self).__init__(size)
    

class Line(pygame.Rect):
    def __init__(self,size):
        super(Line,self).__init__(size)
    

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self,size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.move_ip((WINDOW_WIDTH+1,0))
        self.image.fill(SCORE_BOARD_COLOR)
        self.startButton = Button((700,500),["Start","Stop"])
        self.leaveButton = Button((700,550),["Leave"])
        self.collide = 0
        self.score = 0
        self.render = pygame.sprite.RenderPlain(self.startButton,self.leaveButton)
        self.layerhandlerer = pygame.sprite.LayeredUpdates(self,self.startButton,self.leaveButton)
        self.layerhandlerer.move_to_back(self)
        self.layerhandlerer.move_to_front(self.startButton)
        self.layerhandlerer.move_to_front(self.leaveButton)
    def show(self,screen):
        font=pygame.font.Font(None,30)
        scoretext=font.render("Bounce Times:"+str(self.collide), 1,(255,255,255))
        screen.blit(scoretext, (610, 20))
        self.render.draw(screen)
        self.startButton.showText()
        self.leaveButton.showText()
    def pressStart(self,location):
        if self.startButton.inState("Start") and self.startButton.rect.collidepoint(location):
            self.startButton.nextState()
            return True
        return False
    def pressStop(self,location):
        if self.startButton.inState("Stop") and self.startButton.rect.collidepoint(location):
            self.startButton.nextState()
            return True
        return False
    def pressLeave(self,location):
        if self.leaveButton.inState("Leave")and self.leaveButton.rect.collidepoint(location):
            return True
        return False
def drawLine(background):
    #vertical lines
    i = 0
    while (i <= WINDOW_WIDTH/BASIC_LENGTH):
        pygame.draw.line(background, LINE_COLOR, (i*BASIC_LENGTH,0), (i*BASIC_LENGTH,WINDOW_HEIGHT))
        i+=1
    #horizon lines
    i = 0
    while (i <= WINDOW_HEIGHT/BASIC_LENGTH):
        pygame.draw.line(background, LINE_COLOR, (0,i*BASIC_LENGTH), (WINDOW_WIDTH,i*BASIC_LENGTH))
        i+=1
    
