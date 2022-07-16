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
    def __init__(self, x=0, y=0, kép=pygame.image.load("bg.png")):
        self.x = x
        self.y = y
        self.kép = kép
        self.körvonal = self.kép.get_rect(topleft=(x, y))

    def megjelenés(self):
        display.blit(self.kép, self.körvonal)

#Játékos class
class Player:
    def __init__(self, x, y, kép=pygame.image.load("walk_1.png"), speed=5, irány=0):
        self.x = x
        self.y = y
        self.kép = kép
        self.körvonal = self.kép.get_rect(center=(x, y))
        self.speed = speed
        self.irány = irány


    def mozgás(self):
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
        self.pos = (self.x, self.y)
        print(self.pos)
        self.körvonal.midbottom = self.pos


    def megjelenés(self):
        display.blit(self.kép, self.körvonal)

#Példányosítás
player = Player(250,250)
háttér = Background(0, 0)

#fő loop
running = True
while running:

    #kilépés a játékból
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    háttér.megjelenés()
    player.mozgás()
    player.megjelenés()
    pygame.display.update()
    clock.tick(40)

