from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class mojaApka(App):
    def build (self):
        plocha = BoxLayout(orientation = "vertical")

        popisok = Label( text = zatial nic)
        plocha.add_widget(popisok)

    tlacidlo = Button  (text( "klikli na mna"))
    tlacidlo.bind(on_press = self.klik)
    plocha.add_widget(tlacidlo)
   
 return tlacidlo

def klik (selgf,kto_zavolal)
   print ("Niekto na mna klikol")
    
  MojaApka().run()
