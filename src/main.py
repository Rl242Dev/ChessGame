import pygame
from pawns import *
from board import board
from time import sleep
from pieces import Pieces

def setup_game(StringFEN):
    pygame.init()

    icon = pygame.image.load(Pieces.BishopClass.spriteBlack)
    pygame.display.set_icon(icon)
    screen_width, screen_height = 640, 640
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("Chess Board")

    square_width, square_height = 80, 80
    light_color = pygame.Color(240, 217, 181)
    dark_color = pygame.Color(181, 136, 99)

    row_counter = 0
    #Generate the board
    for row in range(8):
        column_counter = 0
        for column in range(8):
            if (row_counter + column_counter) % 2 == 0:
                pygame.draw.rect(screen, light_color, (column * square_width, row * square_height, square_width, square_height))
            else:
                pygame.draw.rect(screen, dark_color, (column * square_width, row * square_height, square_width, square_height))
            column_counter += 1
        row_counter += 1

    #Place the pieces
    pos = 80
    columnPOS = 0
    pW = 1
    rW = 1
    bW = 1
    nW = 1

    pB = 1
    rB = 1
    bB = 1
    kB = 1
    for i in range(len(StringFEN)):
        size = (80,80)
        if i > 17: #Black else White   
            if StringFEN[i] == 'p':
                image = pygame.image.load(Pieces.PawnClass.spriteWhite)   
                image = pygame.transform.scale(image, size)
                if pW in (1,2,3,4,5,6,7,8):
                    if pW == 1:
                        WhitePawn1('White', image.get_rect())
                    elif pW == 2:
                        WhitePawn2('White', image.get_rect())
                    elif pW == 3:
                        WhitePawn3('White', image.get_rect())
                    elif pW == 4:
                        WhitePawn4('White', image.get_rect())
                    elif pW == 5:
                        WhitePawn5('White', image.get_rect())
                    elif pW == 6:
                        WhitePawn6('White', image.get_rect())
                    elif pW == 7:
                        WhitePawn7('White', image.get_rect())
                    elif pW == 8:
                        WhitePawn8('White', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                pW = pW + 1    
            elif StringFEN[i] == 'r':
                image = pygame.image.load(Pieces.RookClass.spriteWhite)   
                image = pygame.transform.scale(image, size)
                if rW in (1,2):
                    if rW == 1:
                        WhiteRook1('White', image.get_rect())
                    elif rW == 2:
                        WhiteRook2('White', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                rW = rW + 1
            elif StringFEN[i] == 'n': #Knight uses n because the king uses k
                image = pygame.image.load(Pieces.KnightClass.spriteWhite)   
                image = pygame.transform.scale(image, size)
                if nW in (1,2):
                    if nW == 1:
                        WhiteKnight1('White', image.get_rect())
                    elif nW == 2:
                        WhiteKnight2('White', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                nW = nW + 1
            elif StringFEN[i] == 'b':
                image = pygame.image.load(Pieces.BishopClass.spriteWhite)
                image = pygame.transform.scale(image, size)
                if bW in (1,2):
                    if bW == 1:
                        WhiteBishop1('White', image.get_rect())
                    elif bW == 2:
                        WhiteBishop2('White', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                bW = bW + 1
            elif StringFEN[i] == 'q':
                image = pygame.image.load(Pieces.QueenClass.spriteWhite)
                image = pygame.transform.scale(image, size)
                if i == 1:
                    rect = image.get_rect()
                    rect.x = 0
                    rect.y = columnPOS
                    screen.blit(image, rect)
                    global Wq
                    Wq = WhiteQueen('White', rect)
                else:
                    rect = image.get_rect()
                    rect.x = pos
                    rect.y = columnPOS
                    screen.blit(image, rect)
                    Wq = WhiteQueen('White', rect)
            elif StringFEN[i] == 'k':
                image = pygame.image.load(Pieces.KingClass.spriteWhite)
                image = pygame.transform.scale(image, size)
                if i == 1:
                    rect = image.get_rect()
                    rect.x = 0
                    rect.y = columnPOS
                    screen.blit(image, rect)
                    global Wk
                    Wk = WhiteKing('White', rect)
                else:
                    rect = image.get_rect()
                    rect.x = pos
                    rect.y = columnPOS
                    screen.blit(image, rect)
                    Wk = WhiteKing('White', rect)
            elif StringFEN[i] in ('1', '2', '3', '4', '5', '6', '7'):
                if StringFEN[i] == '1':
                    pos = pos + 80
                elif StringFEN[i] == '2':
                    pos = pos + 160
                elif StringFEN[i] == '3':
                    pos = pos + 240
                elif StringFEN[i] == '4':
                    pos = pos + 320
                elif StringFEN[i] == '5':
                    pos = pos + 400
                elif StringFEN[i] == '6':
                    pos = pos + 480
                elif StringFEN[i] == '7':
                    pos = pos + 560
            elif StringFEN[i] == '/':
                if columnPOS == 0:
                    columnPOS = 80
                    pos = -80
                else:
                    columnPOS = columnPOS + 80
                    pos = -80
            if i == 1:
                pos = pos
            else:
                pos = pos + 80
        else:
            if StringFEN[i] == 'p':
                image = pygame.image.load(Pieces.PawnClass.spriteBlack)   
                image = pygame.transform.scale(image, size)
                if pB in (1,2,3,4,5,6,7,8):
                    if pB == 1:
                        BlackPawn1('Black', image.get_rect())
                    elif pB == 2:
                        BlackPawn2('Black', image.get_rect())
                    elif pB == 3:
                        BlackPawn3('Black', image.get_rect())
                    elif pB == 4:
                        BlackPawn4('Black', image.get_rect())
                    elif pB == 5:
                        BlackPawn5('Black', image.get_rect())
                    elif pB == 6:
                        BlackPawn6('Black', image.get_rect())
                    elif pB == 7:
                        BlackPawn7('Black', image.get_rect())
                    elif pB == 8:
                        BlackPawn8('Black', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                pB = pB + 1
            elif StringFEN[i] == 'r':
                image = pygame.image.load(Pieces.RookClass.spriteBlack)   
                image = pygame.transform.scale(image, size)
                if rB in (1,2):
                    if rB == 1:
                        BlackRook1('Black', image.get_rect())
                    elif rB == 2:
                        BlackRook2('Black', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                rB = rB + 1
            elif StringFEN[i] == 'n': #Knight uses n because the king uses k
                image = pygame.image.load(Pieces.KnightClass.spriteBlack)   
                image = pygame.transform.scale(image, size)
                if kB in (1,2):
                    if kB == 1:
                        BlackKnight1('Black', image.get_rect())
                    elif kB == 2:
                        BlackKnight2('Black', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                kB = kB + 1
            elif StringFEN[i] == 'b':
                image = pygame.image.load(Pieces.BishopClass.spriteBlack)
                image = pygame.transform.scale(image, size)
                if bB in (1,2):
                    if bB == 1:
                        BlackBishop1('Black', image.get_rect())
                    elif bB == 2:
                        BlackBishop2('Black', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
                bB = bB + 1
            elif StringFEN[i] == 'q':
                image = pygame.image.load(Pieces.QueenClass.spriteBlack)
                image = pygame.transform.scale(image, size)
                BlackQueen('Black', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
            elif StringFEN[i] == 'k':
                image = pygame.image.load(Pieces.KingClass.spriteBlack)
                image = pygame.transform.scale(image, size)
                BlackKing('Black', image.get_rect())
                if i == 1:
                    screen.blit(image, (0,columnPOS))
                else:
                    screen.blit(image, (pos,columnPOS))
            elif StringFEN[i] in ('1', '2', '3', '4', '5', '6', '7'):
                if StringFEN[i] == '1':
                    pos = pos + 80
                elif StringFEN[i] == '2':
                    pos = pos + 160
                elif StringFEN[i] == '3':
                    pos = pos + 240
                elif StringFEN[i] == '4':
                    pos = pos + 320
                elif StringFEN[i] == '5':
                    pos = pos + 400
                elif StringFEN[i] == '6':
                    pos = pos + 480
                elif StringFEN[i] == '7':
                    pos = pos + 560
            elif StringFEN[i] == '/':
                if columnPOS == 0:
                    columnPOS = 80
                    pos = -80
                else:
                    columnPOS = columnPOS + 80
                    pos = -80
            if i == 1:
                pos = pos
            else:
                pos = pos + 80            
    
    pygame.display.flip()

clock = pygame.time.Clock()
clicked = False

# To generate moves we get the array of the piece in the board and do -X or +X and -Y or +Y
#
#  Y [[], [], [], [], [], [], [], []],
#    [[], [], [], [], [], [], [], []],
#    [[], [], [], [], [], [], [], []],
#    [[], [], [], [], [], [], [], []],
#    [[], [], [], [], [], [], [], []],
#    [[], [KNIGHT], [], [], [], [], [], []],
#    [[], [], [], [], [], [], [], []],
#
#    X
#                                           Y  X      
# We try to get the KNIGHT Array eg : board[5][1] and do Y +/- 2 and X +/- 1 if X/Y are greater than 8 then the moves is not possible
#
# To set the color of the cell after that the pawn moved we can simply do
#
#if (Wq.rect.y%2) == 0 and (Wq.rect.x%2) == 0: #Ligth else dark
#   screen.fill((240, 217, 181), rect=(Wq.rect.x,Wq.rect.y,80,80))
#else:
#   screen.fill((181, 136, 99), rect=(Wq.rect.x,Wq.rect.y,80,80))
#

def main():
    Run = True

    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    setup_game('rnbqkbnr/pppppppp/////pppppppp/rnbqkbnr')
    while Run == True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Wq.rect.collidepoint(pygame.mouse.get_pos()):
                    print('King touched')
                    #attach sprite to mouse position
            elif event.type == pygame.QUIT:
                Run = False
        clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    main()
