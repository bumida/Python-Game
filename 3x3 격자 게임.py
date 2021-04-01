#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame #파이 게임 모듈 임포트

def is_free_position(grid, column_index, row_index):

    return grid[row_index][column_index] == ' '

def is_winner(grid, mark):
    if (grid[0][0] == mark and grid[0][1] == mark and grid[0][2] == mark) or    (grid[1][0] == mark and grid[1][1] == mark and grid[1][2] == mark) or    (grid[2][0] == mark and grid[2][1] == mark and grid[2][2] == mark) or    (grid[0][0] == mark and grid[1][0] == mark and grid[2][0] == mark) or    (grid[0][1] == mark and grid[1][1] == mark and grid[2][1] == mark) or    (grid[0][2] == mark and grid[1][2] == mark and grid[2][2] == mark) or    (grid[0][0] == mark and grid[1][1] == mark and grid[2][2] == mark) or    (grid[2][0] == mark and grid[1][1] == mark and grid[0][2] == mark):
        return True
    else:
        return False

def is_grid_full(grid):
    if grid[0][0] != ' ' and     grid[0][1] != ' ' and     grid[0][2] != ' ' and     grid[1][0] != ' ' and     grid[1][1] != ' ' and     grid[1][2] != ' ' and     grid[2][0] != ' ' and     grid[2][1] != ' ' and     grid[2][2] != ' ':
        return True
    else:
        return False

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 

#변수

BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont('malgungothic', 72)
CELL_SIZE = 200
COLUMN_COUNT = 3
ROW_COUNT = 3
X_WIN = 1
O_WIN = 2
DRAW = 3
game_over = 0

grid = [[' ', ' ', ' '], 
        [' ', ' ', ' '], 
        [' ', ' ', ' ']]



turn = 0 
while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기

    #변수 업데이트

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
        column_index = event.pos[0] // CELL_SIZE
        row_index = event.pos[1] // CELL_SIZE
        print(column_index, row_index)

        if turn == 0:    
            if is_free_position(grid, column_index, row_index):
                grid[row_index][column_index] = 'X'
              

                if is_winner(grid, 'X'):
                    game_over = X_WIN
                   
               
                elif is_grid_full(grid):
                    game_over = DRAW
                    
               

                turn += 1
                turn %= 2

        elif turn == 1:     
            if is_free_position(grid, column_index, row_index):
                grid[row_index][column_index] = 'O'  
               

                if is_winner(grid, 'O'):
                    game_over = O_WIN 
                    pygame.mixer.music.stop()
                    o_win_sound.play()
                elif is_grid_full(grid):
                    game_over = DRAW
                    pygame.mixer.music.stop()
                    draw_sound.play()

                turn += 1
                turn %= 2

    #화면 그리기

    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            pygame.draw.rect(screen, WHITE, pygame.Rect(column_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            mark = grid[row_index][column_index]
            if mark == 'X':
                X_image = large_font.render('X', True, YELLOW)
                screen.blit(X_image, X_image.get_rect(centerx=column_index * CELL_SIZE  + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2)) 
            elif mark == 'O':
                O_image = large_font.render('O', True, WHITE)
                screen.blit(O_image, O_image.get_rect(centerx=column_index * CELL_SIZE + CELL_SIZE // 2, centery=row_index * CELL_SIZE + CELL_SIZE // 2)) 

    if game_over > 0: 
        if game_over == X_WIN:
            x_win_image = large_font.render('X 승리', True, RED)
            screen.blit(x_win_image, x_win_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
        elif game_over == O_WIN:
            o_win_image = large_font.render('O 승리', True, RED)
            screen.blit(o_win_image, o_win_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
        else:
            draw_image = large_font.render('무승부', True, RED)
            screen.blit(draw_image, draw_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 


# In[ ]:




