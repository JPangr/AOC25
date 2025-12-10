FILENAME = "07_input.txt"

def task1():
    with open(FILENAME) as f:
        lines: list[list[str]] = [list(line) for line in f.readlines()]
    
    result: int = 0
    # not very elegant, but works well enough
    for i in range(1, len(lines)):
        for k in range(len(lines[i])-1): #assuming no splits on very last line
            if lines[i-1][k] == "S" or lines[i-1][k] == "|":
                if lines[i][k] == ".":
                    lines[i][k] = "|"
                elif lines[i][k] == "^":
                    if k > 0:
                        lines[i][k-1] = "|"
                    if k < len(lines)-1:
                        lines[i][k+1] = "|"
                    result += 1
    return result


def task2():
    with open(FILENAME) as f:
        lines: list[list[str]] = [list(line) for line in f.readlines()]
    
    # having previously tried to implement it without cache and with
    # just a regular DFS, I think it's safe to say this speeds it up
    # several hundred times at the very least
    cache: dict[tuple[int, int], int] = {}
    
    return DFS(lines[0].index("S"), 1, cache, lines)


def DFS(x: int, y: int, cache: dict[tuple[int, int], int], lines: list[list[str]]):
    if y == len(lines)-1:
        return 1
    
    if lines[y][x] == ".":
        return DFS(x, y+1, cache, lines)

    if cache.get((x, y)) is not None:
        return cache[(x, y)]

    if lines[y][x] == "^":
        res = DFS(x-1, y+1, cache, lines) + DFS(x+1, y+1, cache, lines)
        cache[(x, y)] = res
        return res


print(f"The code to day 7 part 1 is: {task1()}")
print(f"The code to day 7 part 2 is: {task2()}")
