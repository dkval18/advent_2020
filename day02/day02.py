test = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
'''

def parse_input(text):
    parsed = []
    for line in text.splitlines():
        ls = line.split(' ')
        low_high = ls[0].split('-')
        low = low_high[0]
        high = low_high[1]
        letter = ls[1].split(':')
        letter = letter[0]
        code = ls[2]
        parsed.append([int(low),int(high),letter,code])
    return parsed

def policy(row):
    letter = row[2]
    code = row[3]
    if (code[row[0] - 1] == letter) ^ (code[row[1] - 1] == letter):
        return True
    else:
        return False

# for row in parse_input(test):
#     print(policy(row))  
with open('input02.txt') as data:
    inputs = data.read()

policy_list = [policy(row) for row in parse_input(inputs)]

print(sum(policy_list))