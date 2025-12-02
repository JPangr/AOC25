FILENAME: str = "01_input.txt"
START: int = 50

LEFT = -1
RIGHT = 1

def task1(FILENAME, START):
    position: int = START
    zero_count: int = 0

    with open(FILENAME) as f:
        lines: list[str] = f.readlines()
        for line in lines:
            line = line.strip("\n")

            rotation: tuple[int, int] = parse(line)
            direction, clicks = rotation

            position += (direction * clicks)
            position %= 100

            if position == 0:
                zero_count += 1

    return zero_count


def task2(FILENAME, START):
    position: int = START
    zero_count: int = 0

    with open(FILENAME) as f:
        lines: list[str] = f.readlines()
        for line in lines:
            line = line.strip("\n")

            rotation: tuple[int, int] = parse(line)
            direction, clicks = rotation

            zero_count += clicks // 100
            clicks %= 100
            
            prev = position
            position += direction * clicks
            if position > 99 or (position <= 0 and prev != 0):
                zero_count += 1

            position %= 100

    return zero_count
            

def parse(line: str):
    r1: int = RIGHT if line[0] == "R" else LEFT
    r2: int = int(line[1:])
    return (r1, r2)

print(f"The code to day 1 part 1 is: {task1(FILENAME, START)}")
print(f"The code to day 1 part 2 is: {task2(FILENAME, START)}")
