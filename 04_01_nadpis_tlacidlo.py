from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class mojaApka(App):
    def build (self):
        plocha = BoxLayout(orientation = "vertical")
        plocha.add_widget(Label(text = "zatial nic"))
        plocha.add_widget(Button( text = "klikni na"))

        return plocha

mojaApka().run()