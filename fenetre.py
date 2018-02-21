import pygame

from etoiles import Etoiles

class Fenetre:
    dirge = -90

    def __init__(self, arg_largeur = 800, arg_hauteur = 600, nb_etoiles = 300):
        self.l = arg_largeur
        self.h = arg_hauteur
        self.xc = arg_largeur // 2
        self.yc = arg_hauteur // 2

        self.nb_etoiles = nb_etoiles
        self.etoiles = [Etoiles() for i in range(self.nb_etoiles)]

        pygame.init()
        self.ecran = pygame.display.set_mode((self.l, self.h), pygame.RESIZABLE)

    def resize(self, dimensions):
        self.l = dimensions[0]
        self.h = dimensions[1]
        self.xc = dimensions[0] // 2
        self.yc = dimensions[1] // 2
        self.ecran = pygame.display.set_mode(dimensions, pygame.RESIZABLE)
        return True
        
"""
if __name__ == "__main__":
    Fenetre().run()
"""