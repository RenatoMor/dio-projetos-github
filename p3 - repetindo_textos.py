print("Repetindo textos v1")
print("-"*20)

texto = input("Digite uma string: ")
repetir = int(input("Digite um número: "))

resultado = texto * repetir

print(resultado)

print("\n")
print("-"*100)
print("\n")

print("Repetindo textos v2")
print("-"*20)
texto = input("Digite uma string: ")
repetir = int(input("Digite um número: "))

resultado = (texto + ' • ') * repetir

print(f"{'\n\rTexto':<10} {'Repetições':<15} {'Resultado':<10}")
print(f"{texto:<10} {repetir:<15} {resultado:<10}")
