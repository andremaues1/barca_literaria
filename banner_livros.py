from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle,Color
from botoes import *


class BannerLivros(GridLayout):
    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()


        with self.canvas:
            Color(rgb=(0.8,0.8,0.8,1))
            self.rec = Rectangle(size=(self.width-200, self.height),pos=(self.x+100, self.y-60))
        self.bind(size=self.atualizar_rec,pos=self.atualizar_rec) # serve pra atualizar o retangulo quando voce redimensionar a tela

        titulo = kwargs['titulo']
        autor = kwargs['autor']
        genero = kwargs['genero']
        faixa_etaria = kwargs['faixa_etaria']
        status = kwargs['status']
        numero_paginas = kwargs['numero_paginas']
        quantidade = kwargs['quantidade']
        data_aquisicao = kwargs['data_aquisicao']
        id = kwargs['id']
        self.funcao = kwargs['funcao']

        esquerda = FloatLayout()
        esquerda_label1 = Label(text=f"Título: {titulo}", pos_hint={"right": 1.15, "top": 0.4}, size_hint=(1, 0.33),color=(0,0,0,1))
        esquerda_label2 = Label(text=f'Autor: {autor}', pos_hint={"right": 1.15, "top": 0.1}, size_hint=(1, 0.33),color=(0,0,0,1))
        esquerda_label3 = Label(text=f'ID: {id}', pos_hint={"right": 1.15, "top": -0.2}, size_hint=(1, 0.33),color=(0,0,0,1))

        esquerda.add_widget(esquerda_label1)
        esquerda.add_widget(esquerda_label2)
        esquerda.add_widget(esquerda_label3)

        meio = FloatLayout()
        meio_label1 = Label(text=f"Faixa etária: {faixa_etaria}", pos_hint={"right": 0.9, "top": 0.4}, size_hint=(1, 0.33),color=(0,0,0,1))
        meio_label2 = Label(text=f"Gênero: {genero}", pos_hint={"right": 0.9, "top": 0.1}, size_hint=(1, 0.33),color=(0,0,0,1))
        meio_label3 = Label(text=f"Status: {status}", pos_hint={"right": 0.9, "top": -0.2}, size_hint=(1, 0.33),
                       color=(0, 0, 0, 1))

        meio.add_widget(meio_label1)
        meio.add_widget(meio_label2)
        meio.add_widget(meio_label3)

        direita = FloatLayout()
        direita_label_data = Label(text=f"Data de aquisição: {data_aquisicao}", pos_hint={"right": 0.65, "top": 0.4}, size_hint=(1, 0.33),color=(0,0,0,1))
        direita_label_preco = Label(text=f"Número de páginas: {numero_paginas}", pos_hint={"right": 0.65, "top": 0.1},
                                    size_hint=(1, 0.33),color=(0,0,0,1))
        direita_label_quantidade = Label(text=f"Quantidade em estoque: {quantidade}", pos_hint={"right": 0.65, "top": -0.2},
                                         size_hint=(1, 0.33),color=(0,0,0,1))
        direita_imagem = ImageButton(source="Images/lixeira_preta.png", pos_hint={"right": 1.25, "top": 0.1},
                                     size_hint=(1.3, 0.3))

        direita_imagem.bind(on_touch_down=self.on_touch_down)

        direita.add_widget(direita_label_data)
        direita.add_widget(direita_label_preco)
        direita.add_widget(direita_label_quantidade)
        direita.add_widget(direita_imagem)



        self.add_widget(esquerda)
        self.add_widget(meio)
        self.add_widget(direita)

    def atualizar_rec(self, *args):  # o *args é necessário pra receber argumentos
        self.rec.pos = (self.x+100, self.y-60)
        self.rec.size = (self.width-200, self.height)


    def on_touch_down(self, touch,*args):
        # Verifica se o toque ocorreu dentro do retângulo
        if self.is_within_rectangle(touch.pos):
            self.funcao()


    def is_within_rectangle(self, touch_pos):
        # Calcula a área do retângulo
        rect_x, rect_y = self.rec.pos
        rect_width, rect_height = self.rec.size
        rect_right = rect_x + rect_width
        rect_top = rect_y + rect_height

        # Verifica se o toque ocorreu dentro do retângulo
        if (rect_x <= touch_pos[0] <= rect_right and
                rect_y <= touch_pos[1] <= rect_top):
            return True
        return False