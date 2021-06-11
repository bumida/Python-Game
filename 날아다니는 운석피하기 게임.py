#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pygame
from pygame.rect import *
import random
import math
import sys
import time

pygame.init()


# 비행기에 화면 이동을 제한하는 함수
def movePlayer():
    if not GameOver:
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

# 적이 차례대로 나오게 지연하는 함수   
def timeDelay500ms():
    global time_delay_500ms 
    if time_delay_500ms > 5:
        time_delay_500ms = 0
        return True
    
    time_delay_500ms += 1
    return False    
    
    
    
# 화면에서 랜덤한 적 생성 함수           
def makeEnemy():
    if timeDelay500ms():
        idex = random.randint(0, len(enemy_image)-1)
        if enemy[idex].y == -1:
            enemy[idex].x = random.randint(0, SCREEN_WIDTH)
            enemy[idex].y = 0
# 재시작 함수
def restart():
    global restart, GameOver
    GameOver = False
    for i in range(len(enemy_image)):
        enemy[i].y = -1 
    time = 0
    GameOver = False
    
    
def moveEnemy():
    makeEnemy()
    for i in range(len(enemy_image)):
            if enemy[i].y == -1:
                continue
            if not GameOver:
                enemy[i].y += 1
            if enemy[i].y > SCREEN_HEIGHT: 
                enemy[i].y = 0

            screen.blit(enemy_image[i], enemy[i])

# 충돌 함수
def Collision():
    global score, GameOver
    
    if GameOver:
        return
    
    for rec in enemy:
        if rec.y == -1:
            continue
        if rec.top < player.bottom and player.top < rec.bottom and rec.left < player.right         and player.left < rec.right:
            print('충돌')
            GameOver = True
            break

            
# 키의 이벤트를 담는 함수    
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
            if event.key == pygame.K_SPACE:
                restart()    
# 문자 출력 함수
def text():
    global time
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과시간
    print(elapsed_time)
    time += elapsed_time
    font = pygame.font.SysFont(None, 20, True, False)
    # 경과 시간
    if not GameOver:
        screen.blit(font.render(f"Time : {elapsed_time}", True, "green"), (200, 10, 0, 0))
    if GameOver:
        screen.blit(font.render("GAME OVER!!", True, 'red'), (200, 200, 0, 0)) 
        #screen.blit(font.render('RESTART SPACEBAR', True, 'red'), (140, 320, 0, 0))
        #screen.blit(font.render("Time : " + str(int(time)), True, "red"), (200, 150, 0, 0))
    
# 변수 생성
done = True
total_time = 10
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
black = (0, 0, 0)
move = Rect(0, 0, 0, 0)
time_delay_500ms = 0
restart = 0
time = 0
GameOver = False
start_ticks = pygame.time.get_ticks() #시작시간


# 사운드
pygame.mixer.init()
pygame.mixer.music.load('sound/gameStartSound.mp3') #배경 음악
pygame.mixer.music.play(-1) #-1: 무한 반복, 0: 한번

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
enemy_image = [pygame.image.load('img/enemy.png') for i in range(40)]
enemy = [None for i in range(len(enemy_image))]
for i in range(len(enemy_image)):
    enemy_image[i] = pygame.transform.scale(enemy_image[i],(10,10))
    enemy[i] = enemy_image[i].get_rect()
    enemy[i].x = i * 25
    enemy[i].y = -1
clock = pygame.time.Clock()


while done:
    
    screen.fill(black)
    # 키보드
    keyBoard()
    # 사용자
    movePlayer()
    # 운석
    moveEnemy()
    # 폰트
    text()
    # 충돌
    Collision()
    pygame.display.update()  
    clock.tick(100) 
    
    
    # 시간 
    # 시작버튼 만들기
    # 음악


# In[ ]:





# In[ ]:




