#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Carrega os dados dos candidatos
"""
#-- configurações iniciais
caminho_base = "contador_gui/arquivos/eleicao/"
caminho_fotos = "arquivos/eleicao/fotos/"
#----


dicionario_partidos = {}
candidatos = {}


def carrega_fotos(id):
    """carrega_caminho_das_fotos"""
    foto = caminho_fotos + str(id) + ".jpg"
    return foto


def abre_arquivo(nome):
    """Abre um arquivo em modo de leitura"""
    arq = open(caminho_base + nome, "r")
    return arq


def carrega_partidos():
    """Carrega a lista dos partidos cadastrados"""
    arq = abre_arquivo("lista_partidos.txt")

    for i in arq:
        if("-" not in i):
            retorno = i.split(',')
            dicionario_partidos[int(retorno[1])] = retorno[0]
    return dicionario_partidos


def carrega_candidatos():
    """Carrega a lista de candidatos cadastrados"""
    arq = abre_arquivo("candidatos")
    for i in arq:
        if("-" not in i and len(i) > 1):
            dados_candidatos = i.split(',')
            numero = int(dados_candidatos[0])
            foto = carrega_fotos(numero)
            # formata o padrão de dados candidatos
            candidato = [foto, dados_candidatos[1],
                         dados_candidatos[3].replace("\n", ""), numero, dados_candidatos[2]]
            candidatos[numero] = candidato
    return candidatos


def formata_retorno():

    pass


def pesquisa_candidatos_nome(padrao_busca, cargo):
    """Pesquisa os candidatos de acordo com o nome"""
    lista_retorno = []
    # retorna todos os candidatos de acordo com o cargo
    if(padrao_busca == "all"):
        for i in candidatos:
            if(candidatos[i][4].lower() == cargo.lower()):
                lista_retorno.append(candidatos[i])
        return lista_retorno
    else:
        # retorna a lista de candidatos de acordo com o nome
        for i in candidatos:
            if(padrao_busca.lower() in candidatos[i][1].lower() and candidatos[i][4].lower() == cargo.lower()):
                lista_retorno.append(candidatos[i])
        return lista_retorno
