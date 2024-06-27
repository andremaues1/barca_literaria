from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *
import requests
from datetime import date
from banner_livros import BannerLivros
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Line
from functools import partial
from banner_alunos import BannerAlunos
import json
from banner_emprestimo import BannerEmprestimo
from datetime import datetime
from kivy.core.window import Window












GUI = Builder.load_file("main.kv")



# Cria a class do app
class MainApp(App):

    def mudar_tela(self,id_telas):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_telas


    def on_start(self):

        # inicia os banners
        self.lista_livros()
        self.lista_alunos()
        self.lista_emprestimo()


        # faz o usuario logar automaticamente caso ele já tenha logado antes
        try:
            with open("refresh Token.txt", "r") as arquivo:
                conta_salva = json.load(arquivo)
                if conta_salva['login'] == "barcaliteraria14@gmail.com" and conta_salva['senha'] == "Barca_unida@13":
                    self.mudar_tela("homepage")
                else:
                    pass
        except:
            pass



        #Criando página de cadastro



        label_telefone = Label(text="Número de telefone: ", color=(0, 0, 0, 1), size_hint=(0.1, 0.2),
                               pos_hint={"right":1,"top":0.55},font_size=Window.width*0.017)
        telefone = TextInput(color=(0, 0, 0, 1), background_color=(1, 1, 1, 0), size_hint=(0.5, 0.04),
                             pos_hint={"right": 2, "top": 0.47},multiline=False,text="")  # Ajustado pos_hint
        caixa_telefone1 = BoxLayout(size_hint_x=0.1, size_hint_y=1, pos_hint={'right': 0.33, 'top': 1})
        caixa_telefone2 = BoxLayout(size_hint_x=0.235, size_hint_y=1, pos_hint={'right': 0.6, 'top': 1})
        with telefone.canvas.before:
            Color(0, 0, 0, 1)
            Line(width=1, rectangle=(telefone.x+366, telefone.y+323, telefone.width+134, telefone.height-72))

        pagina_cadastro = self.root.ids['cadastrar_aluno']
        flot_pagina = pagina_cadastro.ids['registro_aluno']

        caixa_telefone1.add_widget(label_telefone)
        caixa_telefone2.add_widget(telefone)
        flot_pagina.add_widget(caixa_telefone1)
        flot_pagina.add_widget(caixa_telefone2)




        label_email = Label(text="Email: ", color=(0, 0, 0, 1), size_hint=(0.1, 0.2),
                               pos_hint={"right":0.68,"top":0.55},font_size=Window.width*0.017)
        email = TextInput(color=(0, 0, 0, 1), background_color=(1, 1, 1, 0), size_hint=(0.2, 0.04),
                             pos_hint={"right":0.86,"top":0.47}, multiline=False, text="")  # Ajustado pos_hint
        caixa_email1 = BoxLayout(size_hint_x=0.1, size_hint_y=1, pos_hint={'right': 0.68, 'top': 1})
        caixa_email = BoxLayout(size_hint_x=0.235, size_hint_y=1, pos_hint={'right': 0.89, 'top': 1})
        with email.canvas.before:
            Color(0, 0, 0, 1)
            Line(width=1, rectangle=(telefone.x + 654, telefone.y + 323, telefone.width + 135, telefone.height - 72))

        pagina_cadastro = self.root.ids['cadastrar_aluno']
        cadastro_email = pagina_cadastro.ids['cadastro_email']

        caixa_email1.add_widget(label_email)
        caixa_email.add_widget(email)
        cadastro_email.add_widget(caixa_email1)
        cadastro_email.add_widget(caixa_email)


        pagina_cadastro = self.root.ids['cadastrar_aluno']
        RADIOBUTTONS = pagina_cadastro.ids['registro_aluno']
        choose_box1 = BoxLayout(size_hint_x=0.1, size_hint_y=0.4,pos_hint={'right':0.5,'top':0.57})
        choose_box2 = BoxLayout(size_hint_x=0.15, size_hint_y=1, pos_hint={'right': 0.4, 'top': 1})
        choose_box3 = BoxLayout(size_hint_x=0.1, size_hint_y=1, pos_hint={'right': 0.5, 'top': 1.03})
        numero_label = Label(text="Aluno tem email?", pos_hint={"right": 0, "top": 0.57},
                                      size_hint=(0.4, 0.57), color=(0, 0, 0, 1),font_size=Window.width*0.017)
        numero_label_nao = Label(text="Não", pos_hint={"right": 0, "top": 0.58},
                             size_hint=(0.4, 0.57), color=(0, 0, 0, 1),font_size=Window.width*0.017)
        numero_label_sim = Label(text="Sim", pos_hint={"right": 0, "top": 0.58},
                                 size_hint=(0.4, 0.57), color=(0, 0, 0, 1),font_size=Window.width*0.017)
        first_check = CheckBox(group='numero', size_hint_x=0.4, size_hint_y=0.57, color=[0, 0, 0],
                               allow_no_selection=False,active=True)
        second_check = CheckBox(group='numero', size_hint_x=0.4, size_hint_y=0.57, color=[0, 0, 0],
                                allow_no_selection=False)

        first_check.bind(
            active=partial(self.toggle_telefone_widgets, True, cadastro_email, caixa_email1, caixa_email))
        second_check.bind(
            active=partial(self.toggle_telefone_widgets, False, cadastro_email, caixa_email1, caixa_email))

        choose_box1.add_widget(first_check)
        choose_box1.add_widget(second_check)
        choose_box2.add_widget(numero_label)
        choose_box3.add_widget(numero_label_sim)
        choose_box3.add_widget(numero_label_nao)
        RADIOBUTTONS.add_widget(choose_box1)
        RADIOBUTTONS.add_widget(choose_box2)
        RADIOBUTTONS.add_widget(choose_box3)

        pagina_cadastro = self.root.ids['cadastrar_aluno']
        RADIOBUTTONS2 = pagina_cadastro.ids['registro_aluno']
        escolher_box1 = BoxLayout(size_hint_x=0.1, size_hint_y=0.1, pos_hint={'right': 0.6, 'top': 0.45})
        escolher_box2 = BoxLayout(size_hint_x=0.15, size_hint_y=0.5, pos_hint={'right': 0.45, 'top': 0.73})
        escolher_box3 = BoxLayout(size_hint_x=0.1, size_hint_y=0.5, pos_hint={'right': 0.6, 'top': 0.77})
        email_label = Label(text="Aluno tem número de telefone?", pos_hint={"right": 0, "top": 0.57},
                             size_hint=(0.4, 0.57), color=(0, 0, 0, 1),font_size=Window.width*0.017)
        email_label_nao = Label(text="Não", pos_hint={"right": 0, "top": 0.57},
                                 size_hint=(0.4, 0.57), color=(0, 0, 0, 1),font_size=Window.width*0.017)
        email_label_sim = Label(text="Sim", pos_hint={"right": 0, "top": 0.57},
                                 size_hint=(0.4, 0.57), color=(0, 0, 0, 1),font_size=Window.width*0.017)
        first_check_email = CheckBox(group='email', size_hint_x=0.4, size_hint_y=0.57, color=[0, 0, 0],
                               allow_no_selection=False,active=True)
        second_check_email = CheckBox(group='email', size_hint_x=0.4, size_hint_y=0.57, color=[0, 0, 0],
                                allow_no_selection=False)

        first_check_email.bind(active=partial(self.toggle_telefone_widgets, True,flot_pagina,caixa_telefone1,caixa_telefone2))
        second_check_email.bind(active=partial(self.toggle_telefone_widgets, False,flot_pagina,caixa_telefone1,caixa_telefone2))

        escolher_box1.add_widget(first_check_email)
        escolher_box1.add_widget(second_check_email)
        escolher_box2.add_widget(email_label)
        escolher_box3.add_widget(email_label_sim)
        escolher_box3.add_widget(email_label_nao)
        RADIOBUTTONS2.add_widget(escolher_box1)
        RADIOBUTTONS2.add_widget(escolher_box2)
        RADIOBUTTONS2.add_widget(escolher_box3)







        pagina_cadastro = self.root.ids['cadastrar_aluno']
        cadastro_final = pagina_cadastro.ids['cadastrar']
        cadastro_final.on_release = partial(self.criar_pop_up_cadastro,telefone,email,first_check_email,first_check)

    def toggle_telefone_widgets(self, active,flot_pagina,caixa_telefone1,caixa_telefone2, *args):
        if active:
            # Adicionar widgets de telefone se não estiverem presentes
            if caixa_telefone1.parent is None:
                flot_pagina.add_widget(caixa_telefone1)
            if caixa_telefone2.parent is None:
                flot_pagina.add_widget(caixa_telefone2)
        else:
            # Remover widgets de telefone se estiverem presentes
            if caixa_telefone1.parent is not None:
                flot_pagina.remove_widget(caixa_telefone1)
            if caixa_telefone2.parent is not None:
                flot_pagina.remove_widget(caixa_telefone2)

    def criar_pop_up_cadastro(self,telefone,email,first_check_email,first_check):
            pagina_cadastro = self.root.ids['cadastrar_aluno']
            confirmacao_cadastro = pagina_cadastro.ids['confirmacao_cadastro']
            nome = pagina_cadastro.ids['nome'].text
            data_nascimento = pagina_cadastro.ids['data_nascimento'].text
            endereco = pagina_cadastro.ids['endereco'].text
            telefone_aluno = telefone.text
            email_aluno = email.text

            try:
                if data_nascimento[2] != "/" or data_nascimento[5] != "/" or len(data_nascimento) != 10:
                    data_confirmacao = True
                else:
                    data_confirmacao = False

            except IndexError:
                data_confirmacao = True


            if nome == "":
                confirmacao_cadastro.text = "Campo nome vazio"
                confirmacao_cadastro.color = (1,0,0,1)
            elif data_nascimento == "":
                confirmacao_cadastro.text = "Campo de data vazia"
                confirmacao_cadastro.color = (1,0,0,1)
            elif data_confirmacao:
                confirmacao_cadastro.text = "Data deve ser no formato dd/mm/aa"
                confirmacao_cadastro.color = (1, 0, 0, 1)



            elif endereco == "":
                confirmacao_cadastro.text = "Campo de endereço vazio"
                confirmacao_cadastro.color = (1,0,0,1)
            elif telefone_aluno == "" and first_check_email.active:
                confirmacao_cadastro.text = "Campo de telefone vazio"
                confirmacao_cadastro.color = (1,0,0,1)
            elif (telefone_aluno[0] != "(" and first_check_email.active) or (telefone_aluno[3] != ")" and first_check_email.active):
                confirmacao_cadastro.text = "DDD deve ser no formato (XX)"
                confirmacao_cadastro.color = (1,0,0,1)
            elif email_aluno == "" and first_check.active:
                confirmacao_cadastro.text = "Campo de email vazio"
                confirmacao_cadastro.color = (1,0,0,1)
            else:


                caixa_pop_up = FloatLayout(size=(600, 430), pos_hint={'center_x': 0.5, 'center_y': 0.5})

                # dicionando o botão "Sim"
                button_sim = Button(text="Sim", pos_hint={"right": 0.45, "top": 0.4}, size_hint=(0.18, 0.1),
                                    color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                                    on_release=lambda instance: self.adicionar_aluno(telefone,email,caixa_pop_up,first_check_email,first_check))

                # Adicionando instruções de desenho ao canvas do botão "Sim"
                with button_sim.canvas.before:
                    Color(0.9, 0.9, 0.9, 1)  # Cor do retângulo (verde)
                    Rectangle(size=(button_sim.width + 600, button_sim.height + 350),  # Aumentando o tamanho
                              pos=(button_sim.x + 150, button_sim.y + 160))
                    Color(135 / 255, 206 / 255, 250 / 255, 1)
                    Line(
                        rectangle=(button_sim.x + 150, button_sim.y + 610, button_sim.width + 600, button_sim.height - 550),
                        width=2, color=(135 / 255, 206 / 255, 250 / 255, 1))
                    Color(0, 1, 0, 1)
                    Line(width=2,
                         rectangle=(button_sim.x + 266, button_sim.y + 221, button_sim.width + 89, button_sim.height - 17))

                # Adicionando o botão "Sim" ao FloatLayout
                caixa_pop_up.add_widget(button_sim)

                # Adicionando o botão "Não"
                button_nao = Button(text="Não", pos_hint={"right": 0.75, "top": 0.4}, size_hint=(0.18, 0.1),
                                    color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal=""
                                  ,on_release=lambda instance: self.remover_pop_up_cadastro(caixa_pop_up))

                # Adicionando instruções de desenho ao canvas do botão "Não"
                with button_nao.canvas.before:
                    Color(1, 0, 0, 1)
                    Line(width=2,
                         rectangle=(button_nao.x + 565, button_nao.y + 221, button_nao.width + 89, button_nao.height - 17))

                # Adicionando o botão "Não" ao FloatLayout
                caixa_pop_up.add_widget(button_nao)

                # Adicionando o Label
                label_confirmacao = Label(text="Você deseja confirmar essa ação?", pos_hint={"right": 0.6, "top": 0.7},
                                          size_hint=(0.18, 0.1), color=(0, 0, 0, 1))

                # Adicionando o Label ao FloatLayout
                caixa_pop_up.add_widget(label_confirmacao)

                catalogo = self.root.ids['cadastrar_aluno']

                catalogo.add_widget(caixa_pop_up)



    def adicionar_livro(self,caixa):
        catalogo = self.root.ids['catalogo']
        alerta = catalogo.ids['confirmacao']
        titulo = catalogo.ids['titulo'].text
        titulo = str(titulo.lower())
        autor = catalogo.ids['autor'].text
        autor = str(autor.lower())
        numero_paginas = str(catalogo.ids['pagina'].text)
        quantidade = str(catalogo.ids['quantidade'].text)
        genero = str(catalogo.ids['btn'].text)
        faixa_etaria = str(catalogo.ids['btn11'].text)
        status = str(catalogo.ids['btn14'].text)
        data_aquisicao = date.today()
        data_aquisicao = str(data_aquisicao.strftime('%d/%m/%Y'))



        try:
            numero_paginas = int(numero_paginas)
        except:
            pass
        try:
            quantidade = int(quantidade)
        except:
            pass
        self.remover_lista_livros()

        buscado = requests.get(f'https://catalogo-barca-default-rtdb.firebaseio.com/1/id_proximo_vendedor/.json').json()
        print(buscado)
        id_real = int(buscado) + 1

        id = '*'.join([titulo, autor, genero, faixa_etaria, str(numero_paginas), status])


        buscar = requests.get(f'https://catalogo-barca-default-rtdb.firebaseio.com/.json?orderBy="id"&equalTo="{id}"').json()

        chave = list(buscar.keys())

        if buscar != {}:
            quantidade = float(buscar[chave[0]]['quantidade']) + quantidade
            info = (
                f'{{"titulo": "{titulo}","autor": "{autor}","genero":"{genero}","faixa etaria":"{faixa_etaria}",'
                f'"status":"{status}","numero de paginas":"{numero_paginas}",'
                f'"quantidade":"{quantidade}","data de aquisicao":"{data_aquisicao}","id":"{id}"}}')
            requests.patch(f'https://catalogo-barca-default-rtdb.firebaseio.com/{chave[0]}.json', data=info)

            self.lista_livros()
            self.remover_pop_up(caixa)

        else:
            data_info = f'{{"id_proximo_vendedor":"{id_real}"}}'
            info = (
                f'{{"titulo": "{titulo}","autor": "{autor}","genero":"{genero}","faixa etaria":"{faixa_etaria}",'
                f'"status":"{status}","numero de paginas":"{numero_paginas}",'
                f'"quantidade":"{quantidade}","data de aquisicao":"{data_aquisicao}","id":"{id}","id_real":"{id_real}"}}')
            requests.post('https://catalogo-barca-default-rtdb.firebaseio.com/.json',data=info)
            requests.patch('https://catalogo-barca-default-rtdb.firebaseio.com/1/.json',data=data_info)

            self.lista_livros()
            self.remover_pop_up(caixa)



    def excluir_livro(self,caixa):
        catalogo = self.root.ids['catalogo']
        alerta = catalogo.ids['confirmacao']
        titulo = catalogo.ids['titulo'].text
        titulo = titulo.lower()
        autor = catalogo.ids['autor'].text
        autor = autor.lower()
        numero_paginas = catalogo.ids['pagina'].text
        quantidade = catalogo.ids['quantidade'].text
        genero = catalogo.ids['btn'].text
        faixa_etaria = catalogo.ids['btn11'].text
        status = catalogo.ids['btn14'].text
        data_aquisicao = date.today()
        data_aquisicao = data_aquisicao.strftime('%d/%m/%Y')

        self.remover_pop_up(caixa)

        try:
            numero_paginas = float(numero_paginas)
        except:
            pass
        try:
            quantidade = float(quantidade)
        except:
            pass

        if titulo == "":
            alerta.text = "Título vazio"
            alerta.color = (1, 0, 0, 1)
        elif autor == "":
            alerta.text = "Campo Autor vazio"
            alerta.color = (1, 0, 0, 1)
        elif genero == "Gênero":
            alerta.text = "Selecione um Gênero"
            alerta.color = (1, 0, 0, 1)
        elif faixa_etaria == "Faixa-Etária":
            alerta.text = "Selecione uma Faixa etária"
            alerta.color = (1, 0, 0, 1)
        elif status == "Status":
            alerta.text = "Selecione um status"
            alerta.color = (1, 0, 0, 1)
        elif numero_paginas == "":
            alerta.text = "Campo de páginas vazio"
            alerta.color = (1, 0, 0, 1)
        elif quantidade == "":
            alerta.text = "Campo de quantidade vazio"
            alerta.color = (1, 0, 0, 1)
        elif not isinstance(numero_paginas, int):
            alerta.text = "Campo de páginas deve \n ser um número inteiro"
            alerta.color = (1, 0, 0, 1)
        elif not isinstance(quantidade, int):
            alerta.text = "Campo de páginas deve \n ser um número inteiro"
            alerta.color = (1, 0, 0, 1)
        else:
            alerta.text = "Livro adicionado com sucesso"
            alerta.color = (0, 1, 0, 1)

            parametros = {
                "titulo": f"{titulo}",
                "autor": f"{autor}",
                "genero": f"{genero}",
                "faixa etaria": f"{faixa_etaria}",
                "numero de paginas": f"{numero_paginas}",
                "status": f"{status}",
            }

            def todos_iguais(lista):
                if lista:
                    return lista.count(lista[0]) == len(lista)
                return False

            buscado = []
            for chave, valores in zip(list(parametros.keys()), list(parametros.values())):
                buscar = requests.get(
                    f'https://catalogo-barca-default-rtdb.firebaseio.com/.json?orderBy="{chave}"&equalTo="{valores}"',
                    params=parametros).json()
                if len(list(buscar)) > 1:
                    buscado.append(list(buscar)[0])
                else:
                    buscado.append(list(buscar))

            if todos_iguais(buscado):

                info = buscado[0]

                requests.delete(f'https://catalogo-barca-default-rtdb.firebaseio.com/{info}/.json')


            else:
                alerta.text = "Pacote de livro \nnão encontrado"
                alerta.color = (1, 0, 0, 1)

    def criar_pop_up(self):
        catalogo = self.root.ids['catalogo']
        alerta = catalogo.ids['confirmacao']
        titulo = catalogo.ids['titulo'].text
        titulo = titulo.lower()
        autor = catalogo.ids['autor'].text
        autor = autor.lower()
        numero_paginas = catalogo.ids['pagina'].text
        quantidade = catalogo.ids['quantidade'].text
        genero = catalogo.ids['btn'].text
        faixa_etaria = catalogo.ids['btn11'].text
        status = catalogo.ids['btn14'].text




        try:
            numero_paginas = int(numero_paginas)
        except:
            pass
        try:
            quantidade = int(quantidade)
        except:
            pass

        if titulo == "":
            alerta.text = "Título vazio"
            alerta.color = (1, 0, 0, 1)
        elif autor == "":
            alerta.text = "Campo Autor vazio"
            alerta.color = (1, 0, 0, 1)
        elif genero == "Gênero":
            alerta.text = "Selecione um Gênero"
            alerta.color = (1, 0, 0, 1)
        elif faixa_etaria == "Faixa-Etária":
            alerta.text = "Selecione uma Faixa etária"
            alerta.color = (1, 0, 0, 1)
        elif status == "Status":
            alerta.text = "Selecione um status"
            alerta.color = (1, 0, 0, 1)
        elif numero_paginas == "":
            alerta.text = "Campo de páginas vazio"
            alerta.color = (1, 0, 0, 1)
        elif quantidade == "":
            alerta.text = "Campo de quantidade vazio"
            alerta.color = (1, 0, 0, 1)
        elif not isinstance(numero_paginas, int):
            alerta.text = "Campo de páginas deve \n ser um número inteiro"
            alerta.color = (1, 0, 0, 1)
        elif not isinstance(quantidade, int):
            alerta.text = "Campo de páginas deve \n ser um número inteiro"
            alerta.color = (1, 0, 0, 1)
        else:



            caixa_pop_up = FloatLayout(size=(600, 430), pos_hint={'center_x': 0.5, 'center_y': 0.5})

            # dicionando o botão "Sim"
            button_sim = Button(text="Sim", pos_hint={"right": 0.45, "top": 0.4}, size_hint=(0.18, 0.1),
                                color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                                on_release=lambda instance: self.adicionar_livro(caixa_pop_up))

            # Adicionando instruções de desenho ao canvas do botão "Sim"
            with button_sim.canvas.before:
                Color(0.9, 0.9, 0.9, 1)  # Cor do retângulo (verde)
                Rectangle(size=(button_sim.width + 600, button_sim.height + 350),  # Aumentando o tamanho
                          pos=(button_sim.x + 150, button_sim.y + 160))
                Color(135/255,206/255,250/255,1)
                Line(rectangle=(button_sim.x+150, button_sim.y+610, button_sim.width+600, button_sim.height-550), width=2,color=(135 / 255, 206 / 255, 250 / 255, 1))
                Color(0, 1, 0, 1)
                Line(width=2, rectangle=(button_sim.x+266, button_sim.y+221, button_sim.width+89, button_sim.height-17))

            # Adicionando o botão "Sim" ao FloatLayout
            caixa_pop_up.add_widget(button_sim)
            catalogo = self.root.ids['catalogo']
            # Adicionando o botão "Não"
            button_nao = Button(text="Não", pos_hint={"right": 0.75, "top": 0.4}, size_hint=(0.18, 0.1),
                                color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                                on_release= lambda instance: self.remover_pop_up(caixa_pop_up))

            # Adicionando instruções de desenho ao canvas do botão "Não"
            with button_nao.canvas.before:
                Color(1, 0, 0, 1)
                Line(width=2, rectangle=(button_nao.x+565, button_nao.y+221, button_nao.width+89, button_nao.height-17))

            # Adicionando o botão "Não" ao FloatLayout
            caixa_pop_up.add_widget(button_nao)

            # Adicionando o Label
            label_confirmacao = Label(text="Você deseja confirmar essa ação?", pos_hint={"right": 0.6, "top": 0.7},
                                      size_hint=(0.18, 0.1), color=(0, 0, 0, 1))

            # Adicionando o Label ao FloatLayout
            caixa_pop_up.add_widget(label_confirmacao)

            catalogo = self.root.ids['catalogo']


            catalogo.add_widget(caixa_pop_up)

    def remover_pop_up(self, caixa, *args):
        catalogo = self.root.ids['catalogo']

        if caixa:
            catalogo.remove_widget(caixa)

    def remover_pop_up_cadastro(self, caixa, *args):
        catalogo = self.root.ids['cadastrar_aluno']

        if caixa:
            catalogo.remove_widget(caixa)

    def criar_pop_up2(self):
        catalogo = self.root.ids['catalogo']
        alerta = catalogo.ids['confirmacao']
        titulo = catalogo.ids['titulo'].text
        titulo = titulo.lower()
        autor = catalogo.ids['autor'].text
        autor = autor.lower()
        numero_paginas = catalogo.ids['pagina'].text
        quantidade = catalogo.ids['quantidade'].text
        genero = catalogo.ids['btn'].text
        faixa_etaria = catalogo.ids['btn11'].text
        status = catalogo.ids['btn14'].text




        try:
            numero_paginas = float(numero_paginas)
        except:
            pass
        try:
            quantidade = float(quantidade)
        except:
            pass

        if titulo == "":
            alerta.text = "Título vazio"
            alerta.color = (1, 0, 0, 1)
        elif autor == "":
            alerta.text = "Campo Autor vazio"
            alerta.color = (1, 0, 0, 1)
        elif genero == "Gênero":
            alerta.text = "Selecione um Gênero"
            alerta.color = (1, 0, 0, 1)
        elif faixa_etaria == "Faixa-Etária":
            alerta.text = "Selecione uma Faixa etária"
            alerta.color = (1, 0, 0, 1)
        elif status == "Status":
            alerta.text = "Selecione um status"
            alerta.color = (1, 0, 0, 1)
        elif numero_paginas == "":
            alerta.text = "Campo de páginas vazio"
            alerta.color = (1, 0, 0, 1)
        elif quantidade == "":
            alerta.text = "Campo de quantidade vazio"
            alerta.color = (1, 0, 0, 1)
        elif not isinstance(numero_paginas, int):
            alerta.text = "Campo de páginas deve \n ser um número inteiro"
            alerta.color = (1, 0, 0, 1)
        elif not isinstance(quantidade, int):
            alerta.text = "Campo de páginas deve \n ser um número inteiro"
            alerta.color = (1, 0, 0, 1)
        else:



            caixa_pop_up = FloatLayout(size=(600, 430), pos_hint={'center_x': 0.5, 'center_y': 0.5})

            # dicionando o botão "Sim"
            button_sim = Button(text="Sim", pos_hint={"right": 0.45, "top": 0.4}, size_hint=(0.18, 0.1),
                                color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                                on_release=lambda instance: self.excluir_livro(caixa_pop_up))

            # Adicionando instruções de desenho ao canvas do botão "Sim"
            with button_sim.canvas.before:
                Color(0.9, 0.9, 0.9, 1)  # Cor do retângulo (verde)
                Rectangle(size=(button_sim.width + 600, button_sim.height + 350),  # Aumentando o tamanho
                          pos=(button_sim.x + 150, button_sim.y + 160))
                Color(135/255,206/255,250/255,1)
                Line(rectangle=(button_sim.x+150, button_sim.y+610, button_sim.width+600, button_sim.height-550), width=2,color=(135 / 255, 206 / 255, 250 / 255, 1))
                Color(0, 1, 0, 1)
                Line(width=2, rectangle=(button_sim.x+266, button_sim.y+221, button_sim.width+89, button_sim.height-17))

            # Adicionando o botão "Sim" ao FloatLayout
            caixa_pop_up.add_widget(button_sim)
            catalogo = self.root.ids['catalogo']
            # Adicionando o botão "Não"
            button_nao = Button(text="Não", pos_hint={"right": 0.75, "top": 0.4}, size_hint=(0.18, 0.1),
                                color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                                on_release= lambda instance: self.remover_pop_up(caixa_pop_up))

            # Adicionando instruções de desenho ao canvas do botão "Não"
            with button_nao.canvas.before:
                Color(1, 0, 0, 1)
                Line(width=2, rectangle=(button_nao.x+565, button_nao.y+221, button_nao.width+89, button_nao.height-17))

            # Adicionando o botão "Não" ao FloatLayout
            caixa_pop_up.add_widget(button_nao)

            # Adicionando o Label
            label_confirmacao = Label(text="Você deseja confirmar essa ação?", pos_hint={"right": 0.6, "top": 0.7},
                                      size_hint=(0.18, 0.1), color=(0, 0, 0, 1))

            # Adicionando o Label ao FloatLayout
            caixa_pop_up.add_widget(label_confirmacao)

            catalogo = self.root.ids['catalogo']


            catalogo.add_widget(caixa_pop_up)






    def lista_livros(self):
        biblioteca = requests.get('https://catalogo-barca-default-rtdb.firebaseio.com/.json').json()

        try:
            biblioteca = list(biblioteca.values())[1:]
        except AttributeError:
            biblioteca = biblioteca[1]
        try:

            biblioteca_barca = self.root.ids['relatorio']
            lista_livros = biblioteca_barca.ids['lista_livros']
            lista_livros.clear_widgets()
            for livro in biblioteca:

                banner = BannerLivros(titulo=livro['titulo'], autor=livro['autor'],
                                     genero=livro['genero'], faixa_etaria=livro['faixa etaria'], status=livro['status'],
                                     numero_paginas=livro['numero de paginas'], quantidade=livro['quantidade'], data_aquisicao=livro['data de aquisicao'],id=livro['id_real'],funcao=partial(self.criar_pop_up_livro,livro['id_real']))

                lista_livros.add_widget(banner)

        except Exception as excessao:
            print(excessao)

    def remover_lista_livros(self):
        biblioteca = requests.get('https://catalogo-barca-default-rtdb.firebaseio.com/.json').json()
        print(biblioteca)
        try:
            biblioteca = list(biblioteca.values())[1:]
        except AttributeError:
            biblioteca = biblioteca[1]
        try:

            biblioteca_barca = self.root.ids['relatorio']
            lista_livros = biblioteca_barca.ids['lista_livros']

            lista_livros.clear_widgets()

        except Exception as excessao:
            print(excessao)

    def update_label(self, instance, value):
        self.ids.result_label.text = f'Você selecionou: {value}'

    def adicionar_aluno(self,telefone,email,caixa,first_check_email,first_check):
        pagina_cadastro = self.root.ids['cadastrar_aluno']
        confirmacao_cadastro = pagina_cadastro.ids['confirmacao_cadastro']
        nome = pagina_cadastro.ids['nome'].text
        data_nascimento = pagina_cadastro.ids['data_nascimento'].text
        endereco = pagina_cadastro.ids['endereco'].text
        telefone_aluno = telefone.text
        email_aluno = email.text

        if not first_check_email.active:
            telefone_aluno = ""
        if not first_check.active:
            email_aluno = ""

        self.remover_lista_alunos()

        buscar = requests.get('https://alunos-barca-default-rtdb.firebaseio.com/turma/proximo_id_aluno.json').json()

        id = int(buscar) + 1


        cancelador = f'{{"cancelador": "10"}}'
        data_patch = f'{{"proximo_id_aluno": "{id}"}}'
        info = f'{{"nome": "{nome}","data_nascimento": "{data_nascimento}","endereco": "{endereco}","telefone": "{telefone_aluno}","email": "{email_aluno}","historico": "","id": "{id}","emprestado":"","reservado":"","livro_favorito":"{{}}","genero_favorito":"{{}}","autor_favorito":"{{}}","quant_visitas":"0"}}'

        requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/.json',data=data_patch)
        ultimate = requests.post(f'https://alunos-barca-default-rtdb.firebaseio.com/.json',data=info)
        requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/{ultimate.json()["name"]}/emprestado.json',data=cancelador)
        requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/{ultimate.json()["name"]}/reservado.json',data=cancelador)

        self.remover_pop_up_cadastro(caixa)
        self.lista_alunos()

    def lista_alunos(self):
        sala = requests.get('https://alunos-barca-default-rtdb.firebaseio.com/.json').json()
        sala = list(sala.values())


        try:

            biblioteca_barca = self.root.ids['perfil_aluno']
            lista_alunos = biblioteca_barca.ids['lista_alunos']
            lista_alunos.clear_widgets()

            turma = requests.get('https://alunos-barca-default-rtdb.firebaseio.com/turma.json').json()

            banner_turma = BannerAlunos(nome="Turma",data_nascimento="",endereco="",telefone="",email="",id=turma['id'],funcao=None,quant_visitas=turma['quant_visitas'],genero_fav=turma['genero_favorito']['genero_favorito'],livro_fav=turma['livro_favorito']['livro_favorito'],autor_fav=turma['autor_favorito']['autor_favorito'])
            lista_alunos.add_widget(banner_turma)
            for aluno in sala:


                banner = BannerAlunos(nome=aluno['nome'],data_nascimento=aluno['data_nascimento'],endereco=aluno['endereco'],telefone=aluno['telefone'],email=aluno['email'],id=aluno['id'],funcao=partial(self.criar_pop_up_alunos,aluno['id']),quant_visitas=aluno['quant_visitas'],genero_fav=aluno['genero_favorito']['genero_favorito'],livro_fav=aluno['livro_favorito']['livro_favorito'],autor_fav=aluno['autor_favorito']['autor_favorito'])

                lista_alunos.add_widget(banner)

        except Exception as excessao:
            print(excessao)

    def remover_lista_alunos(self):


        try:

            biblioteca_barca = self.root.ids['perfil_aluno']
            lista_alunos = biblioteca_barca.ids['lista_alunos']

            lista_alunos.clear_widgets()

        except Exception as excessao:
            print(excessao)

    def emprestar_livro(self):
        globe = self.root.ids['emprestimo']
        id_do_aluno = globe.ids['id_aluno'].text
        id_do_livro = globe.ids['id_livro'].text

        bd_id_livro = requests.get(f'https://catalogo-barca-default-rtdb.firebaseio.com/.json?orderBy="id_real"&equalTo="{id_do_livro}"').json()
        bd_id_aluno = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/.json?orderBy="id"&equalTo="{id_do_aluno}"').json()



        data_expiracao = globe.ids['input_validade'].text

        globe.ids['id_confirmacao'].text = ""

        try:
            if data_expiracao[2] != "/" or data_expiracao[5] != "/" or len(data_expiracao) != 10:
                data_confirmacao = True
            else:
                data_confirmacao = False

        except IndexError:
            data_confirmacao = True
        try:
            dia = int(data_expiracao[0:2])
            mes = int(data_expiracao[3:5])

            if data_expiracao[0] == 0:
                dia = int(data_expiracao[1])
            if data_expiracao[3] == 0:
                mes = int(data_expiracao[4])
            ano = int(data_expiracao[6:10])
            data = datetime(ano, mes, dia)
        except:
            pass



        # Obtém a data atual
        data_atual = datetime.now()

        if id_do_aluno == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno vazio"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif id_do_livro == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do livro vazio"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif isinstance(id_do_aluno, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif isinstance(id_do_livro, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do livro deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif bd_id_aluno == {}:
            globe.ids['id_confirmacao'].text = "ID do aluno não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif bd_id_livro == {}:
            globe.ids['id_confirmacao'].text = "ID do livro não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif  not list(bd_id_livro.values())[0]['status'] == "Disponível":
            globe.ids['id_confirmacao'].text = "O livro não está disponível"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif data_expiracao == "":
            globe.ids['id_confirmacao'].text = "Campo de data vazia"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif data_confirmacao:
            globe.ids['id_confirmacao'].text = "Campo de data deve ser no formato dd/mm/aa"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif data <= data_atual:
            globe.ids['id_confirmacao'].text = "A data de expiração é menor que a data atual"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        else:

            dict_livro = list(bd_id_livro.values())[0]
            dict_livro['status'] = 'Emprestado'
            info_dict2 = f'{{"emprestado":"{dict_livro}","id_historico":"{id_do_livro}"}}'
            indice_aluno = list(bd_id_aluno.keys())[0]
            indice_livro = list(bd_id_livro.keys())[0]
            acumulador_genero = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/genero_favorito.json').json()
            chave = list(bd_id_livro.values())[0]['genero']
            if acumulador_genero == "{}":
                acumulador_genero = eval(acumulador_genero)
                acumulador_genero[chave] = 1
            else:
                acumulador_genero = requests.get(
                    f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/genero_favorito/historico.json').json()
                acumulador_genero = eval(acumulador_genero)
                if chave in acumulador_genero:
                    acumulador_genero[chave] += 1
                else:
                    acumulador_genero[chave] = 1
            chave_maxima = max(acumulador_genero, key=acumulador_genero.get)
            info_genero = f'{{"historico": "{acumulador_genero}","genero_favorito":"{chave_maxima}"}}'
            acumulador_genero_turma = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/genero_favorito.json').json()
            chave = list(bd_id_livro.values())[0]['genero']
            if acumulador_genero_turma == "{}":
                acumulador_genero_turma = eval(acumulador_genero_turma)
                acumulador_genero_turma[chave] = 1
            else:
                acumulador_genero_turma = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/genero_favorito/historico.json').json()
                print(acumulador_genero_turma)
                acumulador_genero_turma = eval(acumulador_genero_turma)
                if chave in acumulador_genero_turma:
                    acumulador_genero_turma[chave] += 1
                else:
                    acumulador_genero_turma[chave] = 1
            chave_maxima = max(acumulador_genero_turma, key=acumulador_genero_turma.get)
            info_genero_turma = f'{{"historico": "{acumulador_genero_turma}","genero_favorito":"{chave_maxima}"}}'
            acumulador_titulo = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/livro_favorito.json').json()
            chave = list(bd_id_livro.values())[0]['titulo']

            if acumulador_titulo == "{}":
                acumulador_titulo = eval(acumulador_titulo)
                acumulador_titulo[chave] = 1
            else:
                acumulador_titulo = requests.get(
                    f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/livro_favorito/historico.json').json()

                acumulador_titulo = eval(acumulador_titulo)


                if chave in acumulador_titulo:
                    acumulador_titulo[chave] += 1
                else:
                    acumulador_titulo[chave] = 1
            chave_maxima = max(acumulador_titulo, key=acumulador_titulo.get)
            info_titulo = f'{{"historico": "{acumulador_titulo}","livro_favorito":"{chave_maxima}"}}'
            acumulador_titulo_turma = requests.get(
                f'https://alunos-barca-default-rtdb.firebaseio.com/turma/livro_favorito.json').json()
            chave = list(bd_id_livro.values())[0]['titulo']
            if acumulador_titulo_turma == "{}":
                acumulador_titulo_turma = eval(acumulador_titulo_turma)
                acumulador_titulo_turma[chave] = 1
            else:
                acumulador_titulo_turma = requests.get(
                    f'https://alunos-barca-default-rtdb.firebaseio.com/turma/livro_favorito/historico.json').json()
                acumulador_titulo_turma = eval(acumulador_titulo_turma)
                if chave in acumulador_titulo_turma:
                    acumulador_titulo_turma[chave] += 1
                else:
                    acumulador_titulo_turma[chave] = 1
            chave_maxima = max(acumulador_titulo_turma, key=acumulador_titulo_turma.get)
            info_titulo_turma = f'{{"historico": "{acumulador_titulo_turma}","livro_favorito":"{chave_maxima}"}}'

            acumulador_autor = requests.get(
                f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/autor_favorito.json').json()

            chave = list(bd_id_livro.values())[0]['autor']
            if acumulador_autor == "{}":
                acumulador_autor = eval(acumulador_autor)
                acumulador_autor[chave] = 1
            else:
                acumulador_autor = requests.get(
                    f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/autor_favorito/historico.json').json()
                acumulador_autor = eval(acumulador_autor)
                if chave in acumulador_autor:
                    acumulador_autor[chave] += 1
                else:
                    acumulador_autor[chave] = 1
            chave_maxima = max(acumulador_autor, key=acumulador_autor.get)
            info_autor = f'{{"historico": "{acumulador_autor}","autor_favorito":"{chave_maxima}"}}'
            acumulador_autor_turma = requests.get(
                f'https://alunos-barca-default-rtdb.firebaseio.com/turma/autor_favorito.json').json()
            chave = list(bd_id_livro.values())[0]['autor']
            if acumulador_autor_turma == "{}":
                acumulador_autor_turma = eval(acumulador_autor_turma)
                acumulador_autor_turma[chave] = 1
            else:
                acumulador_autor_turma = requests.get(
                    f'https://alunos-barca-default-rtdb.firebaseio.com/turma/autor_favorito/historico.json').json()
                acumulador_autor_turma = eval(acumulador_autor_turma)
                if chave in acumulador_autor_turma:
                    acumulador_autor_turma[chave] += 1
                else:
                    acumulador_autor_turma[chave] = 1
            chave_maxima = max(acumulador_autor_turma, key=acumulador_autor_turma.get)
            info_autor_turma = f'{{"historico": "{acumulador_autor_turma}","autor_favorito":"{chave_maxima}"}}'

            info_dict1 = f'{{"emprestado":"{dict_livro}","id_emprestimo":"{id_do_livro}","data_expiracao":"{data_expiracao}"}}'
            info = '{"status":"Emprestado"}'
            quant_visitas = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/quant_visitas.json').json()
            quant_visitas_turma = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/quant_visitas.json').json()
            quant_visitas = int(quant_visitas) + 1
            if quant_visitas_turma == "":
                quant_visitas_turma = 1
            else:
                quant_visitas_turma = int(quant_visitas_turma) + 1
            quant_dict = f'{{"quant_visitas":"{quant_visitas}"}}'
            quant_dict_turma = f'{{"quant_visitas":"{quant_visitas_turma}"}}'
            requests.post(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/emprestado.json',data=info_dict1)
            requests.post(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/historico.json',data=info_dict2)
            requests.post(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/historico.json',data=info_dict2)
            requests.patch(f'https://catalogo-barca-default-rtdb.firebaseio.com/{indice_livro}.json',data=info)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}.json', data=quant_dict)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/turma.json', data=quant_dict_turma)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/genero_favorito.json', data=info_genero)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/livro_favorito.json',data=info_titulo)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/autor_favorito.json',data=info_autor)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/genero_favorito.json',
                           data=info_genero_turma)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/livro_favorito.json',
                           data=info_titulo_turma)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/turma/autor_favorito.json',
                           data=info_autor_turma)

            globe.ids['id_confirmacao'].text = "Livro emprestado com sucesso"
            globe.ids['id_confirmacao'].color = (0, 1, 0, 1)
            self.lista_emprestimo()



    def devolver_livro(self):
        globe = self.root.ids['emprestimo']
        id_do_aluno = globe.ids['id_aluno'].text
        id_do_livro = globe.ids['id_livro'].text

        bd_id_livro = requests.get(f'https://catalogo-barca-default-rtdb.firebaseio.com/.json?orderBy="id_real"&equalTo="{id_do_livro}"').json()
        bd_id_aluno = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/.json?orderBy="id"&equalTo="{id_do_aluno}"').json()
        try:

            dict_livro = list(bd_id_livro.values())[0]
            info_dict = f'{{"emprestado":"{dict_livro}"}}'
            indice_aluno = list(bd_id_aluno.keys())[0]
            indice_livro = list(bd_id_livro.keys())[0]

            lista_emprestado = list(bd_id_aluno.values())[0]['emprestado']
            usuario_devolver = list(lista_emprestado.keys())[0]
            lista_emprestado_final = list(lista_emprestado.values())

            devolver = 0
            for id_emprestimo in lista_emprestado_final:


                try:
                    # Corrigindo a representação JSON substituindo as aspas simples por duplas
                    emprestado_json_corrigido = id_emprestimo['emprestado'].replace("'", '"')

                    # Convertendo a string JSON corrigida para um dicionário Python
                    emprestado_dict = json.loads(emprestado_json_corrigido)

                    # Agora você pode acessar os dados como um dicionário Python
                    print(f"ID_real: {emprestado_dict['id_real']}")
                    if emprestado_dict['id_real'] == str(id_do_livro):
                        devolver = id_emprestimo
                        print(devolver)


                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar JSON: {e}")
                except KeyError as e:
                    print(f"Chave não encontrada: {e}")
                except Exception as e:
                    print(f"Erro inesperado: {e}")
        except:
                pass









        globe.ids['id_confirmacao'].text = ""
        globe.ids['id_confirmacao'].color = (0, 0, 0, 0)


        if id_do_aluno == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno vazio"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif id_do_livro == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do livro vazio"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif isinstance(id_do_aluno, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif isinstance(id_do_livro, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do livro deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1,0,0,1)
        elif bd_id_aluno == {}:
            globe.ids['id_confirmacao'].text = "ID do aluno não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif bd_id_livro == {}:
            globe.ids['id_confirmacao'].text = "ID do livro não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif not dict_livro['status'] == "Emprestado":
            globe.ids['id_confirmacao'].text = "O livro não foi emprestado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif devolver == 0:
            globe.ids['id_confirmacao'].text = "Não foi emprestado esse livro para esse aluno"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        else:
            dict_livro = list(bd_id_livro.values())[0]
            info_dict = f'{{"emprestado":"{dict_livro}"}}'
            indice_aluno = list(bd_id_aluno.keys())[0]
            indice_livro = list(bd_id_livro.keys())[0]

            lista_emprestado = list(bd_id_aluno.values())[0]['emprestado']
            usuario_devolver = list(lista_emprestado.keys())[0]
            lista_emprestado_final = list(lista_emprestado.values())
            info = '{"status":"Disponível"}'
            requests.delete(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/emprestado/{usuario_devolver}.json',data=devolver)
            requests.patch(f'https://catalogo-barca-default-rtdb.firebaseio.com/{indice_livro}.json',data=info)
            globe.ids['id_confirmacao'].text = "Livro devolvido com sucesso"
            globe.ids['id_confirmacao'].color = (0, 1, 0, 1)
            self.lista_emprestimo()


    def reservar_livro(self):

        globe = self.root.ids['emprestimo']
        id_do_aluno = globe.ids['id_aluno'].text
        id_do_livro = globe.ids['id_livro'].text

        bd_id_livro = requests.get(
            f'https://catalogo-barca-default-rtdb.firebaseio.com/.json?orderBy="id_real"&equalTo="{id_do_livro}"').json()
        bd_id_aluno = requests.get(
            f'https://alunos-barca-default-rtdb.firebaseio.com/.json?orderBy="id"&equalTo="{id_do_aluno}"').json()


        data_expiracao = globe.ids['input_validade'].text

        globe.ids['id_confirmacao'].text = ""

        try:
            if data_expiracao[2] != "/" or data_expiracao[5] != "/" or len(data_expiracao) != 10:
                data_confirmacao = True
            else:
                data_confirmacao = False

        except IndexError:
            data_confirmacao = True
        try:
            dia = int(data_expiracao[0:2])
            mes = int(data_expiracao[3:5])

            if data_expiracao[0] == 0:
                dia = int(data_expiracao[1])
            if data_expiracao[3] == 0:
                mes = int(data_expiracao[4])
            ano = int(data_expiracao[6:10])
            data = datetime(ano, mes, dia)
        except:
            pass



        # Obtém a data atual
        data_atual = datetime.now()

        if id_do_aluno == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno vazio"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif id_do_livro == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do livro vazio"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif isinstance(id_do_aluno, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif isinstance(id_do_livro, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do livro deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif bd_id_aluno == {}:
            globe.ids['id_confirmacao'].text = "ID do aluno não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif bd_id_livro == {}:
            globe.ids['id_confirmacao'].text = "ID do livro não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)



        elif not list(bd_id_livro.values())[0]['status'] == "Disponível":
            globe.ids['id_confirmacao'].text = "O livro não está disponível"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif data_expiracao == "":
            globe.ids['id_confirmacao'].text = "Campo de data vazia"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif data_confirmacao:
            globe.ids['id_confirmacao'].text = "Campo de data deve ser no formato dd/mm/aa"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif data <= data_atual:
            globe.ids['id_confirmacao'].text = "A data de expiração é menor que a data atual"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        else:
            dict_livro = list(bd_id_livro.values())[0]
            dict_livro['status'] = 'Reservado'
            info_dict2 = f'{{"reservado":"{dict_livro}","id_historico":"{id_do_livro}"}}'
            indice_aluno = list(bd_id_aluno.keys())[0]
            indice_livro = list(bd_id_livro.keys())[0]
            info_dict1 = f'{{"reservado":"{dict_livro}","id_emprestimo":"{id_do_livro}","data_expiracao":"{data_expiracao}"}}'
            info = '{"status":"Reservado"}'
            quant_visitas = requests.get(
                f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/quant_visitas.json').json()
            quant_visitas = int(quant_visitas) + 1
            quant_dict = f'{{"quant_visitas":"{quant_visitas}"}}'
            requests.post(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/reservado.json',
                          data=info_dict1)
            requests.post(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/historico.json',
                          data=info_dict2)
            requests.patch(f'https://catalogo-barca-default-rtdb.firebaseio.com/{indice_livro}.json', data=info)
            requests.patch(f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}.json', data=quant_dict)
            globe.ids['id_confirmacao'].text = "Livro reservado com sucesso"
            globe.ids['id_confirmacao'].color = (0, 1, 0, 1)
            self.lista_emprestimo()


    def desfazer_reserva(self):
        globe = self.root.ids['emprestimo']
        id_do_aluno = globe.ids['id_aluno'].text
        id_do_livro = globe.ids['id_livro'].text

        bd_id_livro = requests.get(
            f'https://catalogo-barca-default-rtdb.firebaseio.com/.json?orderBy="id_real"&equalTo="{id_do_livro}"').json()
        bd_id_aluno = requests.get(
            f'https://alunos-barca-default-rtdb.firebaseio.com/.json?orderBy="id"&equalTo="{id_do_aluno}"').json()
        try:
            dict_livro = list(bd_id_livro.values())[0]
            info_dict = f'{{"emprestado":"{dict_livro}"}}'
            indice_aluno = list(bd_id_aluno.keys())[0]
            indice_livro = list(bd_id_livro.keys())[0]

            lista_emprestado = list(bd_id_aluno.values())[0]['reservado']
            usuario_devolver = list(lista_emprestado.keys())[0]
            lista_emprestado_final = list(lista_emprestado.values())


            devolver = 0
            for id_emprestimo in lista_emprestado_final:

                try:
                    # Corrigindo a representação JSON substituindo as aspas simples por duplas
                    emprestado_json_corrigido = id_emprestimo['reservado'].replace("'", '"')

                    # Convertendo a string JSON corrigida para um dicionário Python
                    emprestado_dict = json.loads(emprestado_json_corrigido)

                    # Agora você pode acessar os dados como um dicionário Python
                    print(f"ID_real: {emprestado_dict['id_real']}")
                    if emprestado_dict['id_real'] == str(id_do_livro):
                        devolver = id_emprestimo
                        print(devolver)


                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar JSON: {e}")
                except KeyError as e:
                    print(f"Chave não encontrada: {e}")
                except Exception as e:
                    print(f"Erro inesperado: {e}")
        except:
            pass

        globe.ids['id_confirmacao'].text = ""
        globe.ids['id_confirmacao'].color = (0, 0, 0, 0)

        if id_do_aluno == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno vazio"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif id_do_livro == "":
            globe.ids['id_confirmacao'].text = "Campo de ID do livro vazio"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif isinstance(id_do_aluno, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do aluno deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif isinstance(id_do_livro, int):
            globe.ids['id_confirmacao'].text = "Campo de ID do livro deve ser um inteiro"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif bd_id_aluno == {}:
            globe.ids['id_confirmacao'].text = "ID do aluno não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif bd_id_livro == {}:
            globe.ids['id_confirmacao'].text = "ID do livro não encontrado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif not dict_livro['status'] == "Reservado":
            globe.ids['id_confirmacao'].text = "O livro não foi Reservado"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        elif devolver == 0:
            globe.ids['id_confirmacao'].text = "Não foi emprestado esse livro para esse aluno"
            globe.ids['id_confirmacao'].color = (1, 0, 0, 1)
        else:
            info = '{"status":"Disponível"}'
            requests.delete(
                f'https://alunos-barca-default-rtdb.firebaseio.com/{indice_aluno}/reservado/{usuario_devolver}.json',
                data=devolver)
            requests.patch(f'https://catalogo-barca-default-rtdb.firebaseio.com/{indice_livro}.json', data=info)
            globe.ids['id_confirmacao'].text = "Cancelamento da reserva feita com sucesso"
            globe.ids['id_confirmacao'].color = (0, 1, 0, 1)
            self.lista_emprestimo()


    def lista_emprestimo(self):

        sala = requests.get('https://alunos-barca-default-rtdb.firebaseio.com/.json').json()
        sala = list(sala.values())
        biblioteca_emprestimo = self.root.ids['emprestimo']
        lista_alunos = biblioteca_emprestimo.ids['lista_emprestimo']
        lista_alunos.clear_widgets()
        for aluno in sala:
            if not len(list(aluno.keys())) == 7:

                dict_emprestado = list(aluno['emprestado'].values())
                dict_emprestado.append(list(aluno['reservado'].values())[0])

                for livro in dict_emprestado:
                    if isinstance(livro, dict):
                        id_aluno = aluno['id']
                        nome = aluno['nome']
                        data_expiracao = livro['data_expiracao']
                        try:
                            dict_livro = livro['emprestado']
                        except:
                            try:
                                dict_livro = livro['reservado']
                            except:
                                pass
                        print(dict_livro)
                        try:
                            # Corrigindo a representação JSON substituindo as aspas simples por duplas
                            emprestado_json_corrigido = dict_livro.replace("'", '"')

                            # Convertendo a string JSON corrigida para um dicionário Python
                            emprestado_dict = json.loads(emprestado_json_corrigido)

                            # Agora você pode acessar os dados como um dicionário Python
                            autor = emprestado_dict['autor']
                            titulo = emprestado_dict['titulo']
                            id_real = emprestado_dict['id_real']
                            status = emprestado_dict['status']


                            banner = BannerEmprestimo(nome=nome, id_aluno=id_aluno, data_expiracao=data_expiracao,autor=autor,
                                                  titulo=titulo,id_livro=id_real, status=status)


                            lista_alunos.add_widget(banner)


                        except json.JSONDecodeError as e:
                            print(f"Erro ao decodificar JSON: {e}")
                        except KeyError as e:
                            print(f"Chave não encontrada: {e}")
                        except Exception as e:
                            print(f"Erro inesperado: {e}")


    def criar_pop_up_alunos(self,id_aluno):
        caixa_pop_up = FloatLayout(size=(600, 430), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # dicionando o botão "Sim"
        button_sim = Button(text="Sim", pos_hint={"right": 0.45, "top": 0.4}, size_hint=(0.18, 0.1),
                            color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                            on_release=lambda instance: self.deletar_aluno(id_aluno,caixa_pop_up))

        # Adicionando instruções de desenho ao canvas do botão "Sim"
        with button_sim.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Cor do retângulo (verde)
            Rectangle(size=(button_sim.width + 600, button_sim.height + 350),  # Aumentando o tamanho
                      pos=(button_sim.x + 150, button_sim.y + 160))
            Color(135 / 255, 206 / 255, 250 / 255, 1)
            Line(rectangle=(button_sim.x + 150, button_sim.y + 610, button_sim.width + 600, button_sim.height - 550))
            Color(0, 1, 0, 1)
            Line(width=2,
                 rectangle=(button_sim.x + 266, button_sim.y + 221, button_sim.width + 89, button_sim.height - 17))

        # Adicionando o botão "Sim" ao FloatLayout
        caixa_pop_up.add_widget(button_sim)
        catalogo = self.root.ids['perfil_aluno']
        # Adicionando o botão "Não"
        button_nao = Button(text="Não", pos_hint={"right": 0.75, "top": 0.4}, size_hint=(0.18, 0.1),
                            color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                            on_release=lambda instance: self.remover_pop_up_alunos(caixa_pop_up))

        # Adicionando instruções de desenho ao canvas do botão "Não"
        with button_nao.canvas.before:
            Color(1, 0, 0, 1)
            Line(width=2,
                 rectangle=(button_nao.x + 565, button_nao.y + 221, button_nao.width + 89, button_nao.height - 17))

        # Adicionando o botão "Não" ao FloatLayout
        caixa_pop_up.add_widget(button_nao)

        # Adicionando o Label
        label_confirmacao = Label(text="Você deseja confirmar essa ação?", pos_hint={"right": 0.6, "top": 0.7},
                                  size_hint=(0.18, 0.1), color=(0, 0, 0, 1))

        # Adicionando o Label ao FloatLayout
        caixa_pop_up.add_widget(label_confirmacao)

        catalogo = self.root.ids['perfil_aluno']

        catalogo.add_widget(caixa_pop_up)


    def deletar_aluno(self,id_aluno,caixa):
        buscar = requests.get(f'https://alunos-barca-default-rtdb.firebaseio.com/.json?orderBy="id"&equalTo="{id_aluno}"').json()
        id_post = list(buscar.keys())[0]
        requests.delete(f'https://alunos-barca-default-rtdb.firebaseio.com/{id_post}.json')
        self.remover_pop_up_alunos(caixa)
        self.lista_alunos()

    def remover_pop_up_alunos(self, caixa, *args):
        catalogo = self.root.ids['perfil_aluno']

        if caixa:
            catalogo.remove_widget(caixa)


    def fazer_login(self):
        login = self.root.ids['fazer_login']
        email = login.ids['email'].text
        senha = login.ids['senha'].text

        if email == "":
            login.ids['login_confirmacao'].text = "O campo email está vazio"
            login.ids['login_confirmacao'].color = (1,0,0,1)
        elif senha == "":
            login.ids['login_confirmacao'].text = "O campo senha está vazio"
            login.ids['login_confirmacao'].color = (1,0,0,1)
        elif email != "barcaliteraria14@gmail.com":
            login.ids['login_confirmacao'].text = "Email inválido!!"
            login.ids['login_confirmacao'].color = (1, 0, 0, 1)
        elif senha != "Barca_unida@13":
            login.ids['login_confirmacao'].text = "Senha inválida!!"
            login.ids['login_confirmacao'].color = (1, 0, 0, 1)
        else:
            criar_conta = {"login":"barcaliteraria14@gmail.com","senha":"Barca_unida@13"}
            with open("refresh Token.txt", 'w') as arquivo:
                json.dump(criar_conta, arquivo)

            self.mudar_tela("homepage")

    def criar_pop_up_livro(self,id_livro):
        caixa_pop_up = FloatLayout(size=(600, 430), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # dicionando o botão "Sim"
        button_sim = Button(text="Sim", pos_hint={"right": 0.45, "top": 0.4}, size_hint=(0.18, 0.1),
                            color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                            on_release=lambda instance: self.deletar_livro(id_livro,caixa_pop_up))

        # Adicionando instruções de desenho ao canvas do botão "Sim"
        with button_sim.canvas.before:
            Color(0.9, 0.9, 0.9, 1)  # Cor do retângulo (verde)
            Rectangle(size=(button_sim.width + 600, button_sim.height + 350),  # Aumentando o tamanho
                      pos=(button_sim.x + 150, button_sim.y + 160))
            Color(135 / 255, 206 / 255, 250 / 255, 1)
            Line(rectangle=(button_sim.x + 150, button_sim.y + 610, button_sim.width + 600, button_sim.height - 550))
            Color(0, 1, 0, 1)
            Line(width=2,
                 rectangle=(button_sim.x + 266, button_sim.y + 221, button_sim.width + 89, button_sim.height - 17))

        # Adicionando o botão "Sim" ao FloatLayout
        caixa_pop_up.add_widget(button_sim)
        catalogo = self.root.ids['perfil_aluno']
        # Adicionando o botão "Não"
        button_nao = Button(text="Não", pos_hint={"right": 0.75, "top": 0.4}, size_hint=(0.18, 0.1),
                            color=(0, 0, 0, 1), background_color=(1, 1, 1, 1), background_normal="",
                            on_release=lambda instance: self.remover_pop_up_livros(caixa_pop_up))

        # Adicionando instruções de desenho ao canvas do botão "Não"
        with button_nao.canvas.before:
            Color(1, 0, 0, 1)
            Line(width=2,
                 rectangle=(button_nao.x + 565, button_nao.y + 221, button_nao.width + 89, button_nao.height - 17))

        # Adicionando o botão "Não" ao FloatLayout
        caixa_pop_up.add_widget(button_nao)

        # Adicionando o Label
        label_confirmacao = Label(text="Você deseja confirmar essa ação?", pos_hint={"right": 0.6, "top": 0.7},
                                  size_hint=(0.18, 0.1), color=(0, 0, 0, 1))

        # Adicionando o Label ao FloatLayout
        caixa_pop_up.add_widget(label_confirmacao)

        catalogo = self.root.ids['relatorio']

        catalogo.add_widget(caixa_pop_up)


    def deletar_livro(self,id_livro,caixa):
        buscar = requests.get(f'https://catalogo-barca-default-rtdb.firebaseio.com/.json?orderBy="id_real"&equalTo="{id_livro}"').json()
        id_post = list(buscar.keys())[0]
        requests.delete(f'https://catalogo-barca-default-rtdb.firebaseio.com/{id_post}.json')
        self.remover_pop_up_alunos(caixa)
        self.lista_livros()

    def remover_pop_up_livros(self, caixa, *args):
        catalogo = self.root.ids['relatorio']

        if caixa:
            catalogo.remove_widget(caixa)

    def build(self):
        return GUI



MainApp().run()
