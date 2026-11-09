# Descrição: Exibir os números ímpares de 0 a 20.
# Parâmetros de entrada: Nenhuma.
# Valores de saída: Números ímpares da faixa solicitada.
# Autor: Vinicius Gabriel Marcelino Maciel


for numero in range(0, 21):
    if numero % 2 != 0:
        print(numero)
