##verificando se um número é perfeito
number = int(input("Insira um número: "))
soma_divisores = 0

for i in range(1, number):
    if number % i == 0:
        soma_divisores += i

if soma_divisores == number:
    print(number, "é um número perfeito.")
else:
    print(number, "não é um número perfeito.")
