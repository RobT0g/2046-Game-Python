import pygame
import GridManager
import random
import math

class Screen:
    def __init__(self, display) -> None:
        self.display = display
        self.board = pygame.image.load('Images\Frame.png')
        self.font = pygame.font.SysFont('Times New Roman', 58)
        self.numbers = {}
        self.colors = {}
        for i in range(12):
            self.numbers[2**i] = self.font.render(f'{2**i}', False, (0, 0, 0))
            self.colors[2**i] = ((i*80)%255, (i*135)%255, (i*40)%255)
        self.numbersPos = {'10': [50, 30], '100': [35, 30], '1000': [20, 30], '10000': [8, 30]}
        self.grid = [[0 for i in range(4)] for j in range(4)]
    
    def setOnScreen(self):
        self.display.blit(self.board, (0, 0))
        for k1, v1 in enumerate(self.grid):
            for k2, v2 in enumerate(v1):
                if v2 != 0:
                    pos = self.getActualPos((k1, k2))
                    pygame.draw.rect(self.display, self.colors[v2], pygame.Rect(pos[0]+4, pos[1]+4, 120, 120))
                    self.display.blit(self.numbers[v2], self.getNumberPos(v2, pos))
        pygame.display.flip()
    
    def update(self, coord):
        if coord[0] > 16 and coord[0] < (17*32)-16 and coord[1] > 16 and coord[1] < (17*32)-16:
            spot = [math.floor((coord[0]-16)/128), math.floor((coord[1]-16)/128)]
            v = self.grid[spot[0]][spot[1]]
            self.grid[spot[0]][spot[1]] = 2 if v == 0 else (v*2 if v < 2048 else v)
        self.setOnScreen()
    
    def getActualPos(self, pos):
        return [pos[0]*128 + 16, pos[1]*128 + 16]
    
    def getNumberPos(self, number, pos):
        for i in self.numbersPos:
            if number < int(i):
                return [pos[0]+self.numbersPos[i][0], pos[1]+self.numbersPos[i][1]]
        return pos
