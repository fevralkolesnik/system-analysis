import json
import numpy as np


def rang_length(ranking) -> int:
    length = 0
    for i in ranking:
        if type(i) is str:
            length+=1
        else:
            length+=len(i)
    return length

def matrix_relationship(rang):
    rangs = dict()
    length = rang_length(rang)
    for i, rank in enumerate(rang):
        if type(rank) is str:
            rangs[int(rank)] = i
        else:
            for r in rank:
                rangs[int(r)] = i

    return np.matrix([[1 if rangs[i+1] <= rangs[j+1] else 0 for j in range(length)] for i in range(length)])


    
def task(str1: str, str2: str):
    rang1 = json.loads(str1)
    rang2 = json.loads(str2)

    matrix1 = matrix_relationship(rang1)
    transp_matrix1 = matrix1.transpose()

    matrix2 = matrix_relationship(rang2)
    transp_matrix2 = matrix2.transpose()

    mult_matrix = np.multiply(matrix1, matrix2)
    mult_transp_matrix = np.multiply(transp_matrix1, transp_matrix2)

    answer = []

    for i in range(mult_matrix.shape[0]):
        for j in range(mult_transp_matrix[i].shape[1]):
            if int(mult_matrix[i,j]) == 0 and int(mult_transp_matrix[i,j]) == 0:
                if (str(j+1),str(i+1)) not in answer:
                    answer.append((str(i+1),str(j+1)))

    return json.dumps(answer)