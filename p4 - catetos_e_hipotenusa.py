from math import hypot

co = float(input("Cateto Oposto: "))
ca = float(input("Cateto Adjacente: "))

h = hypot(co, ca)
hp = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir: {:.2f}".format(h))
print("A hipotenusa vai medir: {:.2f}".format(hp))
