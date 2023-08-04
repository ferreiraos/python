## verifica se um número é múltiplo de 3 ou de 5
num = int(input("Digite um número inteiro: "))

if num % 3 == 0:
    print("O número", num, "é multiplo de 3.")
elif num % 5 == 0:
    print("O número", num , "é múltiplo de 5.")
else:
    print("O número", num, "não é múltiplo de 3 nem de 5.")
