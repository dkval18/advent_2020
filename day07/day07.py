import re

test = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

def parse_input(raw):
    sentences = raw.split('.')
    sentences = sentences[:-1]
    for sentence in sentences:
        parent_child = sentence.split('contain')
        parent = parent_child[0]
        child = parent_child[-1]
        print(f'Parent {parent}')
        print(f'Child {child}')

    # regex = r'(?P<parent>[a-z]/s)'

print(parse_input(test))