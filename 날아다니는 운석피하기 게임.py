#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pygame
from pygame.rect import *
import random
import math

pygame.init()


    
def movePlayer():
    player.x += move.x
    player.y += move.y
    if player.x < 0:
        player.x = 0
    if player.x > SCREEN_WIDTH - player.width:
        player.x = SCREEN_WIDTH - player.width
        
    if player.y < 0:
        player.y = 0
    if player.y > SCREEN_HEIGHT - player.height:
        player.y = SCREEN_HEIGHT - player.height
    screen.blit(player_image, player)
    
def moveEnemy():
    enemy.y += random.randint(1, 5)
    enemy.x += random.randint(1, 5)
    if enemy.y > SCREEN_HEIGHT or enemy.x > SCREEN_WIDTH: 
        enemy.y = 0
        enemy.x = 0
    screen.blit(enemy_image, enemy)

    
def keyBoard():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_LEFT:
                move.x = -1
            if event.key == pygame.K_RIGHT:
                move.x = 1
            if event.key == pygame.K_UP:
                move.y = -1
            if event.key == pygame.K_DOWN:
                move.y = 1
# 변수 생성
done = True
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
black = (0, 0, 0)
move = Rect(0, 0, 0, 0)

# 게임 화면
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('운석 피하기 게임')

# player 생성
player_image = pygame.image.load('img/ufo2.png')
player_image = pygame.transform.scale(player_image,(20,30))
player = player_image.get_rect()
player.centerx = (SCREEN_WIDTH/2)
player.centery = (SCREEN_HEIGHT/2)

# 운석 생성
enemy_image = pygame.image.load('img/enemy.png')
enemy_image = pygame.transform.scale(enemy_image,(10,10))
enemy = enemy_image.get_rect()
enemy.centerx = random.randint(1, SCREEN_WIDTH)
enemy.centery = 0
clock = pygame.time.Clock()
while done:
    screen.fill(black)
    keyBoard()
    movePlayer()
    moveEnemy()
    pygame.display.update()  
    clock.tick(100) 
    


# In[ ]:





# In[ ]:




