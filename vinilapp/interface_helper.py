# -*- coding: utf-8 -*-
#!/usr/bin/env


class Gerenciador(object):
    """docstring for Gerenciador"""
    def __init__(self):
        self.main_window = None

    def autenticar(self, username, password):
        # TODO: obter 'resultado' do servidor
        # resultado = self.fazer_requisicao_http(username, password)
        resultado = self.resultado
        if resultado['erro'] is None:
            return 'Usuário autenticado com sucesso'
        else:
            if resultado['erro'] == 1:
                raise UsuarioInexistenteException()
            elif resultado['erro'] == 2:
                raise PasswordIncorretoException()

    def fazer_requisicao_http(self, username, password):
        # TODO: fazer requisição ao servidor, transformar a resposta em objeto
        # (dict) e retornar o objeto
        pass

    def mock_resultado_requisicao(self, erro):
        self.resultado = {'erro': erro}

    def set_main_window(self, main_window):
        self.main_window = main_window

    def trocar_tela(self, proxima_tela):
        self.main_window.adicionar_tela(proxima_tela)
        self.main_window.trocar_tela(proxima_tela)


class UsuarioInexistenteException(Exception):
    def __init__(self):
        super(UsuarioInexistenteException, self).__init__()


class PasswordIncorretoException(Exception):
    def __init__(self):
        super(PasswordIncorretoException, self).__init__()
