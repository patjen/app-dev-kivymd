from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.widget import Widget

class Notizen(MDApp):
    anzahl = 0

    def add_note(self, text):
        button = MyButton(text)
        self.root.ids.liste.add_widget(button)
        self.anzahl = self.anzahl + 1
        self.update_counter()

    def remove_note(self, id):
        self.root.ids.liste.remove_widget(id)
        self.anzahl = self.anzahl -1
        self.update_counter()

    def update_counter(self):
        if self.anzahl > 0:
            self.root.ids.toolbar.title = str(self.anzahl) + " Notizen"
        else:
            self.root.ids.toolbar.title = "Notizen"

class MyButton(BoxLayout):

    def __init__(self, text):
        self.c += 1
        super().__init__()
        self.ids.textfeld.text = text
    
    def set_button_text(self, text):
        self.ids.button.text = text


Notizen().run()