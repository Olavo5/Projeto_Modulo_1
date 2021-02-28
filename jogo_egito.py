# Ambientação do jogo
print('''Em um mundo onde a ganância dos deuses pode levar a ruína da humanidade, somente 
um(a) jovem estudante,''')



#Início da hitória
print('''Você é um(a) arqueólogo(a) brasileiro(a) e ganhou uma bolsa de doutorado da Universidade do Cairo,
no Egito, com todos os gastos de passagem e moradia e demais despesas por conta do governo egípcio.
No entanto, apesar de ser o seu sonho, você nunca se candidatou a tal vaga.
         E aí, vai aceitar a oferta? Sim ou não?
 ''') 


resposta = input(': ')

if resposta == 'sim':
    print('Uhul! Pegue as malas e partiu Egito')
else:
    print('fim de jogo')

# História
print('''Seguindo os conselhos do reitor Amon, após chegar ao Egito e antes das aulas começarem, 
o ideal é iniciar uma adaptação ao país e visitar a redondeza.  
    Escolha onde quer ir (a)Museu, (b)Esfinge de Gizé, (c)Pirâmides''')

onde_ir = input(': ') 

if onde_ir == 'a':
    print('')
elif onde_ir == 'b':
    print(''' 
    Eu sou um número de quatro dígitos.
    O primeiro dígito é 1/2 do último.
    O segundo dígito é três vezes o primeiro. 
    Já o terceiro é o segundo dígito mais três. 
    Multiplique tudo por dois, em que ano eu nasci? ''')

elif onde_ir == 'c':
    print('As pirâmides de Quéops, a pedra mais leve pesa 500 kg e a mais pesada, 6 toneladas! ')
    print('(v) Verdadeiro (f) falso')

else:
    print('escolha uma opção válida')
    
def local1():

    print(''' Eu sou um número de quatro dígitos.
    O primeiro dígito é 1/2 do último.
    O segundo dígito é três vezes o primeiro. 
    Já o terceiro é o segundo dígito mais três. 
    Multiplique tudo por dois, em que ano eu nasci?''')

    resposta = int(input(': '))
    
    if resposta == 2724:
        print(' Você chegou ao destino' )
    else:
        ('Errado')