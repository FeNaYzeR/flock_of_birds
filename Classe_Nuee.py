#FeNaYzeR
from Classe_Vecteur import*
from classe_Animal import*
import random

class Nuee:
    def __init__(self, essaim, l_univers, h_univers):
        self.vecteur_nul = Vecteur([0, 0])
        self.max_voisins = 5
        self.essaim = essaim
        self.l_univers = l_univers
        self.h_univers = h_univers

    def mouvement(self):
        """Met à jour la position de tous les animaux de la nuée"""
        for animal in self.essaim:
            animal.maj_position()

    def regles(self):
        """Applique à chaque animal les règles de séparation, de cohésion et d'alignement"""
        separation, alignement, cohesion = self.voisins()
        for i in range(len(self.essaim)):
            for j in range(len(self.essaim)):
                if separation[i][j]:
                    self.separation(i, j)
                elif alignement[i][j]:
                    self.alignement(i, j)
                elif cohesion[i][j]:
                    self.cohesion(i, j)

    def voisins(self):
        """Renvoie les trois listes de séparation, de cohésion et d'alignement, ainsi que la distance des différents animaux"""
        separation = []
        cohesion = []
        alignement = []
        for i in range(len(self.essaim)):
            liste_sep = []
            liste_coh = []
            liste_ali = []
            for j in range(len(self.essaim)):
                if self.essaim[i].distance(self.essaim[j]) <= Animal.perception[0]:
                    liste_sep.append(True)
                else:
                    liste_sep.append(False)
                if self.essaim[i].distance(self.essaim[j]) > Animal.perception[0] and self.essaim[i].distance(
                        self.essaim[j]) <= Animal.perception[1]:
                    liste_coh.append(True)
                else:
                    liste_coh.append(False)
                if self.essaim[i].distance(self.essaim[j]) > Animal.perception[1] and self.essaim[i].distance(
                        self.essaim[j]) <= Animal.perception[2]:
                    liste_ali.append(True)
                else:
                    liste_ali.append(False)
            separation.append(liste_sep)
            cohesion.append(liste_coh)
            alignement.append(liste_ali)
        return separation, alignement, cohesion

    def separation(self, i, j):
        """S'applique à l'animal i pour l'éloigner de l'animal j s'ils sont trop proches"""
        distance = self.essaim[i].distance(self.essaim[j])
        min_distance = 3 * Animal.taille  # Distance minimale à maintenir entre les animaux
        if distance < min_distance:
            # Calcul de la force de séparation
            force_separation = Vecteur([(self.essaim[i].position[0] - self.essaim[j].position[0]),
                                        (self.essaim[i].position[1] - self.essaim[j].position[1])])
            force_separation.normalisation()
            force_separation.prodk(min_distance - distance)

            # Réduction de la vitesse de l'animal i
            self.essaim[i].vitesse.diff(force_separation.vecteur)


    def alignement(self, i, j):
        """S'applique à l'animal i pour lui faire s'aligner avec l'animal j"""
        vx = self.essaim[j].vitesse.vecteur[0] * 0.8
        vy = self.essaim[j].vitesse.vecteur[1] * 0.8
        self.essaim[i].vitesse.somme([vx, vy])

    def cohesion(self, i, j):
        """S'applique à l'animal i pour lui faire se rapprocher de l'animal j"""
        force_cohesion = Vecteur([(self.essaim[j].position[0] - self.essaim[i].position[0]),
                                  (self.essaim[j].position[1] - self.essaim[i].position[1])])
        force_cohesion.normalisation()
        force_cohesion.prodk(self.essaim[i].vitesse.norme() / 2)
        self.essaim[i].vitesse.somme(force_cohesion.vecteur)

    def centripete(self, centre, force):
        """Modifie les vitesses des animaux pour se diriger vers un centre avec une force donnée"""
        for animal in self.essaim:
            direction = centre - animal.position  # Vecteur direction vers le centre
            direction_normalisee = direction.normalisation()  # Vecteur direction normalisé
            vitesse_modifiee = direction_normalisee * force  # Vecteur vitesse modifiée
            animal.vitesse = vitesse_modifiee

    def fuite(self, predateur, force):
        """Fuit le prédateur en modifiant aléatoirement la vitesse"""
        for animal in self.essaim:
            if animal.distance(predateur) < Animal.taille * 5:  # Condition de fuite
                angle = np.random.uniform(-90, 190)  # Angle aléatoire entre -90 et 190 degrés
                vitesse_modifiee = animal.vitesse.rotation(angle)  # Rotation de la vitesse actuelle de l'animal
                animal.vitesse = vitesse_modifiee * force  # Multiplie la vitesse par la force de fuite




