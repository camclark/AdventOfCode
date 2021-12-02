import csv

y = 0 
x = 0

with open('./input.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
        instruction = row[0]
        value = int(row[1])

        print(instruction, value)

        if instruction == 'forward':
            x = x + value
        elif instruction == 'up':
            y = y - value
        else:
            y = y + value
        
print(x, y)
print(x * y)
