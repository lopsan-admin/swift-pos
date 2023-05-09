import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox

class HomeWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class HomeApp(App):
    def build(self):
        return HomeWindow()

if __name__=="__main__":
    ha = HomeApp()
    ha.run()