#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pygame # 1. pygame 선언
import random

pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
size = [400, 400]
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()

sky_img = pygame.image.load('backgrounds/Background.png')
sky = pygame.transform.scale(sky_img, (400, 300))
print(">> sky_img : ", sky_img)

ground_img = pygame.image.load('backgrounds/Ground.png')
ground = pygame.transform.scale(ground_img, (400, 150))

castle_img = pygame.image.load('backgrounds/castle.png')
castle = pygame.transform.scale(castle_img, (200, 150))

heart_img = pygame.image.load('backgrounds/heart.png')
heart = pygame.transform.scale(heart_img, (50, 50))

player_images = ['backgrounds/Player_Attack_R.png',
                 'backgrounds/Player_Attack_L.png']
player_img = pygame.image.load(player_images[0]) # 첫 시작은 R

# 4. pygame 무한루프
def runGame():
    global done
    global player_img
    bounce = False
    
    player_x = 100
    player_y = 250
    to_x = 5
    to_y = -18
    while not done:
        clock.tick(10)
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x -= 10
                    to_x = -5
                    player_img = pygame.image.load(player_images[1])
                elif event.key == pygame.K_RIGHT:
                    player_x += 10
                    to_x = 5
                    player_img = pygame.image.load(player_images[0])
                elif event.key == pygame.K_SPACE and bounce == False: # 점프하고 있으면, 점프 상태 유지
                    bounce = True
                    bounce_count = 0
        
        #sky_rect = sky.get_rect()
        #print(sky_rect)
        
        screen.blit(sky, (0, 0))
        screen.blit(ground, (0, 300))
        screen.blit(castle, (200, 150))
        screen.blit(heart, (0, 0))

        
        ## bounce
        if bounce == True:
            player_x += to_x
            player_y += (to_y + 0.5)
            if player_y <= 200 or player_y >= 250 : # y좌표의 한계치에 다다르면, 방향을 
                if player_y >= 250:
                        player_y = 250 # 조건검사전 연산을 하므로, 땅 아래로 내려갈 수 있으므로 좌표를 재설정해준다.
                to_y = to_y * -1 
                bounce_count += 1
            if player_x <= 0 or player_x >= size[0]: # x좌표의 한계치에 다다르면, 방향을 바꿈
                to_x = to_x * -1    
            
            if bounce_count >= 2:
                bounce = False
            
        player = pygame.transform.scale(player_img, (50, 50)) # 크기
        screen.blit(player, (player_x, player_y)) # 위치

        
        pygame.display.update()

runGame()
pygame.quit()


# In[ ]:




