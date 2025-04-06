def matrix_mult(a, b):
    rows_A = len(a)
    cols_A = len(a[0])
    rows_B = len(b)
    cols_B = len(b[0])

    if cols_A != rows_B:
        return None  


    c = [[0 for row in range(cols_B)] for col in range(rows_A)]  

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  
                c[i][j] += a[i][k] * b[k][j]
    return c