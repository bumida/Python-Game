#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import pygame  # 1. pygame 선언
import random

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
RED = (255, 0, 0)

size = [400, 400]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

offs = 30   # 격자 크기
thick = 3   # 선굵기

def drawGrid(m, n):
    '''
    :param m: 격자무늬 행 개수
    :param n: 격자무늬 열 개수
    '''
    x = 0
    y = 0
    for j in range(0, m+2):
        pygame.draw.line(screen, RED, (x, y), (x + n * offs, y), thick)
        y = j * offs
    x = 0
    y = 0
    for i in range(0, n+2):
        pygame.draw.line(screen, RED, (x, y), (x, y + m * offs), thick)
        x = i * offs

# 4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        ############################
        # 여기에 도형을 그리세요
        ############################
        drawGrid(3, 4)
        #drawGrid(2, 5)

        pygame.display.update()

runGame()
pygame.quit()