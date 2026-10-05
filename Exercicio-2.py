nome = input("Digite o seu nome: ")
anoAtual = int(input("Digite o ano que estamos: "))
anoNascimento = int(input("Digite o ano que nasceu: "))

idade = anoAtual - anoNascimento

if idade >= 18:
    print("Você já é maior de idade")

elif idade >= 16:
    print("Você ja pode fazer o titulo de eleitor")

else:
    print("Você não pode fazer nada.")