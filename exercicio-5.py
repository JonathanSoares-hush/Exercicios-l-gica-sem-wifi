soma = 0
quantidade = 0

for i in range(1, 6):
    numero = int(input(f"Digite o {i}º número: "))
    
    # Verifica se o número é par
    if numero % 2 == 0:
        soma += numero
        quantidade += 1

# Exibe o resultado evitando divisão por zero
if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos números pares digitados é: {media}")
else:
    print("Nenhum número par foi digitado.")