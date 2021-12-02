import csv

increased_vals = -1
previous = 0

with open('./input.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        value = int(row[0])

        if value > previous:
            increased_vals += 1
        previous = value
        
print(increased_vals)
