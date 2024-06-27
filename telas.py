from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color, Line
import math


class HomePage(Screen):
    pass


class Emprestimo(Screen):
    def calculate_font_size(self, width):
        initial_font_size = width * 0.11  # Tamanho inicial da fonte
        return initial_font_size / math.log(width * 0.03)


class Catalogo(Screen):
    def calculate_font_size(self, width):
        initial_font_size = width * 0.11  # Tamanho inicial da fonte
        return initial_font_size / math.log(width * 0.03)


class Relatorio(Screen):
    def calculate_font_size(self, width):
        initial_font_size = width * 0.11  # Tamanho inicial da fonte
        return initial_font_size / math.log(width * 0.03)


class PerfilAluno(Screen):
    def calculate_font_size(self, width):
        initial_font_size = width * 0.11  # Tamanho inicial da fonte
        return initial_font_size / math.log(width * 0.15)



class CadastrarAluno(Screen):
    def calculate_font_size(self, width):
        initial_font_size = width * 0.45  # Tamanho inicial da fonte
        return initial_font_size / math.log(width * 0.15)




class LoginPage(Screen):
    def calculate_font_size(self, width):
        initial_font_size = width*0.11  # Tamanho inicial da fonte
        return initial_font_size / math.log(width*0.03)

