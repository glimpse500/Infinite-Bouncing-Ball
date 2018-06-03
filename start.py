#Author : SingGu
#Lastest Moddifid Date: 2015/12/28

import sys,random,math,os,getopt,pygame
from pygame.locals import *
from entities import *
from setting import *
from socket import *
from pygame.locals import *
from background import*
from collide_handler import*
                            


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH+SCORE_BOARD_WIDTH,WINDOW_HEIGHT ))
    pygame.display.set_caption('Infinite Bouncing Ball')

    # draw 12*12 squares
    drawLine(screen)

    # create background
    background = Background(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    # create scoreboard
    scoreboard = ScoreBoard((SCORE_BOARD_WIDTH,WINDOW_HEIGHT))
    
    #rand = ((0.1 * (random.randint(5,8))))

    # initial ball at coodrinate (10,10)
    ball = Ball((300,300),(0.47,0),scoreboard)

    # Initialise sprites
    #playersprites = pygame.sprite.RenderPlain((player1, player2))
    ballsprite = pygame.sprite.RenderPlain(ball)
    barriersprite = pygame.sprite.RenderPlain(scoreboard)
    #barriersprite.add(startButton)
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error

    # Initialise clock
    clock = pygame.time.Clock()
    # Event loop

    playing  = True
    while playing:
    # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == QUIT:
                        return
                elif event.type == MOUSEBUTTONDOWN:
                        location = pygame.mouse.get_pos()
                        if scoreboard.rect.collidepoint(location):
                                if scoreboard.pressStart(location):
                                        ball.setSpeed(SPEED)
                                elif scoreboard.pressStop(location):     
                                        ball.setSpeed(0)
                                elif scoreboard.pressLeave(location):
                                        playing = False
                        else:
                                if pygame.mouse.get_pressed()[0]:
                                        barrier = Barrier(location)
                                        if not pygame.sprite.collide_rect(ball,barrier):
                                                barriersprite.add(barrier)
                                elif pygame.mouse.get_pressed()[2]:

                                        repeat_detect(location,barriersprite)
                                        barrier_for_remove = repeat_detect(location,barriersprite)
                                        barriersprite.draw(screen)
                                        barriersprite.remove(barrier_for_remove)
        screen.blit(background, ball.rect, ball.rect)
        if collide_detect(ball,barriersprite):
                scoreboard.collide += 1
        if ball.update():
                scoreboard.collide += 1
        #print scoreboard.collide
        drawLine(screen)         
        #ballsprite.update()
        ballsprite.draw(screen)
        #barriersprite.update()
        barriersprite.draw(screen)
        scoreboard.show(screen)
        pygame.display.flip()
    pygame.quit()
if __name__ == '__main__': main()
