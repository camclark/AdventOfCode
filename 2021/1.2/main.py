import csv

increased_vals = -3
queue = [0,0,0]
previous_sum = 0

with open('./input.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        value = int(row[0])

        queue.pop(0)
        queue.append(value)
        stack_sum = sum(queue)

        if stack_sum > previous_sum:
            increased_vals += 1
        previous_sum = stack_sum
        
print(increased_vals)
