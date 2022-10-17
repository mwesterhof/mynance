from kivy.uix.screenmanager import ScreenManager, Screen


class CustomScreen(Screen):
    @property
    def title(self):
        raise NotImplementedError('title')

    def __init__(self, *args, **kwargs):
        name = self.title
        kwargs.setdefault('name', name)
        super().__init__(*args, **kwargs)
