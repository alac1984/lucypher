from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget, ObjectProperty, ListProperty
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.write()


kv = Builder.load_file('app.kv')


class MainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MainApp().run()
