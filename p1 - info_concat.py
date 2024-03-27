from termcolor import colored

info1 = colored(input("Digite a primeira informação: "), 'green')
info2 = colored(input("Digite a segunda Informação: "), 'blue')

info_concatenadas = info1 + " " + info2

print("A concatenação dos valores informados:", colored(
    info_concatenadas, 'yellow', attrs=['bold', 'underline']))
