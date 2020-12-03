test = '''..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#'''

def parse_input(test):
    parsed = test.splitlines()
    return parsed

def repeat_lines(col, length_row):
    new_col = col % (length_row)
    return new_col

def one_slope(position, right, down, length):
    new_position = (repeat_lines(position[0] + right, length), position[1] + down)
    return new_position

def check_trees(position, grid):
    row = grid[position[1]]
    char = row[position[0]]
    if char == '#':
        return True
    elif char == '.':
        return False
    else:
        return print(f'There was an error, your char was {char}')

def the_ride(input, right, down):
    input = parse_input(input)
    length_row = len(input[0])
    hill_size = len(input)
    position = (0,0)
    trees =[]
    while position[1] < hill_size:
        trees.append(check_trees(position, input))
        position = one_slope(position, right, down, length_row)
    return sum(trees)

def mult_list(ls):
    result = 1
    for x in ls:
        result *= x
    return result

def multi_ride(input, rights, downs):
    rides = [the_ride(input, right, down) for right, down in zip(rights,downs)]
    multi = mult_list(rides)
    return multi

assert mult_list([1,2,3]) == 6

assert the_ride(test,3,1) == 7

rights = [1,3,5,7,1]
downs = [1,1,1,1,2]

assert multi_ride(test,rights,downs) == 336

with open('input03.txt') as data:
    inputs = data.read()

print(multi_ride(inputs, rights, downs))
