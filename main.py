import pygame
import sys
from pytmx.util_pygame import load_pygame

pygame.init()

WIDTH = 1800
HEIGHT = 1000
szín = (0, 0, 0)
SPEED = 5
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
deli = load_pygame("deli2.tmx")
sprite_group = pygame.sprite.Group()
eltolas = [0, 0]
bg = pygame.Surface((WIDTH, HEIGHT))
trains = pygame.sprite.Group()
coliding = False


#rajzolt háttér
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = pos)
def hatter_rajzolas():
    sprite_group.empty()
    trains.empty()
    layer = deli.get_layer_by_name("Tile Layer 1")
    for x, y, surf in layer.tiles():
        pos = (x * 64 + eltolas[0], y * 64 + eltolas[1])
        Tile(pos=pos, surf=surf, groups=sprite_group)
    layer = deli.get_layer_by_name("trains")
    for x, y, surf in layer.tiles():
        pos = (x * 64 + eltolas[0], y * 64 + eltolas[1])
        Tile(pos=pos, surf=surf, groups=trains)
#rajzolt háttér mozgatása
def mozgás():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        eltolas[1] += 10
    elif keys[pygame.K_s]:
        eltolas[1] -= 10
    if keys[pygame.K_d]:
        eltolas[0] -= 10
    elif keys[pygame.K_a]:
        eltolas[0] += 10

#(kép)Háttér class
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
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, kép=pygame.image.load("walk_1.png"), speed=5, irány=0):
        self.x = x
        self.y = y
        self.kép = kép
        self.körvonal = self.kép.get_rect(center=(x, y))
        self.rect = pygame.Rect(*display.get_rect().center, 0, 0).inflate(75, 75)
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
player = Player(WIDTH/2,HEIGHT/2)
háttér = Background(0, 0)

#vonatok kiválogatás
#fő loop
running = True
while running:
    #kilépés a játékból
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    if pygame.sprite.spritecollideany(player, trains):
        coliding = True
    display.fill(szín)
    mozgás()
    hatter_rajzolas()
    sprite_group.draw(display)
    trains.draw(display)
    #háttér.mozgás()
    #háttér.megjelenés()
    #player.mozgás()
    player.megjelenés()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(40)

