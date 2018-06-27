#!/usr/bin/env python
# -*- coding: utf-8 -*-
import eel
import eleicao as eleicao
import vvpat as confirmacao
eel.init('urna_gui')


partidos = eleicao.carrega_partidos()
candidatos = eleicao.carrega_candidatos()


def get_candidados(vetor):
    """Retorna o dado dos candidatos"""
    lista_retorno = []
    for i in vetor:
        lista_retorno.append(candidatos[int(i)])
    return lista_retorno


@eel.expose
def confirma_escolha(cargos):
    """Formata para gerar o VVPAT """
    candidatos = get_candidados(cargos)
    prefeito = candidatos[0][1]
    vereador = candidatos[1][1]
    num_prefeito = candidatos[0][3]
    num_vereador = candidatos[1][3]
    # print(cargos)
    dados = ['Segundo Turno: ' + prefeito, 'Primeiro Turno: ' + vereador]
    confirmacao.gera_qrcode(dados, [num_prefeito, num_vereador])


@eel.expose
def carrega_final(escolhas):
    """Realiza a pesquisa pelo numero e carrega os dados finais"""
    candidatos = get_candidados(escolhas)
    eel.tabela_final(candidatos)


@eel.expose
def pesquisar(palavra, cargo):
    """Realiza a pesquisa por uma pessoa de acordo com a palavra chave"""
    print(palavra, cargo)
    if(len(palavra) < 1):
        palavra = "all"
    retorno = eleicao.pesquisa_candidatos_nome(palavra, cargo)
    eel.get_retorno(retorno)
eel.start('index_urna.html')
