# -*- coding: utf-8 -*-
#!/usr/bin/env


class Gerenciador(object):
    """docstring for Gerenciador"""
    def __init__(self):
        self.main_window = None

    def autenticar(self, username, password):
        resultado = self.fazer_requisicao_http(username, password)
        if resultado['erro'] is None:
            return 'Usuário autenticado com sucesso'
        else:
            if resultado['erro'] == 1:
                raise UsuarioInexistenteException()
            elif resultado['erro'] == 2:
                raise PasswordIncorretoException()

    def fazer_requisicao_http(self, username, password):
        # import requests, base64
        # #A url que você vai acessar pra pegar a informação desejada
        # url = 'http://127.0.0.1:5000/api/musics.json' 
        # #seu usuário e senha, que você vai ter que guardar para mandar todas as vezes
        # base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
        # authheader =  "Basic %s" % base64string
        # headers = {'Content-Type':'application/json','Authorization':authheader}
        # #o método pode ser get ou post!
        # r=requests.get(url,headers=headers)

        # TODO: fazer requisição ao servidor, transformar a resposta em objeto
        # (dict) e retornar o objeto (no mesmo formato do mock)
        # self.resultado = urllib2.urlopen() ...
        return self.resultado

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
