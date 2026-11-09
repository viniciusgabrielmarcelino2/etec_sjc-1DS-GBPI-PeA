# Descrição: Calcular média e situação de um aluno.
# Parâmetros de entrada: Duas notas parciais.
# Valores de saída: Média e situação do aluno.
# Autor: Vinicius Gabriel Marcelino Maciel


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Média: {media:.2f}")
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
