##Programa que verifica se um número é par, ímpar ou positivo
num = float(input("Digite um número: "))

if num % 2 == 0:
    print("O número é par.")
elif num > 0:
    print("O número é ímpar.")
else:
    print("O número é positivo.")
