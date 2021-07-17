#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done
    radius = 15
    circle_draw = False
    mousepos = []
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                circle_draw = True
                mousepos.append(event.pos)
                print(mousepos)

        ############################
        # 여기에 도형을 그리세요
        ############################
        if circle_draw == True:
            for pos in mousepos:
                pygame.draw.circle(screen, (0,0,255), (pos[0], pos[1]), 5)
        
        pygame.display.update()


runGame()
pygame.quit()


# In[16]:


import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done
    radius = 15
    circle_draw = False
    mousepos = []
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                circle_draw = True
                mousepos.append(event.pos)
                print(mousepos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print('up')
                elif event.key == pygame.K_DOWN:
                    print('down')
                elif event.key == pygame.K_LEFT:
                    print('left')
                elif event.key == pygame.K_RIGHT:
                    print('right')
        ############################
        # 여기에 도형을 그리세요
        ############################
        
        
        pygame.display.update()


runGame()
pygame.quit()


# In[ ]:




