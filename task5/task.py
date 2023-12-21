import json
import numpy as np


def get_clusters_from_str(str_json):
    # Convert string representation of JSON to a Python list
    clusters_list = json.loads(str_json)
    clusters = []

    for item in clusters_list:
        if isinstance(item, list):
            clusters.append(item)
        else:
            clusters.append([item])

    return clusters


def get_matrix_from_expert(str_json: str):
    clusters = get_clusters_from_str(str_json)
    n = sum(len(cluster) for cluster in clusters)

    matrix = np.ones((n, n), dtype=int)

    worse = []
    for cluster in clusters:
        for worse_elem in worse:
            for elem in cluster:
                matrix[elem - 1][worse_elem - 1] = 0
        worse.extend(cluster)

    return matrix


def get_AND_matrix(matrix1, matrix2):
    return np.multiply(matrix1, matrix2)


def get_OR_matrix(matrix1, matrix2):
    return np.maximum(matrix1, matrix2)


def get_clusters(matrix, est1, est2):
    clusters = {}
    exclude = set()

    rows, cols = matrix.shape
    for row in range(rows):
        if row + 1 in exclude:
            continue
        clusters[row + 1] = [row + 1]
        for col in range(row + 1, cols):
            if matrix[row][col] == 0:
                clusters[row + 1].append(col + 1)
                exclude.add(col + 1)

    result = []
    for k in clusters:
        if not result:
            result.append(clusters[k])
            continue

        for i, elem in enumerate(result):
            if (
                np.sum(est1[elem[0] - 1]) == np.sum(est1[k - 1])
                and np.sum(est2[elem[0] - 1]) == np.sum(est2[k - 1])
            ):
                result[i].extend(clusters[k])
                break

            if (
                np.sum(est1[elem[0] - 1]) < np.sum(est1[k - 1])
                or np.sum(est2[elem[0] - 1]) < np.sum(est2[k - 1])
            ):
                result = result[:i] + clusters[k] + result[i:]
                break

        result.append(clusters[k])

    final = [r[0] if len(r) == 1 else r for r in result]
    return str(final)


def task(string1, string2):
    mx1 = get_matrix_from_expert(string1)
    mx2 = get_matrix_from_expert(string2)

    mx_and = get_AND_matrix(mx1, mx2)
    mx_and_t = get_AND_matrix(np.transpose(mx1), np.transpose(mx2))

    mx_or = get_OR_matrix(mx_and, mx_and_t)
    clusters = get_clusters(mx_or, mx1, mx2)
    return clusters


if __name__ == "__main__":
    string1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    string2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    results = task(string1, string2)
    print(results)
