single = '''abcx
abcy
abcz'''

test = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

def define_group(group):
    group = group.split()
    questions = set()
    for person in group:
        for question in person:
            questions.add(question)
    return len(questions)

def define_sets(group):
    group = group.split()
    the_sets = [set(person) for person in group]
    first = True
    for the_set in the_sets:
        if first:
            final = the_set
            first = False
        else:
            final = final.intersection(the_set)
    return len(final)


def group_everyone(group):
    group = group.split()
    first = True
    for person in group:
        if first:
            questions = [question for question in person]
            first = False
        else:
            for question in questions:
                if question not in list(person):
                    questions.remove(question)
                else:
                    pass
    print(questions)
    print(len(questions))
    return len(questions)

def add_groups(input):
    total = 0
    for group in input.split('\n\n'):
        total += define_sets(group)
    return total

with open('input06.txt') as data:
    inputs = data.read()

# print(add_groups(inputs))

print(add_groups(inputs))