#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64
import hashlib
"""
Este modulo é utilizado pela autoridade eleitoral antes da eleição
para gerar as chaves pública e privada.
"""

def gerar_hash(nome_arquivo):
    """Gera hash do arquivo"""
    m = hashlib.sha256()
    arquivo = open(nome_arquivo,'rb').read()
    m.update(arquivo)
    hash_votos = m.digest()
    return hash_votos

def verifica_hash():
    hash=open("hash_votos_cifrados.txt","r").read()
    hash_votos_cifrados=gerar_hash("votosCifrados.txt")
    if(hash== hash_votos_cifrados):
        return True
    print "Arquivo Corrompido."

def descriptografa_votos():
    votos = open('votos_resultado.txt','w')
    chave_simetrica=descriptografa_chave_simetrica()
    decrypto= Crypto.Cipher.AES.new(chave_simetrica)
    resultado_eleicao = decrypto.decrypt(base64.b32decode(open("votosCifrados.txt", "r").read()))
    resultado_eleicao = resultado_eleicao.rstrip("#")
    votos.write(resultado_eleicao)
    votos.close()

def descriptografa_chave_simetrica():
    arq = open("chave_privada.txt", "r")
    arq2 = open("simetrica_cifrada.txt", "r")
    chave_privada= arq.read()
    chave_cifrada= arq2.read()
    chave_privada = base64.b32decode(chave_privada)
    chave_cifrada = base64.b32decode(chave_cifrada)
    objeto_chave_privada = RSA.importKey(chave_privada)
    simetrica_plana = objeto_chave_privada.decrypt(chave_cifrada)
    return simetrica_plana

if(verifica_hash()):
    descriptografa_votos()
