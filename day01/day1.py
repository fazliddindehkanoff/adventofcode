with open('day1.txt') as f:
    subres = 0
    lines = []
    for line in f:
        if line == '\n':
            lines.append(subres)
            subres = 0
        else:
            subres += int(line)
# first solution
print(max(lines))

#second solution
lines.sort(reverse=True)
print(lines[0])
