# Descrição: Identificar se um valor é positivo ou negativo.
# Parâmetros de entrada: Um número real.
# Valores de saída: Classificação do valor informado.
# Autor: Vinicius Gabriel Marcelino Maciel


numero = float(input("Digite um número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero (nem positivo nem negativo)")
