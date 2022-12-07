
input_f = "input.txt"
file = open(input_f, 'r')

stream = file.readline()

def get_stream_code_start(stream):
    for i in range(len(stream) - 4):
        next_four = [letter for letter in stream[i:i + 4]]
        if len(set(next_four)) == 4:
            return i + 4

def get_stream_message_start(stream):
    for i in range(len(stream) - 14):
        next_four = [letter for letter in stream[i:i + 14]]
        if len(set(next_four)) == 14:
            return i + 14
 
    
print(get_stream_code_start(stream))
print(get_stream_message_start(stream))
