n = int(input("Digite um número inteiro: "))

if n < 2:
    print("O número não é primo.")
else:
    i = 2
    res = False
    
    while i < n and not res:
        x = n % i
        if x == 0:
            res = True
        i += 1
    
    if res:
        print("O número não é primo.")
    else:
        print("O número é primo.")
