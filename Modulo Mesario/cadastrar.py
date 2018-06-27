

arquivo=open('usuarios.txt','r')

# (2, '10911109817', 'Alexia', 'Barbosa', '28/02/1995', '31983160034', '36309016', '78', 0, '281562'),
id= 5
cpf= '109513'
data_nascimento=["28/02/1994","13/03/1978","14/05/1993"]
telefone='31983160034'
cep='36309016'
zona='78'
votou=0
impressao='114952'
for i in arquivo:
    pos=0
    if(pos>2):
        pos=0
    if(len(i)>1):
        nome=i.split(" ")[0]
        last=i.split(" ")[1].replace("\n","")
        print(id,cpf+str(id),nome,last,data_nascimento[pos],telefone,zona,0,impressao)
    pos+=1
    id+=1
