import re

with open('4.txt') as f:
    lines = f.read().split('\n\n')
    passports = [line.split() for line in lines]

def hgt(x: str):
    c = x.find('c')
    i = x.find('i')
    if c >= 0:
        return 150 <= int(x[:c]) <= 193
    elif i >= 0:
        return 59 <= int(x[:i]) <= 76
    return False

hcl = re.compile(r'^#[0-9a-f]{6}$')
pid = re.compile(r'^\d{9}$')

validators = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': hgt,
    'hcl': lambda x: hcl.match(x) is not None,
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: pid.match(x) is not None,
}

class Passport:
    def __init__(self, fields):
        self.fields = {}
        self.valid = True
        for field in fields:
            key, val = field.split(':')
            if key == 'cid':
                continue
            self.fields[key] = val
            if not validators[key](val):
                self.valid = False
        if len(self.fields) < 7:
            self.valid = False

passports = [Passport(passport) for passport in passports]

total = 0
for passport in passports:
    if len(passport.fields) == 7:
        total += 1
print(total)

total = 0
for passport in passports:
    if passport.valid:
        total += 1
print(total)
