import pygame

class Slider:
    def __init__(self, x, y, w, h, name):
        self.min = x
        self.max = x + w
        self.handle = pygame.rect.Rect(x-w/5/2, y-h/2, w/5, h*2)
        self.slide = pygame.rect.Rect(x, y, w, h)
        self.dragging = False
        self.volume = 0
        self.name = name + ":"

    def draw(self, screen):
        text = pygame.font.SysFont(None, 70).render(self.name, True, (196, 0, 0))
        screen.blit(text, (self.slide.x - 300, self.slide.y))

        pygame.draw.rect(screen, (0, 0, 0), self.slide)
        pygame.draw.rect(screen, (255, 0, 0), self.handle)

    def get_volume(self):
        self.volume = int((self.handle.centerx - self.slide.x) / float(self.slide.w) * 100)
        print(self.volume)
