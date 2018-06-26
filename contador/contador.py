#!/usr/bin/env python
# -*- coding: utf-8 -*-
import criptografia as crip
import qr as qr_code
import eleicao as eleicao
import eel
import os
eel.init('contador_gui')

partidos = eleicao.carrega_partidos()
candidatos = eleicao.carrega_candidatos()
v_prefeito = {}
v_vereador = {}

@eel.expose
def salvarVotos():
    total_prefeito = 0
    total_vereador = 0
    max_votos = 0
    eleito = ''
    arq = open("votos.txt", "w")
    arq.write("Primeiro Turno\n")
    for i in candidatos:
        if candidatos[i][4] == 'Presidente':
            arq.write(candidatos[i][1] + ': ')
            arq.write(str(candidatos[i][5]) + '\n')
            if candidatos[i][5] > max_votos:
                eleito = candidatos[i][1]
                max_votos = candidatos[i][5]
            total_prefeito += candidatos[i][5]
    arq.write('Total de votos --> '+ str(total_prefeito) + '\n')
    arq.write('Mais Votado primeiro turno: ' + eleito + ' ' +str(max_votos) + ' votos\n')

    max_votos = 0
    arq.write("\nSegundo Turno\n")
    for i in candidatos:
        if candidatos[i][4] == 'Segundo Turno':
            arq.write(candidatos[i][1] + ': ')
            arq.write(str(candidatos[i][5]) + '\n')
            if candidatos[i][5] > max_votos and candidatos[i][1] != 'Nulo':
                eleito = candidatos[i][1]
                max_votos = candidatos[i][5]
            total_vereador += candidatos[i][5]
    arq.write('Total de votos --> '+ str(total_prefeito) + '\n')
    arq.write('Mais Votado segundo turno: ' + eleito + ' ' +str(max_votos) + ' votos')
    arq.close()
    crip.cifraVotos("votosCifrados.txt")
    crip.gerar_hash("votosCifrados.txt")
    os.system("rm votos.txt")
    #enviarVotos()

def enviarVotos():
    email = 'sendemail -f '
    remetente = 'lucasgscruz10@gmail.com'
    destinatario = 'lucasgscruz10@gmail.com'
    assunto = 'Resultado da Eleição'
    mensagem = 'Segue em anexo os arquivos com os votos.'
    anexos = 'votos.txt votosCifrados.txt'
    servidor = 'smtp.gmail.com:587'
    senha = 'senha123'
    email += remetente
    email += ' -t '
    email += destinatario
    email += ' -u '
    email += assunto
    email += ' -m '
    email += mensagem
    email += ' -a '
    email += anexos
    email += ' -s '
    email += servidor
    email += ' -xu '
    email += remetente
    email += ' -xp '
    email += senha
    #print email
    os.system(email)

def inicializaHash():
    for i in candidatos:
        candidatos[i].append(0)

def contarVoto(vereador, prefeito):
    candidatos[int(vereador)][5] += 1
    candidatos[int(prefeito)][5] += 1
    #print candidatos[int(vereador)][1], str(candidatos[int(vereador)][5])
    #print candidatos[int(prefeito)][1], str(candidatos[int(prefeito)][5])


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
    if codigo is not None:
        vereador=codigo[0]
        prefeito=codigo[1]
        contarVoto(vereador,prefeito)
        eel.redirecionar(vereador,prefeito)

inicializaHash()
eel.start('index_contador.html')
