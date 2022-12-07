# Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

score = {
    'X' : { 'A':1+3, 'B':1+0, 'C':1+6 }, # Rock defeats Scissors
    'Y' : { 'A':2+6, 'B':2+3, 'C':2+0 }, # Paper defeats Rock
    'Z' : { 'A':3+0, 'B':3+6, 'C':3+3 }  # Scissors defeats Paper
}

strategy = {
    'X' : { 'A':'Z', 'B':'X', 'C':'Y' }, # Lose
    'Y' : { 'A':'X', 'B':'Y', 'C':'Z' }, # Draw
    'Z' : { 'A':'Y', 'B':'Z', 'C':'X' }  # Win
}

m = [x.strip().split() for x in open("input.txt").readlines()]

print( sum(score[me][elf] for elf,me in m) )
print( sum(score[strategy[me][elf]][elf] for elf,me in m) )