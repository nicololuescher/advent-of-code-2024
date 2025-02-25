def test_numbers(target, subtotal, numbers, part2=False):
    if target == subtotal:
        return True

    if subtotal > target or len(numbers) == 0:
        return False
    
    print(target, f"{subtotal} + {numbers[0]} = {subtotal + numbers[0]}", numbers[1:])
    print(target, f"{subtotal} * {numbers[0]} = {subtotal * numbers[0]}", numbers[1:])
    print(target, f"{str(subtotal)} || {str(numbers[0])} =  {int(str(subtotal) + str(numbers[0]))}", numbers[1:])

    return (
        test_numbers(target, subtotal + numbers[0], numbers[1:], part2)
        or test_numbers(target, subtotal * numbers[0], numbers[1:], part2)
        or (part2 and test_numbers(target, int(str(subtotal) + str(numbers[0])), numbers[1:], part2))
    )


def part1(configurations):
    total = 0
    for entry in configurations:
        total += (
            entry["result"] if test_numbers(entry["result"], 0, entry["numbers"]) else 0
        )
    return total


def part2(configurations):
    total = 0
    for entry in configurations:
        total += (
            entry["result"]
            if test_numbers(entry["result"], 0, entry["numbers"], True)
            else 0
        )
    return total


def main():
    configurations = []
    with open("day7/data.txt") as f:
        for line in f:
            parts = line.strip().split(": ")
            configurations.append(
                {
                    "result": int(parts[0]),
                    "numbers": [int(x) for x in parts[1].split(" ")],
                }
            )
        print(part1(configurations))
        print(part2(configurations))


if __name__ == "__main__":
    main()