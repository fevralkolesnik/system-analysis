from io import StringIO
import csv
import math


def task4(csvString):
    gr = StringIO(csvString)
    reader = csv.reader(gr, delimiter=',')
    gr = []
    for row in reader:
        gr.append(row)
        
    out = []
    nodes = []
    for x in gr:
        for y in x:
            if y not in nodes:
                nodes.append(y)
    nodes.sort()

    
    r1 = []
    for x in gr:
        if x[0] not in r1:
            r1.append(str(x[0]))

    r2 = []
    for x in gr:
        if x[1] not in r2:
            r2.append(str(x[1]))

    r3 = []
    for i in range(len(gr)):
        for j in range(len(gr)):
            if i != j and gr[i][0] not in r3 and gr[i][1] == gr[j][0]:
                r3.append(str(gr[i][0]))

    r4 = []
    for i in range(len(gr)):
        for j in range(len(gr)):
            if i != j and gr[i][1] not in r4 and gr[i][0] == gr[j][1]:
                r4.append(str(gr[i][1]))

    r5 = []
    for i in range(len(gr)):
        for j in range(len(gr)):
            if i != j and gr[i][1] not in r5 and gr[i][0] == gr[j][0]:
                r5.append(str(gr[i][1]))
                
                

    for v in nodes:
        out.append([])
        out[int(v)-1].append(r1.count(v))
        out[int(v)-1].append(r2.count(v))
        out[int(v)-1].append(r3.count(v))
        out[int(v)-1].append(r4.count(v))
        out[int(v)-1].append(r5.count(v))

        
    sum = 0
    for j in range(len(nodes)):
        for i in range(5):
            if out[j][i] != 0:
                sum += (out[j][i] / (len(nodes) - 1)) * math.log(out[j][i] / (len(nodes) - 1), 2)


    return -sum