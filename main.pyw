import pygame
import vlc
import eyed3

#import time

from fenetre import Fenetre
from etoiles import Etoiles
from clavier import reagir_au_clavier

NB_ETOILES = 500
MP3_FILEPATH = "C:\\Eric Burdon - House Of The Rising Sun.mp3"

# crée la fenêtre
fenetre = Fenetre()

# crée les étoiles
etoiles = [Etoiles(arg_fenetre = fenetre, arg_vitesse_min = 0.1, arg_vitesse_max = 10) for etoile in range(NB_ETOILES)]
for etoile in etoiles:
    etoile.creer(fenetre)

# permet aux touches du clavier d'être enfoncées en continu
pygame.key.set_repeat(1, 10)

# gestion et lecture du mp3
fichier = "file:///" + MP3_FILEPATH.replace("\\\\", "/").replace("\\", "/")
audiofile = eyed3.load(MP3_FILEPATH)
mp3_stream = vlc.MediaPlayer(fichier)
mp3_stream.play()
vol = 0

# boucle principale
while not fenetre.quitter:
    # fixe les FPS
    fenetre.reveil.tick(25)

    if vol < 100:
        vol += 1
        mp3_stream.audio_set_volume(vol)

    # efface l'écran
    if fenetre.effacer:
        fenetre.ecran.fill((0,0,0))

    # déplace les étoiles
    for etoile in etoiles:
        etoile.deplacer(fenetre)

    # affiche l'écran
    pygame.display.flip()

    # gère les événements
    for evenement in pygame.event.get():
        # clic sur fermeture de fenêtre via Windows
        if evenement.type == pygame.QUIT:
            fenetre.quitter = True
            break
        # clic droit souris
        if evenement.type == pygame.MOUSEBUTTONUP:
            if evenement.button == 3:
                fenetre.quitter = True
                break
        # touches clavier
        if pygame.key.get_focused():
            if reagir_au_clavier(pygame.key.get_pressed(), fenetre):
                break

    if fenetre.mvt_general != 0:
        fenetre.changer_angle(fenetre.mvt_general)


pygame.quit()
 