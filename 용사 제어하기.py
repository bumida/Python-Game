#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('/usr/bin/env python')
# coding: utf-8

# In[8]:


import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((400,400))
sky = pygame.image.load('backgrounds/Background.png')
heart = pygame.image.load('backgrounds/heart.png')
castle = pygame.image.load('backgrounds/castle.png')
player = pygame.image.load('backgrounds/Player_Attack_R.png')
ground = pygame.image.load('backgrounds/Ground.png')
sky = pygame.transform.scale(sky, (400, 300))
heart = pygame.transform.scale(heart, (50, 50))
castle = pygame.transform.scale(castle, (200, 150))
player = pygame.transform.scale(player, (50, 50))
ground = pygame.transform.scale(ground, (400, 300))
done = False
clock = pygame.time.Clock()
# 4. pygame 무한루프

def runGame():
    global done
    radius = 5
    x = 250
    y = 250
    jumpCnt = 10
    jump = False
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
     
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x > radius:
                    x -= radius
                if event.key == pygame.K_RIGHT and x < 360 - radius:  
                    x += radius     
                if jump == False and event.key == pygame.K_SPACE: 
                    jump = True
                elif jump == True:
                    y -= jumpCnt * 0.8
                    jumpCnt -= 1
                    if jumpCnt < -10:
                        jump = False
                        jumpCnt = 10
    
                # 스페이바를 꾹누르세요.
                
            else:
                
                    
                        screen.blit(sky, (0, 0))
                        screen.blit(heart, (20, 20))
                        screen.blit(castle, (200, 150))
                        screen.blit(player, (int(x), int(y)))
                        screen.blit(ground, (0, 300))
                          
                        pygame.display.update()   
        
        
runGame()
pygame.quit()





