# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from interface_controller import Gerenciador
from controller import Controller


class MainWindow(QtGui.QMainWindow):
    def __init__(self, gerenciador):
        super(QtGui.QMainWindow, self).__init__()
        self.telas = {}
        self.gerenciador = gerenciador
        self.gerenciador.set_main_window(self)

        self.configurar_interface()

    def configurar_interface(self):
        self.setGeometry(300, 100, 700, 500)
        self.setWindowTitle("VinilApp")
        self.show()

    def adicionar_tela(self, tipo_de_tela):
        if tipo_de_tela not in self.telas:
            self.telas[tipo_de_tela] = tipo_de_tela(self, self.gerenciador)

    def trocar_tela(self, tipo_de_tela):
        self.setCentralWidget(self.telas[tipo_de_tela])


class LoginFrame(QtGui.QWidget):
    """docstring for LoginFrame"""

    def __init__(self, parent, gerenciador):
        super(LoginFrame, self).__init__(parent)

        self.gerenciador = gerenciador
        self.construir_interface()
        self.conectar_sinais()

    def construir_interface(self):

        self.label_image = QtGui.QLabel()
        self.label_image.setPixmap(QtGui.QPixmap("vinil2.png"))
        self.label_username = QtGui.QLabel('Username')
        self.label_password = QtGui.QLabel('Password')
        self.input_username = QtGui.QLineEdit()
        self.input_password = QtGui.QLineEdit()
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.label_erro = QtGui.QLabel()
        self.botao_entrar = QtGui.QPushButton("Entrar")

        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.label_image, 0, 1, 1, 2)
        layout.addWidget(self.label_username, 1, 0)
        layout.addWidget(self.input_username, 1, 1)
        layout.addWidget(self.label_password, 2, 0)
        layout.addWidget(self.input_password, 2, 1)
        layout.addWidget(self.label_erro, 3, 1)
        layout.addWidget(self.botao_entrar, 4, 3)

        self.show()

    def conectar_sinais(self):
        self.botao_entrar.clicked.connect(self.on_entrar_click)
        # Para se o usuário digitar e dar enter em algum dos campos de texto
        self.input_username.returnPressed.connect(self.on_entrar_click)
        self.input_password.returnPressed.connect(self.on_entrar_click)

    def on_entrar_click(self):
        username = self.input_username.text()
        password = self.input_password.text()
        status_code, text = self.gerenciador.autenticar(username, password)  # _mock()  #
        if status_code == 200:
            self.label_erro.setText(u"Usuário autenticado com sucesso!")
            self.gerenciador.trocar_tela(CarregadorDeArquivosEPlayerFrame)
        else:
            self.label_erro.setText(text)


class CarregadorDeArquivosEPlayerFrame(QtGui.QWidget):
    """docstring for CarregadorDeArquivosEPlayerFrame"""
    def __init__(self, parent, gerenciador):
        super(CarregadorDeArquivosEPlayerFrame, self).__init__(parent)
        self.gerenciador = gerenciador
        self.controller = Controller("user.cfg")
        
        self.construir_interface()
        self.conectar_sinais()
        self.carregar_ultima_execucao()

    def construir_interface(self):
        self.lista_musicas = QtGui.QListWidget()
        self.escolher_pasta = QtGui.QPushButton("Escolher pasta")
        self.update = QtGui.QPushButton(u"Enviar Músicas")
        self.next = QtGui.QPushButton("Next")
        self.play = QtGui.QPushButton("Play")
        self.stop = QtGui.QPushButton("Stop")
        self.quit = QtGui.QPushButton("Quit")

        layout = QtGui.QGridLayout(self)

        layout_interacao = QtGui.QHBoxLayout(self)
        layout_interacao.addWidget(self.escolher_pasta)
        layout_interacao.addWidget(self.update)
        layout_interacao.addWidget(self.quit)

        layout_controles = QtGui.QHBoxLayout(self)
        layout_controles.addWidget(self.play)
        layout_controles.addWidget(self.next)
        layout_controles.addWidget(self.stop)

        layout.addWidget(self.lista_musicas, 0, 0)
        layout.addLayout(layout_controles, 1, 0)
        layout.addLayout(layout_interacao, 2, 0)

        self.setLayout(layout)
        self.show()

    def conectar_sinais(self):
        self.escolher_pasta.clicked.connect(self.pegar_caminho_pasta_musicas)
        self.update.clicked.connect(self.enviar_musicas_para_servidor)
        self.play.clicked.connect(self.tocar)
        self.next.clicked.connect(self.seguinte)
        self.stop.clicked.connect(self.parar)
        self.quit.clicked.connect(self.fechar_programa)

    def carregar_ultima_execucao(self):
        try:
            self.controller.update_library()
            nome_musicas = self.pegar_nome_musicas()
            self.mostrar_lista_musicas(nome_musicas)
        except:
            print "Última execução indisponível"

    def fechar_programa(self):
        self.parentWidget().destroy()

    def pegar_caminho_pasta_musicas(self):
        filename_qt_str = QtGui.QFileDialog.getExistingDirectory(self)
        filename = str(filename_qt_str)
        print filename
        if filename != "":
            self.controller.config.set_library_path(filename)
            self.controller.update_library()
            self.mostrar_lista_musicas(self.pegar_nome_musicas())

        # método do Tácio para buscar lista de músicas no servidor
        # adicionar lista de músicas na janela
        # habilitar botão de enviar para servidor
        # começar a tocar as músicas

    def mostrar_lista_musicas(self, lista):
        self.lista_musicas.clear()
        self.lista_musicas.addItems(lista)

    def enviar_musicas_para_servidor(self):
        self.gerenciador.enviar_lista_musicas(self.controller.get_musics_list())

    def pegar_nome_musicas(self):
        return [music.title for music in self.controller.musics]

    def tocar(self):
        self.controller.play()
        self.timer = QtCore.QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.verificar_playback)

    def parar(self):
        self.controller.pause()

    def seguinte(self):
        self.buscar_proxima_musica()
        self.controller.play()

    def verificar_playback(self):
        # Se tiver acabado de tocar, buscar nova música no servidor
        current_music = self.controller.get_current_music()
        if current_music.is_busy():
            print "busy"
        # Se não, não fazer nada
        else:
            self.buscar_proxima_musica()

    def buscar_proxima_musica(self):
        self.gerenciador.atualizar_voto(self.controller.get_current_music())
        lista_musicas = self.gerenciador.buscar_lista_musicas()  # buscar aqui próxima música buscada no servidor
        print lista_musicas
        proxima_musica = lista_musicas[0]
        self.controller.reorder_music_list(proxima_musica["hash"])
        self.controller.play()


def main():
    app = QtGui.QApplication(sys.argv)
    gerenciador = Gerenciador()
    main_window = MainWindow(gerenciador)
    main_window.adicionar_tela(LoginFrame)
    main_window.trocar_tela(LoginFrame)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
