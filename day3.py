import math
import typing

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


def count_slope_trees(board: typing.Sequence[str], slope: typing.Tuple[int, int]) -> int:
    tree_count = 0
    i, j = 0, 0
    while True:
        i += slope[1]
        j = (j + slope[0]) % len(board[0])

        if i >= len(board):
            break

        if board[i][j] == '#':
            tree_count += 1

    return tree_count


def main() -> None:
    with open('day3.txt', mode='r') as f:
        lines = [l.strip() for l in f.readlines()]

    tree_counts = [count_slope_trees(lines, slope) for slope in SLOPES]
    print(f'Found {math.prod(tree_counts)} trees')


if __name__ == '__main__':
    main()
