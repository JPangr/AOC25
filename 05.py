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

    # for optimization purposes, allows for early break
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

def task2():
    ranges: list[tuple[int, int]] = []
    with open(FILENAME) as f:
        for line in f.readlines():
            if line == "\n":
                break
            r: list[str] = line.strip("\n").split("-")
            ranges.append((int(r[0]), int(r[1])))

    # solve for overlapping ranges

    ## naive solution, very inefficient. Overflows the memory
    # ids: set[int] = set()
    # for rn in ranges:
    #     bottom, top = rn
    #     for i in range(bottom, top+1):
    #         ids.add(i) 
    # return len(ids)

    ranges.sort(key=lambda x: x[0])
    ranges = collapse_ranges(ranges)

    result: int = 0
    for rn in ranges:
        bottom, top = rn
        result += top - bottom + 1
    
    return result

def collapse_ranges(ranges: list[tuple[int, int]]):
    # merge overlapping ranges into a single range
    # (2, 10) and (6, 14) are collapsed into (2, 14)
    # (1, 10) and (2, 8) are collapsed into (1, 10)
    # etc
    changes: int = 1    
    new_ranges: list[tuple[int, int]] = []
    while changes != 0: # awkwared looking, but alas, no do-while
        changes = 0

        rn = ranges[0]
        for i in range(1, len(ranges)):
            r1_bottom, r1_top = rn
            r2_bottom, r2_top = ranges[i]

            if r1_top >= r2_bottom:
                changes += 1
                rn = (r1_bottom, max(r2_top, r1_top))
            else:
                new_ranges.append(rn)
                rn = ranges[i]

        if new_ranges[-1] != rn:
            new_ranges.append(rn)
        
        ranges = new_ranges.copy()
        new_ranges = []

    return ranges

print(f"The code to day 5 part 1 is: {task1()}")
print(f"The code to day 5 part 2 is: {task2()}")