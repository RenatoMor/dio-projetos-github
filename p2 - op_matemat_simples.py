import operator

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operadores = input("Informe a operação desejada (+, -, *, /): ")

operacoes = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

if operadores in operacoes:
    resultado = operacoes[operadores](numero1, numero2)
    print(resultado)
else:
    resultado = "Operador inválido"
