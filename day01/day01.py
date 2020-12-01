from itertools import combinations

test_list = [
    1721,
    979,
    366,
    299,
    675,
    1456,
]

def sum_2020(x,y,z):
    if x + y + z == 2020:
        return True
    else:
        return False

def combos(ls):
    combo = combinations(ls,3)
    for pair in combo:
        if sum_2020(pair[0],pair[1], pair[2]):
            return pair[0] * pair[1] * pair[2]
        else:
            pass
    return 'No answers found'

assert combos(test_list) == 241861950

with open('input01.txt') as data:
    inputs = data.read()

inputs = inputs.splitlines()

inputs = [int(line) for line in inputs]
print(combos(inputs))