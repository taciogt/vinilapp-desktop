# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
from PyQt4.QtCore import QObject, SIGNAL, SLOT, pyqtSignal
from interface_helper import Gerenciador, UsuarioInexistenteException, PasswordIncorretoException


class MainWindow(QtGui.QMainWindow):
    def __init__(self, gerenciador):
        super(QtGui.QMainWindow, self).__init__()
        self.telas = {}
        self.gerenciador = gerenciador
        self.gerenciador.set_main_window(self)

        self.configurar_interface()

    def configurar_interface(self):
        self.setGeometry(300, 100, 500, 200)
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
        self.gerenciador.mock_resultado_requisicao(None)
        self.construir_interface()
        self.conectar_sinais()

    def construir_interface(self):

        self.label_username = QtGui.QLabel('Username')
        self.label_password = QtGui.QLabel('Password')
        self.input_username = QtGui.QLineEdit()
        self.input_password = QtGui.QLineEdit()
        self.input_password.setEchoMode(QtGui.QLineEdit.Password)
        self.label_erro = QtGui.QLabel()
        self.botao_entrar = QtGui.QPushButton("Entrar")

        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.label_username, 1, 0)
        layout.addWidget(self.input_username, 1, 1)
        layout.addWidget(self.label_password, 2, 0)
        layout.addWidget(self.input_password, 2, 1)
        layout.addWidget(self.label_erro, 3, 1)
        layout.addWidget(self.botao_entrar, 4, 3)

        self.show()

    def conectar_sinais(self):
        self.botao_entrar.clicked.connect(self.on_entrar_click)
        self.input_username.returnPressed.connect(self.on_entrar_click)
        self.input_password.returnPressed.connect(self.on_entrar_click)

    def on_entrar_click(self):
        username = self.input_username.text()
        password = self.input_password.text()
        try:
            self.gerenciador.autenticar(username, password)
        except UsuarioInexistenteException:
            self.label_erro.setText(u"Usuario inexistente")
        except PasswordIncorretoException:
            self.label_erro.setText(u"Password incorreto")
        except:
            self.label_erro.setText(u"Verifique sua conexão com a internet")
        self.gerenciador.trocar_tela(CarregadorDeArquivosEPlayerFrame)


class CarregadorDeArquivosEPlayerFrame(QtGui.QWidget):
    """docstring for CarregadorDeArquivosEPlayerFrame"""
    def __init__(self, parent, gerenciador):
        super(CarregadorDeArquivosEPlayerFrame, self).__init__(parent)
        self.gerenciador = gerenciador
        self.construir_interface()
        self.conectar_sinais()

    def construir_interface(self):

        self.lista_musicas = QtGui.QListView()
        self.a = QtGui.QLineEdit()
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.lista_musicas, 0, 0)
        layout.addWidget(self.a, 1, 0)
        self.show()
        self.count = 0

    def conectar_sinais(self):
        self.a.returnPressed.connect(self.addElem)

    def addElem(self):
        text = self.a.text()
        self.lista_musicas.setText(self.count, text)
        self.count += 1

    def mostrar(self):
        print 'clicou!'


def main():
    app = QtGui.QApplication(sys.argv)
    gerenciador = Gerenciador()
    main_window = MainWindow(gerenciador)
    main_window.adicionar_tela(LoginFrame)
    main_window.trocar_tela(LoginFrame)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
