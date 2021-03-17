#!/usr/bin/env python
# coding: utf-8

# # [과제]격자 무늬 그리기 민경범

# In[39]:



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

def grid(num1, num2):
    global done
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
        
            if num1 == 3 and num2 == 4:
              for i in range(0, 4):
                for j in range(0, 5):
                    #가로줄
                    pygame.draw.line(screen, (255, 0, 0), (0, i*20), (80, i*20), 3)
                    #세로줄
                    pygame.draw.line(screen, (255, 0, 0), (j*20, 0), (j*20, 60), 3)
                    pygame.display.update()
                
            elif num1 == 2 and num2 == 5:
              for i in range(0, 3):
                for j in range(0, 6):
                    #가로줄
                    pygame.draw.line(screen, (255, 0, 0), (0, i*20), (100, i*20), 3)
                    #세로줄
                    pygame.draw.line(screen, (255, 0, 0), (j*20, 0), (j*20, 40), 3)
                    pygame.display.update()
            else:
                print('다시입력해주세요')

grid(2,5)
pygame.quit()


# In[ ]:





# In[ ]:




