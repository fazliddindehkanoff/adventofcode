ELF_PLAYS = ["A", "B", "C"]
MY_PLAYS = ["X", "Y", "Z"]
ROUND_POINTS = [0, 3, 6]
P2_MODS = [-1, 0, 1]

result1 = result2 = 0

with open("day2.txt") as f:
    for line in f:
        elf, me = line.strip().split(" ")
        elfIdx, meIdx = ELF_PLAYS.index(elf), MY_PLAYS.index(me)
        result1 += meIdx + 1 + ROUND_POINTS[(meIdx - elfIdx + 1) % 3]
        result2 += ((elfIdx + P2_MODS[meIdx]) % 3) + 1 + ROUND_POINTS[meIdx]

print("First result is {}\nSecond result is : {}".format(result1, result2))
