import re


def part1(input):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


def part2(input):
    parts = input.split("do()")
    parts = [part.split("don't()")[0] for part in parts]
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, "".join(parts))
    total = 0
    for match in matches:
        total += int(match[0]) * int(match[1])
    return total


def main():
    with open("day3/data.txt", "r") as file:
        input = file.read()
        # input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        print(part1(input))
        print(part2(input))


if __name__ == "__main__":
    main()
