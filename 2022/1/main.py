# finput = open('input.txt','r').read().rstrip()
# elves = finput.split('\n\n')

# high_cal_carrier = 0
# high_cal = 0

# for i, elf in enumerate(elves):
#     elf_cals = sum(list(map(int, elf.split('\n'))))

#     if elf_cals > high_cal:
#         high_cal_carrier = i
#         high_cal = int(elf_cals)

# print(high_cal_carrier, high_cal)

# __

finput = open('input.txt','r').read().rstrip()
elves = finput.split('\n\n')

cal_elves = []

for i, elf in enumerate(elves):
    elf_cals = sum(list(map(int, elf.split('\n'))))
    cal_elves.append(elf_cals)

sort_elves = sorted(cal_elves)
print(sort_elves[-1], sum(sort_elves[-3:]))

