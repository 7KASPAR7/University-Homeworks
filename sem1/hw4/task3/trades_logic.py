def begin(file_name):
    file = open(file_name, 'r')
    line = file.readline()
    amountlst = []
    costlst = []
    birgelst = []
    timelst = []
    while line:
        time = ''
        cost = 0
        amount = 0
        birge = ''
        line = file.readline()
        for i in range(0, len(line) - 5):
            line = line.replace('.', '')
            line = line.replace(':', '')
            time = line[0:9]
            for l in range(10, len(line) - 2):
                if line[l] == ',':
                    cost = line[10:l]
                    if len(cost) == 4:
                        cost = cost + '0'
                    amount = line[l + 1: len(line) - 3]
                    birge = line[len(line) - 2]
                    break
        timelst.append(time)
        costlst.append(int(cost))
        amountlst.append(int(amount))
        birgelst.append(birge)
    timelst = timelst[:-1]
    costlst = costlst[:-1]
    amountlst = amountlst[:-1]
    birgelst = birgelst[:-1]
    file.close()
    return timelst, costlst, amountlst, birgelst


def find_birge(birgelst):
    birge = ''
    dictionary = {}
    for i in range(0, len(birgelst)):
        if birgelst[i] not in birge:
            birge = birge + birgelst[i]
            dictionary[birgelst[i]] = 0
    return birge, dictionary


def totallst(timelst, costlst, amountlst, birgelst, birge):
    max = 0
    for i in range(0, len(timelst)):
        count = 0
        summa = 0
        if birgelst[i] in birge:
            for l in range(i, len(timelst)):
                if birgelst[l] in birge:
                    if int(timelst[l])-int(timelst[i]) <= 1000:
                        count = count + 1
                        summa = summa + int(costlst[l]) * int(amountlst[l])
                    if count > max:
                        index = i
                        max = count
                        maxsumma = summa
    return [index, max, maxsumma/100, birge]


def share(timelst, costlst, amountlst, birgelst, birge):
    if len(birge) > 1:
        res = [totallst(timelst, costlst, amountlst, birgelst, birge)]
    else:
        res = []
    for symbol in birge:
        res = res + [totallst(timelst, costlst, amountlst, birgelst, symbol)]
    return res


def output(timelst, LIST, dictionary, birgelst):
    RESULT = []
    for i in range(0, len(LIST)):
        data = LIST[i]
        time = timelst[data[0]]
        time = time[0:2] + ':' + time[2:4] + ':' + time[4:6] + '.' + time[6:]
        if len(data[3]) <= 1:
            RESULT.append([time, data[1], data[2], data[3]])
        else:
            for birge in range(data[0], data[0] + data[1]):
                dictionary[birgelst[birge]] = dictionary[birgelst[birge]] + 1
            RESULT.append([time, data[1], data[2], dictionary])
    return RESULT
