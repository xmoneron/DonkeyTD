from pygame.locals import *
from ..assets import sprite
from ..Elements.Perso import Perso

from .. import constantes as c


class NiveauState():
    def __init__(self, state_machine):
        self.state_machine = state_machine
        self.structure_niveau = {}
        self.sprites = {
            "m": sprite.image_mur,
            "a": sprite.image_arrivee,
            "d": sprite.image_depart ,
            "0": sprite.image_herbe
        }
        self.bloquant = {
            "m": True,
            "a": False,
            "d": False,
            "0": False
        }
        self._height_map = 0
        self._width_map = 0
        self.perso = None
        self.fin = ()

    def on_enter(self, niveau):
        """

        :param niveau:
        :return:
        """

        with open(niveau, "r") as fichier:
            pos_y = 0
            for ligne in fichier:
                self._width_map = 0
                self._height_map += 1
                pos_x = 0
                for sprit in ligne:
                    if sprit != '\n':
                        position = (pos_x, pos_y)
                        self.structure_niveau[position] = sprit
                        if sprit == 'a':
                            self.fin = position
                        pos_x += 1
                        self._width_map += 1

                pos_y += 1

        self.perso = Perso()

    def render(self, fenetre):
        """

        :param fenetre:
        :return:
        """
        for index_ligne in range(self._height_map):
            for index_sprit in range(self._width_map):
                position_x = index_sprit * c.taille_sprite
                position_y = index_ligne * c.taille_sprite
                case_courante = self.structure_niveau[(
                    index_sprit, index_ligne)]
                sprite_courant = self.sprites[case_courante]
                fenetre.blit(
                    sprite_courant, (position_x, position_y))

        self.perso.render(fenetre)

    def on_exit(self):
        """

        :return:
        """
        self.structure_niveau = {}
        self._height_map = 0
        self._width_map = 0

    def update(self, event):
        """

        :param event:
        :return:
        """
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.state_machine.change(c.MENU)
        self.perso.update(event, self)

        if self.perso.get_map_position() == self.fin:
            self.fin_niveau()

    def deplacement_possible(self, position):
        """

        :param position:
        :return:
        """
        if self.hors_map(position):
            return False
        if self.bloquant[self.structure_niveau[position]]:
            return False
        else:
            return True

    def hors_map(self, position):
        """

        :param position:
        :return:
        """
        hors_map = [True for element in position if element <
                    0 or element > c.nombre_sprite_cote - 1]
        return True in hors_map

    def fin_niveau(self):
        self.state_machine.change(c.MENU)