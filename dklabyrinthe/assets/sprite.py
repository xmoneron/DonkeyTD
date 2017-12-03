import pygame
import os


image_accueil = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/accueil.png')
image_fond = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/fond.jpg')
image_mur =  pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/mur.png')
image_depart = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/depart.png')
image_arrivee = pygame.image.load(os.path.dirname(os.path.realpath(__file__))+ '/arrivee.png')
image_herbe = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) +'/herbe.png')

dk_droite = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/dk_droite.png')
dk_gauche = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/dk_gauche.png')
dk_haut = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/dk_haut.png')
dk_bas = pygame.image.load(os.path.dirname(os.path.realpath(__file__)) + '/dk_bas.png')

def load_image(image):
    return pygame.image.load(os.path.dirname(os.path.realpath(__file__))+'/'+image)
