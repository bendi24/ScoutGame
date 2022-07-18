import pygame
pygame.font.init()
font = pygame.font.Font(None, 50)

messages = ["Szép jó napot kivánok!", "Tass Bulcsú vagyok, a 46-os számú Kapisztrán", "Szent János Cserkészcsapat csapatparancsnoka."]



class DynamicText(object):
    def __init__(self, font, pos, autoreset=False, texts=messages, counter=0):
        self.done = False
        self.counter = counter
        self.texts = texts
        self.font = font
        self.text = texts[counter]
        self._gen = self.text_generator(self.text)
        self.pos = pos
        self.autoreset = autoreset
        self.update(self.texts)

    def text_generator(self, text):
        tmp = ''
        for letter in text:
            tmp += letter
            if letter != ' ':
                yield tmp

    def reset(self, texts):
        self._gen = self.text_generator(self.text)
        self.done = False
        self.update(self.texts)

    def update(self, texts):
        if not self.done:
            try:
                self.rendered = self.font.render(next(self._gen), True, (0, 128, 0))
            except StopIteration:
                self.done = True
                #pygame.time.wait(500)
                print(len(texts), self.counter)
                if len(texts)-1 <= self.counter:
                    pass
                else:
                    pygame.time.wait(500)
                    self.counter += 1
                    self.text = texts[self.counter]
                    self.reset(self.texts)

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)
        self.update(self.texts)