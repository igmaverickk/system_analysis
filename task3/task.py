import pandas as pd 
import numpy as np

def task(input_str):
    lines = input_str.split('\n')
    data = [line.split(',') for line in lines]
    file = np.array(data, dtype=int)
    file = file.transpose()

    answer = [[], [], [], [], []]

    # Extract unique values from each column
    for column in file:
        unique_values = np.unique(column)
        answer[0].extend(unique_values)

    # Check for common elements between the first and second columns
    for i, value in enumerate(file[0]):
        if file[1][i] in file[0] and value not in answer[2]:
            answer[2].append(value)

    # Check for common elements between the second and first columns
    for i, value in enumerate(file[0]):
        if value in file[1] and file[1][i] not in answer[3]:
            answer[3].append(file[1][i])

    # Check for elements in the first column not in the second column
    for i, value in enumerate(file[0]):
        if value in np.delete(file, i) and file[1][i] not in answer[4]:
            answer[4].append(file[1][i])

    return answer
