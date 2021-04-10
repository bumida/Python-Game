#!/usr/bin/env python
# coding: utf-8

# #  pygame colliderect()

# In[1]:


import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WIHTE = (255, 255, 255)
size = [300, 300]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
sysfont = pygame.font.SysFont('malgungothic', 36)

# 4. pygame 무한루프
def runGame():
    global done
    base_x = 100
    base_y = 100
    x = 0 
    y = 0
    while not done:
        clock.tick(10)
        screen.fill(WIHTE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = -10
                elif event.key == pygame.K_RIGHT: 
                    x = 10
                elif event.key == pygame.K_UP:
                    y = -10
                elif event.key == pygame.K_DOWN:
                    y = 10
            elif event.type == pygame.KEYUP:
                x = 0; y=0
        
        ## 파란색 네모
        rect1 = pygame.draw.rect(screen, (0,0,255), (0, 0, 30, 30)) #<rect(0, 0, 30, 30)>
        
        ## 빨간색 네모
        base_x = base_x + x
        base_y = base_y + y
        rect2 = pygame.draw.rect(screen, (255,0,0), (base_x, base_y, 30, 30)) #<rect(0, 0, 30, 30)>
        
        if rect1.colliderect(rect2) == True:
            print("충돌!!!!!")
            text = sysfont.render("충돌!!!", True, (0, 255, 0))
            screen.blit(text, (200,200))
            
        pygame.display.update()

runGame()
pygame.quit()


# In[3]:


import random
random.randint(0, 10)


# In[ ]:




