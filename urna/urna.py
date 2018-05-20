#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel
import eleicao as eleicao
eel.init('urna_gui')


partidos = eleicao.carrega_partidos()
candidatos = eleicao.carrega_candidatos()


@eel.expose
def carrega_final(escolhas):
    """realiza a pesquisa pelo numero e carrega os dados finais"""
    lista_retorno = []
    for k in escolhas:
        lista_retorno.append(candidatos[int(k)])
    eel.tabela_final(lista_retorno)


@eel.expose
def pesquisar(palavra, cargo):
    print(palavra, cargo)
    if(len(palavra) < 1):
        palavra = "all"
    retorno = eleicao.pesquisa_candidatos_nome(palavra, cargo)
    eel.get_retorno(retorno)
eel.start('index_urna.html')
