import math
import pygame
import random


class Etoiles:
    class constantes:
        # 'constantes'
        CHAMP_D_ETOILES = 1
        TOUT_DROIT = 2
        PLUIE = 3
        NEIGE = 4
        FEU_D_ARTIFICE = 5

    class formes:
        POINT = 0
        ROND = 1
        CERCLE = 2
        BULLE = 3
        CARRE = 4
        IMAGE = 5

        FORMES_ETOILE = (0,1)
        FORMES_FANTAISIE = (1,2,3,4,5)
        TOUTES_FORMES = (0,1,2,3,4,5)

    def __init__(self, arg_fenetre,
                 arg_rayon_max = 2, arg_couleur = (255,255,0),
                 arg_vitesse_min = 0.1, arg_vitesse_max = 10):
        self.col = arg_couleur               # couleur
        self.rayon_max = arg_rayon_max       # rayon maximal
        self.vitesse_min = arg_vitesse_min   # vitesse minimale
        self.vitesse_max = arg_vitesse_max   # vitesse maximale
        self.creer(arg_fenetre)

    def __str__(self):
        return ("\nx = "+str(self.x) +"\t y = "+str(self.y)
               +"\nrayon = "+str(self.r) +"\t angle = "+str(self.a)
               +"\ndistance = "+str(self.d) +"\t vitesse = "+str(self.v)
               +"\ncolor = "+str(self.col))


    def creer(self, arg_fenetre):
        if arg_fenetre.mode_courant == self.constantes.CHAMP_D_ETOILES:
            self.col = (255,255,random.randint(0,255))   # couleur
            self.x = arg_fenetre.xc                      # abscisse
            self.y = arg_fenetre.yc                      # ordonnée
            self.r = random.randint(0, self.rayon_max)   # rayon
            self.d = random.randint(0, arg_fenetre.dist_max) # distance
            self.a = random.random() * 360               # direction
            self.v = self.vitesse_min + (random.random() * self.vitesse_max) # vitesse

            # forme
            if arg_fenetre.forme_forcee == -1:
                self.forme = random.choice(self.formes.FORMES_ETOILE)
            elif arg_fenetre.forme_forcee == -2:
                self.forme = random.choice(self.formes.TOUTES_FORMES)
            else:
                self.forme = arg_fenetre.forme_forcee
        
        elif arg_fenetre.mode_courant == self.constantes.TOUT_DROIT:
            # couleur
            self.col = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            # forme
            if arg_fenetre.forme_forcee == -1:
                self.forme = random.choice(self.formes.FORMES_FANTAISIE)                                                
            elif arg_fenetre.forme_forcee == -2:
                self.forme = random.choice(self.formes.TOUTES_FORMES)
            else:
                self.forme = arg_fenetre.forme_forcee

            # abscisse et ordonnée
            if 0 < arg_fenetre.angle_general < 90:
                self.x = 0
                self.y = random.randint(0, arg_fenetre.h)
            elif 90 < arg_fenetre.angle_general < 180:
                self.x = random.randint(0, arg_fenetre.l)
                self.y = arg_fenetre.h
            elif 180 < arg_fenetre.angle_general < 270:
                self.x = arg_fenetre.l
                self.y = random.randint(0, arg_fenetre.h)
            else:
                self.x = random.randint(0, arg_fenetre.l)
                self.y = 0

            self.r = random.randint(0, self.rayon_max * 5)  # rayon
            self.d = 0                                                         # distance
            self.a = random.random() * 360                                     # direction
            self.v = self.vitesse_min + (random.random() * (self.vitesse_max)) # vitesse
        elif arg_fenetre.mode_courant == self.constantes.PLUIE:
            pass
        elif arg_fenetre.mode_courant == self.constantes.NEIGE:
            pass
        elif arg_fenetre.mode_courant == self.constantes.FEU_D_ARTIFICE:
            pass

    def deplacer(self, arg_fenetre):
        if arg_fenetre.mode_courant == self.constantes.CHAMP_D_ETOILES:
            self.d += self.v + arg_fenetre.acceleration
            if self.x < 0 or self.y < 0 or self.x > arg_fenetre.l or self.y > arg_fenetre.h: # j'ai enlevé "self.d >= arg_fenetre.dist_max or"
                self.creer(arg_fenetre)
            # calculer la position de façon trigonométrique par rapport au centre de la fenêtre
            angle = math.radians(self.a + arg_fenetre.angle_general)
            self.x = arg_fenetre.xc + (self.d * math.cos(angle))
            self.y = arg_fenetre.yc + (self.d * -math.sin(angle))
        
        elif arg_fenetre.mode_courant == self.constantes.TOUT_DROIT:
            self.d += self.v + arg_fenetre.acceleration
            if self.x < 0 or self.y < 0 or self.x > arg_fenetre.l or self.y > arg_fenetre.h:
                self.creer(arg_fenetre)
            # forcer des angles droits
            if 0 < arg_fenetre.angle_general < 90:
                angle = math.radians(0)
            elif 90 < arg_fenetre.angle_general < 180:
                angle = math.radians(90)
            elif 180 < arg_fenetre.angle_general < 270:
                angle = math.radians(180)
            else:
                angle = math.radians(270)
            #angle = math.radians(arg_fenetre.angle_general)
            # calculer la position de façon trigonométrique par rapport à la position précédente
            self.x = self.x + ((self.v + arg_fenetre.acceleration) * math.cos(angle))
            self.y = self.y + ((self.v + arg_fenetre.acceleration) * -math.sin(angle))
        
        elif arg_fenetre.mode_courant == self.constantes.PLUIE:
            pass
        
        elif arg_fenetre.mode_courant == self.constantes.NEIGE:
            pass
        
        elif arg_fenetre.mode_courant == self.constantes.FEU_D_ARTIFICE:
            pass
            
        # dessiner l'étoile selon sa forme
        temp_x = int(self.x)
        temp_y = int(self.y)
        if self.forme == self.formes.POINT:
            arg_fenetre.ecran.set_at((temp_x,temp_y), self.col)

        elif self.forme == self.formes.ROND:
            temp_r = int(self.r)
            pygame.draw.circle(arg_fenetre.ecran, self.col, (temp_x,temp_y), temp_r, 0)

        elif self.forme == self.formes.CERCLE:
            temp_r = int(1 + (self.r * 1.5))
            pygame.draw.circle(arg_fenetre.ecran, self.col, (temp_x,temp_y), temp_r, 1)

        elif self.forme == self.formes.BULLE:
            temp_r = 2 + int(self.r * 2)
            temp_br = temp_r * 0.6
            temp_2br = temp_br * 2
            temp_x2 = temp_x - temp_br
            temp_y2 = temp_y - temp_br
            # arg_fenetre.ecran.set_at((temp_x,temp_y), self.col)
            pygame.draw.circle(arg_fenetre.ecran, self.col, (temp_x,temp_y), temp_r, 1)
            pygame.draw.arc(arg_fenetre.ecran, self.col, (temp_x2,temp_y2,temp_2br,temp_2br), 0.5, 1.5, 1)

        elif self.forme == self.formes.CARRE:
            temp_l = int(self.r * 2)
            temp_2l = 2 * temp_l
            pygame.draw.rect(arg_fenetre.ecran, self.col, (temp_x-temp_l,temp_y-temp_l,temp_2l,temp_2l), 0)

        elif self.forme == self.formes.IMAGE:
            temp_x = temp_x - 32
            temp_y = temp_y - 32
            arg_fenetre.ecran.blit(arg_fenetre.icon_image, (temp_x,temp_y))