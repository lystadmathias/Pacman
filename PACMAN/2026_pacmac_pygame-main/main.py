import pygame as pg
from constants import *
import random as r
from board import Board
from pacman import PacMan
from coin import Coin

pg.init()
board = Board()
vindu = pg.display.set_mode(board.window_size())
clock = pg.time.Clock()


pacman = PacMan(3, 4)

coins = []

# Legg en coin på hver tilgjengelig rute (dvs. ikke vegg).
for y in range(board.rows):
    for x in range(board.cols):
        if board.is_road(x, y):
            # Unngå å plassere en coin der Pacman starter
            if not (y == pacman.row and x == pacman.col):
                coins.append(Coin(y, x))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)

    # Tegn brettet først, og pacman og andre ting "oppå":
    board.draw(vindu)

    # TODO: Oppdater objektene våre:

    # Tegn objektene våre:
    pacman.draw(vindu)
    pacman.oppdater(board)

    for coin in coins:
        coin.draw(vindu)
        coin.oppdater(board, pacman)

        if coin.collected:
            coins.remove(coin)

    # Har alltid disse med til slutt:
    pg.display.flip()
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
