# Descrição: Solicitar dois números e apresentar o maior deles.
# Parâmetros de entrada: Dois números reais.
# Valores de saída: Maior número ou aviso de igualdade.
# Autor: Vinicius Gabriel Marcelino Maciel


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
if a > b:
    print("Maior número:", a)
elif b > a:
    print("Maior número:", b)
else:
    print("Os números são iguais.")
