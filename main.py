import pygame
import os

pygame.init()
WIDTH, HEIGHT = 800, 500
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    pygame.time.Clock()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
