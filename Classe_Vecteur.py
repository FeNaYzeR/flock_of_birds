# FeNaYzeR
from math import sqrt
import math
import random

# Classe Vecteur
class Vecteur:
    def __init__(self, vecteur):
        self.vecteur = vecteur

    # Méthodes du vecteur

    def est_nul(self):
        """Renvoie True si le vecteur est nul, False sinon"""
        return self.vecteur[0] == 0 and self.vecteur[1] == 0

    def vect_nul(self):
        """Met les coordonnées du vecteur à 0"""
        self.vecteur[0] = 0
        self.vecteur[1] = 0

    def norme(self):
        """Renvoie la norme du vecteur"""
        calcul_norm = math.hypot(self.vecteur[0], self.vecteur[1])
        return calcul_norm

    def somme(self, v):
        """Transforme le self courant en self + v"""
        self.vecteur[0] = self.vecteur[0] + v[0]
        self.vecteur[1] = self.vecteur[1] + v[1]

    def diff(self, v):
        """Transforme le self courant en self - v"""
        self.vecteur[0] = self.vecteur[0] - v[0]
        self.vecteur[1] = self.vecteur[1] - v[1]

    def oppose(self):
        """Transforme le vecteur courant en -self"""
        self.vecteur[0] = self.vecteur[0] * (-1)
        self.vecteur[1] = self.vecteur[1] * (-1)

    def prodk(self, k):
        """Transforme le vecteur courant self en k*self"""
        self.vecteur[0] = self.vecteur[0] * k
        self.vecteur[1] = self.vecteur[1] * k

    def affectation(self, v):
        """Affecte les coordonnées de v à celle du vecteur courant self"""
        self.vecteur[0] = v[0]
        self.vecteur[1] = v[1]

    def est_egal(self, v):
        """Renvoie un booléen True si les vecteurs sont égaux"""
        return self.vecteur[0] == v[0] and self.vecteur[1] == v[1]

    def normalisation(self):
        """Transforme le vecteur courant self en vecteur de même sens et direction, mais de norme 1"""
        if not self.est_nul():
            self.vecteur[0] = self.vecteur[0] / self.norme()
            self.vecteur[1] = self.vecteur[1] / self.norme()

    def prod_scal(self, v):
        """Renvoie le produit scalaire de self et v = x * x' + y * y'"""
        return self.vecteur[0] * v[0] + self.vecteur[1] * v[1]

    def angle(self, v):
        """Renvoie l'angle orienté entre deux vecteurs en degrés"""
        norme1 = self.norme()
        norme2 = sqrt(v[0] ** 2 + v[1] ** 2)
        if norme1 != 0 and norme2 != 0:
            produit_scalaire = (self.vecteur[0] * v[0] + self.vecteur[1] * v[1]) / (norme1 * norme2)
            produit_scalaire = max(min(produit_scalaire, 1), -1)  # Limite le produit scalaire à la plage valide
            angle_radian = math.acos(produit_scalaire)
            return math.degrees(angle_radian)
        return 0













