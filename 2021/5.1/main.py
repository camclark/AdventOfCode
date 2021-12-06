from collections import defaultdict

def inclusive_range(a, b):
    return range(a, b + 1) if b > a else range(a, b - 1, -1)

finput = open('input.txt','r').read().rstrip()

lines = finput.strip().split('\n')
point_dict = defaultdict(int)
for line in lines:
    x0, y0, x1, y1 = [int(n) for n in line.replace(' -> ', ',').split(',')]
    if x0 == x1:
        for y in inclusive_range(y0, y1):
            point_dict[(x0, y)] += 1
    elif y0 == y1:
        for x in inclusive_range(x0, x1):
            point_dict[(x, y0)] += 1
        

answer = sum(line_count > 1 for line_count in point_dict.values())
print(answer)