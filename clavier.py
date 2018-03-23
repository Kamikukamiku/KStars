import pygame
from etoiles import Etoiles

def reagir_au_clavier(touches_pressees, arg_fenetre):

    if touches_pressees[pygame.K_ESCAPE]:   # Echap pour quitter
        arg_fenetre.quitter = True
        return True
    if touches_pressees[pygame.K_LEFT]:     # Gauche pour tourner en sens horaire
        arg_fenetre.changer_angle(-1)
        return True
    if touches_pressees[pygame.K_RIGHT]:    # Droite pour tourner en sens antihoraire
        arg_fenetre.changer_angle(1)
        return True
    if touches_pressees[pygame.K_DOWN]:     # Bas pour imprimer un mouvement permanent en sens horaire
        arg_fenetre.mvt_general = -1
        arg_fenetre.changer_angle(-1)
        return True
    if touches_pressees[pygame.K_UP]:       # Haut pour imprimer un mouvement permanent en sens antihoraire
        arg_fenetre.mvt_general = 1
        arg_fenetre.changer_angle(1)
        return True
    if touches_pressees[pygame.K_KP1]:     # Bas pour imprimer un mouvement permanent en sens horaire
        arg_fenetre.mode_courant = Etoiles.constantes.CHAMP_D_ETOILES
        return True
    if touches_pressees[pygame.K_KP2]:       # Haut pour imprimer un mouvement permanent en sens antihoraire
        arg_fenetre.mode_courant = Etoiles.constantes.TOUT_DROIT
        return True
    if touches_pressees[pygame.K_KP0]:      # 0 du clavier numérique pour arrêter le mouvement permanent
        arg_fenetre.changer_angle(0)
        return True
    if touches_pressees[pygame.K_BACKSPACE]:
        arg_fenetre.effacer ^= True # switcher entre True et False
        return True
    if touches_pressees[pygame.K_DELETE]:
        arg_fenetre.souris_visible ^= True # switcher entre True et False
        pygame.mouse.set_visible(arg_fenetre.souris_visible) # masque la souris (ou la réaffiche)
        return True
    if touches_pressees[pygame.K_KP_PLUS]:     # Bas pour imprimer un mouvement permanent en sens horaire
        arg_fenetre.accelerer()
        return True
    if touches_pressees[pygame.K_KP_MINUS]:       # Haut pour imprimer un mouvement permanent en sens antihoraire
        arg_fenetre.decelerer()
        return True
    if touches_pressees[pygame.K_0]:       # forcer les étoiles à toutes avoir la forme choisie
        arg_fenetre.forme_forcee = 0
        return True
    if touches_pressees[pygame.K_1]:      # forcer les étoiles à toutes avoir la forme choisie
        arg_fenetre.forme_forcee = 1
        return True
    if touches_pressees[pygame.K_2]:      # forcer les étoiles à toutes avoir la forme choisie
        arg_fenetre.forme_forcee = 2
        return True
    if touches_pressees[pygame.K_3]:      # forcer les étoiles à toutes avoir la forme choisie
        arg_fenetre.forme_forcee = 3
        return True
    if touches_pressees[pygame.K_4]:      # forcer les étoiles à toutes avoir la forme choisie
        arg_fenetre.forme_forcee = 4
        return True
    if touches_pressees[pygame.K_5]:      # forcer les étoiles à toutes avoir la forme choisie
        arg_fenetre.forme_forcee = 5
        return True
    if touches_pressees[pygame.K_MINUS]:      # forcer les étoiles à ne plus avoir de forme forcée
        arg_fenetre.forme_forcee = -1
        return True
    if touches_pressees[pygame.K_EQUALS]:     # forcer les étoiles à pouvoir prendre n'importe quelle forme même hors du mode courant
        arg_fenetre.forme_forcee = -2
        return True
    
    # si aucune touche utilisée n'a été enfoncée
    return False