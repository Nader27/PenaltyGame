import pygame, sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((450,380),0,32)

background=pygame.image.load("bg.jpg").convert()
background2=pygame.image.load("bge.jpg").convert()
ball=pygame.image.load("ball.png").convert_alpha()
player_stand=pygame.image.load("player.png").convert_alpha()
player_shoot=pygame.image.load("playerShot.png").convert_alpha()
k_up=pygame.image.load("up.png").convert_alpha()
k_right=pygame.image.load("left.png").convert_alpha()
k_left=pygame.image.load("right.png").convert_alpha()
goal=pygame.image.load("goal.jpg").convert()
bad_luck=pygame.image.load("bad_luck.jpg").convert()
n_0=pygame.image.load("numbers/0.png").convert_alpha()
n_1=pygame.image.load("numbers/1.png").convert_alpha()
n_2=pygame.image.load("numbers/2.png").convert_alpha()
n_3=pygame.image.load("numbers/3.png").convert_alpha()
n_4=pygame.image.load("numbers/4.png").convert_alpha()
n_5=pygame.image.load("numbers/5.png").convert_alpha()
n_6=pygame.image.load("numbers/6.png").convert_alpha()
n_7=pygame.image.load("numbers/7.png").convert_alpha()
n_8=pygame.image.load("numbers/8.png").convert_alpha()
n_9=pygame.image.load("numbers/9.png").convert_alpha()
you_win=pygame.image.load("you-win.jpg").convert()
you_lose=pygame.image.load("you-lose.jpg").convert()
clock=pygame.time.Clock()
m = 0
win = 0
lose = 0
temp = 0 
while True:
    xg=0
    ok = 1
    if win == 10:
        win = 0
        lose = 0
        screen.blit(you_win,(0,0))
        pygame.display.update()
        pygame.time.delay(2000)
    if lose == 10:
        win = 0
        lose = 0
        screen.blit(you_lose,(0,0))
        pygame.display.update()
        pygame.time.delay(2000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if event.type == KEYDOWN:
        screen.blit(background2,(0,0))
        screen.blit(player_shoot,(0,80))

        mil=clock.tick()
        m = mil % 3
        if m == 0:
            screen.blit(k_up,(190,100))
        if m == 2:
            screen.blit(k_left,(260,100))
        if m == 1:
            screen.blit(k_right,(70,100))
        if event.key == K_LEFT:
            screen.blit(ball,(100,120))
            n=1
        if event.key == K_RIGHT:
            screen.blit(ball,(300,120))
            n=2
        if event.key == K_DOWN:
            screen.blit(ball,(190,180))
            n=0
        if event.key == K_UP:
            screen.blit(ball,(190,120))
            n=0
        pygame.display.update()
        pygame.time.delay(1000)
        if m == n:
            lose+=1
            while xg < 380 :
                pygame.time.delay(5)
                xg+=2
                screen.blit(background2,(0,0))
                screen.blit(bad_luck,(xg,200))
                pygame.display.update()
        if m != n:
            win+=1
            while xg < 380 :
                pygame.time.delay(5)
                xg+=2
                screen.blit(background2,(0,0))
                screen.blit(goal,(xg,200))
                pygame.display.update()
        
    screen.blit(background,(0,0))
    while ok != 5 :
        if win <= 9:
            if ok == 1:
                x = win
                screen.blit(n_0,(20,20))
                y = 40
        elif win > 9:
            if ok == 1:
                x = win/10
                temp = win%10
                y = 20
            elif ok == 2:
                x = temp
                y = 40
        if lose <= 9:
            if ok == 3:
                x = lose
                screen.blit(n_0,(340,20))
                y = 360
        elif lose > 9:
            if ok == 3:
                x = lose/10
                temp = lose%10
                y = 340
            elif ok == 4:
                x = temp
                y = 360

        if x == 0:
            screen.blit(n_0,(y,20))
        if x == 1:
            screen.blit(n_1,(y,20))
        if x == 2:
            screen.blit(n_2,(y,20))
        if x == 3:
            screen.blit(n_3,(y,20))
        if x == 4:
            screen.blit(n_4,(y,20))
        if x == 5:
            screen.blit(n_5,(y,20))
        if x == 6:
            screen.blit(n_6,(y,20))
        if x == 7:
            screen.blit(n_7,(y,20))
        if x == 8:
            screen.blit(n_8,(y,20))
        if x == 9:
            screen.blit(n_9,(y,20))
        ok+=1
  
    screen.blit(player_stand,(30,130))
    screen.blit(k_up,(190,130))

    pygame.display.update()
