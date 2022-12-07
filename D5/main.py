# reads initial config

# positions
# [D] [D] [T] [F] [G] [B] [B] [H] [Z]
#  1   2   3   4   5   6   7   8   9 
#  1   5   9   13  17...

import string
import copy

input_f = "input.txt"
file = open(input_f, 'r')

stacks = [[] for _ in range(9)]
# there are 9 lines of initial configs
for _ in range(10):
    line = file.readline()
    for i in range(1, len(line), 4):
        if line[i] in string.ascii_letters:
            stacks[(i - 1) // 4].append(line[i])

moves = []
for line in file.readlines():
    coords = [int(word) for word in line.rstrip().split() if word.isdigit()]
    n = coords[0]
    orig, dest = coords[1] - 1, coords[2] - 1
    moves.append((n, orig, dest))
    

def stacker9000(stacks, move):
    n, orig, dest = move
    stacks[dest] = list(reversed(stacks[orig][:n])) + stacks[dest]
    stacks[orig] = stacks[orig][n:]

def stacker9001(stacks, move):
    n, orig, dest = move
    stacks[dest] = stacks[orig][:n] + stacks[dest]
    stacks[orig] = stacks[orig][n:]

stacks2 = copy.deepcopy(stacks)
for move in moves:
    stacker9000(stacks, move)
    stacker9001(stacks2, move)

print("".join([str(stack[0]) for stack in stacks]))
print("".join([str(stack[0]) for stack in stacks2]))
