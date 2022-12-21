
tasks = [[*map(int, s.replace("-", ",").split(","))] 
    for s in open("input.txt").read().split()]

def part1(tasks):
    return sum([((a<=c<=d<=b) or (c<=a<=b<=d)) 
        for a,b,c,d in tasks])
def part2(tasks):
    return sum([((a<=c<=b) or (c<=a<=d))
        for a,b,c,d in tasks])

print(part1(tasks))
print(part1(tasks))

print("Part 1:", part1(tasks))
print("Part 2:", part2(tasks))