def median(l):
    if len(l) == 1:
        return l[0]
    middle = float(len(l)) / 2
    print(middle)
    temp = sorted(l)
    print(temp)
    if middle % 1 == 0:
        res = 0.0
        middle = int(middle)
        print(temp[middle -1])
        print(temp[middle])
        res = temp[middle - 1] + temp[middle]
        res = float(res) / 2
        return res
    else:
        return temp[int(middle)]
    

