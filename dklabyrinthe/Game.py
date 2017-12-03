from dklabyrinthe.States.Tools import StateMachine
from dklabyrinthe.States import MenuState, NiveauState

import constantes as c
import pygame
import pygame.locals as pg_const


class Game:

    def __init__(self):
        self.state_machine = StateMachine()
        self.continuer = True
        self.clock = pygame.time.Clock()
        self.fenetre = pygame.display.set_mode((c.cote_fenetre, c.cote_fenetre))
        self.fps = 30


        #pygame.display.set_icon(c.iconeicon)
        pygame.display.set_caption(c.titre_fenetre)

    def run(self):
        self.state_machine.add(c.MENU, MenuState.MenuState(self.state_machine))
        self.state_machine.add(c.JEU, NiveauState.NiveauState(self.state_machine ))
        self.state_machine.change(c.MENU)
        self.main_loop()

    def load_asset(self):
        pass

    def main_loop(self):
        while self.continuer:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pg_const.QUIT:
                    self.continuer = False
                self.state_machine.update(event)

            self.state_machine.render(self.fenetre)
            pygame.display.flip()


