import pygame,entities,os,math

from pygame.locals import *
from setting import*

def load_png(name):
        """ Load image and return image object"""
        fullname = os.path.join('data', name)
        try:
                image = pygame.image.load(fullname)
                if image.get_alpha is None:
                        image = image.convert()
                else:
                        image = image.convert_alpha()
        except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
        
        return image, image.get_rect()

class BasicEntity(pygame.sprite.Sprite):
        # location  = ((int)x ,(int)y), which represent the start coordinates of the entity
        # vector = ( (int)angle, (int)velocity), which represent the moving direction of the entity
        # size = ((int)width,(int)height), which represent the intitial size of the entity
        # color = initial color of the entity, balck for default(255,255,255)
        def __init__(self,location = (0,0),vector = (0,0),size = (0,0),color = (255,255,255),isImage = False):
                pygame.sprite.Sprite.__init__(self)
                if not isImage:
                        self.location = location
                        self.vector = vector
                        self.image = pygame.Surface(size)
                        self.rect = self.image.get_rect()
                        self.image.fill(color)
                        self.setLocation(location)
        def update(self):
                pass
        def setLocation(self):
                pass
class Ball(BasicEntity):
        def __init__(self, location, vector,scoreboard):
                #pygame.sprite.Sprite.__init__(self)
                super(Ball,self).__init__(location,vector,isImage = True)
                self.image, self.rect = load_png('ball.png')
                self.scoreboard = scoreboard
                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.vector = vector
                self.prect = self.rect

        def update(self):
                newpos = self.calcnewpos(self.rect,self.vector)
                self.prect = self.rect
                self.rect = newpos
                #print self.prect,self.rect
                (angle,z) = self.vector
                if not self.area.contains(newpos):
                    tl = not self.area.collidepoint(newpos.topleft)
                    tr = not self.area.collidepoint(newpos.topright)
                    bl = not self.area.collidepoint(newpos.bottomleft)
                    br = not self.area.collidepoint(newpos.bottomright)
                    if tr and tl or (br and bl):
                        self.reflectH()
                    if tl and bl:
                        #angle = math.pi - angle
                        if tl or bl:
                            self.reflectV()
                            return True
                if pygame.sprite.collide_rect(self,self.scoreboard):
                    self.reflectV()
                    return True
        def setSpeed(self,speed):
                (angle,z) = self.vector
                self.vector = (angle,speed)
        def calcnewpos(self,rect,vector):
                (angle,z) = vector
                (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
                return rect.move(dx,dy)
        def reflectH(self):
                (angle,z) = self.vector
                self.rect = self.prect
                self.vector = (-angle,z)
        def reflectV(self):
                (angle,z) = self.vector
                self.rect = self.prect
                self.vector = (math.pi - angle,z)
        def reflect(self):
                (angle,z) = self.vector
                self.rect = self.prect
                self.vector = (angle,-z)
                
        '''def towardRight(self):
                (angle,z) = self.vector
                (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
                if dx >0:
                        return True
                return False
        def towardLeft(self):
                (angle,z) = self.vector
                (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
                if dx <0:
                        return True
                return False
        def towardUp(self):
                (angle,z) = self.vector
                (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
                if dy >0:
                        return True
                return False
        def towardDown(self):
                (angle,z) = self.vector
                (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
                if dy <0:
                        return True
                return False'''
class Barrier(BasicEntity):
        def __init__(self,location):
                super(Barrier,self).__init__(location,size = (49,49),color = SCORE_BARRIER_COLOR)
                #screen = pygame.display.get_surface()
        def setLocation(self,location):
                (x,y) = location[0]/BASIC_LENGTH,location[1]/BASIC_LENGTH
                self.rect.move_ip((BASIC_LENGTH*x+1,BASIC_LENGTH*y+1))
class Button(BasicEntity):
        def __init__(self,location,textSeq):
                super(Button,self).__init__(location,size = [75, 30],color = BUTTON_COLOR)
                self.text = textSeq
                self.currentState = 0
                #self.start = True
                #screen = pygame.display.get_surface()
        def setLocation(self,location):
                (self.x,self.y) = location[0],location[1]
                self.rect.move_ip((self.x-2,self.y-2))
                
        def showText(self       ):
                #print self.x,self.y
                screen = pygame.display.get_surface()
                font=pygame.font.Font(None,30)
                scoretext=font.render(self.text[self.currentState],1,TEXT_COLOR)
                screen.blit(scoretext, (self.x, self.y))
        def inState(self,text):
                #print self.start
                if self.text[self.currentState] == text:
                        return True
                return False
        def nextState(self):
                self.currentState+=1
                if self.currentState == len(self.text):
                        self.currentState = 0
        def toState(self,text):
                i = 0
                for t in self.text:
                        if self.text == text:
                                self.currentState = i
                                return
                        i+=1
                return 
