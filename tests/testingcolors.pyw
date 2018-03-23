import pygame

from fenetre import Fenetre
from etoiles import Etoiles
from overdrive import Overdrive

angle_general = 0

nb_etoiles = 100
etoiles = [Etoiles() for etoile in range(nb_etoiles)]

fenetre = Fenetre()
rouge = 47
sens_rouge = 1
vert = 166
sens_vert = 2
bleu = 128
sens_bleu = 3

quitter = False
while 1:
    # Lock the framerate at n FPS.
    fenetre.reveil.tick(60)
  
    rouge += sens_rouge
    if rouge > 254 or rouge < 1:
        sens_rouge = -sens_rouge
    vert += sens_vert
    if vert > 253 or vert < 2:
        sens_vert = -sens_vert
    bleu += sens_bleu
    if bleu > 252 or bleu < 3:
        sens_bleu = -sens_bleu

    fenetre.ecran.fill((rouge,vert,bleu))
    pygame.display.flip()

    # Handle events.
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            fenetre.resize((event.w, event.h))

        if event.type == pygame.QUIT:
            quitter = True
            break

    if quitter:
        pygame.quit()
        break
 