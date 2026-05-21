from pathlib import Path
import pygame as pg
from constants import *
from board import Board


class PacMan:
    IMAGE_FILE = Path(__file__).parent / "sprites" / "pacman2.png"

    def getImageSpriteList(self, x_start, y_start, num_frames) -> list[pg.Surface]:
        full_image = pg.image.load(self.IMAGE_FILE)
        frame_width = 16

        # Dele opp bildet i frames, som lagres i en liste:
        frames = []
        for i in range(num_frames):
            # Bildene er kvadratiske - bruker frame widht både som høye og bredde:
            frame = full_image.subsurface(
                pg.Rect(x_start + i * frame_width, y_start, frame_width, frame_width))
            frames.append(frame)
        return frames

    def __init__(self, row, col):
        self.row = row
        self.col = col

        self.directions = ""

        self.frames_idle = self.getImageSpriteList(0, 0, 4)
        # Bildet vi skal vise til å starte med er idle:
        self.frames = self.frames_idle

        self.rect = self.frames[0].get_rect()
        # Om vi vil ha animasjon som går gjennom frames:
        self.current_frame = 0

        # Om vi vil speile bildet:
        self.venstre = False

    def draw(self, surface):

        # Få bildet fra en liste av bilder (om du vil bruke animasjon/sprites):
        current_frame_image = self.frames[self.current_frame]

        # Speiler bildet hvis det trengs:
        if self.venstre:
            current_frame_image = pg.transform.flip(
                current_frame_image, True, False)

        # Avrund til nærmeste heltall for å holde Pacman sentrert i rutene
        rounded_col = round(self.col)
        rounded_row = round(self.row)

        # Sørg for at vi tegner midt i "Tile":
        mid = TILE_SIZE // 2
        self.rect = current_frame_image.get_rect()
        self.rect.center = (rounded_col * TILE_SIZE + mid,
                            rounded_row * TILE_SIZE + mid)

        # Blit images på skjermen (der self.rect befinner seg):
        surface.blit(current_frame_image, self.rect)

    def oppdater(self, board: Board):
        keys = pg.key.get_pressed()

        if keys[pg.K_d]:
            self.directions = "right"
        if keys[pg.K_a]:
            self.directions = "left"
        if keys[pg.K_w]:
            self.directions = "up"
        if keys[pg.K_s]:
            self.directions = "down"

        # Bruker rounded posisjoner for collisionsjekk
        current_col = round(self.col)
        current_row = round(self.row)

        if self.directions == "right" and board.is_road(current_col + 1, current_row) == True:
            self.col += 0.1
            self.venstre = False
        if self.directions == "left" and board.is_road(current_col - 1, current_row) == True:
            self.col -= 0.1
            self.venstre = True
        if self.directions == "up" and board.is_road(current_col, current_row - 1) == True:
            self.row -= 0.1
        if self.directions == "down" and board.is_road(current_col, current_row + 1) == True:
            self.row += 0.1
