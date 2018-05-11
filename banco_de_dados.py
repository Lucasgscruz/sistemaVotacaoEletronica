#!/usr/bin/env python
# -*- coding: utf-8 -*-
import conector_bd as conexao

"""
Modulo responsavel pelas consultas no banco de dados.
"""

# inicia conexao com o banco de dados.
consulta = conexao.iniciar_conexao()


def consulta_cpf(cpf):
    """realiza a consulta a partir do cpf"""
    consulta.execute("SELECT * from eleitores WHERE cpf='%s'" % cpf)
    #(1, '10911109809', 'Carlos', 'Magno', '28/02/1993', '31983160034', '36309010', '78', 0, None)
    dados = consulta.fetchall()
    return dados


def consulta_nome(nome_pesquisa):
    """realiza a consulta a partir do nome"""
    consulta.execute("SELECT * from eleitores WHERE nome='%s'" % nome_pesquisa)
    #(1, '10911109809', 'Carlos', 'Magno', '28/02/1993', '31983160034', '36309010', '78', 0, None)
    dados = consulta.fetchall()
    return dados


def valida_digital(id, codigo):
    """valida a impressao digital"""
    consulta.execute(
        "SELECT digital from eleitores WHERE id_eleitor='%s' and digital='%s'" % id, codigo)
    digital = consulta.fetchall()
    print("Digital, Validacao", digital, codigo)
    if(codigo == digital):
        return True
    else:
        return False
