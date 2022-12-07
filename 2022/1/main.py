finput = open('input.txt','r').read().rstrip()
elves = finput.split('\n\n')

cal_elves = []

for i, elf in enumerate(elves):
    elf_cals = sum(list(map(int, elf.split('\n'))))
    cal_elves.append(elf_cals)

sort_elves = sorted(cal_elves)
print(sort_elves[-1], sum(sort_elves[-3:]))

