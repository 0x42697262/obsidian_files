puzzle_input    = list()
with open("input") as file:
    puzzle_input    = file.readlines()

puzzle_input_cleaned = list()
for line in puzzle_input:
    temp    = list()
    for section_assignments in line.strip('\n').split(','):
        temp.append(section_assignments.split('-'))

    puzzle_input_cleaned.append(temp)

def part1():
    result  = 0
   
    for section_assignments in puzzle_input_cleaned:
        left        = section_assignments[0]
        right       = section_assignments[1]

        sign_left   = int(left[0]) - int(right[0])
        sign_right  = int(left[1]) - int(right[1])



        print(left, right, sign_left, sign_right)

        if sign_left >= 0 and sign_right <= 0 \
            or sign_left <= 0 and sign_right >= 0:
                result  = result + 1

    print("Part 1: ", result)


def part2():
    result  = None



    print("Part 2: ", result)

part1()
