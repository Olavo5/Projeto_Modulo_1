

'''onu = ['China', 'EUA', 'Rússia', 'Inglaterra', 'França' ]
 
for pais in onu:
    print(pais)
    idioma = input('Qual é o idioma desse país? ')
print('A ordem correta é: chinês, inglês, russo, inglês e francês') '''



''' def taboada():
    num = int(input('Digite um número para saber a taboada: '))    
    n = 1

    print('A toaboada do n° {} é:' .format(num))

    while n <= 9: 
    
        print( num * n)

        n = n + 1 

taboada() '''



'''numero = 1
soma  = 0
print('Digite os númesros que desejar e, para finalizar a soma, digite 0')

while numero != 0:
    
    numero = int(input('digite um número a sua soma: '))
    
    soma = (soma + numero)

print('A soma desses valores é igual a:', soma)'''

'''numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20, ]

for item in numero:
    if item  % 2 == 0:
        print(item)''' 


num       = 8
n         = 1
tentativa = 3
print('Lembre-se! Você só terá 3 chances.')
while n <= tentativa:
    chute = int(input('arrisque o seu número: '))
    
    if chute == num:
        print('Você acertou! Leia a mensagem')
        print('F1lh0 d3 T0t, ret0rne 4 e22e me2m0 loc4l d0is tmp0s 4pós a cheg4d4 da n01te') 
        break
    n = n + 1