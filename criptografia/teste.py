#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Util.randpool import RandomPool
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from base64 import b64decode
import os
import base64

chaveSimetrica = "123456789abcdefg"

def cifraVotos():
    aes = AES.new(chaveSimetrica, AES.MODE_ECB)
    #recebe o arquivo a ser criptografado
    arquivo = 'votos.txt'
    #ler o arquivo e corrigir o seu tamanho
    #o tanho dever ser um multiplo de 16 caracters
    arq_entrada = open(arquivo, "r")
    arq_entrada = arq_entrada.read()
    cryptoSaida = arq_entrada+'#'*(16-len(arq_entrada)%16)

    texto_cifrado = aes.encrypt(cryptoSaida)
    arq_saida = open('votosCifrados.txt','w')
    arq_saida.write(texto_cifrado)
    arq_saida.close()

def cripArquivo():
    #criando uma chave de criptografia
    chave = "0123456789ABCDEF"
    aes = AES.new(chave, AES.MODE_ECB)

    #recebe o arquivo a ser criptografado
    arquivo = 'votos.txt'

    #ler o arquivo e corrigir o seu tamanho
    #o tanho dever ser um multiplo de 16 caracters
    arq_entrada = open(arquivo, "r")
    arq_entrada = arq_entrada.read()
    #arq_entrada = 'Vai Brasil!!\n'

    #caso o tamanho nao seja muliplo de 16 ele verifica quantos caracteres
    #faltam para prencher e os preenche com o caractere '#'
    cryptoSaida = arq_entrada+'#'*(16-len(arq_entrada)%16)

    #criptografando o arquivo corrigido
    #alem disso vamos colocar os dados criptografados
    #em uma forma que caracteres estranhos nao aparecam
    texto_cifrado = base64.b32encode(aes.encrypt(cryptoSaida))

    #nesta etapa eh realizado os passos anteriores mas desta vez no titulo
    titulo_novo=base64.b32encode(aes.encrypt(arquivo+'#'*(16-len(arquivo)%16)))

    arq_saida = open(titulo_novo,'w')
    arq_saida.write(texto_cifrado)
    arq_saida.close()

def decriArquivo():
    #criando uma chave de criptografia
    chave = "0123456789ABCDEF"
    aes = AES.new(chave, AES.MODE_ECB)

    #recebe o arquivo a ser descriptografado
    arquivo = '2UCCIDQMNXF44CYFYUOEO4X3AY======'
    #ler o arquivo
    arq_entrada = open(arquivo, "r")
    #esta etapa iremos decodificar os caracteres para sua forma original
    arq_entrada = base64.b32decode(arq_entrada.read())

    #vamos recuperar o nome do arquivo e retirar os
    #caracteres adicionais que colocamos na etapa passada
    titulo_antigo=aes.decrypt(base64.b32decode(arquivo))
    titulo_antigo=titulo_antigo.rstrip('#')

    #vamos repetir o processo para o conteudo do arquivo
    texto_recuperado=aes.decrypt(arq_entrada)
    texto_recuperado=texto_recuperado.rstrip('#')

    #e por fim vamos recriar o arquivo na sua forma original
    arq_saida2 = open(titulo_antigo,"w")
    arq_saida2.write(texto_recuperado)

def assimetrica():
    texto = "texto a encriptar"

    # Você deve usar a melhor fonte de dados aleatórios que tiver à
    # disposição. Pra manter o exemplo mais portável, usaremos o
    # RandomPool do próprio PyCrypto:

    pool = RandomPool(384)
    pool.stir()

    # randfunc(n) deve retornar uma string de dados aleatórios de
    # comprimento n, no caso de RandomPool, o método get_bytes
    randfunc = pool.get_bytes

    # Se tiver uma fonte segura (como /dev/urandom em sistemas unix), ela
    # deve ser usada ao invés de RandomPool

    # pool = open("/dev/urandom")
    # randfunc = pool.read

    # Tamanho da chave, em bits
    N = 1024

    # O algoritmo RSA usado aqui não utiliza K, que pode ser uma string
    # nula.
    K = ""

    # Geramos a chave (contendo a chave pública e privada):
    key = RSA.generate(N, randfunc)
    print key.exportKey()
    print '\n\n'

    # Criptografamos o texto com a chave:
    enc = key.encrypt(texto, K)
    print enc
    # Podemos decriptografar usando a chave:
    dec = key.decrypt(enc)
    print dec + '\n\n'
    # Separando apenas a chave pública:
    pub_key = key.publickey()
    print pub_key.exportKey()
    print '\n\n'

    # Criptografando com a chave pública:
    enc = pub_key.encrypt(texto, K)
    print enc

    # Decriptografando com a chave privada:
    dec = key.decrypt(enc)
    print dec + '\n\n'
    # As informações da chave são compostas de seis atributos: 'n', 'e',
    # 'd', 'p', 'q' e 'u'. Se quiser armazenar ou enviar uma chave você
    # pode usar pickle ou simplesmente usar esses atributos com o método
    # construct. Por exemplo:

    # Os atributos 'n' e 'e' correspondem à chave pública:
    n, e = key.n, key.e

    # E recriamos a chave pública com esses dados:
    pub_key = RSA.construct((n, e))
    print dir(RSA)

def assinar():
    message = "I want this stream signed"
    digest = SHA256.new()
    digest.update(message)

    # Read shared key from file
    private_key = False
    with open ("privada.pem", "r") as myfile:
        private_key = RSA.importKey(myfile.read())

    # Load private key and sign message
    signer = PKCS1_v1_5.new(private_key)
    sig = signer.sign(digest)

    # Load public key and verify message
    verifier = PKCS1_v1_5.new(private_key.publickey())
    verified = verifier.verify(digest, sig)
    assert verified, 'Signature verification failed'
    print 'Successfully verified message'

def verificaAss():
    pub_key = open('publica.txt', "r").read()
    rsakey = RSA.importKey(pub_key)
    signer = PKCS1_v1_5.new(rsakey)
    digest = SHA256.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(b64decode('texto a encriptar'))
    if signer.verify(digest, b64decode('3e2d83bbdcab4294644bcfb2e67024b67f70a8352eced60a067f3951ddf0e9fe')):
        return True
    return False

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
enviarVotos()
