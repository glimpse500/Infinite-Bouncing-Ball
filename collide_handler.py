#Author SingGu
#Date: 2015/12/25
import pygame
from pygame.locals import*
from entities import*
from setting import*

barrier_remover = pygame.sprite.RenderPlain()


def repeat_detect(location,barriers):
        for barrier in barriers:
                if barrier.rect.collidepoint(location):
                        barrier.image.fill(BACKGROUND_COLOR)
                        return barrier

def collide_detect(b,barriers):
        for barrier in barriers:
                #print b.rect,barrier.rect
                if pygame.sprite.collide_rect(b,barrier) :
                        ct =  barrier.rect.collidepoint(b.rect.midtop)
                        cr =  barrier.rect.collidepoint(b.rect.midright)
                        cb =  barrier.rect.collidepoint(b.rect.midbottom)
                        cl =  barrier.rect.collidepoint(b.rect.midleft)
                        rect = b.rect
                        tl =  barrier.rect.collidepoint(b.rect.topleft)
                        tr =  barrier.rect.collidepoint(b.rect.topright)
                        bl =  barrier.rect.collidepoint(b.rect.bottomleft)
                        br =  barrier.rect.collidepoint(b.rect.bottomright)
                        #print "tb",b.rect.midtop,b.rect.midbottom
                        #print "rl",b.rect.midright,b.rect.midleft
                        if ct or cb:
                                #print "tb",b.rect.midtop,b.rect.midbottom
                                b.reflectH()
                                return True
                        elif cr or cl:
                                #print "rl",b.rect.midright,b.rect.midleft
                                b.reflectV()
                                return True
                        elif tl:
                                p = b.prect.topleft
                                rp1 = barrier.rect.right
                                rp2 = barrier.rect.bottom
                                #print p,rp1,rp2,"1"
                                if p[0]>rp1 and p[1] > rp2:
                                        b.reflect()
                                        return True
                                elif p[0] <rp1 or p[1] > rp2:
                                        b.reflectH()
                                        return True
                                elif p[0] > rp1 or p[1] < rp2:
                                        b.reflectV()
                                        return True
                                
                        elif tr :
                                p = b.prect.topright
                                rp1 = barrier.rect.left
                                rp2 = barrier.rect.bottom
                                #print p,rp1,rp2,"2"
                                if p[0]<rp1 and p[1] > rp2:
                                        b.reflect()
                                        #print "a"
                                        return True
                                elif p[0] < rp1 or p[1] < rp2:
                                        b.reflectV()
                                        #print "b"
                                        return True
                                elif p[0] > rp1 or p[1] > rp2:
                                        b.reflectH()
                                        #print "b"
                                        return True
                                               
                        elif bl :
                                p = b.prect.bottomleft
                                rp1 = barrier.rect.right
                                rp2 = barrier.rect.top
                                #print p,rp1,rp2,"3"
                                if p[0]>rp1 and p[1] < rp2:
                                        b.reflect()
                                        return True
                                elif p[0] < rp1 or p[1] < rp2:
                                        b.reflectH()
                                        return True
                                elif p[0] > rp1 or p[1] > rp2:
                                        b.reflectV()
                                        return True
                        elif br :
                                p = b.prect.bottomright
                                rp1 = barrier.rect.left
                                rp2 = barrier.rect.top
                                #print p,rp1,rp2,"4"
                                if p[0]<rp1 and p[1] < rp2:
                                        b.reflect()
                                        #print "a"
                                        return True
                                elif p[0] < rp1 or p[1] > rp2:
                                        b.reflectV()
                                        return True
                                elif p[0] > rp1 or p[1] < rp2:
                                        b.reflectH()
                                        return  True
        return False
