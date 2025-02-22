# Usando % formatea un número con un número específico de decimales
import random
num = random.random()
ans = "%.2f" % num
print("%")
print(ans)

# Usando "format" formatea un número con un número específico de decimales
num2 = 53936.936202730
ans2 = "{:.2f}".format(num2)
print ("format")
print(ans2)

# Usando "round" redondea un número a una cantidad específica de decimales
ans3 = round(num2, 5)
print("round")
print(ans3)

# Usando función "trunc" devuelve la parte entera de un número
import math
ans4 = math.trunc(num2)
print("trunc")
print(ans4)

# Usando "ceil" y "floor" para redondear un número hacia arriba o hacia abajo
ans5 = math.ceil(num2)
ans6 = math.floor(num2)
print("ceil")
print(ans5)
print("floor")
print(ans6)

