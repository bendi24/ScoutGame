import pygame
import sys
pygame.init()

WIDTH = 500
HEIGHT = 500
szín = (0, 0, 0)
SPEED = 10
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.clock()

#Játékos class
class Player:
    def __init__(self, x, y, kép, speed=5, irány=0):
        self.x = x
        self.y = y
        self.kép = kép
        self.körvonal = self.kép.get_rect(center=(x, y))
        self.speed = speed
        self.irány = irány

    def megjelenés(self):
        display.blit(self.kép, self.körvonal)

    def mozgás(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.irány = 0
        elif keys[pygame.K_s]:
            self.y += self.speed
            self.irány = 1
        if keys[pygame.K_d]:
            self.x += self.speed
            self.irány = 2
        elif keys[pygame.K_a]:
            self.x -= self.speed
            self.irány = 3

#Példányosítás
player = Player(0, 0, pygame.image.load("walk_1.png").convert_alpha(), SPEED)
háttér = Background(0, 0)

#fő loop
running = True
billentyűk = pygame.key.get_pressed()
while running:

    háttér.megjelenés()
    player.mozgás(billentyűk)
    player.megjelenés()


    #kilépés a játékból
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    pygame.display.update()

