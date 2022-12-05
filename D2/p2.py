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

play_to_num = lambda p: ord(p) - ord('A')

score = 0
for play in plays:
    opponent, desired_result = play
    if desired_result == 'X':
        my_play_num = (play_to_num(opponent) - 1) % 3
        me = chr(ord('A') + my_play_num)
    elif desired_result == 'Y':
        me = opponent
        score += 3
    else:
        my_play_num = (play_to_num(opponent) + 1) % 3
        me = chr(ord('A') + my_play_num)
        score += 6

    score += play_to_num(me) + 1
    
print(score)

