import typing


def run_program(program: typing.Sequence[str]) -> typing.Tuple[bool, int]:
    """Returns a tuple with (program_terminated, accumulator)"""
    instructions = set()
    accumulator, current_int = 0, 0
    while current_int < len(program):
        if current_int in instructions:
            return False, accumulator

        instructions.add(current_int)

        line = program[current_int]
        inst, val = line.split()
        if inst == 'nop':
            current_int += 1
        elif inst == 'acc':
            accumulator += int(val)
            current_int += 1
        elif inst == 'jmp':
            current_int += int(val)

    return True, accumulator


def main() -> None:
    with open('day8.txt', mode='r') as f:
        program = [l.strip() for l in f.readlines()]

    changeable_instr = {i: l.split() for i, l in enumerate(program) if l.startswith('nop') or l.startswith('jmp')}
    instruction_opposite = {
        'jmp': 'nop',
        'nop': 'jmp'
    }

    for line_no, instruction in changeable_instr.items():
        new_program = (
                program[:line_no] +
                [instruction_opposite[instruction[0]] + " " + instruction[1]] +
                program[line_no + 1:]
        )

        terminated, acc = run_program(new_program)
        if terminated:
            print(f'Accumulator value: {acc}')
            break


if __name__ == '__main__':
    main()