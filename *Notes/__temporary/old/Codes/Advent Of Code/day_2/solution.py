puzzle_input    = list()
shape_score     = {
                'A': 1,
                'X': 1,
                'B': 2,
                'Y': 2,
                'C': 3,
                'Z': 3
                }
puzzle_input = str()

with open("input") as file:
    puzzle_input    = file.readlines()

def part1():
    my_score        = 0

    for i in range(len(puzzle_input)):
        my_pick         = puzzle_input[i][2]
        enemy_pick      = puzzle_input[i][0]
        
        # Don't ask why I did this method... I forgot how rock paper scissors worked
        # so I was confused why it kept spitting out the wrong answer.
        # This makes it easier for my brain why my initial method did not work.

        match enemy_pick:
            case 'A':
                match my_pick:
                    case 'X':
                        my_score = my_score + 3 + 1
                    case 'Y':
                        my_score = my_score + 6 + 2
                    case 'Z':
                        my_score = my_score + 0 + 3 
            case 'B':
                match my_pick:
                    case 'X':
                        my_score = my_score + 0 + 1 
                    case 'Y':
                        my_score = my_score + 3 + 2
                    case 'Z':
                        my_score = my_score + 6 + 3
            case 'C':
                match my_pick:
                    case 'X':
                        my_score = my_score + 6 + 1
                    case 'Y':
                        my_score = my_score + 0 + 2
                    case 'Z':
                        my_score = my_score + 3 + 3 
    print("Part 1: ", my_score)


def part2():
    my_score    = 0
    rps = [1, 2, 3] # score
    rps_map = {'A': 0, 'B': 1, 'C': 2} # index
    for i in range(len(puzzle_input)):
        my_pick     = puzzle_input[i][2]
        enemy_pick  = puzzle_input[i][0]

        match my_pick:
            case 'X': # lose
                my_score = my_score + rps[(rps_map[enemy_pick] - 1) % 3]
                print(rps[(rps_map[enemy_pick] - 1) % 3])
            case 'Y': # draw
                my_score = my_score + rps[rps_map[enemy_pick]] + 3
                print(rps[rps_map[enemy_pick]] + 3)
            case 'Z': # win
                my_score = my_score + rps[(rps_map[enemy_pick] + 1) % 3] + 6
                print(rps[(rps_map[enemy_pick] + 1) % 3] + 6)

    print(my_score)


part1()
part2()

