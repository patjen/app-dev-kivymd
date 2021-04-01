from kivymd.app import App
from kivymd.uix.label import Label

class MainApp(App):
    def build(self):
        label = Label(
            text="Hello from KivyMD",
            size_hint=(.5,.5),
            pos_hint={"center_x": .5, "center_y": .5}
        )
        return label

if __name__ == "__main__":
    app = MainApp()
    app.run()