import pygame
import random
from etoiles import Etoiles

class Fenetre:
    def __init__(self, arg_largeur = 0, arg_hauteur = 0):
        # définir l'icône
        pygame.init()
        self.icon_image = pygame.image.load("icon_stars.png") #.convert()
        self.icon_dimensions = self.icon_image.get_rect()
        pygame.display.set_icon(self.icon_image) #pygame.image.load('icon_stars.png'))

        # attribue les variables
        if arg_largeur == 0 and arg_hauteur == 0:
            self.ecran = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
            self.l, self.h = pygame.display.get_surface().get_size()
        else:
            # démarrer la fenêtre aux dimensions voulues
            self.l = arg_largeur
            self.h = arg_hauteur
            self.ecran = pygame.display.set_mode((self.l, self.h), pygame.FULLSCREEN & pygame.RESIZABLE)

        self.angle_general = 270
        self.mvt_general = 0
        self.acceleration = 0
        self.forme_forcee = -1
        self.mode_courant = Etoiles.constantes.CHAMP_D_ETOILES

        self.xc = self.l // 2
        self.yc = self.h // 2
        self.dist_max = max(self.l, self.h) * 1.5
        self.effacer = True
        self.souris_visible = True

        self.reveil = pygame.time.Clock()
        self.quitter = False
        
    def resize(self, dimensions):
        self.l, self.h = dimensions
        self.xc = self.l // 2
        self.yc = self.h // 2
        self.dist_max = max(self.l, self.h) * 1.5
        self.ecran = pygame.display.set_mode(dimensions, pygame.RESIZABLE)
        return True

    def changer_angle(self, plus = 1):
        if plus > 0:
            self.angle_general += 1
            if self.angle_general >= 360:
                self.angle_general = 0 + (self.angle_general - 360)
        elif plus < 0:
            self.angle_general -= 1
            if self.angle_general <= 0:
                self.angle_general = 360 + self.angle_general
        elif plus == 0:
            self.mvt_general = 0

    def accelerer(self):
        self.acceleration += 0.1
        if self.acceleration > 10:
            self.acceleration = 10

    def decelerer(self):
        self.acceleration -= 0.1
        if self.acceleration < 0:
            self.acceleration = 0
