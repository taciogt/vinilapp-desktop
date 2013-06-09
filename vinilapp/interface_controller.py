# -*- coding: utf-8 -*-
#!/usr/bin/env
import requests
import base64
import json


class Gerenciador(object):
    """docstring for Gerenciador"""
    def __init__(self):
        self.main_window = None
        self.username = None
        self.password = None
        self.url_base = "http://vinilapp.herokuapp.com"

    def autenticar(self, username, password):
        self.username = username
        self.password = password
        resultado = self.fazer_requisicao_http("/api/login")
        return (resultado.status_code, resultado.text)

    def fazer_requisicao_http(self, endereco):
        # endereco deve conter o caminho que você quer acessar
        # 'http://127.0.0.1:5000/api/musics.json'
        url = self.url_base + endereco
        # seu usuário e senha, que você vai ter que guardar para mandar todas as vezes
        base64string = base64.encodestring('%s:%s' % (self.username, self.password))[:-1]
        authheader = "Basic %s" % base64string
        headers = {'Content-Type': 'application/json', 'Authorization': authheader}
        # o método pode ser get ou post!
        return requests.get(url, headers=headers)
        # # TODO: fazer requisição ao servidor, transformar a resposta em objeto
        # # (dict) e retornar o objeto (no mesmo formato do mock)
        # # self.resultado = urllib2.urlopen() ...
        # return self.resultado

    def enviar_lista_musicas(self, musics):
        url = self.url_base + "/api/musics.json"
        # seu usuário e senha, que você vai ter que guardar para mandar todas as vezes
        base64string = base64.encodestring('%s:%s' % (self.username, self.password))[:-1]
        authheader = "Basic %s" % base64string
        headers = {'Content-Type': 'application/json', 'Authorization': authheader}
        # o método pode ser get ou post!
        enviar = json.dumps({'musics': musics})
        print enviar
        return requests.post(url, headers=headers, data=enviar)

    def buscar_lista_musicas(self):
        # Ir no servidor buscar lista de músicas
        pass

    def autenticar_mock(self):
        return (200, "Usuario autenticado com sucesso!")

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
