puzzle_input    = list()
with open("input") as file:
    puzzle_input    = file.readlines()

priority_list   = dict()
for _ in range(97, 123):
    priority_list[chr(_)]   = _ - 96
for _ in range(65, 91):
    priority_list[chr(_)]   = _ - 38
    
def part1():
    # notice that the input length of each line is even
    priority_sum            = 0
    for i in range(len(puzzle_input)):
        rucksack_lenght     = int((len(puzzle_input[i]) - 1) / 2)
        first_half          = puzzle_input[i][:rucksack_lenght]
        second_half         = puzzle_input[i][rucksack_lenght:]

        item_duplicates     = list()
        for c in first_half:
            if c in second_half and c not in item_duplicates:
                item_duplicates.append(c)
                priority_sum    = priority_sum + priority_list[c]
    print(priority_sum)

part1()
