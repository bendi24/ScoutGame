import pygame
import sys
pygame.init()

WIDTH = 500
HEIGHT = 500
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.clock()

#main loop
while True:

    for event in pygame.event:
        if event.type == pygame.quit():
            sys.exit()
            pygame.Quit()
