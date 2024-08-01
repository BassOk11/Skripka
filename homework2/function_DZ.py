def get_matrix(n=int(input()), m=int(input()), value=int(input())):
    matrix = []
    for i in range(n):
        matrix1 = []
        for j in range(m):
            matrix1.append(value)
        matrix.append(matrix1)
    return matrix


resalt = get_matrix()
print(resalt)
