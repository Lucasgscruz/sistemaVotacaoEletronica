#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64
"""
Este modulo é utilizado pela autoridade eleitoral antes da eleição
para gerar as chaves pública e privada.
"""

def gerar_arquivo(dados,nome_arquivo):
    """Grava as chavas em um arquivo"""
    arq=open(nome_arquivo,"w")
    arq.write(dados)
    arq.close()

def gerador_chaves():
    """Realiza a geração das chave pública e privada"""
    random_generator = Random.new().read
    chave = RSA.generate(1024, random_generator) #generate pub and priv key
    chave_publica = chave.publickey().exportKey('DER')# pub key export for exchange
    chave_privada = chave.exportKey('DER')
    gerar_arquivo(base64.b32encode(chave_privada),"chave_privada.txt")
    gerar_arquivo(base64.b32encode(chave_publica),"chave_publica.txt")

gerador_chaves()
