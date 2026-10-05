soma = 0

for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero  # Somando o número informado ao total

print(f"\nA soma de todos os números informados é: {soma}")