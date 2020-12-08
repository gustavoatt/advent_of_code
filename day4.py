import re
import typing


def read_passport(file: typing.IO) -> typing.Optional[typing.Dict[str, str]]:
    passport = dict()
    while True:
        line = file.readline()

        # If empty line, return nothing
        if line == '':
            return None

        if line.isspace():
            return passport

        for key_val in line.strip().split():
            key, val = key_val.split(':')
            passport[key] = val


def validate_passport(passport: typing.Dict[str, str]) -> bool:
    birth_year = int(passport['byr'])
    if birth_year < 1920 or birth_year > 2002:
        return False

    issue_year = int(passport['iyr'])
    if issue_year < 2010 or issue_year > 2020:
        return False

    expire_year = int(passport['eyr'])
    if expire_year < 2020 or expire_year > 2030:
        return False

    height_match = re.match(r'\d+(cm|in)', passport['hgt'])
    if not height_match:
        return False

    return True


def main() -> None:
    required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'hcl', 'ecl', 'pid'}

    count = 0
    with open('day4.txt', mode='r') as f:
        while True:
            passport = read_passport(file=f)
            if passport is None:
                break

            if set(passport.keys()).issuperset(required_keys):
                count += 1

    print(f'Valid passports: {count}')


if __name__ == '__main__':
    main()