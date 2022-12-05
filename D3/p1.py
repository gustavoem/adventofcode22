input_f = "input.txt"
file = open(input_f, 'r')

rucksacks = []
for line in file.readlines():
    rucksack = line.rstrip()
    rucksacks.append(rucksack)

def get_repeating_item(rucksack):
    size = len(rucksack)
    half1, half2 = rucksack[:size // 2], rucksack[size // 2:]
    for c in half1:
        if c in half2:
            return c

def item_to_priority(item):
    if ord(item) >= ord('a') and ord(item) <= ord('z'):
        return 1 + ord(item) - ord('a')
    return 27 + ord(item) - ord('A')

repeating_items = [
    get_repeating_item(rucksack)
    for rucksack in rucksacks
]

print(sum([item_to_priority(item) for item in repeating_items]))
