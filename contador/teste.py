#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eleicao as eleicao
import qr as qr_code


partidos = eleicao.carrega_partidos()
candidatos = eleicao.carrega_candidatos()

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
    for i in candidatos:
        print candidatos[i][1]+ ": " + str(candidatos[i][5])


def get_candidados(vetor):
    """Retorna o dado dos candidatos"""
    lista_retorno = []
    for i in vetor:
        lista_retorno.append(candidatos[int(i)])
    return lista_retorno

salvarVotos()
