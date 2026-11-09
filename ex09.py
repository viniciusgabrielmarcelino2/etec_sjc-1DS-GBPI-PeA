# Descrição: Somar os números pares de 1 a 500.
# Parâmetros de entrada: Nenhuma.
# Valores de saída: Soma dos pares na faixa solicitada.
# Autor: Vinicius Gabriel Marcelino Maciel


soma = 0
for numero in range(1, 501):
    if numero % 2 == 0:
        soma += numero
print("Soma dos pares de 1 a 500:", soma)
