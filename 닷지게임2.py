#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import math
import pygame
import sys
from pygame.locals import QUIT,Rect, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE

class Total:
    def __init__(self,col,rect,speed = 0): #col:채우는색, rect:그리는 직사각형(위치,크기), speed(이동속도,공만),dir(이동방향, 공만)
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-85, 85) +200

    def move(self):#공을 움직인다 , radians를 사용해서 dir을 라디안으로 변환, X축과Y축의 방향성분구분
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed
    def draw(self):
        pygame.draw.ellipse(SURFACE, self.col, self.rect)

pygame.init()
pygame.display.set_caption("Dodge")
pygame.key.set_repeat(15,15)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
SURFACE = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
FPSCLOCK = pygame.time.Clock()


def main():
    # 게임 진행과 메세지
    game_start = False
    game_over = False

    time = 0
    Small_font = pygame.font.SysFont(None, 40)
    message_start = Small_font.render("Game_Start : Click the SpaceBar", True, (255, 255, 255))


    # player Circle
    C_x = 400
    C_y = 400
    Cir = Total((255, 255, 255), Rect(C_x, C_y, 10, 10))

    # Obstacle
    Ball_x = []
    Ball_y = []
    B_one = []  # i의 반복되는 만큼 1이 저장된다.
    B_point = []  # i가 반복되는 값을 저장한다
    B_velocity = []  # 공 하나당의 속도를 담는다
    for i in range(1,80):
        i *= 10
        B_point.append(i)
        B_one.append(1)
        B_velocity.append(random.randint(2,10))

    while True:
        message_time = Small_font.render("time : %.2f s" %time, True, (255, 255, 255))
        if game_start == True:
            time += 0.035 #시간을 측정 
        if game_over == True:
            game_start = False
        SURFACE.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    Cir.rect.centerx -= 10
                if event.key == K_RIGHT:
                    Cir.rect.centerx += 10
                if event.key == K_UP:
                    Cir.rect.centery -= 10
                if event.key == K_DOWN:
                    Cir.rect.centery += 10
                if event.key == K_SPACE:
                    game_start = True
                    game_over = False
                    time = 0
                    Ball_x = []
                    Ball_y = []

        if game_start == False:
            SURFACE.blit(message_start, (180, 350))
            SURFACE.blit(message_time, (200, 430))
        else:
            Cir.draw()
            if Cir.rect.centerx > 795:
                Cir.rect.centerx = 795
            elif Cir.rect.centerx < 5:
                Cir.rect.centerx = 5
            if Cir.rect.centery > 795:
                Cir.rect.centery = 795
            elif Cir.rect.centery < 5:
                Cir.rect.centery = 5
            for i in range(len(B_point)):
                Ball_x.append(Total((255, 255, 0), Rect(B_point[i], B_one[i], 2, 2),B_velocity[i]))
                Ball_y.append(Total((255, 255, 0), Rect(B_one[i], B_point[i], 2, 2),B_velocity[i]))
                Ball_x[i].draw()
                Ball_y[i].draw()
                if Ball_x[i].rect.centery < 1000:
                    Ball_x[i].move()
                if Ball_y[i].rect.centery < 1000:
                    Ball_y[i].move()

                if Ball_x[i].rect.centery < 0 or Ball_x[i].rect.centery >800:
                    Ball_x[i].dir = - Ball_x[i].dir
                elif Ball_x[i].rect.centerx < 0 or Ball_x[i].rect.centerx >800:
                    Ball_x[i].dir = 180 - Ball_x[i].dir
                if Ball_y[i].rect.centery < 0 or Ball_y[i].rect.centery > 800:
                    Ball_y[i].dir = - Ball_y[i].dir
                elif Ball_y[i].rect.centerx < 0 or Ball_y[i].rect.centerx > 800:
                    Ball_y[i].dir = 180 - Ball_y[i].dir

                if Cir.rect.colliderect(Ball_x[i].rect) or Cir.rect.colliderect(Ball_y[i].rect):
                    game_over = True
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()


# In[ ]:




