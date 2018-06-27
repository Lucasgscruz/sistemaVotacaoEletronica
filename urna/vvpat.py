#!/usr/bin/env python
# -*- coding: utf-8 -*-
# biblioteca
# https://pypi.org/project/qrcode/

import qrcode
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
"""
Geração do QrCode
"""
caminhho_urna = "urna_vvpats/"


def contador_vvpat(contador):
    arq = open('contador.txt', 'a')
    arq.write(str(contador) + "\n")
    arq.close()


def recuperar_contador():
    try:
        arq = open('contador.txt', "r")
        pos = arq.readlines()
    except Exception as e:
        # contador auxiliar, o arquivo original não foi encontrado
        contador_vvpat(3000)
        arq = open('contador.txt', "r")
        pos = arq.readlines()
    valor = int(pos[len(pos) - 1])
    return valor


def gera_qrcode(impressao, contagem):
    """Gera o qrcode"""
    print(impressao, contagem)
    img = qrcode.make(str(contagem))
    gera_vvpat(img, impressao)


def gera_vvpat(img, dados):
    """Combina o QrCode com info para gerar vvpat"""
    #img = Image.open("teste.png")
    pos = recuperar_contador()
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("Roboto-Medium.ttf", 16)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((40, 250), str(dados[0]), font=font)
    draw.text((40, 270), str(dados[1]), font=font)
    name = 'vvpat_' + str(pos) + '.png'
    img.save(caminhho_urna + name)
    # exibe o vvpat salvo..
    visualizar = Image.open(caminhho_urna + name)
    #visualizar.show()

    pos += 1
    contador_vvpat(pos)
