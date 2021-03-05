def linha1():
    print('=' * 60)

def linha2():
    print('*' * 80)



linha1()
print('O LIVRO DE TOT')
linha1()


# Ambientação do jogo.
print('''Uma pequena arca que contem um livro e uma adaga de ouro está em algum lugar do Egito.
O deus Seth é capaz de qualquer coisa pelo livro, que pode torná-lo o Senhor do Mundo,
causando a ruína da humanidade. Somente você pode ajudar a mudar essa história. ''')
linha2()
print ("""\n    _
               __ -
           /     __   \/
             /   _ -    |
         | '  | (_)  |                        _L/L
            |  __  /   /                    _LT/l_L_
           \ \  __  /                     _LLl/L_T_lL_
               -      _T/L              _LT|L/_|__L_|_L_
                    _Ll/l_L_          _TL|_T/_L_|__T__|_l_
                  _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_
                _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_
              _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_
   jjs_ ___ _LT_l_l/|__|__l_T _T_L|_|_|l/___|_ _|__l__|__|__|_T_l_  ___ _
           . ";;:;.;;:;.;;;;_Ll_|__|_l_/__|___l__|__|___l__L_|_l_LL_
             .  .:::.:::..:::.";;;;:;;:.;.;;;;,;;:,;;;.;:,;;,;::;:".'
                 . ,::.:::.:..:.: ::.::::;..:,:::,::::.::::.:;:.:..
                    . .:.:::.:::.:::: .::.::. :::.::::..::..:.::. . .
                      . ::.:.: :. .:::  ::::.::.:::.::...:. .:::. .
                          .:. ..   . ::.. .: ::. ::::.:: ::::::.   .
                          .  :.         .. :::.::: ::.::::. ::. .
                            . .           .:. :.. :::. ::..: :.
                nn_r   nn_r   .              :  .:::.:: ::..:  .
               /l(\   /l)\      nn_r          . ::. :. : : ..
               `'"``  ``"``    /\(\              . . .:. . : .
                               ' "``                  . :. .
                                                       .   .
                                                          .
n""")
print('''
 Dimitri é um arqueólogo do Rio de Janeiro. É muito curioso e isso pode, o que pode ser um pouco perigoso. 
 Alice é uma matemática do Pernambuco. É extramamente inteligente e adora desafios.
 Miguel é um arquiteto nascido na Bahia. A sua coragem o leva a lugares inimagináveis.
 ''')
 
linha2()



# Início da história e escolha dos personagens.
def personagem():
    
    print('Escolha o seu personagem: ')
    print('(A) Dimitri | (B) Alice | (C) Miguel')
    linha2()
    escolha = input(': ').upper()
    linha2()
    
    if   escolha  == 'A':
        
        print('''
         O Dimitri é um arqueólogo brasileiro e ganhou uma bolsa de doutorado da Universidade do Cairo,
         no Egito, com todos os gastos de passagem e moradia e demais despesas por conta do governo egípcio.
         No entanto, apesar de ser o seu sonho, você nunca se candidatou a tal vaga.
         E aí, vai aceitar a oferta? Digite SIM ou NÃO?''')
        linha2()

    elif escolha  == 'B':
        print('''
         A Alice é uma matemática brasileira e ganhou uma bolsa de doutorado da Universidade do Cairo,
         no Egito, com todos os gastos de passagem e moradia e demais despesas por conta do governo egípcio.
         No entanto, apesar de ser o seu sonho, você nunca se candidatou a tal vaga.
         E aí, vai aceitar a oferta? Sim ou não?''') 
        linha2()

    elif escolha  == 'C':
        print('''
         O Miguel é uma arquiteto brasileira e ganhou uma bolsa de doutorado da Universidade do Cairo,
         no Egito, com todos os gastos de passagem e moradia e demais despesas por conta do governo egípcio.
         No entanto, apesar de ser o seu sonho, você nunca se candidatou a tal vaga.
         E aí, vai aceitar a oferta? Sim ou não? ''' ) 
        linha2()
    else:
        print('Opção inválida. Fim de jogo.')
        personagem1()

personagem()

#Locais da hitória


resposta    = input(': ').upper()

if resposta == 'SIM':
    print('Uhul! Pegue as malas e partiu Egito')
else:
    print('fim de jogo')

