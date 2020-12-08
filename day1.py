
def main() -> None:
    with open('day1.txt', mode='r') as f:
        nums = [int(x.strip()) for x in f.readlines()]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                for k in range(len(nums)):
                    if k == i or k == j:
                        continue

                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c != 2020:
                        continue

                    print(f'Found ({a}, {b}, {c}): {a * b * c}')
                    return


if __name__ == '__main__':
    main()
