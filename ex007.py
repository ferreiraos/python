ano = int(input("Digite um ano: "))

## Descobre se o ano informado é bissexto
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano nãe é bissexto.")