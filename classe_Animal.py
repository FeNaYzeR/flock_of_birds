#FeNaYzeR

from random import *
from Classe_Vecteur import *
import math
import random

class Animal:
    taille = 15
    perception = [5, 20, 50]
    # Unité séparation/ Unité cohésion / Unité alignement

    def __init__(self, position, l_univers, h_univers):
        self.position = position
        self.vitesse = Vecteur([2, 2])
        self.v_max = self.vitesse.norme() * 2
        self.v_init = self.vitesse.norme()
        self.force_max = (0.1,1.5)
        self.l_univers = l_univers
        self.h_univers = h_univers

    def force_alea(self):
        """Crée une force de déplacement aléatoire qui va s'appliquer sur l'animal"""
        vitesse_init = self.vitesse
        self.vitesse.somme([random.randint(-int(self.force_max[0]), int(self.force_max[0])),
                    random.randint(-int(self.force_max[1]), int(self.force_max[1]))])
        if self.vitesse.norme() >= self.v_max:
            self.vitesse = vitesse_init


    def maj_position(self):
        """Déplace l'animal suivant sa vitesse et gère les rebonds contre les murs"""
        next_x = self.position[0] + round(self.vitesse.vecteur[0])
        next_y = self.position[1] + round(self.vitesse.vecteur[1])

        # Vérification des rebonds contre les murs
        if next_x - Animal.taille < 0 or next_x + Animal.taille > self.l_univers:
            self.vitesse.vecteur[0] *= -1
            while next_x - Animal.taille < 0 or next_x + Animal.taille > self.l_univers:
                next_x = self.position[0] + round(self.vitesse.vecteur[0])
                self.position[0] += round(self.vitesse.vecteur[0])
        else:
            self.position[0] = next_x

        if next_y - Animal.taille < 0 or next_y + Animal.taille > self.h_univers:
            self.vitesse.vecteur[1] *= -1
            while next_y - Animal.taille < 0 or next_y + Animal.taille > self.h_univers:
                next_y = self.position[1] + round(self.vitesse.vecteur[1])
                self.position[1] += round(self.vitesse.vecteur[1])
        else:
            self.position[1] = next_y

        # Vérification de la vitesse maximale
        if self.vitesse.norme() > self.v_max:
            self.vitesse.normalisation()  # Normalise le vecteur vitesse
            self.vitesse.prodk(self.v_max)  # Redimensionne la vitesse à la valeur maximale

    def distance(self, objet):
        """Renvoie la distance avec un autre Animal"""
        dist = round(sqrt((self.position[0] - objet.position[0]) ** 2 +
                          (self.position[1] - objet.position[1]) ** 2))
        return dist