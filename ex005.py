idade = int(input("Qual sua idade? "))

## Descobre se o usuário é criança, adulto ou adolescente com base na idade
if idade >= 18:
    print("Você é um adulto.")
elif idade >= 13:
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")
