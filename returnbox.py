from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class MojaApp(App):
    def build(self) -> BoxLayout:
       from kivy.uix.gridlayout import GridLayout

def build(self) -> GridLayout:
    koren = GridLayout(cols=3)
    koren.add_widget(Button(text="A"))
    koren.add_widget(Button(text="B"))
    koren.add_widget(Button(text="C"))
    koren.add_widget(Button(text="D"))
    koren.add_widget(Button(text="E"))
    return koren

MojaApp().run()
