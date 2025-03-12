from random import randrange
import numpy as np
import multiprocessing

def product(args):
    row_a, column_b, a, b = args
    return sum(a[row_a][column_a] * b[column_a][column_b] for column_a in range(len(a[0])))

def matrices_product(a, b):
    rows_a = len(a)
    columns_b = len(b[0])
    matrices_product = [[0] * columns_b for _ in range(rows_a)]
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        indexes = [(row_a, column_b, a, b) for row_a in range(rows_a) for column_b in range(columns_b)]
        values = pool.map(product, indexes)
    for i, (row_a, column_b, _, _) in enumerate(indexes):
        matrices_product[row_a][column_b] = values[i]
    return matrices_product

if __name__ == "__main__":
    matrix_a = np.array([
        [randrange(1, 10), randrange(1,10), randrange(1,10)],
        [randrange(1, 10), randrange(1,10), randrange(1,10)],
        [randrange(1, 10), randrange(1,10), randrange(1,10)]
    ])

    matrix_b = np.array([
        [randrange(1, 10), randrange(1,10), randrange(1,10)],
        [randrange(1, 10), randrange(1,10), randrange(1,10)],
        [randrange(1, 10), randrange(1,10), randrange(1,10)]
    ])

    print("Matrix A:", matrix_a)
    print("Matrix B:", matrix_b)
    print("Matrices product", matrices_product(matrix_a, matrix_b))
    print("Checking", np.dot(matrix_a, matrix_b))
