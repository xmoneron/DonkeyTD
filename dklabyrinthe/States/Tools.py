class EmptyState:
    def update(self, event):
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

    def update(self, pygame_event):
        """

        :param pygame_event:
        :return:
        """
        self._states[self._current_state].update(pygame_event)

    def render(self, fenetre):
        """

        :param fenetre:
        :return:
        """
        self._states[self._current_state].render(fenetre)

    def change(self, state_name, param=None):
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


def _States():
    def __init__(self):
        self._stateMachine = None

    def update():
        pass

    def draw():
        pass

    def on_enter(self):
        pass

    def render(self):
        pass

    def on_exit(self):
        pass




