##verifica se um número é primo
num = int(input("Digite um número inteiro: "))

if num > 1:
    i = 2
    while i < num:
        if (num % i) == 0:
            print(num, "não é um número primo")
            break
        i = i + 1
    else:
        print(num, "é um número primo")
else:
    print(num, "não é um número primo")

