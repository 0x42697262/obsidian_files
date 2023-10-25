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

        if sign_left >= 0 and sign_right <= 0 \
            or sign_left <= 0 and sign_right >= 0:
                result  = result + 1

    print("Part 1: ", result)


def part2():
    result  = 0


    for section_assignments in puzzle_input_cleaned:
        left        = section_assignments[0]
        right       = section_assignments[1]

        overlap1     = int(left[1]) - int(right[0])
        overlap2     = int(left[0]) - int(right[1])

        if overlap1 >= 0 and overlap2 <= 0: 
            result  = result + 1



    print("Part 2: ", result)

part1()
part2()
