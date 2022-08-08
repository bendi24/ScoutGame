import pygame

class Button():
    def __init__(self, x, y, img, screen):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
        self.screen = screen

    def draw(self):
        action = False
        self.screen.blit(self.img, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        return action
