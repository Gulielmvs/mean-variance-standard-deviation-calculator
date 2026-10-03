import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    matrix = np.array(list).reshape(3, 3)
    # mean
    mean_col = np.mean(matrix, axis=0).tolist()
    mean_row = np.mean(matrix, axis=1).tolist()
    mean_flat = np.mean(matrix).tolist()
    # variance
    var_col = np.var(matrix, axis=0).tolist()
    var_row = np.var(matrix, axis=1).tolist()
    var_flat = np.var(matrix).tolist()
    # standard deviation
    std_col = np.std(matrix, axis=0).tolist()
    std_row = np.std(matrix, axis=1).tolist()
    std_flat = np.std(matrix).tolist()
    # max
    max_col = np.max(matrix, axis=0).tolist()
    max_row = np.max(matrix, axis=1).tolist()
    max_flat = np.max(matrix).tolist()
    # min
    min_col = np.min(matrix, axis=0).tolist()
    min_row = np.min(matrix, axis=1).tolist()
    min_flat = np.min(matrix).tolist()
    # sum
    sum_col = np.sum(matrix, axis=0).tolist()
    sum_row = np.sum(matrix, axis=1).tolist()
    sum_flat = np.sum(matrix).tolist()

    calculations = {
        'mean': [mean_col, mean_row, mean_flat],
        'variance': [var_col, var_row, var_flat],
        'standard deviation': [std_col, std_row, std_flat],
        'max': [max_col, max_row, max_flat],
        'min': [min_col, min_row, min_flat],
        'sum': [sum_col, sum_row, sum_flat]
    }

    return calculations
