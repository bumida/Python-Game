#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import math
import pygame
import time
import sys
from pygame.locals import QUIT,Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE

pygame.init()  # 2. pygame 초기화
pygame.display.set_caption("운석 피하기 게임")
# 3. pygame에 사용되는 전역변수
pygame.key.set_repeat(15,15)
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
clock = pygame.time.Clock()

class Enemy:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.angle = random.randint(-85, 85) + 200
        
    def move(self):
        self.rect.centerx += math.cos(math.radians(self.angle)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.angle)) * self.speed
    
    def draw(self):
        pygame.draw.arc(screen, self.col, self.rect)
        
        

def runGame():
    global done
    
    game_start = False
    game_over = False
    Small_font = pygame.font.SysFont(None, 40)
    message_start = Small_font.render("GAMESTART", True, (255, 255, 255))
    time = 0 
    
    
    enemy_x = []
    enemy_y = []
    enemy_one = []
    enemy_point = []
    enemy_speed = []
    
    for i in range(1,80):
        i *= 10
        enemy_point.append(i)
        enemy_one.append(1)
        enemy_speed.append(random.randint(1,10))
        
    while True:
        clock.tick(30)
        print("come")
        message_time = Small_font.render("time : %.2f s" %time, True, (255, 255, 255))
        if game_start == True:
            time += 0.035
        if game_over == True:
            game_start = False
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Cir.rect.centerx -= 10
                if event.key == pygame.K_RIGHT:
                    Cir.rect.centerx += 10
                if event.key == pygame.K_UP:
                    Cir.rect.centery -= 10
                if event.key == pygame.K_DOWN:
                    Cir.rect.centery += 10
                if event.key == pygame.K_SPACE:
                    game_start = True
                    game_over = False
                    time = 0
                    enemy_x = []
                    enemy_y = []
        if game_start == False:
            screen.blit(message_start, (180, 350))
            screen.blit(message_time, (200, 430))
        else:
            
             for i in range(len(enemy_point)):
                enemy_x.append(Enemy((255, 255, 0), Rect(enemy_point[i], enemy_one[i], 2, 2),enemy_speed[i]))
                enemy_y.append(Enemy((255, 255, 0), Rect(enemy_one[i], enemy_point[i], 2, 2),enemy_speed[i]))
                enemy_x[i].draw()
                enemy_y[i].draw()
                if enemy_x[i].rect.centery < 500:
                    enemy_x[i].move()
                if enemy_y[i].rect.centery < 500:
                    enemy_y[i].move()

                if enemy_x[i].rect.centery < 0 or enemy_x[i].rect.centery >500:
                    enemy_x[i].angle = - enemy_x[i].angle
                elif enemy_x[i].rect.centerx < 0 or enemy_x[i].rect.centerx >500:
                    enemy_x[i].angle = 180 - enemy_x[i].angle
                if enemy_y[i].rect.centery < 0 or enemy_y[i].rect.centery > 500:
                    enemy_y[i].angle = - enemy_y[i].angle
                elif enemy_y[i].rect.centerx < 0 or enemy_y[i].rect.centerx > 500:
                    enemy_y[i].angle = 180 - enemy_y[i].angle

                if Cir.rect.colliderect(enemy_x[i].rect) or Cir.rect.colliderect(enemy_y[i].rect):
                    game_over = True
        pygame.display.update()
        

if __name__ == "__main__":
    runGame()            
        


# In[3]:





# In[ ]:




