from this import s
import pygame
import os
import sys

# Fonts in the game
pygame.font.init()
STAT_FONT = pygame.font.SysFont("comicsans", 50)

# Window parameters
SCREEN_SIZE = WIN_WIDTH, WIN_HEIGHT = 500, 800

# Images for the game
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))


if __name__ == "__main__":
    screen = pygame.display.set_mode(SCREEN_SIZE)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(BG_IMG, (0, 0))
        screen.blit(BIRD_IMGS[0], (WIN_WIDTH/2, WIN_HEIGHT/2))
        pygame.display.flip()
