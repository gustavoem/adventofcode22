input_f = "input.txt"
file = open(input_f, 'r')

rucksacks = []
for line in file.readlines():
    rucksack = line.rstrip()
    rucksacks.append(rucksack)

groups = []
for i in range(0, len(rucksacks), 3):
    groups.append(rucksacks[i : i + 3])

def get_group_item(rucksacks):
    for item in rucksacks[0]:
        if item in rucksacks[1] and item in rucksacks[2]:
            return item

def item_to_priority(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return 1 + ord(item) - ord('a')
    return 27 + ord(item) - ord('A')

import pdb; pdb.set_trace()
groups_items = [
    get_group_item(group_rucksacks)
    for group_rucksacks in groups
]

print(sum([item_to_priority(item) for item in groups_items]))
