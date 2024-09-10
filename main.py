from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


Window.size = (800, 600)



class MainScreen(Screen):
    def go_to_game_selection(self, *args):
        self.manager.current = "game_selection"

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        self.add_widget(layout)

        self.title = Label(text="Шиндовс", font_size="48sp", size_hint=(1, 0.8))
        layout.add_widget(self.title)

        play_button = Button(text="стартуєм", size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_game_selection)
        layout.add_widget(play_button)



class GameScreen(Screen):
    def go_to_shindaxp(self, *args):
        self.manager.current = "xp"

    def go_to_shinda95(self, *args):
        self.manager.current = "95"

    def __init__(self,**kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")
        self.add_widget(layout)

        play_button = Button(text="Бускетбулл", size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_shindaxp)
        layout.add_widget(play_button)

        play_button = Button(text="КопКоп", size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_shinda95)
        layout.add_widget(play_button)


class BasketballScreen(Screen):
    def __init__(self, **kwargs):
        super(BasketballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        self.background = Image(source = ".png", size_hint=(1, 1))
        layout.add_widget(self.background)
        self.ball = Image(source = ".png",)

# Створити дві бутон





class ClickerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(GameScreen(name="game_selection"))
        return sm


if __name__ == "__main__":
    ClickerApp().run()








