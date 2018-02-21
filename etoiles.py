#import math

class Etoiles:    
    def __init__(self, arg_x = 0, arg_y = 0, arg_rayon = 1, arg_distance = 300, arg_angle = 0, arg_vitesse = 1, arg_couleur = (255,255,0)):
        self.x = arg_x          # abscisse
        self.y = arg_y          # ordonnée
        self.r = arg_rayon      # rayon
        self.d = arg_distance   # distance
        self.a = arg_angle      # direction
        self.v = arg_vitesse    # vitesse
        self.col = arg_couleur  # couleur
