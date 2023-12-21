import math

def task():
    v = [i * j for i in range(1, 7) for j in range(1, 7)]
    v = sorted(list(set(v)))

    vv = [i + j for i in range(1, 7) for j in range(1, 7)]
    vv = sorted(list(set(vv)))

    m = [[0] * len(v) for _ in range(len(vv))]

    index = [0] * (v[-1] + 1)
    t = 0
    for i in range(len(v)):
        index[v[i]] = t
        t += 1

    indexv = [0] * (vv[-1] + 1)
    t = 0
    for i in range(len(vv)):
        indexv[vv[i]] = t
        t += 1

    for i in range(1, 7):
        for j in range(1, 7):
            if i == j:
                m[indexv[i + j]][index[i * j]] = 1
            else:
                m[indexv[i + j]][index[i * j]] = 2

    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] /= 36

    HA = 0
    HB = 0
    HAB = 0
    HaB = 0
    I = 0
    p = []

    for i in range(len(m)):
        t = sum(m[i])
        p.append(t)
        HA -= math.log2(t) * t

    for j in range(len(m[0])):
        t = sum(m[i][j] for i in range(len(m)))
        HB -= math.log2(t) * t

    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]:
                HaB -= math.log2(m[i][j] / p[i]) * m[i][j]

    HAB = HA + HaB
    I = HB - HaB
    ret = [HAB, HA, HB, HaB, I]
    return ret

if __name__ == "__main__":
    # вызов функции task() и вывод результатов
    result = task()
    print(result)
