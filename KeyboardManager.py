import pygame

pygame.init() 

def getMoves():
    keys = [pygame.key.get_pressed()[i] for i in (pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_w)]
    try:
        if keys.count(True) == 1:
            return keys.index(True)
        return None
    except:
        return None
