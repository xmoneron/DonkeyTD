import pygame
import pygame.locals as pg_const
from .. import constantes as c
from ..assets import sprite

class Perso:
    """
        Représentation d'un personne
    """

    def __init__(self):
        """

        :param sprite_haut:
        :param sprite_bas:
        :param sprite_gauche:
        :param sprite_droit:
        """
        self.sprite = {
            "haut": sprite.dk_haut,
            "bas": sprite.dk_bas,
            "gauche": sprite.dk_gauche,
            "droite": sprite.dk_droite
        }

        self.state = "enjeu"

        self._position_x = 0
        self._position_y = 0

        self.direction = "droite"
        self.bloquant = {
            'm': True,
            'd': False,
            'a': False,
            '0': False
        }

    def deplacer(self, orientation,niveau_state):
        if orientation == "gauche":
            self.direction = "gauche"
            if niveau_state.deplacement_possible(
                    (self._position_x - 1, self._position_y)):
                self._position_x -= 1

        if orientation == "droite":
            self.direction = "droite"
            if niveau_state.deplacement_possible(
                    (self._position_x + 1, self._position_y)):
                self._position_x += 1

        if orientation == "bas":
            self.direction = "bas"
            if niveau_state.deplacement_possible(
                    (self._position_x, self._position_y + 1)):
                self._position_y += 1

        if orientation == "haut":
            self.direction = "haut"

            if niveau_state.deplacement_possible(
                    (self._position_x, self._position_y - 1)):
                self._position_y -= 1

    def update(self, event, niveau_state):
        """

        :param event:
        :param niveau_state:
        :return:
        """
        if event.type == pg_const.KEYDOWN:

            if event.key == pg_const.K_DOWN:
                self.deplacer("bas",niveau_state)

            if event.key == pg_const.K_LEFT:
                self.deplacer("gauche",niveau_state)

            if event.key == pg_const.K_RIGHT:
                self.deplacer("droite",niveau_state)

            if event.key == pg_const.K_UP:
                self.deplacer("haut",niveau_state)

    def recup_position(self):
        """ On transforme la position du sprit en pixel """
        return self._position_x * c.taille_sprite, self._position_y * c.taille_sprite

    def render(self, fenetre):
        """
        Je désine le perso en transformant
        position géographique du joueur en position pixel
        """
        fenetre.blit(self.sprite[self.direction],
                     self.recup_position())

    def get_map_position(self):
        return (self._position_x,self._position_y)