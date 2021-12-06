
finput = open('input.txt','r').read().rstrip()

d = [*map(int, finput.split(','))]
f = [*map(d.count, range(9))]

for i in range(256):
    f = f[1:] + f[:1]
    f[6] += f[-1]

    if i == 79:
        print(sum(f))

print(sum(f))