#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame # 1. pygame 선언
import random
import time

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
bug_image = pygame.image.load('img/bug.png')
bug_image = pygame.transform.scale(bug_image, (60, 80))
moving = False
large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) 

rect = (50,60,300,150)
done = False
clock = pygame.time.Clock()

# 4. pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(BLACK)
        bug = pygame.Rect(bug_image.get_rect())
        bugs = []
        for i in range(3):
            bug = pygame.Rect(bug_image.get_rect())
            bug.left = random.randint(0, screen_width)
            bug.top = random.randint(0, screen_height)
            bugx = random.randint(0, 9)
            bugy = random.randint(0, 9)
            bugs.append((bug, bugx, bugy))
            print(bugs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # [X] 종료키가 누르면, 게임 종료
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if bug.collidepoint(event.pos) == True:
                    print("catch")
                    bug = pygame.Rect(bug_image.get_rect())
                else:
                    print("non-catch")
        
        for (bug, bug_x, bug_y) in bugs:
            screen.blit(bug_image, bug)
        pygame.display.update()

runGame()
pygame.quit()


# In[ ]:




