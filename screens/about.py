from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from screens.base import CustomScreen


def get_json_response_callback(screen_obj):
    def json_response_callback(req, result):
        url = result[0]['url']
        screen_obj.open_popup(url)

    return json_response_callback


class AboutScreen(CustomScreen):
    title = 'about'

    def open_popup(self, url):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=url, size_hint_y=1))
        layout.add_widget(AsyncImage(source=url, size_hint_y=10))

        self._popup = Popup(
            title="Cat",
            content=layout,
            size_hint=(.8, .8)
        )
        self._popup.open()

    def cat(self, *args, **kwargs):
        req = UrlRequest('https://api.thecatapi.com/v1/images/search', get_json_response_callback(self))
