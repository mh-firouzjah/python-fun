import math

import numpy as np


def determinant(matrix):
    n_array = np.array(matrix)
    return int(f"{np.linalg.det(n_array):.0f}")


def determinant(matrix):
    return round(np.linalg.det(matrix))
