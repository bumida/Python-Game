#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pygame  # 1. pygame 선언
import random
import os

pygame.init()  # 2. pygame 초기화
pygame.display.set_caption("폭탄피하기 완성하기[과제]")
# 3. pygame에 사용되는 전역변수 선언

BLACK = (0, 0, 0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

done = False
clock = pygame.time.Clock()

def runGame():
    bomb_image = pygame.image.load('img/bomb.png')
    bomb_image = pygame.transform.scale(bomb_image, (50, 50))
    bombs = []

    for i in range(5):
        bomb = pygame.Rect(bomb_image.get_rect())
        bomb.left = random.randint(0, SCREEN_WIDTH)
        bomb.top = -100
        dy = random.randint(3, 9)
        bombs.append((bomb, dy))

    person_image = pygame.image.load('img/person.png')
    person_image = pygame.transform.scale(person_image, (100, 100))
    person = pygame.Rect(person_image.get_rect())
    person.left = SCREEN_WIDTH // 2 - person.width // 2
    person.top = SCREEN_HEIGHT - person.height
    person_dx = 0
    person_dy = 0

    global done
    while not done:
        clock.tick(30)
        screen.fill(BLACK)
        print('1')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    person_dx = -5
                elif event.key == pygame.K_RIGHT:
                    person_dx = 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    person_dx = 0
                elif event.key == pygame.K_RIGHT:
                    person_dx = 0

        for (bomb, dy)in bombs:
            bomb.top += dy
            if bomb.top > SCREEN_HEIGHT:
                bombs.remove((bomb, dy))
                bomb = pygame.Rect(bomb_image.get_rect())
                bomb.left = random.randint(0, SCREEN_WIDTH)
                bomb.top = -100
                dy = random.randint(3, 9)
                bombs.append((bomb, dy))
                print(bombs)
        person.left = person.left + person_dx

        if person.left < 0:
            person.left = 0
        elif person.left > SCREEN_WIDTH - person.width:
            person.left = SCREEN_WIDTH - person.width

        screen.blit(person_image, person)

        for (bomb, dy) in bombs:
            if bomb.colliderect(person):
                print("충돌")
                done = True
            screen.blit(bomb_image, bomb)

        pygame.display.update()


runGame()
pygame.quit()


# In[ ]:




