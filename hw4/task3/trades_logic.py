def begin(file_name):
    f = open(file_name, 'r')
    line = f.readline()
    Qlst = []
    costlst = []
    birgelst = []
    timelst = []
    while line:
        time = ''
        cost = 0
        Q = 0
        birge = ''
        line = f.readline()
        for i in range(0, len(line) - 5):
            line = line.replace('.', '')
            line = line.replace(':', '')
            time = line[0:9]
            for l in range(10, len(line) - 2):
                if line[l] == ',':
                    cost = line[10:l]
                    if len(cost) == 4:
                        cost = cost + '0'
                    Q = line[l + 1: len(line) - 3]
                    birge = line[len(line) - 2]
                    break
        timelst.append(time)
        costlst.append(int(cost))
        Qlst.append(int(Q))
        birgelst.append(birge)
    timelst = timelst[:-1]
    costlst = costlst[:-1]
    Qlst = Qlst[:-1]
    birgelst = birgelst[:-1]
    f.close()
    return timelst, costlst, Qlst, birgelst


def birge(birgelst):
    birge = ''
    dictionary = {}
    for i in range(0, len(birgelst)):
        if birgelst[i] not in birge:
            birge = birge + birgelst[i]
            dictionary[birgelst[i]] = 0
    return birge, dictionary


def qq(timelst, costlst, Qlst, birgelst, birge):
    max = 0
    for i in range(0, len(timelst)):
        count = 0
        summa = 0
        if birgelst[i] in birge:
            for l in range(i, len(timelst)):
                if birgelst[l] in birge:
                    if int(timelst[l])-int(timelst[i]) <= 1000:
                        count = count + 1
                        summa = summa + int(costlst[l]) * int(Qlst[l])
                    if count > max:
                        index = i
                        max = count
                        maxsumma = summa
    return [index, max, maxsumma/100, birge]


def share(timelst, costlst, Qlst, birgelst, birge):
    if len(birge) > 1:
        result = [qq(timelst, costlst, Qlst, birgelst, birge)]
    else:
        result = []
    for i in birge:
        result = result + [qq(timelst, costlst, Qlst, birgelst, i)]
    return result


def output(timelst, spisok, dictionary, birgelst):
    RESULT = []
    for i in range(0, len(spisok)):
        arg = spisok[i]
        time = timelst[arg[0]]
        time = time[0:2] + ':' + time[2:4] + ':' + time[4:6] + '.' + time[6:]
        if len(arg[3]) <= 1:
            RESULT.append([time, arg[1], arg[2], arg[3]])
        else:
            for k in range(arg[0], arg[0] + arg[1]):
                dictionary[birgelst[k]] = dictionary[birgelst[k]] + 1
            RESULT.append([time, arg[1], arg[2], dictionary])
    return RESULT
