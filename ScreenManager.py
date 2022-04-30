import pygame
import GridManager
import random

class Screen:
    def __init__(self, display) -> None:
        self.display = display
        self.board = pygame.image.load('Images\Frame.png')
        self.font = pygame.font.SysFont('Times New Roman', 32)
        self.numbers = {}
        self.colors = {}
        for i in range(12):
            self.numbers[2**i] = self.font.render(f'{2**i}', False, (0, 0, 0))
            self.colors[2**i] = ((i*80)%255, (i*135)%255, (i*40)%255)
    
    def setOnScreen(self):
        self.display.blit(self.board, (0, 0))
        pygame.display.flip()