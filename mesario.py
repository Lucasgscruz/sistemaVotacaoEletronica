#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel
import banco_de_dados as pesquisa

eel.init('mesario_gui')


def pre_urna(id):
    """Inicia o processo de liberacao da urna eletrônica"""
    print("Chamando conexao com a urna...")


@eel.expose
def encerra_voto(id):
    """Conclui a votação e bloquea a urna"""
    print("Chamando conexao com a urna para bloqueio")
    pesquisa.marca_voto(id)


@eel.expose
def my_python_function(palavra):
    if(len(palavra) > 1):
        print("Chamada de função funcionandoo...")
        retorno = pesquisa.consulta_nome(palavra)
    eel.get_retorno(retorno)


@eel.expose
def autenticar_impressao(id, codigo):
    # valida a impressao digital,simulador:)
    resposta = pesquisa.valida_digital(id, codigo)
    if(resposta is True):
        pre_urna(id)
        eel.liberar_urna(True)
    else:
        eel.liberar_urna(False)

eel.start('index.html')
eel.start('liberar.html')
