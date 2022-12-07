# # Your total score is the sum of your scores for each round. 
# # The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
# # plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# finput = open('input_example.txt','r').read().rstrip().split('\n')
# # finput = open('input.txt','r').read().rstrip().split('\n')

with open('input_example.txt') as f:
    sections = list(filter(None, f.read().split('\n')))  

count = 0

for section in sections: 
    section_a,section_b  = section.split(',')
    section_a = section_a.split('-')
    section_b = section_b.split('-')
    print(section_a, section_b)

    if section_a[0] - section_b[0] < 0 and section_a[1] - section_b[1] < 0:
        print(section)
    elif section_a[0] - section_b[0] > 0 and section_a[1] - section_b[1] > 0:
        print(section)
    # common_item = [i for i in compartment_a if i in compartment_b][0] 
    # priority_sum += ord(common_item) - (38 if common_item.isupper() else 96)

# for i in range(0, len(rucksacks), 3): 
#     elf_group = rucksacks[i:i+3]
#     badge = [x for x in elf_group[0] if x in elf_group[1] and x in elf_group[2]][0] 
#     groups_priority_sum += ord(badge) - (38 if badge.isupper() else 96)


