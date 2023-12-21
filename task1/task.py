import pandas as pd

path  = 'C:/Uchu/Системный анализ/system_analysis/task1/ex.csv'

df = pd.read_csv(path)

print(df)

import numpy as np

adjacency_matrix = np.array(df)

num_vertices = adjacency_matrix.shape[0]

# Создайте пустой список для хранения соседей каждой вершины
neighbors_list = []

# Переберите каждую вершину и найдите её соседей
for vertex in range(num_vertices):
    neighbors = np.where(adjacency_matrix[vertex] == 1)[0]
    neighbors_list.append(neighbors)

# Выведите список соседей для каждой вершины
for vertex, neighbors in enumerate(neighbors_list):
    print(f"Соседи вершины {vertex}: {list(neighbors)}")