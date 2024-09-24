from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.graphics import Ellipse, Line, Color
from random import randint



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

        play_button = Button(text="Стартуєм", size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_game_selection)
        layout.add_widget(play_button)

class GameScreen(Screen):
    def go_to_shindaxp(self, *args):
        self.manager.current = "xp"

    def go_to_shinda95(self, *args):
        self.manager.current = "95"

    def go_to_shindalonghorn(self, *args):
        self.manager.current = "longhorn"

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        self.add_widget(layout)

        play_button = Button(text="Бускетбулл", size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_shindaxp)
        layout.add_widget(play_button)

        play_button = Button(text="Paint", size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_shinda95)
        layout.add_widget(play_button)

        play_button = Button(text="Хокей", size_hint=(1, 0.2))
        play_button.bind(on_press=self.go_to_shindalonghorn)
        layout.add_widget(play_button)


class PaintScreen(Widget):
    def on_touch_down_ellipse(self, touch):
        color= (random(), 1, 1)
        with self.canvas:
            Color(*color,mode = "hsv")
            d = 30
            Ellipse(pos =(touch.x - d/2, touch.y - d/2), size=(d,d))
            touch.ud["line"] = Line(points = (touch.x, touch.y))



class HockeyScreen(Screen):
    score = NumericProperty()

    def __init__(self, **kwargs):
        super(HockeyScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        self.click_count = 0

        # Фон
        self.background = Image(source="hockey.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        layout.add_widget(self.background)

        # М'яч
        self.ball = Image(source="hockey_ball.png", allow_stretch=True, size_hint=(0.2, 0.2),
                          pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.ball.bind(on_touch_down=self.on_ball_click)  # Прив'язка події кліку
        layout.add_widget(self.ball)

        # Мітка для відображення кількості натисків
        self.counter_label = Label(text="Натисків: 0", font_size="30sp", pos_hint={"x": 0.4, "y": 0.8},
                                   size_hint=(0.3, 0.2))
        layout.add_widget(self.counter_label)

        # Кнопка на головний екран
        back_button = Button(text="Назад", size_hint=(0.2, 0.1), pos_hint={"x": 0, "y": 0})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

    def on_ball_click(self, instance, touch):
        if self.ball.collide_point(touch.x, touch.y):
            self.click_count += 1
            self.counter_label.text = f"Натисків: {self.click_count}"
            self.ball_click_animation()

    def go_back(self, *args):
        self.manager.current = "game_selection"

    def ball_click_animation(self):
        anim = Animation(size=(150, 150), duration=0.2)
        anim += Animation(size=(100, 100), duration=0.2)
        anim.start(self.ball)

class BasketballScreen(Screen):
    score = NumericProperty()

    def __init__(self, **kwargs):
        super(BasketballScreen, self).__init__(**kwargs)
        layout = FloatLayout()
        self.add_widget(layout)

        self.click_count = 0

        # Фон
        self.background = Image(source="basketball.png", allow_stretch=True, keep_ratio=False, size_hint=(1, 1))
        layout.add_widget(self.background)

        # М'яч
        self.ball = Image(source="basket.png", allow_stretch=True, size_hint=(0.2, 0.2),
                          pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.ball.bind(on_touch_down=self.on_ball_click)  # Прив'язка події кліку
        layout.add_widget(self.ball)

        # Мітка для відображення кількості натисків
        self.counter_label = Label(text="Натисків: 0", font_size="30sp", pos_hint={"x": 0.4, "y": 0.8},
                                   size_hint=(0.3, 0.2))
        layout.add_widget(self.counter_label)

        # Кнопка на головний екран
        back_button = Button(text="Назад", size_hint=(0.2, 0.1), pos_hint={"x": 0, "y": 0})
        back_button.bind(on_press=self.go_back)
        layout.add_widget(back_button)

    def on_ball_click(self, instance, touch):
        if self.ball.collide_point(touch.x, touch.y):
            self.click_count += 1
            self.counter_label.text = f"Натисків: {self.click_count}"
            self.ball_click_animation()

    def go_back(self, *args):
        self.manager.current = "game_selection"

# Не забудь додати ScreenManager в основний клас App
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(GameScreen(name="game_selection"))
        sm.add_widget(HockeyScreen(name="longhorn"))
        sm.add_widget(BasketballScreen(name="xp"))
            sm.add_widget(PaintScreen(name="95"))
        # додай інші екрани, якщо потрібно5
        return sm

if __name__ == "__main__":
    MyApp().run()
