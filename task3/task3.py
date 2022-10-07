from io import StringIO
import csv



def task(csvString):
    out = StringIO(csvString)
    reader = csv.reader(out, delimiter=',')
    out = []
    for row in reader:
        out.append(row)

    r1 = []
    for x in out:
        if x[0] not in r1:
            r1.append(str(x[0]))

    r2 = []
    for x in out:
        if x[1] not in r2:
            r2.append(str(x[1]))

    r3 = []
    for i in range(len(out)):
        for j in range(len(out)):
            if i != j and out[i][0] not in r3 and out[i][1] == out[j][0]:
                r3.append(str(out[i][0]))

    r4 = []
    for i in range(len(out)):
        for j in range(len(out)):
            if i != j and out[i][1] not in r4 and out[i][0] == out[j][1]:
                r4.append(str(out[i][1]))

    r5 = []
    for i in range(len(out)):
        for j in range(len(out)):
            if i != j and out[i][1] not in r5 and out[i][0] == out[j][0]:
                r5.append(str(out[i][1]))

    return [r1, r2, r3, r4, r5]
