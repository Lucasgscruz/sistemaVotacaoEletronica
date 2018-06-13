#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel
import eleicao as eleicao
import qr as qr_code
eel.init('contador_gui')

partidos = eleicao.carrega_partidos()
candidatos = eleicao.carrega_candidatos()
v_prefeito = {}
v_vereador = {}

@eel.expose
def salvarVotos():
    arq = open("votos.txt", "a")
    arq.write("Prefeito:\n")
    for i in candidatos:
        if candidatos[i][4] == 'Prefeito':
            arq.write(candidatos[i][1] + ': ')
            arq.write(candidatos[i][5] + '\n')
            
    arq.write("\nVereador:\n")
    for i in candidatos:
        if candidatos[i][4] == 'Vereador':
            arq.write(candidatos[i][1] + ': ')
            arq.write(candidatos[i][5] + '\n')
    arq.close()

def inicializaHash():
    for i in candidatos:
        candidatos[i].append(0)

def contarVoto(vereador, prefeito):
    inicializaHash()
    candidatos[int(vereador)][5] += 1
    candidatos[int(prefeito)][5] += 1

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
    contarVoto(vereador,prefeito)
    eel.redirecionar(vereador,prefeito)

eel.start('index_contador.html')
