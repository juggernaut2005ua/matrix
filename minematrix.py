import pygame
import sys
import random

class Window:
    def __init__(self, width=500, height=500):
        pygame.init()  # Инициализируем Pygame
        pygame.display.set_caption("matrix")
        self.RES = self.WIDTH, self.HEIGHT = 1000, 700
        self._screen = pygame.display.set_mode((width, height))
        self.matrix = Matrix(self._screen)  # Передаем экран в конструктор Matrix
        self.surface = pygame.Surface(self.RES, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
    
    def draw(self): # закраска раб. поверхности и нанесем на гл. экран
        self.surface.fill((0,0,0,10))
        self.matrix.run()
        self._screen.blit(self.surface, (0,0))

    def run(self): # главн. цикл программы
        while True:
            self.draw() # отрисовка экрана
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip() # обновление поверхности
            self.clock.tick(30) # установка кадров

class Matrix:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('couriernew', 30)
        self._screen = screen
        self.characters = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=!@#$%^&*()_+{:|<>?`~"
        self.letters = self.characters
        self.drops = [random.randint(0, 500 // 20) for _ in range(500 // 20)]
        self.font_size = 20

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0, 255, 0))
            pos = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self._screen.blit(char_render, pos)
            if self.drops[i] * self.font_size > self._screen.get_height() and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] = self.drops[i] + 1

    def run(self):
        self.draw()

if __name__ == "__main__":
    Window().run()
