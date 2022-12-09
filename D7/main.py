input_f = "input.txt"
file = open(input_f, 'r')
lines = [line.rstrip() for line in file.readlines()]

class Stream(object):

    def __init__(self, lines):
        self.lines = lines
        self.idx = 0

    def has_ended(self):
        return self.idx >= len(lines)

    def get_line(self):
        result = self.lines[self.idx]
        self.idx += 1
        return result


stream = Stream(lines)
dirs = {}

def read_dir(dir_path, stream, all_dir_sizes):
    files_sizes = {}
        
    while not stream.has_ended():
        line = stream.get_line()
        if line == "$ cd ..":
            break
        
        if line == "$ ls":
            while not stream.has_ended() and "$" not in stream.lines[stream.idx]:
                size, file = stream.get_line().split()
                if size.isdigit():
                    files_sizes[file] = int(size)
            continue
            
            
        if "$ cd" in line:
            subdir_name = line.split()[2]
            subdir_path = dir_path + "/" + subdir_name
            subdir_size = read_dir(subdir_path, stream, all_dir_sizes)
            files_sizes[subdir_name] = subdir_size
        
    dir_size = sum(list(files_sizes.values()))
    all_dir_sizes[dir_path] = dir_size
    return dir_size

stream.get_line()
all_dir_sizes = {}
file_sizes = read_dir("/", stream, all_dir_sizes)

summed = 0
for dirr, size in all_dir_sizes.items():
    if size <= 100000:
        summed += size
print("Sum of sizes of dirs with at most size 100000", summed)

total_size = 70000000
free_wanted_size = 30000000
available_space = total_size - all_dir_sizes["/"]
print("Starting available space", available_space)

min_deletion = free_wanted_size - available_space
candidates = [
    size for size in all_dir_sizes.values() if size >= min_deletion
]
print("Smallest candidate to free up space size", min(candidates))

