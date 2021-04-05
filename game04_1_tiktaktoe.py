#!/usr/bin/env python
# coding: utf-8
# In[ ]:
import pygame  # 1. pygame 선언
import random

pygame.init()  # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

size = [400, 400]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

#시스템 폰트는 어떤게 있는지...
#for font in pygame.font.get_fonts():
#    print(font)

cellsize = 80

def isPtInRc(pt, rc):   # 마우스 클릭 포인터가 셀 사각영역안에 있는지 판단
    if  pt[0] > rc[0] and \
        pt[1] > rc[1] and \
        pt[0] < rc[2] and \
        pt[1] < rc[3] :
        return True
    return False

# 셀 자료구조...
class Cell(object):
    global cellsizet
    def __init__(self, i, x, y):
        self.idx = i
        self.rect = [x, y, x+cellsize, y+cellsize]      #Cell의 사각영역
        self.mark = ' '     # 'X', 'O', ' '
    def clickInCell(self, x, y, c):
        if isPtInRc((x,y), self.rect):
            if self.mark == ' ':
                print("x={0}, y={1}, c={2}".format(x, y, c))
                self.mark = c
                return True
        return False

cells = []  #셀 배열
index = 0   #셀 인덱스
# 3x3 격자 셀 생
for y in range(0, 3):
    for x in range(0, 3):
        c = Cell(index, x * cellsize, y * cellsize)
        cells.append(c)
        print(c.rect)
        index = index + 1

#시작 / 다시시작 버튼
btn_rc = (100, 100, 300, 300)
btn_img = pygame.image.load('images/start.png')
btn_img = pygame.transform.scale(btn_img, (200, 200))

# Scene 0 : 시작 화면 그리기
def drawScene0():
    font = pygame.font.SysFont("tahomabold", 30)
    font.set_italic(True)
    tx = font.render("TIK TAK TOE", True, BLACK)
    screen.blit(tx, (100, 50))
    screen.blit(btn_img, (btn_rc[0], btn_rc[1]))

# Scene 0 : 게임 화면 그리기
def drawScene2():
    global winner
    s = "winner ==> player({0}) !!!".format(winner)
    font = pygame.font.SysFont("tahomabold", 20)
    tx = font.render(s, True, BLACK)
    screen.blit(tx, (70, 50))
    screen.blit(btn_img, (btn_rc[0], btn_rc[1]))

# Scene 0 : 종 화면 그리기
def drawScene1():
    font_sz = 50
    font = pygame.font.SysFont("Arial", font_sz)
    for c in cells:
        pygame.draw.rect(screen, BLACK, (c.rect[0], c.rect[1], cellsize, cellsize), 1)
        tx = font.render(c.mark, True, BLACK)
        screen.blit(tx, ((c.rect[0]+c.rect[2])/2-font_sz/3, (c.rect[1]+c.rect[3])/2-font_sz/2))

def checkWinner():  #마우스 클릭 시 마다 게임승리조건을 체크하는 함
    """
    기본원리 :
    셀의 개수(9개) 만큼 비트배열(0 or 1)을 만든다.
    자신이 클릭한 수는 1, 상대방 수 및 빈칸은 0으로 놓고,
    """
    # 1st case : player X
    ss = "0b"
    for c in cells:
        b ='0'
        if c.mark == 'X':
            b = '1'
        ss = ss + b
    bb = int(ss, 2)
    """
    아래의 승리조건(8가지) 비트배열과 비트연산을 통해 승리조건에 들어맞는 배열이
    포함되어 있는 지 판
    """
    if bb & 0b111000000 == 0b111000000 or \
        bb & 0b000111000 == 0b000111000 or \
        bb & 0b000000111 == 0b000000111 or \
        bb & 0b100100100 == 0b100100100 or \
        bb & 0b010010010 == 0b010010010 or \
        bb & 0b001001001 == 0b001001001 or \
        bb & 0b100010001 == 0b100010001 or \
        bb & 0b001010100 == 0b001010100:
        return 'X'

    """
    X의 경우와 O의 경우 각각 수
    """

    # 2nd case : player O
    ss = "0b"
    for c in cells:
        b ='0'
        if c.mark == 'O':
            b = '1'
        ss = ss + b
    bb = int(ss, 2)
    if bb & 0b111000000 == 0b111000000 or \
        bb & 0b000111000 == 0b000111000 or \
        bb & 0b000000111 == 0b000000111 or \
        bb & 0b100100100 == 0b100100100 or \
        bb & 0b010010010 == 0b010010010 or \
        bb & 0b001001001 == 0b001001001 or \
        bb & 0b100010001 == 0b100010001 or \
        bb & 0b001010100 == 0b001010100:
        return 'O'

    """
    아직 승리가 결정되지 않았고 더이상 빈칸이 없다면, 무승부인지 확인한다.
    """
    has_blank = False
    for c in cells:
        if c.mark == ' ':
            has_blank = True
            break
    if has_blank == False:
        return 'draw'

    return 'none'

scene = 0
player = 'X'
winner = 'none'

# 4. pygame 무한루프
def runGame():
    global done
    global cells
    global scene
    global player
    global winner

    while not done:
        clock.tick(10)  # 10 frame(100 msec)
        screen.fill(WHITE)
        ############################
        # EVENT
        ############################
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # circle_draw = True
                x = event.pos[0]
                y = event.pos[1]
                if scene == 0:
                    if isPtInRc((x,y), btn_rc):
                        # 시작화면에서 시작 버튼을 누르면 게임화면(scene 1)으로 넘김
                        scene = 1
                elif scene == 2:
                    if isPtInRc((x, y), btn_rc):
                        # 종료화면에서 시작 버튼을 누르면 게임화면(scene 1)으로 넘김
                        # reset !!! ---> restart
                        # 게임을 시작하기 전 필요한 변수들을 초기
                        winner = 'none'
                        for c in cells:
                            c.mark = ' '
                        scene = 1
                else:
                    for c in cells:
                        if c.clickInCell(x, y, player):
                            # 마우스 클릭할 때마다 승리조건을 체크하고...
                            winner = checkWinner()
                            # 플레이어를 교차 시킨다.
                            if winner != "none":
                                scene = 2
                            if player == 'X':
                                player = 'O'
                            else:
                                player = 'X'

        ############################
        # 여기에 도형을 그리세요
        ############################
        if scene == 0:
            drawScene0()
        elif scene == 1:
            drawScene1()
        else:
            drawScene2()

        pygame.display.update()

runGame()
pygame.quit()