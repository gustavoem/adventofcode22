# A  X  1  0  rock   
# B  Y  2  1  paper
# C  Z  3  2  scissors

# who beats who
# 2 -> 1 -> 0 -> 2
# X beats Y if (Y + 1 % 3) == X

input_f = "input.txt"
file = open(input_f, 'r')

plays = []
for line in file.readlines():
    opponent, me = line.rstrip().split(" ")
    plays.append((opponent, me))

my_play_to_num = lambda p: ord(p) - ord('X')
their_play_to_num = lambda p: ord(p) - ord('A')

score = 0
for play in plays:
    opponent, me = play
    score += my_play_to_num(me) + 1
    
    if my_play_to_num(me) == their_play_to_num(opponent):
        score += 3
    elif my_play_to_num(me) == (their_play_to_num(opponent) + 1) % 3:
        score += 6

print(score)

