# BALL VS BOMBERS
# Boule devant désactiver un certain nombre de bombes dans un temps imparti

# Importation des modules
from random import *
import pygame
from pygame.locals import *
import time

# Initialisation
pygame.init()
# Création de la fenêtre et de son titre
fenetre = pygame.display.set_mode((640, 480))
# Titre
pygame.display.set_caption('Ball VS Bombers')
# Non affichage de la souris
pygame.mouse.set_visible(0)
# Repertoire pour ressources
import os

os.chdir("data")
# Chargement de l'image de fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0, 0))
# Rafraîchissement
pygame.display.flip()
# Chargement du personnage
ball = pygame.image.load("ball.png").convert_alpha()
ball_x = 300
ball_y = 343
fenetre.blit(ball, (ball_x, ball_y))
# Rafraîchissement
pygame.display.flip()
# Chargement de la cible
cible = pygame.image.load("cible.png").convert_alpha()
cible_x = 100
cible_y = 200
fenetre.blit(cible, (cible_x, cible_y))
# Rafraîchissement
pygame.display.flip()
# Boucle principale
# Maintien de la touche
pygame.key.set_repeat(1, 20)
# Compteur/Variable score
x = 0
# Durée
length = 60
# Difficulté
dif = 20
# Variable maintenant la fenêtre ouverte
continuer = 1
# Le décompte commence à l'ouverture de la fen^tre
start = time.time()
# Boucle principale
while continuer:
    if time.time() - start < length:
        for event in pygame.event.get():  # Attente des événements
            # Déplacement de la balle
            if event.type == KEYDOWN:
                # Vers le haut
                if event.key == K_UP:
                    if ball_y >= 3:
                        ball = pygame.image.load("ball U.png").convert_alpha()
                        ball_y -= 3
                # Vers le bas
                if event.key == K_DOWN:
                    if ball_y <= 360:
                        ball = pygame.image.load("ball D.png").convert_alpha()
                        ball_y += 3
                # Vers la gauche
                if event.key == K_LEFT:
                    if ball_x >= 3:
                        ball = pygame.image.load("ball L.png").convert_alpha()
                        ball_x -= 3
                # Vers la droite
                if event.key == K_RIGHT:
                    if ball_x <= 597:
                        ball = pygame.image.load("ball R.png").convert_alpha()
                        ball_x += 3
            # La balle touche une bombe -> cette bombe disparaît et une autre apparaît
            if cible_x - 20 <= ball_x <= cible_x + 20 and cible_y - 20 <= ball_y <= cible_y + 20:
                # Le compteur de score s'incrémente de 1 si on touche une cible
                x += 1
                cible_x = randrange(25, 615)
                cible_y = randrange(0, 330)
                fenetre.blit(fond, (0, 0))
                fenetre.blit(ball, (ball_x, ball_y))
                fenetre.blit(cible, (cible_x, cible_y))
        # Re-collage final
        fenetre.blit(fond, (0, 0))
        fenetre.blit(ball, (ball_x, ball_y))
        fenetre.blit(cible, (cible_x, cible_y))
        # Rafraichissement final
        pygame.display.flip()
    # Temps imparti
    elif time.time() - start >= length:
        if x >= dif:
            # Encas de réussite
            # Chargement de l'image de fond
            import os

            os.chdir("D:\Workspace\Python\zhe_ball\data")
            goodend = pygame.image.load("goodend.jpg").convert()
            fenetre.blit(goodend, (0, 0))
            pygame.display.flip()
            # AFFICHAGE DU SCORE
            y = str(x)
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("GAGNE!!!Vous avez désactive " + y + " bombes", 1, (10, 10, 10))
                textpos = text.get_rect(centerx=fond.get_width() / 2)
                fenetre.blit(text, textpos)
            pygame.display.flip()
        elif x < dif:
            # En cas d'échec
            # Chargement de l'image de fond
            import os

            os.chdir("D:\Workspace\Python\zhe_ball\data")
            badend = pygame.image.load("badend.jpg").convert()
            fenetre.blit(badend, (0, 0))
            # AFFICHAGE DU SCORE
            y = str(x)
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("PERDU. Vous n'avez desactive que " + y + " bombes", 1, (10, 10, 10))
                textpos = text.get_rect(centerx=fond.get_width() / 2)
                fenetre.blit(text, textpos)
            pygame.display.flip()
