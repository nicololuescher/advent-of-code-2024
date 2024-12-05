def check_level(level):
    steps = [level[i] - level[i + 1] for i in range(len(level) - 1)]

    all_valid_asc = all(-3 <= step <= -1 for step in steps)
    all_valid_desc = all(1 <= step <= 3 for step in steps)

    return all_valid_asc or all_valid_desc


def safe_with_dampener(level):
    valid = check_level(level)
    if valid:
        return True

    for i in range(len(level)):
        modified_level = level[:i] + level[i + 1 :]
        valid = check_level(modified_level)
        if valid:
            return True
    return False


def part1(levels):
    return sum(1 for level in levels if check_level(level))


def part2(levels):
    return sum(1 for level in levels if safe_with_dampener(level))


def main():
    levels = []
    with open("day2/data.txt", "r") as file:
        for line in file:
            levels.append([int(item) for item in line.split(" ")])
    print("Part 1:", part1(levels))
    print("Part 2:", part2(levels))


if __name__ == "__main__":
    main()
