import numpy as np
from dyers import *

# Matrix Encryption
def mat_enc(matrix, kappa, p, modulus, delta):
    if isinstance(matrix, list):  # turns list types into ndarray types
        matrix = np.array(matrix)
    if len(matrix.shape) == 1:  # Condition where only one column
        rows = matrix.shape[0]
        cols = 1
        enc_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            enc_matrix[i] = enc(matrix[i], kappa, p, modulus, delta)
        return enc_matrix
    else:  # Condition with multiple columns
        rows, cols = np.shape(matrix)
        enc_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            for ii in range(cols):
                enc_matrix[i][ii] = enc(matrix[i][ii], kappa, p, modulus, delta)
        return enc_matrix

#  Matrix Decryption
def mat_dec(matrix, kappa, p, delta):
    if isinstance(matrix, list):
        matrix = np.array(matrix)
    if len(matrix.shape) == 1:
        rows = matrix.shape[0]
        cols = 1
        dec_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            dec_matrix[i] = dec(matrix[i], kappa, p, delta)
        return dec_matrix
    else:
        rows, cols = np.shape(matrix)
        dec_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            for ii in range(cols):
                dec_matrix[i][ii] = dec(matrix[i][ii], kappa, p, delta)
        return dec_matrix

#  matrix multiplication with mod add/mult
def mat_mult(matrix1, matrix2, modulus):
    if isinstance(matrix1, int) or isinstance(matrix2, int):
        mat_prod = mult(matrix1, matrix2, modulus)
    else:
        if isinstance(matrix1, list):
            matrix1 = np.array(matrix1)
        if isinstance(matrix2, list):
            matrix2 = np.array(matrix2)
        if len(matrix1.shape) == 1:  # Condition where only one column
            rows1 = matrix1.shape[0]
            cols1 = 1
        else:
            rows1, cols1 = np.shape(matrix1)
        if len(matrix2.shape) == 1:  # Condition where only one column
            rows2 = matrix2.shape[0]
            cols2 = 1
        else:
            rows2, cols2 = np.shape(matrix2)

        if cols1 != rows2:
            raise ValueError("Matricies do not have correct dimensions for multiplication")
        mat_prod = np.zeros((int(rows1), int(cols2)), dtype=object)
        result = 0
        for i in range(rows1):
            for ii in range(cols2):
                for k in range(cols1):
                    result = add(result, mult(matrix1[i][k], matrix2[k][ii], modulus), modulus)
                mat_prod[i][ii] = result
                result = 0
    return mat_prod

def mat_encode(matrix, delta):
    if isinstance(matrix, list):  # turns list types into ndarray types
        matrix = np.array(matrix)
    if len(matrix.shape) == 1:  # Condition where only one column
        rows = matrix.shape[0]
        cols = 1
        encode_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            encode_matrix[i] = encode(matrix[i], delta)
        return encode_matrix
    else:  # Condition with multiple columns
        rows, cols = np.shape(matrix)
        encode_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            for ii in range(cols):
                encode_matrix[i][ii] = encode(matrix[i][ii], delta)
        return encode_matrix

def mat_decode(matrix, delta):
    if isinstance(matrix, list):  # turns list types into ndarray types
        matrix = np.array(matrix)
    if len(matrix.shape) == 1:  # Condition where only one column
        rows = matrix.shape[0]
        cols = 1
        decode_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            decode_matrix[i] = decode(matrix[i], delta)
        return decode_matrix
    else:  # Condition with multiple columns
        rows, cols = np.shape(matrix)
        decode_matrix = np.zeros((int(rows), int(cols)), dtype=object)
        for i in range(rows):
            for ii in range(cols):
                decode_matrix[i][ii] = decode(matrix[i][ii], delta)
        return decode_matrix