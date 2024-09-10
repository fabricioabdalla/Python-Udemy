"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n1 = input("Informe um número inteiro: ")

if n1.isdigit():
    n1_int = int(n1)
    par_impar = (n1_int % 2) == 0
    par_impar_texto = 'ímpar'
    
    if par_impar:
        par_impar_texto= 'par'
else:
    print("O número informado não é inteiro")
print(f'O número {n1} é {par_impar_texto}')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
n1 = input("Digite a hora em números inteiros: ");

try:
    hora = int(n1)

    if hora >= 0 and hora <= 11:
        print("Bom Dia")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde")
    elif hora >= 18 and hora <= 23:
        print("Boa noite ;D")
    else:
        print("não conheço essa hora")
except:
    print("Favor digite números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
n1 = input("Informe seu nome: ")
tamanho_nome = len(n1)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print("Seu nome é curto")
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
else:
    print('Por favor, digite mais de uma letra;')
