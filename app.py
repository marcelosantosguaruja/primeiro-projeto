# Programa de cálculo de medias de notas
# Autor: Marcelo Félix dos antos

# Entrada
nome   = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

# Processamento
media = (nota_1 + nota_2) / 2

# Saída
print(f"\n Aluno: {nome}")
print(f"\n Média: {media:.2f}")

if media >= 6:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")