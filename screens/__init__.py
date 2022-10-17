from kivy.uix.screenmanager import FadeTransition as Transition
from kivy.uix.screenmanager import ScreenManager

from screens.about import AboutScreen
from screens.balance import BalanceScreen
from screens.menu import MenuScreen
from screens.title import TitleScreen


class MynanceScreenManager(ScreenManager):
    def __init__(self, *args, **kwargs):
        kwargs['transition'] = Transition()

        super().__init__(*args, **kwargs)
        for screen in [
            TitleScreen(),
            BalanceScreen(),
            AboutScreen(),
            MenuScreen(),
        ]:
            self.add_widget(screen)