# História
print('''Seguindo os conselhos do reitor Amon, após chegar ao Egito e antes das aulas começarem, 
o ideal é iniciar uma adaptação ao país e visitar a redondeza.  
    Escolha onde quer ir (a)Esfinge de Gizé, (b)Museu (c)Pirâmides''')

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
        ('Fim fe jogo')

    
def local2():

    print('''As pirâmides de Quéops, 
     a pedra mais leve pesa 500 kg e a mais pesada, 6 toneladas! ')
     (v) Verdadeiro (f) falso''')

    resposta = int(input(': '))
    
    if not resposta == 'v':
        print(' Errado' )
    else:
        ('Você chegou ao seu destino')


def local3():

    print(''' Os tesouros de qual faraó se encontram no museu?
    A) Amenhotep III | B) Tutankhamon| C) Amarna''')

    resposta = input(': ').upper()
    
    if resposta == 'B':
        print(' Você chegou ao seu destino' )
    else:
        ('Errado')


onde_ir = input(': ') 

if onde_ir == 'A':
    print(local1())
elif onde_ir == 'B':
    print(local2())
elif onde_ir == 'C':
    print(local3())
else:
    ('Escolha Inválida.')


#História
print(''' 
Chegando ao local e vendo toda aquela gente, 
uma escrita antiga na parede te chama atenção… mas… ela não faz parte da exposição. 
Ninguém se quer presta a atenção nela. 
Mas com os seus conhecimentos em você logo 
identifica os hieróglifos e percebe se tratar de um enigma.
''')
linha2()
print('''Tente acertar o número para ler o enígma.
Dica: é um número de 1 a 10''')

num       = 8
n         = 1
tentativa = 3
print('Você só terá 3 chances.')
while n <= tentativa:
    chute = int(input('arrisque o seu número: '))
    
    if chute == num:
        print('Você acertou! Leia a mensagem')
        print('F1lh0 d3 T0t, r3t0rne 4 e22e me2m0 loc4l d0is tmp0s 4pós a cheg4d4 da n01te') 
        linha2()
        break
    n = n + 1

print('A que horas seria isso?  A) 18hs00| B) 20hs00| C) 22hs00| D) 00hs00| ')
linha2()
hora_certa    = input(': ').upper()

if hora_certa == 'B':
    print('Vá até o local')
    linha2()
else:
    print('Você errou! A sua mochila foi roubada')
    print('''
     Ao voltar para hospedagem você recebe uma carta anônima marcando um encontro.
     O local é na Esfinge de Gizé, às 20h00, para recuperar os pertences. 
     No entanto, algo parece muito suspeito, pois o sítio arquelógico não abre a noite. ''')

    print('''
    Ao chegar ao local, você ouve um som que parece ter saído da esfinge, 
    o que parece ser loucura. No mesmo instante, uma passagem se abre para dentro da 
    Esfinge de Gizé, e a estátua de Anúbis te dá uma xarada, se a resolver, você terá uma passagem
    segura para dentro do da esfinge, se não...''')
    print(local1())

print('Para ter uma entrada segura, responda o enigma.')
print('''A sabedoria que corre no seu sangue nos une por um ancestral em comum.
Eu sou o entendimento dos homens, eu sou a escrita. Os egípcios me chamam de:

A) Bhrami| B) Nahuatl| C) Hieróglifo| ''')
linha2()

resposta = input(': ').upper()

if resposta == 'C':
    print('Siga em frente')
else:
    ('Uma armadilha te decaptou. Fim de jogo!')

linha2()
print(
''' "Que bom que você leu a minha mensagen!"

Dentro da esfinge, um pouco atordoado. 
Uma garota encapuzada fala sobre coisas em que você tem certeza ser algum tipo de trote da universidade.
Uma ordem secreta do tempo dos faraós, que ajuda os deuses egípcios a manterem o equilíbrio na terra?
E agora a ordem precisa da sua ajuda?? Por quê ??? A mensagem na parede foi dela pra mim?
Ela se apresenta como Nefertari. ''')
linha2()
print(
''' Nefertare fala sobre um livro. 
“...existe um livro de encantamento do deus Tot, o deus da sabedoria. 
Esse livro contem detalhes de como derrotar Set. 
Precismos que você nos ajude a roubá-lo e traduza o livro, 
afinal o artefato só pode ser lido por um descendente do próprio deus.” 
Ma menina te mostra um pedaço de papiro''')
linha2()

def museux():
    print('A) Castelo de Salah Al-din |B) Museu Egípcio |C) Grande Museu Egípcio ')
    resposta = input(': ').upper()
    if resposta == 'A':
        print('Vá até o museu!')

