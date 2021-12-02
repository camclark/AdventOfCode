import csv

y = 0 
x = 0
aim = 0

with open('./input.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        instruction = row[0]
        value = int(row[1])

        print(instruction, value)

        if instruction == 'forward':
            x = x + value
            y = (aim * value) + y
        elif instruction == 'up':
            aim = aim - value
        else:
            aim = aim + value

print('*****') 
print('x {}, y {}'.format(x,y))
print(x * y)
