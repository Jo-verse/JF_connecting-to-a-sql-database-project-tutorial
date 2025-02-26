height =5
# Inicializa el triángulo de Pascal
pascal = [[1]]
# Genera el triángulo de Pascal
for i in range(1, height):
    row = [1]
    for j in range(1, i):
        row.append(pascal[i-1][j-1] + pascal[i-1][j])
    row.append(1)
    pascal.append(row)
# Imprime el triángulo de Pascal
for i in range(height):
    print(" " * (height-i), end=" ", flush=True)
    for j in range(i+1):
        print(pascal[i][j], end=" ", flush=True)
    print()         