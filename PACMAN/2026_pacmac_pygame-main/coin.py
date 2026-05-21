from pathlib import Path
import pygame as pg
from constants import *
from board import Board
from pacman import PacMan


class Coin:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.collected = False

        self.rect = pg.Rect(row, col, 5, 5)

    def draw(self, surface):
        # Avrund til nærmeste heltall for å holde mynten sentrert i rutene
        rounded_col = round(self.col)
        rounded_row = round(self.row)

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        self.rect.center = (rounded_col * TILE_SIZE + mid,
                            rounded_row * TILE_SIZE + mid)

        pg.draw.circle(surface, YELLOW, self.rect.center, 4)

    def oppdater(self, board: Board, pacman: PacMan):
        # Her kan du legge til logikk for å sjekke om Pacman har samlet mynten
        if pacman.rect.colliderect(self.rect):
            self.collected = True
            # Her kan du legge til logikk for å fjerne mynten fra spillet eller oppdatere poengsummen
