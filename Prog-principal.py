#FeNaYzeR
import pygame
from pygame import *
from pygame.gfxdraw import *
from Classe_Vecteur import *
from Classe_Nuee import *
from classe_Animal import *
import random

from codecs import *

def taille_police(largeur, longueur):
    """Cette fonction adapte la police en fonction de la longueur de l'écran de l'utilisateur grâce à un multiplicateur"""
    if (largeur, longueur) == (1366, 768):
        return 1
    if (largeur, longueur) == (1920, 1080):
        return 1.4
    else:
        return 1

pygame.init()  # Initialisation de la fenetre pygame
fenetre = display.set_mode((0, 0), pygame.FULLSCREEN)
display.set_caption("Projet 2022-2023")
fenetre.fill((255, 195, 136))
info = pygame.display.Info()  # Récupère les coordonées de la taille de l'écran
largeur, hauteur = info.current_w, info.current_h

# Couleur
orange = (255, 125, 0)
orange_bis = (255, 221, 189)
blanc = (255, 255, 255)
couleur_active = blanc  # Couleur de base de la fenêtre de saisie
couleur_inactive = orange
couleur = couleur_inactive  # La couleur est inactive à l'initial

box_rect = pygame.Rect(largeur // 2.25, hauteur // 1.5, largeur // 9, hauteur // 10)  # Bouton Start
pygame.draw.rect(fenetre, (orange), box_rect)
police = font.Font("Quoth.otf", round(50 * taille_police(largeur, hauteur)))
textestart = police.render("start", 1, blanc)
position_textestart = (largeur // 2.25 + (largeur // 9) / 3.5, hauteur // 1.5 + (hauteur // 10) / 3.5)
fenetre.blit(textestart, (position_textestart))
commencer = False

# Texte présentation
texte1 = police.render("Simulation d'une nuée d'oiseau", 1, blanc)
position_texte = (largeur // 3, hauteur // 3.5)
fenetre.blit(texte1, (position_texte))
display.flip()

clic_rectangle = pygame.Rect(largeur // 2.35, hauteur // 1.75, largeur // 7, hauteur // 13)  # Crée une box de saisi de caractère
texte = ""
txt_surface = police.render(texte, True, blanc)
activer = False  # Boolean qui vaut false si l'utilisateur n'a pas cliqué sur la fenêtre de saisie
continuer = 1  # Fermeture de la fenêtre graphique
NotInt = False
TexteValue = False
indice_oiseau = 0

essaim = []
nuee = None  # Variable pour stocker la nuée d'oiseaux

while continuer:
    for event in pygame.event.get():
        x, y = mouse.get_pos()

        if event.type == MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                commencer = True
            if commencer == True:
                if clic_rectangle.collidepoint(event.pos):  # Si on clique sur la box elle prend la couleur active
                    activer = not activer  # Si on reclique elle prend la valeur inactive
                else:
                    activer = False
                couleur = couleur_active if activer else couleur_inactive


        if commencer == True:  # Si le bouton start est pressé affiche question et box de saisie
            fenetre.fill((orange_bis))
            pygame.draw.rect(fenetre, couleur, clic_rectangle, 2)

            texte_valeur = police.render("Quel est la valeur d'oiseau que vous voulez ?", 1, blanc)
            position_texte_valeur = (largeur // 3.7, hauteur // 3.5)
            fenetre.blit(texte_valeur, (position_texte_valeur))
        if NotInt == True:  # Si n'est pas un entier alors affiche texte
            fenetre.blit(texte_entier, (position_texte_entier))

        if event.type == KEYDOWN:
            if commencer == True:  # Si le bouton start a été préssé alors on peut rentrer des chaînes de caractères
                if activer:
                    if event.key == K_RETURN:
                        print(texte)
                        nb_oiseau = texte
                        try:
                            test_entier = int(texte)  # Vérifie si la saisie est bien un entier
                            texte = ""
                            TexteValue, commencer, NotInt = True, False, False
                        except ValueError:
                            pasEntier = "La saisie n'est pas un entier"
                            NotInt = True

                            texte_entier = police.render(pasEntier, 1, blanc)
                            position_texte_entier = (largeur // 2.75, hauteur // 2.5)

                        texte = ""
                    elif event.key == K_BACKSPACE:
                        texte = texte[:-1]
                    else:
                        texte = texte + event.unicode

                txt_surface = police.render(texte, True, blanc)
                fenetre.blit(txt_surface, (clic_rectangle.x + 5, clic_rectangle.y + 5))
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                continuer = 0
        pygame.draw.rect(fenetre, couleur, clic_rectangle, 2) if commencer == True else None
        # Appel de la fonction fenetre.blit() pour dessiner la zone de saisie de texte au-dessus de tous les autres éléments
        fenetre.blit(txt_surface, (clic_rectangle.x + 5, clic_rectangle.y + 5))

        if event.type == QUIT:
            pygame.quit()
            continuer = 0

    if TexteValue:
        if nuee is None:  # Créer la nuée d'oiseaux si elle n'existe pas déjà
            nuee = Nuee(essaim, largeur, hauteur)
            for generation_oiseau in range(int(nb_oiseau)):
                x = random.randint(Animal.taille, largeur - Animal.taille)
                y = random.randint(Animal.taille, hauteur - Animal.taille)
                position = [x, y]
                animal = Animal(position, largeur, hauteur)
                essaim.append(animal)

        # Mise à jour de la nuée
        nuee.regles()
        # Mise à jour de la position des animaux
        nuee.mouvement()
        fenetre.fill(orange_bis)
        for animal in nuee.essaim:
            pygame.draw.circle(fenetre, (0, 0, 0), (int(animal.position[0]), int(animal.position[1])), Animal.taille)
            animal.force_alea()
            print(int(animal.position[0]), int(animal.position[1]))
    display.flip()

