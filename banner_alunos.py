from kivy.uix.label import Label
from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle,Color
from botoes import LabelButton,ImageButton
from kivy.uix.button import Button
from datetime import datetime



class BannerAlunos(GridLayout):
    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()


        with self.canvas:
            Color(rgb=(135/255,206/255,250/255,1))
            self.rec = Rectangle(size=(self.width-200, self.height),pos=(self.x+100, self.y-60))
        self.bind(size=self.atualizar_rec,pos=self.atualizar_rec) # serve pra atualizar o retangulo quando voce redimensionar a tela



        nome = kwargs['nome']
        data_nascimento = kwargs['data_nascimento']
        endereco = kwargs['endereco']
        telefone = kwargs['telefone']
        email = kwargs['email']
        id = kwargs['id']
        try:
            ano = int(data_nascimento[6:10])
        except:
            ano = datetime.now().year
        atual = datetime.now().year
        self.funcao = kwargs['funcao']
        quant_visitas = kwargs['quant_visitas']
        genero_favorito = kwargs['genero_fav']
        livro_favorito = kwargs['livro_fav']
        autor_favorito = kwargs['autor_fav']




        esquerda = FloatLayout()
        esquerda_label1 = LabelButton(text=f"Nome: {nome}", pos_hint={"right": 1.25, "top": 0.4}, size_hint=(1, 0.2),color=(0,0,0,1), size_hint_y=None, valign='top')
        esquerda_label2 = LabelButton(text=f"ID: {id}", pos_hint={"right": 0.95, "top": 0.4}, size_hint=(1, 0.2),color=(0,0,0,1), size_hint_y=None, valign='top')
        esquerda_label3= LabelButton(text=f"Total de visitas: {quant_visitas}", pos_hint={"right": 1.05, "top": 0.1}, size_hint=(1, 0.2),
                                      color=(0, 0, 0, 1), size_hint_y=None, valign='top')
        esquerda_label1.bind(texture_size=esquerda_label1.setter('size'))
        max_chars_per_line = 15
        esquerda_label1.text_size = (esquerda.width, None)
        esquerda_label1.text_size = (max_chars_per_line * esquerda_label1.font_size, None)



        esquerda.add_widget(esquerda_label1)
        esquerda.add_widget(esquerda_label2)
        esquerda.add_widget(esquerda_label3)



        meio = FloatLayout()
        meio_label1 = LabelButton(text=f"Endereço: {endereco}", pos_hint={"right": 0.82, "top": 0.45}, size_hint=(1, 0.2),color=(0,0,0,1), size_hint_y=None, valign='top')
        meio_label2 = LabelButton(text=f"Data de nascimento: {data_nascimento}", pos_hint={"right": 0.7, "top": 0}, size_hint=(1, 0.2),color=(0,0,0,1), size_hint_y=None, valign='top')
        meio_label3 = LabelButton(text=f"Idade: {atual-ano}", pos_hint={"right": 0.42, "top": 0.2},
                                  size_hint=(1, 0.2), color=(0, 0, 0, 1), size_hint_y=None, valign='top')

        meio_label1.bind(texture_size=meio_label1.setter('size'))
        max_chars_per_line = 18
        meio_label1.text_size = (meio.width, None)
        meio_label1.text_size = (max_chars_per_line * meio_label1.font_size, None)

        if not nome == "Turma":
            meio.add_widget(meio_label1)
            meio.add_widget(meio_label2)
            meio.add_widget(meio_label3)

        direita = FloatLayout()
        direita_label_data = LabelButton(text=f"Telefone: {telefone}", pos_hint={"right": 0.38, "top": 0.8}, size_hint=(1, 0.2),color=(0,0,0,1), size_hint_y=None, valign='top')
        direita_label_preco = LabelButton(text=f"Email: {email}", pos_hint={"right": 0.86, "top": 0},
                                    size_hint=(1, 0.2),color=(0,0,0,1), size_hint_y=None, valign='top')
        direita_label_data1 = LabelButton(text=f"Genêro favorito: {genero_favorito}", pos_hint={"right": 0.56, "top": 0.6},
                                         size_hint=(1, 0.2), color=(0, 0, 0, 1), size_hint_y=None, valign='top')
        direita_label_data2 = LabelButton(text=f"Livro favorito: {livro_favorito}",pos_hint={"right": 0.495, "top": 0.4},size_hint=(1, 0.2), color=(0, 0, 0, 1), size_hint_y=None, valign='top')
        direita_label_data3 = LabelButton(text=f"Livro favorito: {autor_favorito}",
                                          pos_hint={"right": 0.6, "top": 0.2}, size_hint=(1, 0.2), color=(0, 0, 0, 1),
                                          size_hint_y=None, valign='top')
        direita_imagem = ImageButton(source="Images/lixeira_azul.jpg", pos_hint={"right": 1.2, "top": 0.1},
                                          size_hint=(1.3, 0.3))

        max_chars_per_line = 21
        direita_label_preco.text_size = (direita.width, None)
        direita_label_preco.text_size = (max_chars_per_line * direita_label_preco.font_size, None)

        direita_imagem.bind(on_touch_down=self.on_touch_down)

        direita.add_widget(direita_label_data1)
        direita.add_widget(direita_label_data2)
        direita.add_widget(direita_label_data3)

        if not nome == "Turma":
            direita.add_widget(direita_imagem)
            direita.add_widget(direita_label_preco)
            direita.add_widget(direita_label_data)



        self.add_widget(esquerda)
        self.add_widget(meio)
        self.add_widget(direita)


    def atualizar_rec(self, *args):  # o *args é necessário pra receber argumentos
        self.rec.pos = (self.x+100, self.y-60)
        self.rec.size = (self.width-210, self.height)

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


