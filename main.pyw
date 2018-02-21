import pygame

from fenetre import Fenetre

clock = pygame.time.Clock()
fenetre = Fenetre(800, 600, 300)

while 1:
    # Lock the framerate at 25 FPS.
    clock.tick(25)

    # Handle events.
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            fenetre.resize((event.w, event.h))

        if event.type == pygame.QUIT:
            pygame.quit()
