n1 = int(input("Insira o 1° Número: "))
n2 = int(input("Insira o 2° Número: "))

if n1 > n2:
    print(f"O número {n1=} é maior que {n2=}")
elif n2 > n1:
    print(f"O número {n2=} é maior que {n1=}")
elif n1 == n2:
    print(f"Os números são iguais")
else:
    print(f"Algum dos valores inseridos não é um número")