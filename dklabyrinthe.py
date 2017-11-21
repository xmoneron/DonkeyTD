"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.
"""
import pygame
from pygame.locals import *
from constantes import *
from classes import MenuState, StateMachine, NiveauState


def main():
    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
    icone = pygame.image.load(image_icone)
    titre_fenetre = "DK"
    fps = 50
    clock = pygame.time.Clock()
    pygame.display.set_icon(icone)
    pygame.display.set_caption(titre_fenetre)

    state_machine = StateMachine()
    state_machine.add(MENU,MenuState(state_machine))
    state_machine.add(JEU, NiveauState (state_machine))
    state_machine.change(MENU)


    continuer = True
    while continuer:
        clock.tick(fps)


        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            state_machine.update(event)

        state_machine.render(fenetre)
        pygame.display.flip()

if __name__ == '__main__':
    main()

