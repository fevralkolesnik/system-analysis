import numpy as np
import json

def task(str):
    datas = json.loads(str)
    matrix = []
    for i in range(len(datas)):
        length = len(datas[i])
        mrx = np.zeros((length, length))
        for x in range(length):
            for y in range(length):
                if datas[i][x] < datas[i][y]:
                    mrx[x][y] = 1
                if datas[i][x] == datas[i][y]:
                    mrx[x][y] = 0.5
                if datas[i][x] > datas[i][y]:
                    mrx[x][y] = 0
        matrix.append(mrx)
    
    x = np.zeros((len(datas), len(datas)))
    for i in range(len(datas)):
        x += matrix[i]
    x = x/len(datas)
    k0 = np.array(1*len(datas)/len(datas))
    y = np.dot(x, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k1 = np.dot(1/l, y)

    while max(abs(k1-k0)) >= 0.001:
        k0 = k1
        y = np.dot(x, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k1 = np.dot(1/l, y)
    
    rounded = [np.round(x, 3) for x in k1]

    return rounded