def papiro():
    num       = 7
    n         = 1
    tentativa = 3
    print(''''
    Por ser da descendênca de Tot, o papiro é legível somente para você.
    Mas para ler, resolva o enígma: 

    "O sistema de numeração egípcio baseava-se em quantos números chave? "''')
    
    while n <= tentativa:
        chute = int(input('arrisque o seu número: '))
        
        if chute == num:
            print('Você acertou! Leia a mensagem')
            print('No novo tempo, os filhos dos antigos guardam as histórias dos grandes a margem Nilo, lá também estará o meu livro. ') 
            print(museux())
            break
        n = n + 1 

#Final da história
linha1()
print(''' Já dentro do museu, você e Nefertiti ouvem um barulho de carro chegando.
 Mas o local está fechado. Quem mais estaria lá seria?. Espera… é  o reitor?''')

print(''' O reitor Amon pede a sua ajuda, mas Nerfetiti diz que é armação, o que fazer?
Ele parece tão atordoado!
Nesse momento, o próprio deus Seth se materializa, ele manipula o=as intensões do reitor, que parece um zumbi.
E confessa que tudo fazia parte do plano dele para que o você pudesse chegar ao egito. 
A bolsa de estudos abrir a arca com o livro.

Então você tem o que parece ser a melhor ideia da noite:
Corre até a arca, abre traduzindo a simbologia de Tot, pega o livro e a adaga de ouro. 
Ambos gritam para você jogar o livro para eles, mas você não sabe o que fazer... ''')
linha1()

def final():
    resposta_final = input(''' 
          A) Uso a adaga contra Seth.
          B) Entrgo a adaga a nerfetiti.  
          C) Entrego o livro a nerfetiti.
          D) Abro o livro.
          E) Sai correndo os artefatos.
          F) Entrego o livro a Amon.
          ''').upper()
    linha2()
    
    if resposta_final   =='A':
        linha1()
        print('Seth te segurou pelo pescoço e te desarma. O deus te ergueu como se não fosse nada e você morreu.')
        print('VOCÊ PERDEU! FIM DE JOGO')
        linha1()
    
    elif resposta_final =='B':
        linha1()
        print('Nefertari agradesce e se volta contra você. Ela te mata.')
        print('VOCÊ PERDEU! FIM DE JOGO')
        linha1()
    
    elif resposta_final =='C':
        linha1()
        print('Em um ato surpreedente, Nerfertati joga o livro para Seth. Ela o enganou. O mundo está sob o domínio do deus.')
        print('VOCÊ PERDEU! FIM DE JOGO')
        linha1()
    
    elif resposta_final =='D': 
        linha1()
        print('Amon diz para vc ler a ultima página. O próprio deus Tot é invocado e luta contra Seth')
        print('Parabén! Você salvou o mundo.')
        print(''' 
        Amon me explica que a Ordem realmente existe, mas nefertiti 
        foi uma traidora que se rendeu a ganância de seth e traiu seus companheiros. 
        Como o reitor é descendente de hórus e menbro da ordem,
        ele é quem cuida do oráculo que descobriu que, num passado muito distante. 
        Tot se apaixonou por uma mortal e seus descendentes foram mortos e perseguidos. 
        Os poucos sobrevivente imigraram para o continente americano e que você é o último.''')
        linha1()
    
    elif resposta_final == 'E':
        linha1()
        print('Seth se materializa na sua frente. O deus rasga a sua garganta.')
        print('VOCÊ PERDEU! FIM DE JOGO')
        linha1()
    
    elif resposta == 'F':
        linha1()
        print(''' Entrega o livro a Seth mas... me entrega uma página rasgada. 
        A ultima página que contem o encantamento. Eu leio, Tot é invocado e derrota. ''')
        print('Parabén! Você salvou o mundo.')
        print(''' 
        Amon me explica que a Ordem realmente existe, mas nefertiti 
        foi uma traidora que se rendeu a ganância de seth e traiu seus companheiros. 
        Como o reitor é descendente de hórus e menbro da ordem,
        ele é quem cuida do oráculo que descobriu que, num passado muito distante. 
        Tot se apaixonou por uma mortal e seus descendentes foram mortos e perseguidos. 
        Os poucos sobrevivente imigraram para o continente americano e que você é o último.''')
        linha1()
    
    else:
        linha1()
        print('Você falhou!')
        linha1()
final()
