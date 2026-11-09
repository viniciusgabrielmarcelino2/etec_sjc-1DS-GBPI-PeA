# Descrição: Exibir a tabuada tradicional de um número.
# Parâmetros de entrada: Um número inteiro.
# Valores de saída: Tabuada de 1 a 10.
# Autor: Vinicius Gabriel Marcelino Maciel


numero = int(input("Digite um número inteiro: "))
for multiplicador in range(1, 11):
    print(f"{numero} x {multiplicador} = {numero * multiplicador}")
