def read_up(grid, x, y, search_string):
    if y < len(search_string) - 1:
        return False
    for i, c in enumerate(search_string):
        if grid[y - i][x] != c:
            return False
    return True


def read_down(grid, x, y, search_string):
    if len(grid) - y < len(search_string):
        return False
    for i, c in enumerate(search_string):
        if grid[y + i][x] != c:
            return False
    return True


def read_left(grid, x, y, search_string):
    if x < len(search_string) - 1:
        return False
    for i, c in enumerate(search_string):
        if grid[y][x - i] != c:
            return False
    return True


def read_right(grid, x, y, search_string):
    if len(grid[y]) - x < len(search_string):
        return False
    for i, c in enumerate(search_string):
        if grid[y][x + i] != c:
            return False
    return True


def read_up_left(grid, x, y, search_string):
    if y < len(search_string) - 1 or x < len(search_string) - 1:
        return False
    for i, c in enumerate(search_string):
        if grid[y - i][x - i] != c:
            return False
    return True


def read_up_right(grid, x, y, search_string):
    if y < len(search_string) - 1 or len(grid[y]) - x < len(search_string):
        return False
    for i, c in enumerate(search_string):
        if grid[y - i][x + i] != c:
            return False
    return True


def read_down_left(grid, x, y, search_string):
    if len(grid) - y < len(search_string) or x < len(search_string) - 1:
        return False
    for i, c in enumerate(search_string):
        if grid[y + i][x - i] != c:
            return False
    return True


def read_down_right(grid, x, y, search_string):
    if len(grid) - y < len(search_string) or len(grid[y]) - x < len(search_string):
        return False
    for i, c in enumerate(search_string):
        if grid[y + i][x + i] != c:
            return False
    return True


def read_x(grid, x, y, search_string):
    if x < 1 or x >= len(grid[y]) - 1 or y < 1 or y >= len(grid) - 1:
        return False
    top_left = grid[y + 1][x - 1]
    top_right = grid[y + 1][x + 1]
    bottom_left = grid[y - 1][x - 1]
    bottom_right = grid[y - 1][x + 1]
    current = grid[y][x]
    start = search_string[0]
    middle = search_string[1]
    end = search_string[-1]

    if current != middle:
        return False

    first_cross = (top_left == start and bottom_right == end) or (
        top_left == end and bottom_right == start
    )
    second_cross = (top_right == start and bottom_left == end) or (
        top_right == end and bottom_left == start
    )
    return first_cross and second_cross


def part1(grid):
    total = 0
    search_string = "XMAS"
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            total += read_up(grid, x, y, search_string)
            total += read_down(grid, x, y, search_string)
            total += read_left(grid, x, y, search_string)
            total += read_right(grid, x, y, search_string)
            total += read_up_left(grid, x, y, search_string)
            total += read_up_right(grid, x, y, search_string)
            total += read_down_left(grid, x, y, search_string)
            total += read_down_right(grid, x, y, search_string)
    return total


def part2(grid):
    search_string = "MAS"
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            total += read_x(grid, x, y, "MAS")
    return total


def main():
    data = ""
    with open("day4/data.txt", "r") as file:
        data = file.read()
    #     data = """.M.S......
    # ..A..MSMS.
    # .M.S.MAA..
    # ..A.ASMSM.
    # .M.S.M....
    # ..........
    # S.S.S.S.S.
    # .A.A.A.A..
    # M.M.M.M.M.
    # .........."""
    # data = """SAMX"""
    grid = []
    for line in data.split("\n"):
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    print(grid)
    print(part1(grid))
    print(part2(grid))


if __name__ == "__main__":
    main()
