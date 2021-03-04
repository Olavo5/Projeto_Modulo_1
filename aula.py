def personagem1():
    
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