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


def marca_voto(id):
    """Atualiza o estado do voto"""
    id = str(id)
    sql = "UPDATE eleitores SET votou=1 WHERE id_eleitor=" + id
    consulta.execute(sql)


def valida_digital(id, codigo):
    """valida a impressao digital"""
    id = str(id)
    codigo = str(codigo)
    sql = "SELECT digital from eleitores WHERE id_eleitor=" + \
        id + " AND digital=" + codigo
    estado = consulta.execute(sql)

    if(estado):
        return True
    else:
        return False
