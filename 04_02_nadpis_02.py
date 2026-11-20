from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class mojaApka(App):
     def build (self):
        plocha = BoxLayout (orientation = "vertical")

        self.pocet_klikov = 0
   self.poipisok.text = Label
        tlacidlo = Button(text = "klikni na")
        tlacidlo.bind(on_press = self.klik)
        return tlacidlo

     def klik(self,kto_zavolal):
           (" niekto na mna klikol")

        self.pocet_klikov  =

     self  .poipisok.text = "Lukas, klikni si(self.pocet_klikov) -krat"
mojaApka().run()