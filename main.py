from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


Window.size = (800,600)

class ButtoFF(App):
    def build(self):
        layout = BoxLayout(orientation = "vertical")
        button1 = Button(text="Баскетбол")
        layout.add_widget(button1)
        button1.bind(on_press=self.on_button1_press)

