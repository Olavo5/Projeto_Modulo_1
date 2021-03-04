''' for pais in onu:
    print(pais)
    idioma = input('Qual é o idioma falado nesse país? ')
print('A ordem correta é: chinês, inglês, russo, inglês e francês')'''






















print('''
     Ao voltar para hospedagem você recebe uma carta anônima marcando um encontro.
     O local é na Esfinge de Gizé, às 20h00, para recuperar os pertences. 
     No entanto, algo parece muito suspeito, pois o sítio arquelógico não abre a noite. ''')

def personagem():
    n         = 1
    tentativa = 3
    
    print('Escolha o seu personagem: ')
    print('(A) Dimitri | (B) Alice | (C) Miguel')
    
    escolha = input(': ').upper()
    
    while escolha != 'A' or escolha != 'B' or escolha !='C' and n <=tentativa:
        print('Tente uma escolha válida!')
        
    n = n + 1
    
    if   escolha  == 'A':
        print('Seja bem-vindo ao jogo, Dimitri.')
    elif escolha  == 'B':
        print('Seja bem-vinda ao jogo, Alice.')
    elif escolha  == 'C':
        print('Seja bem-vindo ao jogo, Miguel.')

    


personagem()