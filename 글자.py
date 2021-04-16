#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pygame # 1. pygame 선언
import random
pygame.init() # 2. pygame 초기화
# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
size = [400, 400]

done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        # 파이썬에 여러 이벤트를 가져옴..
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        ############################
        # 여기에 도형을 그리세요
        ############################
        sysfont = pygame.font.SysFont(None, 72)
        text = sysfont.render("Hello world!", True, (0, 0, 255)) # BLUE = (0, 0, 255) 
        screen.blit(text, (0,0))

        pygame.display.update()

runGame()
pygame.quit()


# In[ ]:




