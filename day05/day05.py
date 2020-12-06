test = 'BFFFBBFRRR' #row 70, column 7, seat ID 567

def row_finder(code):
    rows = list(range(0,128))
    for idx in range(7):
        divider = len(rows) // 2
        if code[idx] == 'F':
            rows = rows[:divider]
        elif code[idx] == 'B':
            rows = rows[divider:]
        else:
            print(f'Got a {code[idx]} instead of an F or B')
    return rows[0]

def col_finder(code):
    cols = list(range(8))
    for idx in range(7,10):
        divider = len(cols) // 2
        if code[idx] == 'L':
            cols = cols[:divider]
        elif code[idx] == 'R':
            cols = cols[divider:]
        else:
            print(f'Got a {code[idx]} instead of an L or R')
    return cols[0]

def seat_id(code):
    return row_finder(code) * 8 + col_finder(code)

def find_seat(input):
    seat_ids = [seat_id(code) for code in input.split()]
    seat_ids.sort()
    # print(seat_ids)
    first = True
    for id in seat_ids:
        if first:
            last_id = id
            first = False
            pass
        check = id - last_id
        last_id = id
        if check == 2:
            return print(id - 1)
    return print('didnt find one')
        


def highest_seat_id(input):
    seat_ids = [seat_id(code) for code in input.split()]
    return max(seat_ids)

assert row_finder(test) == 70
assert col_finder(test) == 7
assert seat_id(test) == 567

with open('input05.txt') as data:
    inputs = data.read()

find_seat(inputs)