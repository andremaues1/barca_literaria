from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle,Color
from datetime import datetime


class BannerEmprestimo(GridLayout):
    def __init__(self, **kwargs):
        self.rows = 1
        super().__init__()


        with self.canvas:
            Color(rgb=(0.8,0.8,0.8,1))
            self.rec = Rectangle(size=(self.width-200, self.height),pos=(self.x+100, self.y-60))
        self.bind(size=self.atualizar_rec,pos=self.atualizar_rec) # serve pra atualizar o retangulo quando voce redimensionar a tela

        titulo = kwargs['titulo']
        autor = kwargs['autor']
        nome = kwargs['nome']
        status = kwargs['status']
        id_livro = kwargs['id_livro']
        id_aluno = kwargs['id_aluno']
        data_expiracao = kwargs['data_expiracao']
        try:
            dia = int(data_expiracao[0:2])
            mes = int(data_expiracao[3:5])

            if data_expiracao[0] == 0:
                dia = int(data_expiracao[1])
            if data_expiracao[3] == 0:
                mes = int(data_expiracao[4])
            ano = int(data_expiracao[6:10])
            data = datetime(ano, mes, dia,0,0,0)
        except:
            pass
        difference = data - datetime.now()

        # Calculate total days from timedelta
        total_days = difference.days + difference.seconds / (24 * 3600)



        esquerda = FloatLayout()
        esquerda_label1 = Label(text=f"Nome do aluno: {nome}", pos_hint={"right": 1.15, "top": 0.4}, size_hint=(1, 0.33),color=(0,0,0,1))
        esquerda_label2 = Label(text=f'ID do aluno: {id_aluno   }', pos_hint={"right": 1.15, "top": 0.1}, size_hint=(1, 0.33),color=(0,0,0,1))


        esquerda.add_widget(esquerda_label1)
        esquerda.add_widget(esquerda_label2)


        meio = FloatLayout()
        meio_label1 = Label(text=f"Título do livro: {titulo}", pos_hint={"right": 0.9, "top": 0.4}, size_hint=(1, 0.33),color=(0,0,0,1))
        meio_label2 = Label(text=f"Autor: {autor}", pos_hint={"right": 0.9, "top": 0.1}, size_hint=(1, 0.33),color=(0,0,0,1))
        meio_label3 = Label(text=f"ID do livro: {id_livro}", pos_hint={"right": 0.9, "top": -0.2}, size_hint=(1, 0.33),
                       color=(0, 0, 0, 1))

        meio.add_widget(meio_label1)
        meio.add_widget(meio_label2)
        meio.add_widget(meio_label3)

        direita = FloatLayout()
        if total_days <= 5 and total_days > 0:
            direita_label_data = Label(text=f"Data de expiração: {data_expiracao}", pos_hint={"right": 0.75, "top": 0.4}, size_hint=(1, 0.33),color=(1,1,0,1),bold=True)
        elif total_days <= 0:
            direita_label_data = Label(text=f"Data de expiração: {data_expiracao}",
                                       pos_hint={"right": 0.75, "top": 0.4}, size_hint=(1, 0.33), color=(1, 0, 0, 1),bold=True)
        else:
            direita_label_data = Label(text=f"Data de expiração: {data_expiracao}",
                                       pos_hint={"right": 0.75, "top": 0.4}, size_hint=(1, 0.33), color=(0, 0, 0, 1))
        direita_label_preco = Label(text=f"Status do livro: {status}", pos_hint={"right": 0.75, "top": 0.1},
                                    size_hint=(1, 0.33),color=(0,0,0,1))


        direita.add_widget(direita_label_data)
        direita.add_widget(direita_label_preco)


        self.add_widget(esquerda)
        self.add_widget(meio)
        self.add_widget(direita)

    def atualizar_rec(self, *args):  # o *args é necessário pra receber argumentos
        self.rec.pos = (self.x+100, self.y-60)
        self.rec.size = (self.width-200, self.height)