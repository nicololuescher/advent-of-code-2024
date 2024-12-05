def part1(lists):
    total = 0
    for i in range(len(lists[0])):
        total += abs(lists[0][i] - lists[1][i])
    return total


def part2(lists):
    total = 0
    for element in lists[0]:
        total += element * lists[1].count(element)
    return total


def main():
    with open("day1/data.txt", "r") as data:
        lists = [[], []]
        for line in data:
            elements = line.split("   ")
            lists[0].append(int(elements[0]))
            lists[1].append(int(elements[1]))
        lists[0].sort()
        lists[1].sort()
        print(part1(lists))
        print(part2(lists))


if __name__ == "__main__":
    main()
