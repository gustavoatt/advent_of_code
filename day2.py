import re


PASS_REGEX = re.compile(r'(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)')


def main() -> None:
    with open('day2.txt', mode='r') as f:
        lines = f.readlines()

    valid = 0
    for l in lines:
        result = PASS_REGEX.match(l)
        pos_a, pos_b = int(result.group('min')), int(result.group('max'))
        letter, password = result.group('letter'), result.group('password')

        if (password[pos_a - 1] == letter) ^ (password[pos_b - 1] == letter):
            valid += 1

    print(f'Valid passwords: {valid}')


if __name__ == '__main__':
    main()