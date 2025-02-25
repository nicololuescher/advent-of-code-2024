import copy

class Guard:
    def __init__(self, map: list[list]) -> None:
        self.map = map
        self.position = self.get_start()
        self.map[self.position[0]][self.position[1]] = "X"
        self.directions = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1)
        }
        self.facing = 0
        self.visited = 1
        self.move_history = []
    
    def turn(self) -> None:
        self.facing = (self.facing + 1) % 4
    
    def move(self):
        if self.will_leave():
            return f"I have left and I've visited {self.visited} squares", self.map
        if self.is_blocked():
            self.turn()
        if [self.position, self.get_move()] not in self.move_history:
            self.move_history.append([self.position, self.get_move()])
        else:
            return "I am Stuck", None
        self.position = tuple([sum(x) for x in zip(self.position, self.get_move())])
        self.visit_square()
        return False, None
    
    def get_move(self) -> tuple:
        return self.directions[list(self.directions)[self.facing]]

    def is_blocked(self) -> bool:
        x, y = [sum(x) for x in zip(self.position, self.get_move())]
        if x < 0 or x >= len(self.map) or y < 0 or y >= len(self.map[0]):
            return True
        return self.map[x][y] == "#"
    
    def visit_square(self) -> None:
        x, y = self.position
        if self.map[x][y] == ".":
            self.map[x][y] = "X"
            self.visited += 1
    
    def will_leave(self) -> bool:
        x, y  = self.position
        move_x, move_y = self.get_move()
        return 0 > x + move_x or x + move_x >= len(self.map) or 0 > y + move_y or y + move_y >= len(self.map[0])
    
    def get_start(self) -> tuple:
        for i, row in enumerate(self.map):
            for j, element in enumerate(row):
                if element == "^":
                    return (i, j)
        return None

def part1(grid: list):
    guard = Guard(grid)
    blocked = False
    while not blocked:
        blocked, _ = guard.move()
    del guard
    return blocked

def main():
    grid = []
    with open("day6/data.txt", "r") as data:
        for line in data:
            grid.append(list(line.strip()))
    print(part1(copy.deepcopy(grid)))

if __name__ == "__main__":
    main()