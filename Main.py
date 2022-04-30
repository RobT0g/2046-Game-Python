import pygame
from pygame.locals import *
from ScreenManager import Screen
from KeyboardManager import getMoves

pygame.init()                                                           # inicialização

screen_width = 17*32                                                    # largura da tela
screen_height = 17*32                                                   # altura da tela

display = pygame.display.set_mode((screen_width, screen_height))        # tela definida
pygame.display.set_caption('2046')                                      # legenda da tela
screen = Screen(display)
screen.setOnScreen()

running = True                      # Variável de looping
while running:                      # looping
    for e in pygame.event.get():
        if d := getMoves():
            pass
        if pygame.key.get_pressed()[pygame.K_ESCAPE] or e.type == QUIT:
            running = False