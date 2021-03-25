#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)
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
isTrue = True
clock = pygame.time.Clock()
# 4. pygame 무한루프

def runGame():
    global done
    radius = 15
    circle_draw = False
    x = 250
    y = 250
    to_y = 10
    to_x = 10
    jump = False
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
     
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y-=10
                elif event.key == pygame.K_DOWN:
                    y+=10
                elif event.key == pygame.K_LEFT:
                    x-=10
                elif event.key == pygame.K_RIGHT:  
                    x+=10     
                if jump == False and event.key == pygame.K_SPACE: 
                    jump = True
                elif jump == True:
                    y -= to_y * 4
                    to_y -= 1
                    if to_y < -10:
                        jump = False
                        to_y = 10
    
                # 스페이바를 꾹누르세요.
                
                if (x <= 0 or x >= size[0])                or (y <=0 or y >= size[1]):
                    sysfont = pygame.font.SysFont("malgungothic", 72)
                    text = sysfont.render("경고!!!", True, (0, 0, 255)) # BLUE = (0, 0, 255) 
                    screen.blit(text, (100,100))
            else:
                
                    
                        screen.blit(sky, (0, 0))
                        screen.blit(heart, (20, 20))
                        screen.blit(castle, (200, 150))
                        screen.blit(player, (int(x), int(y)))
                        screen.blit(ground, (0, 300))
                          
                        pygame.display.update()   
        
        
runGame()
pygame.quit()


# In[ ]:




