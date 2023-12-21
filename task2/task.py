import pandas as pd 
import numpy as np

def task(input_str):
    lines = input_str.split('\n')
    data = [line.split(',') for line in lines]
    file = np.array(data, dtype=int)
    file = file.transpose()

    answer = [[], [], [], [], []]

    for column in file:
        unique_values = np.unique(column)
        answer[0].extend(unique_values)

    for i in range(file[0].size):
        if file[1][i] in file[0]:
            if file[0][i] not in answer[2]:
                answer[2].append(file[0][i])

    for i in range(file[0].size):
        if file[0][i] in file[1]:
            if file[1][i] not in answer[3]:
                answer[3].append(file[1][i])

    for i in range(file[0].size):
        if file[0][i] in np.delete(file, i):
            if file[1][i] not in answer[4]:
                answer[4].append(file[1][i])

    return answer