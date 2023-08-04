## verifica se um número é primo ou não, em caso afirmativo, exibe seus divisores
numero = int(input("Digite um número inteiro: "))
divisores = []
i = 2

if numero < 2:
    print("O número deve ser maior ou igual a 2.")
else:
    while i <= numero / 2:
        if numero % i == 0:
            divisores.append(i)
        i = i + 1
## retorna os números da lista de divisores
    if len(divisores) == 0:
        print("O número", numero, "é primo.")
    else:
        print("O número", numero, "não é primo.")
        print("Divisores:", divisores)
