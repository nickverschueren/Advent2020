import re
import inspect

class rulesBase:
    def __init__(self):
        self.rules = [value for key, value in inspect.getmembers(self.__class__, predicate=inspect.isfunction) if not key in ['validateRecords','__init__']]
    
    def validateRecords(self, records):
        validCount = 0
        for record in records:
            valid = True
            for rule in self.rules:
                valid = valid and rule(self, record)
            if valid:
                validCount = validCount + 1
        return validCount

class rulesPart1(rulesBase):
    def byrRule(self, record):
        return 'byr' in record

    def iyrRule(self, record):
        return 'iyr' in record

    def eyrRule(self, record):
        return 'eyr' in record

    def hgtRule(self, record): 
        return 'hgt' in record

    def hclRule(self, record):
        return 'hcl' in record

    def eclRule(self, record):
        return 'ecl' in record

    def pidRule(self, record): 
        return'pid' in record

class rulesPart2(rulesBase):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    def byrRule(self, record):
        if ('byr' in record):
            byr = record['byr']
            if re.search('^((19[2-9][0-9])|(200[0-2]))$', byr):
                return True
        return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    def iyrRule(self, record):
        if('iyr' in record):
            iyr = record['iyr']
            if re.search('^20((1[0-9])|(20))$', iyr):
                return True
        return False
            
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    def eyrRule(self, record):
        if('eyr' in record):
            eyr = record['eyr']
            if re.search('^20((2[0-9])|(30))$', eyr):
                return True
        return False

    # hgt (Height) - a number followed by either cm or in:
    def hgtRule1(self, record):
        if('hgt' in record):
            hgt = record['hgt']
            if re.search('^\d+((in)|(cm))$', hgt):
                return True
        return False

    # If cm, the number must be at least 150 and at most 193.
    def hgtRule2(self, record):
        if('hgt' in record):
            hgt = record['hgt']
            if (re.search('(^1([5-8][0-9])|(9[0-3])cm$)|(^(?!\d*cm))', hgt)):
                return True
        return False
    
    # If in, the number must be at least 59 and at most 76.

    def hgtRule3(self, record):
        if('hgt' in record):
            hgt = record['hgt']
            if (re.search('(^(59)|(6[0-9])|(7[0-6])in$)|(^(?!\d*in))', hgt)):
                return True
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    def hclRule(self, record):
        if('hcl' in record):
            hcl = record['hcl']
            if (re.search('^#([0-9]|[a-f]){6}$', hcl)):
                return True
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    def eclRule(self, record):
        if('ecl' in record):
            ecl = record['ecl']
            if (re.search('^((amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth))$', ecl)):
                return True
        return False

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    def pidRule(self, record):
        if('pid' in record):
            pid = record['pid']
            if (re.search('^\d{9}$', pid)):
                return True
        return False

    # cid (Country ID) - ignored, missing or not.