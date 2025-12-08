FILENAME = "04_input.txt"

def task1():
    with open(FILENAME) as f:
        grid: list[str] = f.readlines()


    ln: int = len(grid[0]) # assuming all lines are the same length
    count: int = 0
    for y in range(0, len(grid)):
        for x in range(0, ln):
            if grid[y][x] != '@':
                continue
            if is_accessible(x, y, grid):
                count += 1
    
    return count


def is_accessible(x: int, y: int, grid: list[str]):
    count: int = 0

    ln: int = len(grid[0])
    low: int = max(0, y-1)
    high: int = min(len(grid), y+2)
    left: int = max(0, x-1)
    right: int = min(ln, x+2)

    for i in range(low, high):
        for k in range(left, right):
            if k == x and i == y:
                continue # could also be accounted for by simply increasing the margin to 4, but I like being explicit
            if grid[i][k] == "@":
                count += 1

    return count < 4


def task2():
    with open(FILENAME) as f:
        grid: list[str] = f.readlines()


    ln: int = len(grid[0]) # assuming all lines are the same length
    count: int = 0

    changes: int = 1 # initializing at a non0 value, since pythond doesn't have a do-while
    while changes != 0:
        changes = 0
        for y in range(0, len(grid)):
            for x in range(0, ln):
                if grid[y][x] != '@':
                    continue
                if is_accessible(x, y, grid):
                    count += 1
                    grid[y] = grid[y][:x] + "." + grid[y][x+1:]
                    changes += 1
    
    return count


print(f"The code to day 4 part 1 is: {task1()}")
print(f"The code to day 4 part 2 is: {task2()}")
