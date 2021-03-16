#!/usr/bin/env python
# coding: utf-8

# # [과제] 신호등 그리기

# In[40]:


import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언

WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        # 원 where = screen, color=(0,0,255), 중심좌표(x,y)=(100,200), radius(반지름)=30
        pygame.draw.circle(screen, (255,0,0), (100, 140), 30)
        pygame.draw.circle(screen, (255,255,0), (100, 200), 30)
        pygame.draw.circle(screen, (0,255,0), (100, 260), 30)
        
        # 도형 where = screen, color=(0, 0, 255), rect = (x,y,width,height), width = 굵기
        pygame.draw.rect(screen, (0, 0, 0), (50, 100, 100, 200), 1)
        
        # 선 where?, color?, (Start x? , start y?), (end x?, end y?), 굵기)
        pygame.draw.line(screen, (0, 0, 0), (100, 300), (100, 400), 1)

        
        pygame.display.update()

runGame()
pygame.quit()


# In[ ]:




