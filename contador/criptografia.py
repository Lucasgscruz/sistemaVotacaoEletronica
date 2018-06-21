#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Util.randpool import RandomPool
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from base64 import b64decode
import getpass
import base64
import os
import hashlib
"""
Módulo responsável pela criptografia do contador de votos da urna
"""

def gerar_hash(nome_arquivo):
    """Gera hash do arquivo"""
    m = hashlib.sha256()
    arquivo = open(nome_arquivo,'rb').read()
    m.update(arquivo)
    hash_votos = m.digest()
    open("hash_votos_cifrados.txt","w").write(hash_votos)

def gera_chave():
    """Gera a chave aes secreta"""
    AES_tamanho_chave = 32
    chave_aes_secreta = os.urandom(AES_tamanho_chave)
    return chave_aes_secreta

def cifra_chave_simetrica(simetrica):
    arq = open("chave_publica.txt", "r")
    arq2 = open("simetrica_cifrada.txt", "w")
    chave_publica = arq.read()
    chave_publica = base64.b32decode(chave_publica)
    public_key_object = RSA.importKey(chave_publica)
    simetrica_encriptada = public_key_object.encrypt(simetrica, 32)[0]
    # print base64.b32encode(simetrica_encriptada)
    arq2.write(base64.b32encode(simetrica_encriptada))
    arq.close()
    arq2.close()

def cifraVotos(nome_arquivo):
    chave_simetrica = gera_chave()
    aes = AES.new(chave_simetrica, AES.MODE_ECB)

    arquivo = 'votos.txt'
    # O tamanho do arquivo deve ser um multiplo de 16 caracters
    arq_entrada = open(arquivo, "r")
    arq_entrada = arq_entrada.read()
    cryptoSaida = arq_entrada+'#'*(16-len(arq_entrada)%16)
    texto_cifrado = base64.b32encode(aes.encrypt(cryptoSaida))

    arq_saida = open(nome_arquivo,'w')
    arq_saida.write(texto_cifrado)
    arq_saida.close()
    cifra_chave_simetrica(chave_simetrica)
