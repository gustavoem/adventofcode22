input_f = "input.txt"
file = open(input_f, 'r')

pairs = []
for line in file.readlines():
    pair = [
        list(map(int, range_string.split("-")))
        for range_string in line.rstrip().split(",")
    ]
    pairs.append(pair)

def contained(first_range, second_range):
    if first_range[0] <= second_range[0] and first_range[1] >= second_range[1]:
        return True
    if second_range[0] <= first_range[0] and second_range[1] >= first_range[1]:
        return True
    return False

def overlaps(first_range, second_range):
    if first_range[0] <= second_range[1] and first_range[1] >= second_range[1]:
        return True
    if second_range[0] <= first_range[1] and second_range[1] >= first_range[1]:
        return True
    return False


print(sum([
    contained(first_range, second_range)
    for first_range, second_range in pairs
]))
print(sum([
    overlaps(first_range, second_range)
    for first_range, second_range in pairs
]))

