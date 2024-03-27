import math

m = float(input("Uma distância em metros: "))
cm = math.floor(m * 100)
mm = math.floor(m * 1000)

print("{}m corresponde a {}cm e {}mm".format(m, cm, mm))


m = float(input("Uma distância em metros: "))
cm = m * 100
mm = m * 1000

print("{}m corresponde a {}cm e {}mm".format(m, cm, mm))
