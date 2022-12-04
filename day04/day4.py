def find_subsets_and_overlaps(elf_pairs):
    subsets = []
    overlaps = []
    for elf_pair in elf_pairs:
        if elf_pair[0].issubset(elf_pair[1]) or elf_pair[1].issubset(elf_pair[0]):
            subsets.append(elf_pair)
            overlaps.append(elf_pair)
        elif elf_pair[0].intersection(elf_pair[1]):
            overlaps.append(elf_pair)
    return subsets, overlaps

with open("day4.txt", "r") as f:
    split_lines = [line.split(",") for line in f.read().split("\n")]
    day4_input = []
    for split_line in split_lines:
        elf1, elf2 = split_line[0].split("-"), split_line[1].split("-")
        day4_input.append([set(range(int(elf1[0]), int(elf1[1])+1)),
                      set(range(int(elf2[0]), int(elf2[1])+1))])
    
print(f"Part1: {len(find_subsets_and_overlaps(day4_input)[0])}")
print(f"Part2: {len(find_subsets_and_overlaps(day4_input)[1])}")