#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pygame
import random
import time

pygame.init() 

BLACK = (0, 0, 0)
screen_width = 200
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height)) 

done = False
clock = pygame.time.Clock() 

def runGame():
    global done

    ## 이미지
    sound_image = pygame.image.load('img/sound_on.png')
    sound_image = pygame.transform.scale(sound_image, (60, 60))
    sound_rect = pygame.Rect(sound_image.get_rect())
    sound_rect.left = (screen_width - 60)/2 
    sound_rect.top = 10

    ## 사운드
    sound = pygame.mixer.Sound( "sound/gameover.wav" )
    is_play = 0

    while not done: 
        clock.tick(30)
        screen.fill(BLACK) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # [X] 종료키가 누르면, 게임 종료
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos[0], event.pos[1])
                if sound_rect.collidepoint(event.pos) == True:
                    is_play = 1
                

        screen.blit(sound_image, sound_rect)

        if is_play == 1:
            print("play....")
            is_play = 0
            sound.play()

        pygame.display.update()

runGame()
pygame.quit()


# In[ ]:




