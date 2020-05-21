"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lynn Myat Aung
Started 9/5/2020
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lynn Myat Aung'


class SquareNumberApp(App):
    
    def build(self):

        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):

        result = value ** 2
        self.root.ids.output_label.text = str(result)


SquareNumberApp().run()
