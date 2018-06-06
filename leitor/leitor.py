#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel
import eleicao as eleicao
import qr as qr_code
eel.init('leitor_gui')

partidos = eleicao.carrega_partidos()
candidatos = eleicao.carrega_candidatos()

def get_candidados(vetor):
    """Retorna o dado dos candidatos"""
    lista_retorno = []
    for i in vetor:
        lista_retorno.append(candidatos[int(i)])
    return lista_retorno

@eel.expose
def carrega_final(escolhas):
    """Realiza a pesquisa pelo numero e carrega os dados finais"""
    candidatos = get_candidados(escolhas)
    eel.tabela_final(candidatos)

@eel.expose
def verificar_vvpat():
    """ verifica o conteudo do vvpat"""
    codigo=qr_code.qr_cam()
    vereador=codigo[0]
    prefeito=codigo[1]
    eel.redirecionar(vereador,prefeito)


eel.start('index_leitor.html')
