# Descrição: Somar os números naturais de 1 a 100.
# Parâmetros de entrada: Nenhuma.
# Valores de saída: Soma dos 100 primeiros naturais.
# Autor: Vinicius Gabriel Marcelino Maciel


soma = 0
for numero in range(1, 101):
    soma += numero
print("Soma de 1 a 100:", soma)
