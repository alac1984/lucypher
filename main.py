from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.core.text import LabelBase
Config.set('graphics', 'resizable', False)
Config.write()

LabelBase.register(
    name="Syncopate",
    fn_regular="Syncopate-Regular.ttf",
    fn_bold="Syncopate-Bold.ttf"
)


Builder.load_file('app.kv')


class TitleBar(BoxLayout):
    def focus(*args, **kwargs):
        print(args)


class Root(GridLayout):
    pass


class MainApp(App):
    def build(self):
        return Root()


if __name__ == "__main__":
    MainApp().run()
