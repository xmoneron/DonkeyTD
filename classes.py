import pygame
from pygame.locals import *

from constantes import *

from enum import Enum

class EmptyState():
    def update(self,event):
        return

    def on_exit(self):
        return

class StateMachine():
    """

    """
    def __init__(self):
        """

        """
        self._states = {"empty": EmptyState()}
        self._current_state = "empty"

    def update(self,pygame_event):
        """

        :param pygame_event:
        :return:
        """
        self._states[self._current_state].update(pygame_event)

    def render(self,fenetre):
        """

        :param fenetre:
        :return:
        """
        self._states[self._current_state].render(fenetre)

    def change(self, state_name, param = None):
        """

        :param state_name:
        :param param:
        :return:
        """
        self._states[self._current_state].on_exit()
        self._current_state = state_name
        if param is not None:
            self._states[self._current_state].on_enter(param)
        else:
            self._states[self._current_state].on_enter()


    def add(self, state_name, state):
        """

        :param state_name:
        :param state:
        :return:
        """
        self._states[state_name] = state

class MenuState():
    """

    """

    def __init__(self, state_machine):
        """
      
        :param state_machine:
        """
        self._state_machine = state_machine


    def update(self, pygame_event):
        """

       :param pygame_event: 
       :return: 
        """
        if pygame_event.type == KEYDOWN:
            if pygame_event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if pygame_event.key == K_F1:
                self._state_machine.change(JEU,niveau1)
            if pygame_event.key == K_F2:
                self._state_machine.change(JEU,niveau2)

    def on_enter(self):
        """

        :param self:
        :return:
        """
        self.image = pygame.image.load(image_accueil).convert_alpha()

    def render(self,fenetre):
        fenetre.blit(self.image, (0,0))

    def on_exit(self):
        return

class NiveauState:

    def __init__(self,state_machine):
        self.state_machine = state_machine
        self.structure_niveau = {}
        self.sprites = {
            "m": pygame.image.load(image_mur).convert_alpha(),
            "a": pygame.image.load(image_arrivee).convert_alpha(),
            "d": pygame.image.load(image_depart).convert_alpha(),
            "0": pygame.image.load(image_herbe).convert_alpha()
        }
        self.bloquant = {
            "m": True,
            "a": False,
            "d": False,
            "0": False
        }
        self._height_map  = 0
        self._width_map = 0
        self.perso = None
        self.fin = ()

    def on_enter(self,niveau):
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

        self.perso = Perso(dk_haut, dk_bas, dk_gauche, dk_droite)

    def render(self,fenetre):
        """

        :param fenetre:
        :return:
        """
        for index_ligne in range(self._height_map):
            for index_sprit in range(self._width_map):
                position_x = index_sprit * taille_sprite
                position_y = index_ligne * taille_sprite
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
                self.state_machine.change(MENU)
        self.perso.update(event,self)

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
                    0 or element > nombre_sprite_cote - 1]
        return True in hors_map

    def fin_niveau(self):
        self.state_machine.change(MENU)


class Perso:
    """
        Représentation d'un personne
    """

    def __init__(self, sprite_haut, sprite_bas, sprite_gauche, sprite_droit):
        """

        :param sprite_haut:
        :param sprite_bas:
        :param sprite_gauche:
        :param sprite_droit:
        """
        self.sprite = {
            Orientation.HAUT: pygame.image.load(sprite_haut).convert_alpha(),
            Orientation.BAS: pygame.image.load(sprite_bas).convert_alpha(),
            Orientation.GAUCHE: pygame.image.load(sprite_gauche).convert_alpha(),
            Orientation.DROITE: pygame.image.load(sprite_droit).convert_alpha()
        }

        self.state = "enjeu"

        self._position_x = 0
        self._position_y = 0

        self.direction = Orientation.DROITE
        self.bloquant = {
            'm': True,
            'd': False,
            'a': False,
            '0': False
        }



    def update(self, event, niveau_state):
        """

        :param event:
        :param niveau_state:
        :return:
        """
        if event.type == KEYDOWN:

            if event.key == K_DOWN:
                self.direction = Orientation.BAS
                if niveau_state.deplacement_possible(
                        (self._position_x, self._position_y + 1)):
                    self._position_y += 1

            if event.key == K_LEFT:
                self.direction = Orientation.GAUCHE
                if niveau_state.deplacement_possible(
                        (self._position_x - 1, self._position_y)):
                    self._position_x -= 1

            if event.key == K_RIGHT:
                self.direction = Orientation.DROITE
                if niveau_state.deplacement_possible(
                        (self._position_x + 1, self._position_y)):
                    self._position_x += 1

            if event.key == K_UP:
                self.direction = Orientation.HAUT

                if niveau_state.deplacement_possible(
                        (self._position_x, self._position_y - 1)):
                    self._position_y -= 1

            if niveau_state.fin == (self._position_x, self._position_y):
                niveau_state.fin_niveau()


    def recup_position(self):
        """ On transforme la position du sprit en pixel """
        return(self._position_x * taille_sprite, self._position_y * taille_sprite)

    def render(self, fenetre):
        """
        Je désine le perso en transformant
        position géographique du joueur en position pixel
        """
        fenetre.blit(self.sprite[self.direction],
                     self.recup_position())



class Orientation(Enum):
    '''
        Orientation possible d'un élement
    '''
    GAUCHE = 1
    DROITE = 2
    HAUT = 3
    BAS = 4
