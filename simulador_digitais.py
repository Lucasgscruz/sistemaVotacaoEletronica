#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from PIL import Image
"""
Modulo que simula a comparação de digitais
"""
caminho = "modelos_digitais"

arquivos = []
for i in range(1, 8):
    arquivos.append("/fingerprint_0" + str(i) + ".jpg")

imagem1 = caminho + arquivos[1]
impressao1 = open(imagem1, "rb")
dados = impressao1.read()
final = bytearray(dados)

print(imagem1, len(final))


def autenticador(file1, original_banco):
    pass
