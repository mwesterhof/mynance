from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from screens import MynanceScreenManager


Window.keyboard_anim_args = {"d":.2,"t":"linear"}
Window.softinput_mode = "below_target"


class TitleBar(BoxLayout):
    title = StringProperty("")


class MynanceApp(App):
    balance = NumericProperty(0)

    def build(self):
        screens = MynanceScreenManager()
        return screens


if __name__ == '__main__':
    MynanceApp().run()
