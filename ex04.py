# Descrição: Mostrar saudação conforme o turno de estudo.
# Parâmetros de entrada: Letra M, V ou N.
# Valores de saída: Saudação ou mensagem de valor inválido.
# Autor: Vinicius Gabriel Marcelino Maciel


turno = input("Turno (M/V/N): ").strip().upper()
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
