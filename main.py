import pygame
import sys
pygame.init()

WIDTH = 500
HEIGHT = 500
szín = (0, 0, 0)
SPEED = 5
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Háttér class
class Background:
    def __init__(self, x, y, kép=pygame.image.load("bg.png")):
        self.x = x
        self.y = y
        self.kép = kép
        self.körvonal = self.kép.get_rect()

    def megjelenés(self):
        display.blit(self.kép, self.körvonal)

    #A háttér mozog és olyan mintha követné a kamera a játékost
    def mozgás(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y += 5
        elif keys[pygame.K_s]:
            self.y -= 5
        if keys[pygame.K_d]:
            self.x -= 5
        elif keys[pygame.K_a]:
            self.x += 5
        self.pos = (self.x, self.y)
        self.körvonal.center = self.pos


#Játékos class
class Player:
    def __init__(self, x, y, kép=pygame.image.load("walk_1.png"), speed=5, irány=0):
        self.x = x
        self.y = y
        self.kép = kép
        self.körvonal = self.kép.get_rect(center=(x, y))
        self.speed = speed
        self.irány = irány

    #A játékos mozog
    """def mozgás(self):
        keys = pygame.key.get_pressed()
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
        #pozició frissítése
        self.pos = (self.x, self.y)
        self.körvonal.midbottom = self.pos
"""

    def megjelenés(self):
        display.blit(self.kép, self.körvonal)

#Példányosítás
player = Player(250,250)
háttér = Background(250, 250)

#fő loop
running = True
while running:
    #kilépés a játékból
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    display.fill(0)
    háttér.mozgás()
    háttér.megjelenés()
    #player.mozgás()
    player.megjelenés()

    pygame.display.update()
    clock.tick(40)

