# harpocrates
Sistema de votação eletrônica Harpocrates

Sistema de votação desenvolvido para a disciplina de segurança de urnas eletrônicas.

- Carlos Magno
- Lucas Geraldo
- Matheus Reis

UFSJ 2018
Site: http://harpocrates.magnustec.com

# Requisitos

- Obrigatorios
* python3
* eel
* mysql
* pill
* qrcode
* opencv
* zbar
* Chrome
## Opcional
* phpmyadmin

Para instalar as dependências execute:
> python3 -m pip install eel

> pip install eel

> pip install qrcode[pil]

> python3 -m pip install qrcode[pil]

> sudo apt-get install python-zbar

# Banco de dados

O módulo de mesário do harpocrates está utilizando um banco de dados mysql para completar as suas funcionalidades, portanto é necessário a criação de um banco e uma tabela.

Configurando o Banco:

- Crie um novo banco importado o banco_de_dados.sql disponível na pasta banco de dados. Será criada um banco chamado eleitores.

- Agora importe os dados do arquivo eleitores.sql que contém a população do banco.

- Agora configure os dados de conexão com o mesmo no arquivo conector_bd.

# Geração vvpat

Os arquivos de vvpat são armazenados no diretorio urna_vvpats. Crie esta pasta dentro da pasta urna se o mesmo não existir.

# Para Executar

Executa o módulo do mesario
> python3 mesario.py

Executa o módulo da urna
> python3 urna.py

Modulo de Confirmação/leitor

> python leitor.py

## Desenvolvido por:
![](https://github.com/ValneyFaria.png?size=100)
Valney Faria ([github](https://github.com/cmagnobarbosa))

![](https://github.com/Lucasgscruz.png?size=100)
Lucas Cruz ([github](https://github.com/lucasgscruz))