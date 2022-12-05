input_f = "input.txt"
file = open(input_f, 'r')

elf_calories = [0]
for line in file.readlines():
    if line == "\n":
        elf_calories.append(0)
    else:
        elf_calories[-1] += int(line)


# i want to be linear :) 
top_cal1 = 0
top_cal2 = 0
top_cal3 = 0
for cal in elf_calories:
    if cal > top_cal3:
        if cal > top_cal2:
            if cal > top_cal1:
                top_cal3 = top_cal2
                top_cal2 = top_cal1
                top_cal1 = cal
            else:
                top_cal3 = top_cal2
                top_cal2 = cal
        else:
            top_cal3 = cal
print(top_cal1)
print(sum([top_cal1, top_cal2, top_cal3]))
