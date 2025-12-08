FILENAME = "05_input.txt"

def task1():
    ranges: list[tuple[int, int]] = []
    available: list[int] = []

    reading_ranges = True
    with open(FILENAME) as f:
        for line in f.readlines():
            if line == "\n":
                reading_ranges = False
                continue
            if reading_ranges:
                r: list[str] = line.strip("\n").split("-")
                ranges.append((int(r[0]), int(r[1])))
            else:
                available.append(int(line))

    # for optimization purposes
    ranges.sort(key=lambda x: x[0])

    result: int = 0
    for id in available:
        if is_fresh(id, ranges):
            result += 1
    return result


def is_fresh(id: int, ranges: list[tuple[int, int]]):
    for range in ranges:
        bottom, top = range
        if id < bottom:
            break
        if bottom <= id <= top:
            return True
    return False


print(f"The code to day 5 part 1 is: {task1()}")