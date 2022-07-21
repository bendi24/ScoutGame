import math
import pygame
import sys
from pytmx.util_pygame import load_pygame
import Dialogue

pygame.init()

WIDTH = 1800
HEIGHT = 1000
szín = (0, 0, 0)
SPEED = 5
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
deli = load_pygame("deli2.tmx")
eltolas = [0, 0]
bg = pygame.Surface((WIDTH, HEIGHT))

#ütközés
coliding = False

#sprite-ok a térképhez
sprite_group = pygame.sprite.Group()
trains = pygame.sprite.Group()
interaktív = pygame.sprite.Group()

#animációk betöltése
alap = pygame.image.load("Sprite-0002- taskas.png")
fel = [pygame.image.load("Sprite-0001.png"), pygame.image.load("Sprite-0002.png"),  pygame.image.load("Sprite-0003.png"), pygame.image.load("Sprite-0004.png")]
le = [pygame.image.load("Sprite-0002- taskas1.png"), pygame.image.load("Sprite-0002- taskas2.png"), pygame.image.load("Sprite-0002- taskas3.png"), pygame.image.load("Sprite-0002- taskas4.png")]
jobbra = [pygame.image.load("Sprite-00031.png"), pygame.image.load("Sprite-00032.png")]
balra = [pygame.transform.flip(pygame.image.load("Sprite-00031.png"), True, False),pygame.transform.flip(pygame.image.load("Sprite-00032.png"), True, False)]
walkcount = 0


def KépernyőFrissités():
    global walkcount

    display.fill(szín)
    hatter3.mozgás()
    hatter3.rajzolas()
    # spriteok kirajzolása csoportonként
    sprite_group.draw(display)
    trains.draw(display)
    interaktív.draw(display)
    # háttér.mozgás()
    # háttér.megjelenés()
    # player.mozgás()
    if walkcount + 1 >= 12:
        walkcount = 0
    print(player.irány)
    if pygame.sprite.spritecollideany(player, trains):
        print("collided")
        hatter3.hátralökés()
    if player.irány == 1:
        display.blit(fel[walkcount//3], player.körvonal)
        walkcount += 1
    if player.irány == 2:
        display.blit(le[walkcount//3], player.körvonal)
        walkcount += 1
    if player.irány == 3:
        display.blit(jobbra[walkcount//6], player.körvonal)
        walkcount += 1
    if player.irány == 4:
        display.blit(balra[walkcount//6], player.körvonal)
        walkcount += 1
    if player.irány == 0:
        display.blit(alap, player.körvonal)
    if pygame.sprite.spritecollideany(player, interaktív):
        pygame.draw.rect(display, (169, 169, 169), pygame.Rect(WIDTH / 4, HEIGHT / 1.3, WIDTH / 2, 200))
        text = pygame.font.SysFont(None, 50).render("Bulcsú", True, (196, 0, 0))
        display.blit(text, (WIDTH / 4, HEIGHT / 1.3 - 30))
        message.draw(display)
    pygame.display.update()

#rajzolt háttér
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = pos)

class hater3:
    def rajzolas(self):
        sprite_group.empty()
        trains.empty()
        interaktív.empty()
        self.kirajzolas(deli.get_layer_by_name("Tile Layer 1"), sprite_group)
        self.kirajzolas(deli.get_layer_by_name("falak"), trains)
        self.kirajzolas(deli.get_layer_by_name("interaktív"), interaktív)
    #hatter kirajzolása
    def kirajzolas(self, layer, groups):
        for x, y, surf in layer.tiles():
            pos = (x * 64 + eltolas[0], y * 64 + eltolas[1])
            Tile(pos=pos, surf=surf, groups=groups)
    #rajzolt háttér mozgatása
    def mozgás(self):
        speed = 10
        counter = 0
        self.fel = False
        self.le = False
        self.bal = False
        self.jobb = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            counter += 1
            if counter >= 2:
                speed = speed/math.sqrt(2)
            eltolas[1] += speed
            player.irány = 1
            self.fel = True
        if keys[pygame.K_s]:
            counter += 1
            if counter >= 2:
                speed = speed / math.sqrt(2)
            eltolas[1] -= speed
            player.irány = 2
            self.le = True
        if keys[pygame.K_d] and self.bal == False:
            counter += 1
            if counter >= 2:
                speed = speed / math.sqrt(2)
            eltolas[0] -= speed
            player.irány = 3
            self.jobb = True
        if keys[pygame.K_a] and self.jobb == False:
            counter += 1
            if counter >= 2:
                speed = speed / math.sqrt(2)
            eltolas[0] += speed
            player.irány = 4
            self.bal = True
        if self.fel == False and self.le == False and self.bal == False and self.jobb == False:
            player.irány = 0



    def hátralökés(self):
        if self.fel:
            eltolas[1] -= 10
        if self.le:
            eltolas[1] += 10
        if player.irány == 3:
            eltolas[0] += 10
        if player.irány == 4:
            eltolas[0] -= 10

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
    def __init__(self, x, y, kép=pygame.image.load("Sprite-0002- taskas.png"), speed=5, irány=0):
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

    def megjelenés(self, kép):
        display.blit(kép, self.körvonal)

#Példányosítás
player = Player(WIDTH/2,HEIGHT/2)
háttér = Background(0, 0)
hatter3 = hater3()

message = Dialogue.DynamicText(Dialogue.font, [WIDTH/4 + 50, HEIGHT/1.2 - 50], autoreset=False)


#fő loop
running = True
while running:
    #kilépés a játékból
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    KépernyőFrissités()
    clock.tick(24)

