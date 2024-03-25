# Solicitar como entrada 2 números e depois realizar uma operação matemática simples entre eles.

# Recebe os números do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operadores = input("Informe a operação desejada (+, -, *, /): ")

# Realiza a operação matemática simples
if operadores == '+':
    print(numero1 + numero2)

elif operadores == '-':
    print(numero1 - numero2)

elif operadores == '*':
    print(numero1 * numero2)

elif operadores == '/':
    print(numero1 / numero2)

else:
    resultado = "Operador inválido"
