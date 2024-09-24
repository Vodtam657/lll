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
from random import random




class PaintScreen(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode="hsv")
            d = 30
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud["line"] = Line(points=(touch.x, touch.y))


    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]

class MyPaintApp(App):
    def build(self):
        paint = Widget()
        self.painted = PaintScreen()
        clear_button = Button(text = "Clear")
        clear_button.bind(on_release = self.clear_canvas)
        paint.add_widget(self.painted)
        paint.add_widget(clear_button)
        return paint

    def clear_canvas(self, obj):
        self.painted.canvas.clear()

if __name__ == "__main__":
    MyPaintApp().run()




