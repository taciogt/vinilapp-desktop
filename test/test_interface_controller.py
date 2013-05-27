# -*- coding: utf-8 -*-
#!/usr/bin/env
import unittest
import os
from vinilapp.interface_controller import *


class GerenciadorTests(unittest.TestCase):
    def setUp(self):
        self.gerenciador = Gerenciador()

    def test_autenticar_usuario_e_senha_corretos(self):
        usuario = 'teste'
        senha = 'teste'
        self.gerenciador.mock_resultado_requisicao(None)
        self.assertEquals(
            mock_autenticado_com_sucesso(),
            self.gerenciador.autenticar(usuario, senha))

    def test_autenticar_usuario_inexistente(self):
        usuario = 'inexistente'
        senha = 'qualquer_coisa'
        self.gerenciador.mock_resultado_requisicao(1)
        self.assertRaises(
            UsuarioInexistenteException,
            self.gerenciador.autenticar,
            usuario,
            senha)

    def test_autenticar_usuario_senha_incorreta(self):
        usuario = 'teste'
        senha = 'incorreta'
        self.gerenciador.mock_resultado_requisicao(2)
        self.assertRaises(
            PasswordIncorretoException,
            self.gerenciador.autenticar,
            usuario,
            senha)


def mock_autenticado_com_sucesso():
    return 'Usuário autenticado com sucesso'


# modelo de json de autenticação:
# temp = {
#     'erro': None,
#     'msg': 'Usuário autenticado com sucesso'
# }
