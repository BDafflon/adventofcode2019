import copy


def mul(data, i):
    if len(data) > i + 3:
        data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
        return i + 4
    return None


def add(data, i):
    if len(data) > i + 3:
        data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
        return i + 4
    return None


def day2_1(data):
    i = 0
    while data[i] != 99:
        if data[i] == 1:
            i = add(data, i)
            if i is None:
                return None
        elif data[i] == 2:
            i = mul(data, i)
            if i is None:
                return None
    return data[0]


def day2_2(data,target):

    backup = copy.deepcopy(data)
    candidat= [[i,j] for i in range(0,99) for j in range(0,99)]

    for c in candidat:
        data = copy.deepcopy(backup)
        data[1]=c[0]
        data[2]=c[1]

        if target == day2_1(data):
            return c
    return None


if __name__ == '__main__':
    fichier = open('input.txt', 'r')
    linesDeMonFichier = fichier.read().split(",")


    data = [ int(d) for d in linesDeMonFichier]

    data2 = copy.deepcopy(data)
    data[1]=12
    data[2]=2

    res = day2_1(data)
    print(res)

    data2 = copy.deepcopy(data2)
    c = day2_2(data2,19690720)
    print(100*c[0]+c[1])


