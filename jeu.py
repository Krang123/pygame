import pygame
pygame.init()
BACKGROUND_COLOR=(255,255,255)
ECRAN = pygame.display.set_mode((350, 350))
ARRET_JEU= False
while not ARRET_JEU:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                ARRET_JEU = True
