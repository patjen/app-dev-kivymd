from kivymd.app import MDApp

class Eingabemaske(MDApp):
    def enter(self):
        eingabe_text = self.root.ids.eingabe.text
        self.root.ids.ausgabe.text = eingabe_text
    
    def clear(self):
        self.root.ids.eingabe.text = ""
        self.root.ids.ausgabe.text = ""

Eingabemaske().run()