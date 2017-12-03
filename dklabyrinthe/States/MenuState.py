import pygame
from pygame.locals import *
from . Tools import _States
from .. import constantes as c
from ..assets import sprite, level


class MenuState():

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
                self._state_machine.change(c.JEU, level.niveau_1)
            if pygame_event.key == K_F2:
                self._state_machine.change(c.JEU, level.niveau_2)

    def on_enter(self):
        """

        :param self:
        :return:
        """
        self.image = sprite.image_accueil

    def render(self, fenetre):
        fenetre.blit(self.image, (0, 0))

    def on_exit(self):
        return
