#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

# conexão com o banco de dados...
"""
Modulo de Conexao com o banco de dados
Realiza a conexao
"""

# atualize este trecho com as configurações pertinentes


def iniciar_conexao():
    """Realiza a conexão com o banco de dados"""
    con = MySQLdb.connect(host="localhost", user='harpocrates',
                               passwd="harpocrates", db='eleicao')

    # retorna um cursor para ser utilizada nas consultas.
    consulta = con.cursor()
    return consulta


def encerrar_conexao(conector):
    """Fecha a conexao"""
    conector.close()
