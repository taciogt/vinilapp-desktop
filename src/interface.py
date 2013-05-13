# coding: utf-8
import sys
from PyQt4 import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.telas = {}

        self.configurar_interface()

    def configurar_interface(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle("VinilApp")


    def adicionar_tela(self, tipo_de_tela, tela):
        self.telas[tipo_de_tela] = tela

    def trocar_tela(self, tipo_de_tela):
        self.hide()
        self.setCentralWidget(self.telas[tipo_de_tela])
        self.show()


class LoginFrame(QtGui.QFrame):
    """docstring for LoginFrame"""
    def __init__(self):
        super(LoginFrame, self).__init__()

        self.label_username = QtGui.QLabel('Username')
        self.label_password = QtGui.QLabel('Password')
        self.input_username = QtGui.QLineEdit()
        self.input_password = QtGui.QLineEdit()
        self.botao_confirmar = QtGui.QPushButton("Confirmar")
        self.botao_desconfirmar = QtGui.QPushButton("Desconfirmar")

        layout = QtGui.QGridLayout()
        layout.addWidget(self.label_username, 0, 0)
        layout.addWidget(self.label_password, 1, 0)
        layout.addWidget(self.input_username, 0, 1)
        layout.addWidget(self.input_password, 1, 1)
        layout.addWidget(self.botao_confirmar, 2, 2)
        layout.addWidget(self.botao_desconfirmar, 2, 1)

        self.setLayout(layout)


def main():
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.adicionar_tela(LoginFrame, LoginFrame())
    main_window.trocar_tela(LoginFrame)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
