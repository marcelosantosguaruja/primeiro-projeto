# Programa de cálculo de médias de notas
# Autor: Marcelo Félix dos antos

# Entrada
nome   = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a nota do primeiro bimestre: "))
nota_2 = float(input("Digite a nota do segundo bimestre: "))
nota_3 = float(input("Digite a nota do terceiro bimestre: "))
nota_4 = float(input("Digite a nota do quarto bimestre: "))

# Processamento
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Saída
print(f"\n Aluno      : {nome}")
print(f"\n Média Final: {media:.2f}")

if media >= 6:
    print("Situação: Parabéns o aluno foi APROVADO")
else:
    print("Situação: Não foi desta vez. Aluno REPROVADO")