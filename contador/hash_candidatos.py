#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import zipfile

"""
Verifica a integridade da base de candidatos.
"""

cripto = hashlib.sha256()

caminho_base = "contador_gui/arquivos/"
# chave.. Atualize a chave de integridade
key = b'-MsT\x9c\xab.\x86\x11W\xac\x88}\xa1J\x12p\xeav\xd9\xf0LJex\xee\xa3\xf7\x8e\x97%\x07'


def descompactar():
    """descompacta o arquivo de configuração da eleicao"""
    zip = zipfile.ZipFile(caminho_base + 'eleicao.zip', "r")
    zip.extractall("arquivos")
    print("Concluído..")


def verifica_integridade():
    """Verifica a integridade do arquivo de eleicao"""
    arquivo = open(caminho_base + "eleicao.zip", 'rb')
    file = arquivo.read()
    cripto.update(file)
    hash = cripto.digest()

    if(hash == key):
        print("Integridade Ok, Iniciando descompactação.")
        descompactar()


verifica_integridade()
