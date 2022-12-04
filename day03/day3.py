result = 0
subres = []
res_2 = 0
with open("day3.txt") as f:
    # first solution
    for line in f:
        mid = len(line)//2
        for i in line[:mid]:
            if i in line[mid:]:
                if i.islower():
                    result += (ord(i) - 96)
                    break
                else:
                    result += (ord(i) - 38)
                    print(f"{i} -> {ord(i) - 38}")
                    break
    # second solution
    for line in f:
        print(subres)
        subres.append(line)
        if len(subres) == 3:
            for i in subres[0]:
                if i in subres[1] and i in subres[2]:
                    if i.islower():
                        res_2 += (ord(i) - 96)
                        break
                    else:
                        res_2 += (ord(i) - 38)
                        break
            del subres
            subres = []
            subres.append(line)


print(res_2)
