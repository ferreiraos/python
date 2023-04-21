## Recebe a altura do usuário e analisa se é suficiente para ir no brinquedo
altura = float(input("Digite sua altura(em m): "))
altura_minima = float(input("Digite a altura mínima do brinquedo: "))

if altura >= altura_minima:
    print("Vocẽ pode ir no brinquedo.")
else:
    print("Você não tem altura suficiente para ir no brinquedo.")