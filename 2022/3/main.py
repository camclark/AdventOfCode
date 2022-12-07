# # Your total score is the sum of your scores for each round. 
# # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# finput = open('input_example.txt','r').read().rstrip().split('\n')
# # finput = open('input.txt','r').read().rstrip().split('\n')

with open('input.txt') as f:
    rucksacks = list(filter(None, f.read().split('\n')))  

priority_sum, groups_priority_sum = 0, 0    

# Part 1
for rucksack in rucksacks: 
    compartment_a,compartment_b  = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):] 
    common_item = [i for i in compartment_a if i in compartment_b][0] 
    priority_sum += ord(common_item) - (38 if common_item.isupper() else 96)

for i in range(0, len(rucksacks), 3): 
    elf_group = rucksacks[i:i+3]
    badge = [x for x in elf_group[0] if x in elf_group[1] and x in elf_group[2]][0] 
    groups_priority_sum += ord(badge) - (38 if badge.isupper() else 96)

print(priority_sum)
print(groups_priority_sum)