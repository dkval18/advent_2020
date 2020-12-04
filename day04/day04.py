import re

test = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

valid = '''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

invalid = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007'''

def parse_input(test):
    test = test.split('\n\n')
    list_passports = []
    for line in test:
        new_dict = {}
        for item in line.split():
            key = item.split(':')
            new_dict[key[0]] = key[1]
        list_passports.append(new_dict)
    return list_passports

def check_required_cat(passport):
    required_cats = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]
    check = []
    for cat in required_cats:
        if cat in passport:
            check.append(True)
        else:
            check.append(False)
    if len(check) == sum(check):
        return True
    else:
        return False


def data_validation(key, value):
    required_cats = {
        'byr': ["re.fullmatch('\d{4}', value) is not None",
                     "(int(value) >= 1920) and (int(value) <= 2002)"],
        'iyr': ["re.fullmatch('\d{4}', value) is not None",
                    "(int(value) >= 2010) and (int(value) <= 2020)"],
        'eyr': ["re.fullmatch('\d{4}', value) is not None",
                    "(int(value) >= 2020) and (int(value) <= 2030)"],
        'hgt': ["re.search(r'cm|in', value) is not None"],
        'hcl': ["re.search(r'#([0-9]|[a-f]){6}', value) is not None"],
        'ecl': ["value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']"],
        'pid': ["re.fullmatch('\d{9}', value) is not None"],
        'cid': []
    }
    statement_list = required_cats[key]
    checker = True
    for statement in statement_list:
        if eval(statement):
            pass
        else:
            checker = False
    if key == 'hgt':
        if 'in' in value:
            num = int(value.split('in')[0])
            if (num < 59) or (num > 76):
                checker = False
        else:
            num = int(value.split('cm')[0])
            if (num < 150) or (num > 193):
                checker = False
    if checker:
        return True
    else:
        return False

def check_data_validation(passport):
    check = []
    for key, value in passport.items():
        check.append(data_validation(key,value))
    if len(check) == sum(check):
        return True
    else:
        return False
    
def all_cat_present(raw):
    parsed = parse_input(raw)
    final_check = []
    for passport in parsed:
        if (check_required_cat(passport)) and (check_data_validation(passport)):
            final_check.append(True)
        else:
            final_check.append(False)
    return sum(final_check)

assert data_validation('byr', '2003') == False
assert data_validation('byr', '2002') == True
assert data_validation('hgt', '190') == False
assert data_validation('hgt', '190cm') == True
assert data_validation('hcl', r'#123abc') == True
assert data_validation('hcl', r'#123abz') == False
assert data_validation('hcl', r'123abz') == False
assert data_validation('ecl', 'brn') == True
assert data_validation('ecl', 'wat') == False
assert data_validation('pid', '000000001') == True
assert data_validation('pid', '0000000012') == False

assert all_cat_present(valid) == 4


with open('input04.txt') as data:
    inputs = data.read()

print(all_cat_present(inputs))
